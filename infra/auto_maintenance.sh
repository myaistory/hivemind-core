#!/bin/bash
cd ~/hivemind
# 1. 检查 API 存活
if ! pgrep -f uvicorn > /dev/null; then
  nohup /home/lianwei_zlw/.local/bin/uvicorn core.api_server:app --host 127.0.0.1 --port 8000 > ~/api.log 2>&1 &
fi
# 2. 自动提交代码 (如果代码有变动)
git add .
git diff-index --quiet HEAD || git commit -m "System: Autonomous maintenance and sync" && git push origin main
