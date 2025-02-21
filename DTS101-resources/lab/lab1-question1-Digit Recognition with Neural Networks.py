# %% md
### 数据预处理
# %%
import pandas as pd
import torch
from torch.utils.data import TensorDataset, DataLoader

# 读取数据！
train_path = "mnist_train.csv"
test_path = "mnist_test.csv"
train_data = pd.read_csv(train_path, header=None)
test_data = pd.read_csv(test_path, header=None)

# 分离特征和标签
y_train = train_data.iloc[:, 0].values
x_train = train_data.iloc[:, 1:].values / 255.0  # 归一化

y_test = test_data.iloc[:, 0].values
x_test = test_data.iloc[:, 1:].values / 255.0  # 归一化

# 转换为Tensor
x_train = torch.tensor(x_train, dtype=torch.float32)
y_train = torch.tensor(y_train, dtype=torch.long)
x_test = torch.tensor(x_test, dtype=torch.float32)
y_test = torch.tensor(y_test, dtype=torch.long)

# 创建DataLoader
batch_size = 64
train_dataset = TensorDataset(x_train, y_train)
train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
test_dataset = TensorDataset(x_test, y_test)
test_loader = DataLoader(test_dataset, batch_size=batch_size)

# %% md
### 构建神经网络
# %%
import torch.nn as nn


class MNIST(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(784, 512)
        self.fc2 = nn.Linear(512, 256)
        self.fc3 = nn.Linear(256, 10)
        self.dropout = nn.Dropout(0.2)  # 添加Dropout防止过拟合

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = self.dropout(x)
        x = torch.relu(self.fc2(x))
        x = self.dropout(x)
        x = self.fc3(x)
        return x


# 初始化模型
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = MNIST().to(device)
print(model)

# %% md
### 训练模型
# %%
import torch.optim as optim
from tqdm.auto import tqdm

criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)
epochs = 10

train_losses = []
for epoch in range(epochs):
    model.train()
    running_loss = 0.0

    for inputs, labels in tqdm(train_loader, desc=f'Epoch {epoch + 1}'):
        inputs, labels = inputs.to(device), labels.to(device)

        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        running_loss += loss.item()

    epoch_loss = running_loss / len(train_loader)
    train_losses.append(epoch_loss)
    print(f'Epoch {epoch + 1} Loss: {epoch_loss:.4f}')

# %% md
### 测试模型
# %%
model.eval()
correct = 0
total = 0

with torch.no_grad():
    for inputs, labels in test_loader:
        inputs, labels = inputs.to(device), labels.to(device)
        outputs = model(inputs)
        _, predicted = torch.max(outputs.data, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

accuracy = 100 * correct / total
print(f'Test Accuracy: {accuracy:.2f}%')