@echo off
echo 正在上传项目到GitHub...

REM 初始化Git仓库
echo 初始化Git仓库...
git init

REM 添加远程仓库
echo 添加远程仓库...
git remote add origin https://github.com/zg919506719/FastApiAndroid.git

REM 添加所有文件
echo 添加文件到暂存区...
git add .

REM 提交更改
echo 提交更改...
git commit -m "Initial commit: Baby Monitor Project with FastAPI backend and Android app"

REM 设置默认分支为main
echo 设置默认分支...
git branch -M main

REM 推送到GitHub
echo 推送到GitHub...
git push -u origin main

echo 上传完成！
echo 项目已成功上传到: https://github.com/zg919506719/FastApiAndroid.git
pause
