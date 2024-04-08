#!/bin/sh
echo "获取根路径"
APP_BASE=$(cd "$(dirname "$0")"; pwd)
echo "根路径是:"$APP_BASE

LOG_DIR="$APP_BASE/log"
if [ ! -d "$LOG_DIR" ]; then
        echo $LOG_DIR"不存在,即将创建"
        mkdir $LOG_DIR
fi

echo "开始启动"
nohup python3 x2e.py > $APP_BASE/log/x2e.log 2>&1 &
echo "x2e server 启动成功 !"