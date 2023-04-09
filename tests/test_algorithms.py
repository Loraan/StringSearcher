import unittest
from algorithms import BruteForce as BF, \
    KnuthMorrisPratt as KMP, \
    RabinKarp as RK, \
    BoyerMoore as BM, \
    BoyerMooreHorspul as BMH


TEXT = "Hello, lets try to do this"


class TestStringMethods(unittest.TestCase):
    def test_brute_force(self):
        bf = BF(TEXT, 'o').run()
        self.assertEqual(bf, 4)
        bf = BF(TEXT, 'ts').run()
        self.assertEqual(bf, 9)
        bf = BF(TEXT, 'at').run()
        self.assertEqual(bf, -1)

    def test_knuth_morris_pratt(self):
        kmp = KMP(TEXT, 'o').run()
        self.assertEqual(kmp, 4)
        kmp = KMP(TEXT, 'ts').run()
        self.assertEqual(kmp, 9)
        kmp = KMP(TEXT, 'at').run()
        self.assertEqual(kmp, -1)

    def test_rabin_karp(self):
        rk = RK(TEXT, 'o').run()
        self.assertEqual(rk, 4)
        rk = RK(TEXT, 'ts').run()
        self.assertEqual(rk, 9)
        rk = RK(TEXT, 'at').run()
        self.assertEqual(rk, -1)

    def test_boyer_moore(self):
        bm = BM(TEXT, 'o').run()
        self.assertEqual(bm, 4)
        bm = BM(TEXT, 'ts').run()
        self.assertEqual(bm, 9)
        bm = BM(TEXT, 'at').run()
        self.assertEqual(bm, -1)

    def test_boyer_moore_horspul(self):
        bmh = BMH(TEXT, 'o').run()
        self.assertEqual(bmh, 4)
        bmh = BMH(TEXT, 'ts').run()
        self.assertEqual(bmh, 9)
        bmh = BMH(TEXT, 'at').run()
        self.assertEqual(bmh, -1)


if __name__ == '__main__':
    unittest.main()
