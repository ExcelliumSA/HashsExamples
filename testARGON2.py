#!/usr/bin/env python3

import argon2
import bcrypt
import sys
import time

with open(sys.argv[1], "rb") as f:
    lines = f.readlines()

start = time.time()

for line in lines:
    argon2.argon2_hash(line, bcrypt.gensalt(), argon_type=argon2.Argon2Type.Argon2_d)

end = time.time()
sec = end - start

if sec >= 60:
    print(f"Compute time: {sec // 60} minutes and {sec%60} seconds")
else:
    print(f"Compute time: {sec} seconds")
