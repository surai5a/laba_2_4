#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


print("Write list elements with spaces: ")
a = list(map(int, input().split()))
if not a:
    print("List is empty", file=sys.stderr)
    exit(1)
x = 0
cnt = 0
for i in a:
    if i > 0 and i % 5 == 0:
        x += i
        cnt += 1
if cnt == 0:
    print("List doesn't contain required numbers")
else:
    print(f"List: {a}\nSum of pos numbers mult 5: {x}\nAmount of these nums: {cnt}")
