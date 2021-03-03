#!/bin/bash
echo "=== Execute Demonstration ==="
for script in test*.py
do
    echo "[+] Execute '$script' ..."
    $($script ./rockyou_1000.txt)
done
exit 0