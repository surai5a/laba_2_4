#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


print("Write list elements with spaces: ")
a = list(map(int, input().split()))
if not a:
    print("List is empty", file=sys.stderr)
    exit(1)
ind_1, ind_2 = 11, 11
min = min(a)
min_ind = a.index(min)
sum = 0;
for ind, val in enumerate(a):
    if val < 0 and ind_1 == 11:
        ind_1 = ind
    elif val < 0 and (ind_1 != 11 and ind_2 == 11):
        ind_2 = ind
for i in a[ind_1 + 1:ind_2]:
    sum += i
print(f"Original list: {a}\nMinimal element index: a[{min_ind}] = {min}\n"
      f"Sum of numbers, between 1st and 2nd elements: {sum}")