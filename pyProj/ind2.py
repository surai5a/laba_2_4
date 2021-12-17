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
    max_ind = a.index(max(a))
    sum_obj = 0
    x = 1
    for i in a:
        if i < 0:
            x *= i
    if x == 1:
        x = "No required numbers"
    print(max_ind)
    for i, item in enumerate(a):
        if i == max_ind:
            break
        else:
            if item > 0:
                sum_obj += item
    if sum_obj == 0:
        sum_obj = "There are no required numbers before max element"
    print(
        f"Original list: {a}\nReverted list: {rev}\n"
        f"Product of negative elements: {x}\n"
        f"Sum of positive numbers, before maximum element: {sum_obj}"
        )
