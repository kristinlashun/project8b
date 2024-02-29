# Author: Kristin Towns
# GitHub: kristinlashun
# Date: 2/28/2024
"""
Description: This script demonstrates the use of decorators to time sorting algorithm functions,
specifically bubble sort and insertion sort. It includes a sort_timer decorator to measure execution time,
bubble_sort and insertion_sort functions decorated to be timed, and functionality to compare these algorithms'
performance across varying list sizes with visualization using matplotlib. The script generates and sorts random
lists of integers, then visualizes the time taken by each sorting algorithm to sort these lists as the list sizes increase.
"""

import time
import random
from functools import wraps
from matplotlib import pyplot as plt

def sort_timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        func(*args, **kwargs)
        end_time = time.perf_counter()
        return end_time - start_time
    return wrapper

@sort_timer
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

@sort_timer
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

def make_lists_of_sort_times(sort_func1, sort_func2, list_of_lengths):
    times1 = []
    times2 = []
    for n in list_of_lengths:
        arr = [random.randint(1, 10000) for _ in range(n)]
        arr_copy = arr.copy()

        time1 = sort_func1(arr)
        time2 = sort_func2(arr_copy)

        times1.append(time1)
        times2.append(time2)
    return (times1, times2)

def compare_sorts(sort_func1, sort_func2):
    list_of_lengths = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
    times1, times2 = make_lists_of_sort_times(sort_func1, sort_func2, list_of_lengths)

    plt.plot(list_of_lengths, times1, 'ro--', linewidth=2, label='Bubble Sort')
    plt.plot(list_of_lengths, times2, 'go--', linewidth=2, label='Insertion Sort')
    plt.xlabel("Number of elements")
    plt.ylabel("Time in seconds")
    plt.legend(loc='upper left')
    plt.show()

def main():
    compare_sorts(bubble_sort, insertion_sort)

if __name__ == "__main__":
    main()
