#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


print("Write list elements with spaces: ")
a = list(map(int, input().split()))
if not a:
    print("List is empty", file=sys.stderr)
    exit(1)
x = 1;
for i in a:
    if i < 0:
        x *= i
if x == 1:
    print("List doesn't contain negative numbers")
else:
    print(f"List: {a}\nProduct of negative numbers: {x}")
