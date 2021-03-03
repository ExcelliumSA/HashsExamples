#!/bin/bash
echo "=== Execute Demonstration ==="
echo "[+] Runner properties"
echo "Memory: $(cat /proc/meminfo | head -1 | cut -d':' -f2)"
echo "CPU: $(cat /proc/cpuinfo | grep "model name" | sort -u | cut -d':' -f2)"
for script in test*.py
do
    echo "[+] Execute '$script' ..."
    ./$script ./rockyou_1000.txt
done
exit 0