#!/usr/bin/env python3

import hashlib
import sys
import time

with open(sys.argv[1], "rb") as f:
    lines = f.readlines()

start = time.time()

for line in lines:
    hashlib.sha1(line)

print(f"Compute time: {time.time()-start} seconds")
