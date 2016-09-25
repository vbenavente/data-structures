# -*- coding: utf-8 -*-
import timeit


best_case = [x for x in range(0, 1000)]
worst_case = best_case[::-1]


def insert_sort(l):
    """Sort a list by inserting values in order after comparing each value."""
    if len(l) <= 1:
        return
    else:
        for idx in range(1, len(l)):
            cur = l[idx]
            spot = idx
            while spot > 0 and l[spot - 1] > cur:
                l[spot] = l[spot - 1]
                spot = spot - 1
            l[spot] = cur


if __name__ == '__main__':
    print("Best Case: a list already in order")
    print("number of runs: 1000 / average time: " + str((timeit.Timer(
        "insert_sort(best_case)", setup="from __main__ import insert_sort, best_case").timeit(
            number=1000))/1000))
    print("Worst Case: a list in reverse order")
    print("number of runs: 1000 / average time: " + str(
        (timeit.Timer(
            "insert_sort(worst_case)", setup="from __main__ import insert_sort, worst_case").timeit(
                number=1000))/1000))
