# 学习会话记录 - 2026-04-25

## 会话概览
- 日期：2026-04-25
- 形式：一对一教学
- 核心主题：Git 复习 + 推送代码到 GitHub

## 学员提出的问题/需求
1. 想复习 Git 操作
2. 想把代码推送到 GitHub 新仓库
3. 想了解如何切换远程仓库地址

## 讲解的概念与教学过程

### 1. Git 三大区域
```
工作区 → 暂存区 → 本地仓库 → 远程仓库
```

### 2. Git 常用命令复习
| 命令 | 作用 |
|-----|------|
| `git clone 地址` | 克隆仓库 |
| `git add .` | 添加所有变化到暂存区 |
| `git add -A` | 添加所有（包括删除的文件） |
| `git commit -m "说明"` | 提交到本地仓库 |
| `git push` | 推送到远程仓库 |
| `git pull` | 从远程拉取更新 |
| `git status` | 查看状态 |
| `git branch -a` | 查看所有分支 |
| `git switch -c 分支名` | 创建并切换新分支 |
| `git switch 分支名` | 切换分支 |
| `git merge 分支名` | 合并分支 |

### 3. 远程仓库操作
```bash
# 查看远程仓库
git remote -v

# 添加远程仓库
git remote add 名字 地址

# 修改远程仓库地址
git remote set-url 名字 新地址

# 推送到指定远程
git push 远程名 分支名
```

### 4. 推送到 GitHub 新仓库
学员想把代码推送到自己新建的 GitHub 仓库：
1. 在 GitHub 网页创建新仓库
2. 设置远程地址：`git remote set-url origin 新地址`
3. 推送：`git push origin main`

### 5. Git 代理设置（VPN）
```bash
git config --global http.proxy http://127.0.0.1:7897
git config --global https.proxy http://127.0.0.1:7897
```

### 6. 克隆仓库练习
学员克隆了队友的仓库：`git@gitee.com:yang9754/job.git`
这是一个 FastAPI 项目，包含：
- app/（应用代码）
- alembic/（数据库迁移）
- static/templates/（静态/模板文件）
- requirements.txt（依赖列表）

## 识别的知识漏洞
- Git 基础操作已比较熟练
- 多人协作流程（Fork + PR）还没学

## 已掌握的 Git 命令
- clone / add / commit / push / pull ✅
- status / branch / switch / merge ✅
- remote 相关操作 ✅

## 今日总结
1. 复习了 Git 基础操作
2. 练习了克隆仓库、创建分支、提交代码
3. 学会了切换远程仓库地址
4. 设置了 Git 代理（Clash Verge 端口 7897）

## 下次继续
```
继续学习，请读取：
1. progress/python-tracker.md
2. sessions/2026-04-25/session-notes.md

上次学完发现：
- Git 基础操作已掌握
- SQLAlchemy 还没学完
- 前端三件套初步了解
```
