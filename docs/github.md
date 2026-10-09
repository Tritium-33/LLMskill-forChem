# GitHub 入门：本地仓库、登录与同步

Git 是本地版本管理；GitHub 是远程托管。没有 GitHub 账号也能整理、安装和测试本仓库，甚至进行本地提交。账号登录和 Git 提交署名是独立设置。

## WSL 没有图形界面也可以登录

GitHub 账号先在 Windows 浏览器中注册。WSL 只需要 Git 和 GitHub CLI（`gh`）。Ubuntu 的一个安装入口是：

```bash
sudo apt update
sudo apt install git gh
```

如果发行版仓库不提供 `gh` 或版本不适用，按 [GitHub CLI 官方安装说明](https://github.com/cli/cli/blob/trunk/docs/install_linux.md)安装。Windows 原生用户也可以使用 [GitHub CLI](https://cli.github.com/)。

在 WSL 中运行：

```bash
gh auth login --hostname github.com --git-protocol https --web
```

终端会显示一次性设备验证码及授权网址。用 Windows 浏览器打开终端显示的网址（通常为 `https://github.com/login/device`），登录后输入验证码并授权。WSL 不需要 Linux 桌面。如果无法自动打开浏览器，手动打开即可，保持终端等待流程完成。

```bash
gh auth status
gh auth setup-git
```

密码、令牌和设备验证码无需发给协作者或写入仓库。认证流程依据 [gh auth login 官方手册](https://cli.github.com/manual/gh_auth_login)。

## 第一次本地提交

在仓库根目录查看状态。若目录还没有初始化 Git，先运行 `git init -b main`。接着设置本仓库的提交身份：

```bash
git config user.name "你的公开署名"
git config user.email "你的 GitHub noreply 邮箱或提交邮箱"
git status
git add .
git diff --cached --stat
git commit -m "Initial chemistry research skill collection"
```

从 GitHub 的邮件设置复制账号提供的 noreply 邮箱，不根据用户名猜地址。没有确定署名和邮箱时可以暂不提交；不要用随意编造的身份代替。

## 首次上传

确定本地提交内容之后，可以先创建私有远程仓库：

```bash
gh repo create LLMskill-forChem --private --source=. --remote=origin --push
```

确认要直接公开时，将 `--private` 改成 `--public`。这是实际创建远程仓库并上传的命令；仅在登录完成、提交内容已检查且可见性已决定后运行。不要对已有远程仓库重复执行创建命令，先用 `git remote -v` 查看配置。

更多参数见 [gh repo create](https://cli.github.com/manual/gh_repo_create)。发布后，在 Actions 页面查看 Windows 与 Ubuntu 检查的真实结果，再更新兼容性记录。

## 日常修改和使用更新

维护者编辑源码后：

```bash
git status
git add .
git diff --cached --stat
git commit -m "Describe the skill change"
git push
```

其他环境首次下载，用仓库页面的 **Code** 按钮复制真实地址：

```bash
git clone <从 GitHub 复制的仓库地址>
cd LLMskill-forChem
python3 tools/manage.py install
```

已有副本则运行 `git pull --ff-only`，再执行安装命令。Windows 原生使用 `py -3`。有未提交修改时先保存和检查；遇到冲突不要直接强制覆盖。

同一台电脑上更新已安装技能不必先上传再下载，可以直接从源码安装测试。上传用于同步与分享，安装用于让本地智能体发现技能。

## 注册失败

先查看 [GitHub Status](https://www.githubstatus.com/)，服务异常时稍后重试。若状态正常而注册仍失败，用 Windows 浏览器的隐私窗口检查是否是扩展或旧 Cookie 干扰，保留完整报错和发生步骤，必要时联系 [GitHub Support](https://support.github.com/)。仅凭“服务器故障”不能确定原因，也不需要为此安装 WSL 图形桌面。
