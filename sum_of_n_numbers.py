import os
import sys
import math


def sum_numbers(numbers):
    x = 0
    assert 1 <= len(numbers) <= math.pow(10, 4), "Number of elements out of range"
    for element in numbers:
        assert 1 <= element <= math.pow(10, 4), "Number of elements out of range"
        x += element
    return x

if __name__ == '__main__':
    alist = [1, 2, 3]
    print(sum_numbers(alist))