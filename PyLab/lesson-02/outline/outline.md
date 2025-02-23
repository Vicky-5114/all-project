# Lesson 02

## 1. 学习 shell

终端（termimal），作用是提供一个命令的输入输出环境。

shell是一个命令行解释器，是linux内核的一个外壳, 负责外界与linux内核的交互。当打开一个terminal时，操作系统会将terminal和shell关联起来，当我们在terminal中输入命令后，shell就负责解释命令。

### 1.1 常用命令

- `ls`：列出当前目录下的文件和文件夹
- `cd`：切换目录
- `pwd`：显示当前目录
- `mkdir`：创建目录
- `touch`：创建文件
- `rm`：删除文件或目录
- `cp`：复制文件或目录
- `mv`：移动文件或目录
- `cat`：查看文件内容

### 1.2 编译运行 C++ 程序

```bash
cd ~/Desktop
mkdir cpp-test
cd cpp-test
touch main.cpp
```

打开 `main.cpp` 文件，输入以下内容：

```cpp
#include <iostream>

int main()
{
    std::cout << "Hello World" << std::endl;
    return 0;
}
```

回到 terminal，输入以下命令：

```bash
cd ~/Desktop/cpp-test
g++ main.cpp -o main.whatever-extension-name
ls
./main.whatever-extension-name
~/Desktop/cpp-test/main.whatever-extension-name
$(pwd)/main.whatever-extension-name
```

### 1.2 修改 PATH 环境变量

```bash
cd ~/Desktop/cpp-test
echo $PATH
export PATH=$(pwd):$PATH
echo $PATH
cd ~
main.whatever-extension-name
```

### 1.3 如何在 windows terminal 的 powershell 中直接运行 bash

这里就涉及到 windows 手动更改 PATH 环境变量

## 2. 学习 conda

- `conda -v`: 查看 conda 版本
- `conda list`: 查看当前环境下安装的包
- `conda env list`: 查看所有环境
- `conda create -n env-name python=3.10`: 创建一个新环境
- `conda activate env-name`: 激活一个环境
- `conda deactivate`: 退出当前环境
- `conda remove -n env-name --all`: 删除一个环境
- `conda remove package-name`: 删除当前环境的一个包
- `conda install package-name`: 安装一个包
- `conda update package-name`: 更新一个包

## 3. 学习 pip

