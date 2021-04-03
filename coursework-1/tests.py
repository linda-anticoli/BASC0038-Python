import unittest
import algorithms as a


class TestExercise1(unittest.TestCase):
    label = "p"
    primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59,
              61, 67, 71, 73, 79, 83, 89, 97}

    def test_negative(self):
        self.assertEqual(a.labelled_primes(-1, self.label),
                         [])

    def test_zero(self):
        self.assertEqual(a.labelled_primes(0, self.label),
                         [])

    def test_one(self):
        self.assertEqual(a.labelled_primes(1, self.label),
                         [0])

    def test_two(self):
        self.assertEqual(a.labelled_primes(2, self.label),
                         [0, 1])

    def test_three(self):
        self.assertEqual(a.labelled_primes(3, self.label),
                         [0, 1, self.label])

    def test_odd_n(self):
        self.assertEqual(a.labelled_primes(99, self.label),
                         [self.label if i in self.primes else i
                          for i in range(99)])

    def test_even_n(self):
        self.assertEqual(a.labelled_primes(100, self.label),
                         [self.label if i in self.primes else i
                          for i in range(100)])


class TestExercise2(unittest.TestCase):
    def _sort(self, lst):
        original = lst.copy()
        a.folding_sort(lst)
        return original, lst

    def test_empty(self):
        orig, srtd = self._sort([])
        self.assertEqual(srtd, orig)

    def test_singular(self):
        orig, srtd = self._sort([0])
        self.assertEqual(srtd, orig)

    def test_two(self):
        orig, srtd = self._sort([1, 0])
        self.assertEqual(srtd, sorted(orig))

    def test_sorted(self):
        orig, srtd = self._sort([-4, -2, -1, 0, 1, 2, 4, 8, 24])
        self.assertEqual(srtd, orig)

    def test_reverse(self):
        orig, srtd = self._sort([24, 8, 4, 2, 1, 0, -1, -2, -4])
        self.assertEqual(srtd, sorted(orig))


class TestExercise3(unittest.TestCase):
    def _sort(self, lst):
        original = lst.copy()
        a.introsort(lst)
        return original, lst

    def test_empty(self):
        orig, srtd = self._sort([])
        self.assertEqual(srtd, orig)

    def test_singular(self):
        orig, srtd = self._sort([0])
        self.assertEqual(srtd, orig)

    def test_two(self):
        orig, srtd = self._sort([1, 0])
        self.assertEqual(srtd, sorted(orig))

    def test_sorted(self):
        orig, srtd = self._sort([-4, -2, -1, 0, 1, 2, 4, 8, 24])
        self.assertEqual(srtd, orig)

    def test_reverse(self):
        orig, srtd = self._sort([24, 8, 4, 2, 1, 0, -1, -2, -4])
        self.assertEqual(srtd, sorted(orig))


if __name__ == "__main__":
    unittest.main()
