"""Experiments counting the number of comparisons performed by algorithms."""

__author__ = "Sam J. Griffiths"

from algorithms import *
from tabulate import tabulate
import math


def experiment(func, prediction_func):
    """Perform and report a comparison-counting experiment.

    Args:
        func: Algorithm callable of the form func(n).
        prediction_func: Comparison prediction function of the form
        prediction_func(n).

    """
    problem_sizes = [1, 2, 5, 10, 32, 64, 100, 500, 512, 1000, 1024,
                     5000, 8192, 10000]
    results = []

    for n in problem_sizes:
        func(n)
        results.append(compare.count)
        compare.reset_count()

    prediction = list(map(prediction_func, problem_sizes))
    error = [(r - p) for (r, p) in zip(results, prediction)]

    print(tabulate(zip(problem_sizes, results, prediction, error),
                   headers=["n", "comparisons", "predicted", "error"]))


def main():
    """Script entry point."""
    # Linear search (worst case)
    experiment(lambda n: linear_search_iterative([i for i in range(n)], n),
               lambda n: n)

    # Binary search (worst case)
    # experiment(lambda n: binary_search_iterative([i for i in range(n)], n),
    #            lambda n: math.floor(math.log2(n) + 1))

    # Selection sort (all cases)
    # experiment(lambda n: selection_sort([i for i in range(n)]),
    #            lambda n: n * (n - 1) / 2)

    # Insertion sort (worst case)
    # experiment(lambda n: insertion_sort([(n - i - 1) for i in range(n)]),
    #            lambda n: n * (n - 1) / 2)

    # Insertion sort (best case)
    # experiment(lambda n: insertion_sort([i for i in range(n)]),
    #            lambda n: n - 1)

    # Mergesort (worst case)
    # experiment(lambda n: mergesort_recursive(
    #             recursive_pile_shuffle([i for i in range(n)], 2)
    #            ),
    #            lambda n: n * math.floor(math.log2(n) + 1)
    #            - 2**math.floor(math.log2(n) + 1) + 1)

    # Mergesort (best case) - NON-TRIVIAL (correct only for powers of 2)
    # experiment(lambda n: mergesort_recursive([i for i in range(n)]),
    #            lambda n: n / 2 * math.log2(n))

    # Quicksort (worst case)
    # experiment(lambda n: quicksort([i for i in range(n)], False),
    #            lambda n: n * (n - 1) / 2)

    # Quicksort (best case) (correct only for one less than powers of 2)
    # experiment(lambda n: quicksort([i for i in range(n)]),
    #            lambda n: n*math.log2(n+1) + math.log2(n+1) - 2*n)

    # Heapsort (worst case) - NON-TRIVIAL
    # experiment(lambda n: heapsort([i for i in range(n)]),
    #            lambda n: n + n*math.log2(n))


if __name__ == "__main__":
    main()
