#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import deque, OrderedDict
import timeit

BEST_CASE = [x for x in range(0, 1000)]
WORST_CASE = [123, 333, 444, 555, 666, 10000000000000000]


def radix_sort(my_list):
    """Implement radix sort in python."""
    buckets = OrderedDict()
    for _ in range(10):
        buckets[str(_)] = deque()
    max_digit_num = len(str(max(my_list)))
    my_list = [str(item).zfill(max_digit_num) for item in my_list]
    c = 0
    while c < max_digit_num:
        for item in my_list:
            digit = item[-(c + 1)]
            buckets[digit].append(item)
        my_list = []
        for queue in buckets.values():
            while len(queue) > 0:
                my_list.append(queue.popleft())
        c += 1

    return [int(item) for item in my_list]


if __name__ == '__main__':  # pragma: no cover
    print("Best Case: a list already in order")
    print("number of runs: 1000 / average time: " + str((timeit.Timer(
        "radix_sort(BEST_CASE)", setup="from __main__ import radix_sort, BEST_CASE").timeit(
            number=1000))/1000))
    print("Worst Case: a list in reverse order")
    print("number of runs: 1000 / average time: " + str(
        (timeit.Timer(
            "radix_sort(WORST_CASE)", setup="from __main__ import radix_sort, WORST_CASE").timeit(
                number=1000)/1000)))
