#!/bin/bash
echo "=== Execute Demonstration ==="
echo "[+] Runner properties"
cat /proc/meminfo | head -1
cat /proc/cpuinfo | grep "model name" | sort -u
for script in test*.py
do
    echo "[+] Execute '$script' ..."
    ./$script ./rockyou_1000.txt
done
exit 0