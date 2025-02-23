# Git Tutorial

将一个目录创建为 git repository:

```bash
git init
```

将本地的更改加入 staging area (还没被记录为一次 commit):

```bash
# Stage some files
git add <file-path>
# Stage all files
git add .
```

查看当前的 HEAD commit:

```bash
git log -n 1
```

将 staging area 中的更改提交为一次 commit:

```bash
git commit -m "<commit-message>"
```

查看最新两个 commit:

```bash
git log -n 2
```

回退到某个 commit:

```bash
# Keep the changes
git reset --soft <commit-id>
# Revoke the changes
git reset --hard <commit-id>
```

基于当前分支创建一个分支 (新分支的 commit 记录和当前分支相同):

```bash
git switch -c <branch-name>
```

切换到某个分支:

```bash
git switch <branch-name>
```

查看远程 repo 状态:

```bash
git fetch
```

合并远程 repo 中的新 commit 到本地当前分支:

```bash
git pull origin <branch-name> --rebase
```

如果出现 conflict, 进入 rebase 状态, 解决完后先将改动添加到 staging area, 然后进行下一步 rebase, 直到所有 commit rebase 完成:

```bash
git rebase --continue
```

将本地的新 commit 提交到远程 repo:

```bash
git push origin <local-branch-name>:<remote-branch-name>
```

创建 Pull Request, 等待管理者进行代码审阅和 merge.

