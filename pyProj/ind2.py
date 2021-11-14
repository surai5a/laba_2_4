#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    print("Write list elements with spaces: ")
    a = list(map(int, input().split()))
    if not a:
        print("List is empty", file=sys.stderr)
        exit(1)
    rev = a.copy()
    rev.reverse()
    maxInd = a.index(max(a))
    sumObj = 0
    x = 1
    for i in a:
        if i < 0:
            x *= i
    if x == 1:
        x = "No required numbers"
    for i in a:
        if a.index(i) == maxInd:
            break
        else:
            if i > 0:
                sumObj += i
    if sumObj == 0:
        sumObj = "There are no required numbers before max element"
    print(f"Original list: {a}\nReverted list: {rev}\n"
          f"Product of negative elements: {x}\n"
          f"Sum of positive numbers, before maximum element: {sumObj}")
