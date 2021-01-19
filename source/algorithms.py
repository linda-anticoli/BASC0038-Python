"""Provides a variety of common algorithms and utilities relating to them."""

__author__ = "Sam J. Griffiths"

import time


# CORE

class CallCount:
    """Decorator counting the number of times a function is called.

    Attributes:
        function: Callable wrapped.
        count: Number of times function has been called.

    """

    def __init__(self, function):
        """Construct a CallCount instance.

        Args:
            function: Callable to wrap.

        """
        self.function = function
        self.count = 0

    def __call__(self, *args, **kwargs):
        """Call wrapped function."""
        self.count += 1
        return self.function(*args, **kwargs)

    def reset_count(self):
        """Reset the function call count to zero."""
        self.count = 0


@CallCount
def compare(a, b):
    """Compare two values by their natural ordering.

    Args:
        a: First value.
        b: Second value.

    Returns:
        0 if a == b, value less than 0 if a > b, value greater than 1 if a > b.

    """
    return a - b


def time_function(function, runs=1, average=min):
    """Test the average execution time of a given function.

    Args:
        function: Callable to time.
        runs (int, optional): Number of runs. Defaults to 1.
        average (optional): Average function to apply. Defaults to min.

    Returns:
        Function time (average of runs).

    """
    results = [None] * runs
    for i in range(runs):
        t0 = time.perf_counter()
        function()
        t1 = time.perf_counter()
        results[i] = t1 - t0

    return average(results)


def time_function_total(function, runs=1):
    """Test the total execution time of a given function.

    Args:
        function: Function to time.
        runs (int, optional): Number of runs. Defaults to 1.

    Returns:
        Function time (total of runs).

    """
    t0 = time.perf_counter()
    for _ in range(runs):
        function()
    t1 = time.perf_counter()

    return t1 - t0


# SEARCH ALGORITHMS

def linear_search_iterative(array, value):
    """Query if a value is in an array via iterative linear search.

    Args:
        array: List of elements to query.
        value: Value to query presence of.

    Returns:
        True if value is in array, False otherwise.

    """
    for elt in array:
        if compare(elt, value) == 0:
            return True

    return False


def linear_search_recursive(array, value):
    """Query if a value is in an array via recursive linear search.

    Args:
        array: List of elements to query.
        value: Value to query presence of.

    Returns:
        True if value is in array, False otherwise.

    """
    # Base case for empty list
    n = len(array)
    if n == 0:
        return False

    # Recursive case
    if compare(array[0], value) == 0:
        return True
    else:
        return linear_search_recursive(array[1:], value)


def binary_search_recursive(array, value):
    """Query if a value is in an array via recursive binary search.

    Args:
        array: List of elements to query.
        value: Value to query presence of.

    Returns:
        True if value is in array, False otherwise.

    """
    # Base cases for empty or singular list
    n = len(array)
    if n == 0:
        return False
    elif n == 1:
        return compare(array[0], value) == 0

    # Recursive case
    middle = n // 2
    if compare(array[middle], value) == 0:
        return True
    elif compare(array[middle], value) < 0:
        return binary_search_recursive(array[middle + 1:], value)
    else:
        return binary_search_recursive(array[:middle], value)


def binary_search_iterative(array, value):
    """Query if a value is in an array via iterative binary search.

    Args:
        array: List of elements to query.
        value: Value to query presence of.

    Returns:
        True if value is in array, False otherwise.

    """
    # Iteration terminates when (min, max) range has shrunk such that min > max
    min = 0
    max = len(array) - 1
    while min <= max:
        middle = (min + max) // 2
        comparison = compare(array[middle], value)
        if comparison == 0:
            return True
        elif comparison < 0:
            min = middle + 1
        else:
            max = middle - 1

    return False


# SORTING ALGORITHMS

def selection_sort(array):
    """Sort a list via selection sort.

    Args:
        array: Unsorted list.

    Returns:
        A new list containing all elements in array, sorted.

    """
    n = len(array)
    result = array.copy()
    for i in range(n - 1):
        # Find next-smallest value
        smallest = i
        for j in range(i + 1, n):
            if compare(result[j], result[smallest]) < 0:
                smallest = j
        # Swap next-smallest value into position
        if i != smallest:
            result[i], result[smallest] = result[smallest], result[i]

    return result


def selection_sort_recursive(array):
    """Sort a list via recursive selection sort.

    Args:
        array: Unsorted list.

    Returns:
        A new list containing all elements in array, sorted.

    """
    # Base case for empty or singular list
    n = len(array)
    if n < 2:
        return array

    # Find smallest value
    result = array.copy()
    smallest = 0
    for i in range(1, n):
        if compare(result[i], result[smallest]) < 0:
            smallest = i

    # Swap smallest into first position
    if smallest != 0:
        result[0], result[smallest] = result[smallest], result[0]

    # Recur on remainder of array
    return [result[0]] + selection_sort_recursive(result[1:])


def insertion_sort(array):
    """Sort a list via insertion sort.

    Args:
        array: Unsorted list.

    Returns:
        A new list containing all elements in array, sorted.

    """
    n = len(array)
    result = array.copy()

    # Swap each value backwards until in correct position
    for i in range(1, n):
        j = i
        while j > 0 and compare(result[j], result[j - 1]) < 0:
            result[j], result[j - 1] = result[j - 1], result[j]
            j -= 1

    return result


def merge(a, b):
    """Merge two sorted lists into one.

    Args:
        a: First sorted list.
        b: Second sorted list.

    Returns:
        A new list containing all elements in a and b, sorted.

    """
    result = []

    # Append smallest values to result until either list is exhausted
    i = j = 0
    while i < len(a) and j < len(b):
        if compare(a[i], b[j]) < 0:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1

    # Append all remaining values from the unexhausted list
    if i < len(a):
        result.extend(a[i:])
    else:
        result.extend(b[j:])

    return result


def mergesort_recursive(array):
    """Sort a list via recursive (top-down) mergesort.

    Args:
        array: Unsorted list.

    Returns:
        A new list containing all elements in array, sorted.

    """
    # Base case for empty or singular list
    n = len(array)
    if n < 2:
        return array

    # Recur on two halves of array and merge results
    mid = n // 2
    return merge(
        mergesort_recursive(array[:mid]),
        mergesort_recursive(array[mid:]))


# MISCELLANEA

def pile_shuffle(array, n):
    """Shuffle a list by partition into n piles.

    Args:
        array: List to shuffle.
        n: Number of piles.

    Returns:
        A new shuffled list.

    """
    result = []
    for i in reversed(range(n)):
        result += array[i::n]

    return result


def recursive_pile_shuffle(array, n):
    """Shuffle a list by recursively pile-shuffling each pile.

    Args:
        array: List to shuffle.
        n: Number of piles.

    Returns:
        A new shuffled list.

    """
    # Base case for empty or singular list
    if len(array) < 2:
        return array

    # Pile-shuffle and recur on each of n piles
    piles = [array[i::n] for i in reversed(range(n))]
    result = []
    for pile in piles:
        result += recursive_pile_shuffle(pile, n)

    return result
