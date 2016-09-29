
# -*- coding: utf-8 -*-
from radix_sort import radix_sort


def test_radix_sort():
    """Test merge sort sorts any list passed in."""
    result = radix_sort([5, 30, 20, 3, 17, 11, 2, 6, 35])
    assert result == sorted([5, 30, 20, 3, 17, 11, 2, 6, 35])
