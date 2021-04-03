import math


# 1) Python fundamentals

def is_prime(x):
    if x < 2:
        return False

    for i in range(2, x//2 + 1):
        if x % i == 0:
            return False

    return True


def labelled_primes_naive(n, label):
    result = [None] * n

    for i in range(n):
        result[i] = label if is_prime(i) else i

    return result


def labelled_primes_sieve(n, label):
    primes = [True] * n

    for i in range(min(2, n)):
        primes[i] = False

    for i in range(2, n//2 + 1):
        if primes[i]:
            for j in range(i**2, n, i):
                primes[j] = False

    return [label if primes[i] else i for i in range(n)]


def labelled_primes_sieve_inplace(n, label):
    result = [label] * n

    for i in range(min(2, n)):
        result[i] = i

    for i in range(2, n//2 + 1):
        if result[i] == label:
            for j in range(i**2, n, i):
                result[j] = j

    return result


def labelled_primes(n, label):
    # return labelled_primes_naive(n, label)
    # return labelled_primes_sieve(n, label)
    return labelled_primes_sieve_inplace(n, label)


# 2) 'Folding' sort

def insertion_sort(lst, start, end):
    for i in range(start+1, end):
        j = i
        while j > start and lst[j] < lst[j-1]:
            lst[j], lst[j-1] = lst[j-1], lst[j]
            j -= 1


def folding_sort(lst):
    n = len(lst)
    mid = n // 2
    insertion_sort(lst, 0, mid)
    insertion_sort(lst, mid, n)

    for i in range(mid, n - 1):
        temp = lst[i]
        destination = 2*(i - mid) + 1
        j = i
        while j > destination:
            lst[j] = lst[j - 1]
            j -= 1
        lst[destination] = temp

    insertion_sort(lst, 0, n)



def folding_sort_out(lst):
    n = len(lst)
    partitions = [0, math.ceil(n / 2), n]

    insertion_sort(lst, partitions[0], partitions[1])
    insertion_sort(lst, partitions[1], partitions[2])

    result = [None] * n
    result[0::2] = lst[partitions[0]:partitions[1]]
    result[1::2] = lst[partitions[1]:partitions[2]]

    lst[:] = result
    insertion_sort(lst, 0, n)


def folding_sort_k(lst, k=2):
    n = len(lst)
    partitions = [i * math.ceil(n/k) for i in range(k)]
    partitions.append(n)

    for i in range(k):
        insertion_sort(lst, partitions[i], partitions[i+1])

    result = [None] * n
    for i in range(k):
        result[i::k] = lst[partitions[i]:partitions[i+1]]

    lst[:] = result
    insertion_sort(lst, 0, n)


lst = []
folding_sort(lst)
print(lst)


def builtin_sort(lst):
    lst.sort()
