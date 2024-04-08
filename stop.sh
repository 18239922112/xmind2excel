#!/bin/sh
for pid in `ps -ef|grep x2e.py|grep -v grep|awk '{print $2}'`
do
  kill -9 $pid
done
echo "x2e server 已停止"