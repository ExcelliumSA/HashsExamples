#!/usr/bin/env python3

import bcrypt
import sys
import time

with open(sys.argv[1], "rb") as f:
    lines = f.readlines()

start = time.time()

decode = False
try:
    bcrypt.hashpw(lines[0], bcrypt.gensalt())
except TypeError:
    decode = True

for line in lines:
    if decode:
        bcrypt.hashpw(line.decode(), bcrypt.gensalt())
    else:
        bcrypt.hashpw(line, bcrypt.gensalt())

end = time.time()
sec = end - start

if sec >= 60:
    print(f"Compute time: {sec // 60} minutes and {sec%60} seconds")
else:
    print(f"Compute time: {sec} seconds")
