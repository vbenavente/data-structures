# -*- coding: utf-8 -*-
"""The following code implements an insertion_sort function designed
to be used on a standart Python list."""
from __future__ import unicode_literals
import random
import datetime


def insertion_sort(sort_lst):
    if not isinstance(sort_lst, list):
        raise TypeError("Your input must be a Python list.")
    sort_position = -1
    while sort_position < len(sort_lst):
        sort_position += 1
        comp_indx = sort_position + 1
        while comp_indx < len(sort_lst):
            if sort_lst[comp_indx] < sort_lst[sort_position]:
                sort_lst[comp_indx], sort_lst[sort_position] = sort_lst[sort_position], sort_lst[comp_indx]
            else:
                comp_indx += 1
    return sort_lst


if __name__ == "__main__":

    demo_list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    demo_list_2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    demo_list_3 = random.sample(range(1000), random.randrange(2, 500))
    demo_list_4 = random.sample(range(100000), random.randrange(2, 10000))

    """The insertion_sort method sorts individual items in a list by their
    value, from smallest to largest, until the entire list is sorted.  It
    performs best in very short lists.

    Below you'll find a demonstration of best case, worst case and random
    scenarios."""
    print("")
    print("Input for insertion_sort: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]")
    time_1 = datetime.datetime.now()
    print("Output:", insertion_sort(demo_list_1))
    time_2 = datetime.datetime.now()
    print("Run time:", time_2 - time_1)
    print("")
    print("Input for insertion_sort: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]")
    time_3 = datetime.datetime.now()
    print("Output:", insertion_sort(demo_list_2))
    time_4 = datetime.datetime.now()
    print("Run time:", time_4 - time_3)
    print("")
    print("Input for insertion_sort: random.sample(range(1000), random.randrange(2, 500))")
    time_5 = datetime.datetime.now()
    print("Output:", insertion_sort(demo_list_3))
    time_6 = datetime.datetime.now()
    print("Run time:", time_6 - time_5)
    print("")
    print("Input for insertion_sort: random.sample(range(100000), random.randrange(2, 10000))")
    time_7 = datetime.datetime.now()
    print("Output:", insertion_sort(demo_list_4))
    time_8 = datetime.datetime.now()
    print("Run time:", time_8 - time_7)