找包: 直接上 [pypi](https://pypi.org/).

换源: 

```bash
pip config set global.index-url https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple
```

常用命令:

- `pip install package-name`: 安装一个包
- `pip install package-name==version`: 安装指定版本的包
- `pip uninstall package-name`: 卸载一个包
- `pip list`: 查看当前环境下安装的包
- `pip freeze > requirements.txt`: 导出当前环境下的包
- `pip install -r requirements.txt`: 安装 requirements.txt 中的包

## 4. 基础语法
### 4.1 行结构
一个 Python 程序可分为许多逻辑行，一般来说：一个语句就是一行代码，不会跨越多行. 比如下面的 Python 程序，一共有3个逻辑行，每一行都通过 print() 输出一个结果

```python
print(123)
print(456)
print(123456)
```

而如果是下面这种写法，程序执行是会报错的，因为 print() 一个语句跨越了 2 行.

```python
print(12
3)
print(4
56)
print(123
456)
```

也可以把多个语句利用英文输入下的分号（ ;）写在一行之内，不过通常我们不这么做

```python
print(123); print(456); print(123456)
```

也有语句是可以跨越多行的，比如：复合语句。复合语句可由多行子语句组成，通常它会跨越多行. 比如下面的 `if ... else ...` 语句就是一个复合语句，它跨越了多行:

```python
a = 4
if a < 3:
    print(True)
else:
    print(False)
```

有的时候，整个复合语句也可能包含于一行之内. 下面这种写法，叫做三元表达式，它把 if ... else ... 复合语句写在了一行之内

```python
print(True) if a < 3 else print(False)
```

### 4.2 缩进

一个逻辑行开头处的空白被用来计算该行的缩进等级，以决定语句段落的组织结构

比如前面提到的 if 语句，可以看到这里的第一个 `print()` 前面是有空白的，这就是缩进，它说明了第一个 `print()` 是 if 语句的下级

第二个 `print()` 前面没有缩进，那么它和 if 语句是平级的。

如果 if 条件不成立，那么第一个 `print()` 不会执行，因为它是 if 语句的下级，而第二个 `print()` 仍会执行，因为它和 if 语句是平级的，并会不受 if 条件的影响

```python
a = 4
if a < 3:
print(True)
print(789)
```

在 IDE 中写程序时，需要缩进的语句，一般敲回车换行会自动缩进的，一般是占 4 个空格，我们在写代码需要缩进时通常用 Tab 键，而不用按 4 次空格（Tab 键一般可以把光标缩进 4 个空格，通常这是IDE 可设置的）

缩进的空格数是可变的，并非固定 4 个空格，但是同一个代码块的语句必须包含相同的缩进空格数

```python
a = 4
if a < 3:
    print(True)
    print(123) # 这个缩进不对，同为if语句下的代码，应该和上面一个print缩进一样
else:
    print(False) # 这个缩进没问题，它在else语句下面，可以和if语句下的print缩进不一样
    print(789) # 这个print是在if...else...语句外面的，是平级的，不需要缩进
```

### 4.3 注释

注释在 Python 解释器的语法分析中会被忽略。通说的说，注释是给人看的，而程序执行时会被无视

- 单行注释：以 # 开头
- 多行注释：每行都用一个 # 开头，或者用 三引号（可单 ''' 、可双"""）把注释内容包起来

```python
print(1234)
# 第一个注释
# 第二个注释
'''
第三个注释

三引号可以多行注释
'''
"""
第四个注释
三引号可以多行注释
"""
print("Hello, Python!") # 第五个注释
```

### 4.4 拼接

显式的行拼接：Python 通常是一行写完一条语句，但如果语句很长，可以使用续行符（\）来实现多行语句

隐式的行拼接：圆括号、方括号或花括号以内的多行语句，无需使用续行符（\）

```python
""" 下面 a,b 两种写法都是可以的，结果是一样的 """
a = 1 + 2 + 3
b = 1 + \
2 + \
3
```

```python
month_names = ['Januari', 'Februari', 'Maart',      # These are the
                'April', 'Mei', 'Juni',             # Dutch names
                'Juli', 'Augustus', 'September',    # for the months
                'Oktober', 'November', 'December']  # of the year
```

### 4.5 变量

变量就是可以变化的量。是计算机语言中能储存计算结果或能表示值的抽象概念

变量需要先定义再使用，解释器执行到变量定义的代码时会申请内存

空间存放变量值，然后将变量值的内存地址绑定给变量名

变量的定义由三部分组成：

- 变量名：指向值所在的内存地址，通过它访问值
- 等于号（=）：赋值符号，用来将数据的内存地址绑定给变量
名
- 值：变量的值就是内存地址对应存储的数据

标识符：用于变量、函数、类、模块等的名称

标识符命名规范：
- 变量名只能包括字母、数字和下划线；变量名不能以数字开头
- 变量名不能包括空格，可以使用下划线来分隔多个单词
- 不能使用 Python 的关键字及内置函数名作变量名
- 变量名要尽量简短及具描述性，尽量做到短小精悍，见名知义
- Python 中变量名是区分大小写的，例如，Name 和 name 是两个不同的变量名


### 4.6 常量

常量就是不变化的量。在程序运行过程中，有些值是固定的、不应该被改变，比如圆周率 3.141592653...

所以单从语法层面去讲，常量的使用与变量完全一致

### 4.7 函数

函数是一段可以重复使用的代码块，它接受输入、处理数据并返回输出。

函数的定义：

```python
def function_name(parameters):
    """docstring"""
    statement(s)
    return expression
```

## 5. 实战

### 5.1 add

要求：写一个函数，输入两个数字，返回两个数字的和

### 5.2 sub

要求：写一个函数，输入两个数字，返回两个数字的差

### 5.3 guess number v1

要求：随机生成一个数字，用户输入一个数字，判断大了还是小了，直到猜对为止

### 5.4 guess number v2

要求：用户自己心里想一个数字，让计算机来猜，用户输入大了还是小了，直到计算机猜对为止

### 5.5 dice game

要求：电脑掷一个骰子，等待用户输入 y；如果输入 y，用户掷一个骰子，接着让用户猜用户大还是小于电脑，输出对了还是错了

## 6. 作业

写一个 Python 程序，判断用户输入 r 还是 l 还是 q；如果输入 r，则提示用户输入用户名和密码，分别保存在 username 和 password 变量中，然后重新提示用户输入 r 或 l；如果输入 l，则提示用户输入用户名和密码，检查是否和 username 和 password 变量中的值一致，如果一致则输出登录成功，否则输出登录失败。如果输入 q 就推出成勋。



