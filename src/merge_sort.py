""" This module will implement a merge sort on a list"""
# This solution was heavily influenced by the example found on interactive
# python found at the URL below. I've attempted to make the function a class
# with a recursive method:
# http://interactivepython.org/runestone/static/pythonds/SortSearch/TheMergeSort.html


class MergeSort(object):

    def merge_sort(self, merge_list):
        """This function will call the recursive merge sort method and returb a
        sorted list"""
        if len(merge_list) <= 1:
            mid_point = len(merge_list) // 2
            left = merge_list[:mid_point]
            right = merge_list[mid_point:]

        self._merge_sort_recursive(merge_list, left, right)
        self._merge_sort_recursive(merge_list, left, right)

    def _merge_sort_recursive(self, merge_list, left, right):

        """This is the recurssive method that will operate on the list to merge
        sort the supplied list"""

        left_i = 0
        right_i = 0
        ml_i = 0

        while left_i < len(left) and right_i < len(right):
            if left[left_i] < right[right_i]:
                merge_list[ml_i] = left[left_i]
                left_i += 1
            else:
                merge_list[ml_i] = right[right_i]
                right_i += 1
            ml_i += 1

        while left_i < len(left):
            merge_list[ml_i] = left[left_i]
            left_i += 1
            ml_i += 1

        while right_i < len(right):
            merge_list[ml_i] = right[right_i]
            right_i += 1
            ml_i += 1

        return merge_list
