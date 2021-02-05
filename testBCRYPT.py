#!/usr/bin/env python3

import bcrypt
import sys
import time

with open(sys.argv[1], "rb") as f:
    lines = f.readlines()

start = time.time()

for line in lines:
    bcrypt.hashpw(line, bcrypt.gensalt())

end = time.time()
sec = end - start

if sec >= 60:
    print(f"Compute time: {sec // 60} minutes and {sec%60} seconds")
else:
    print(f"Compute time: {sec} seconds")
