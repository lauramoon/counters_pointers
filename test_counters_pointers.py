import unittest
from construct_note import construct_note
from average_pair import average_pair

class testCountersPointers(unittest.TestCase):
    def test_construct_note(self):
        self.assertFalse(construct_note('aa', 'abc'))
        self.assertTrue(construct_note('abc', 'dcba'))
        self.assertTrue(construct_note('aabbcc', 'bcabcaddff'))
        self.assertFalse(construct_note("abcd", ""))
        self.assertTrue(construct_note("", "abc"))
        self.assertTrue(construct_note("skbjjjvnnd", "fdjlkjfeburevjvnfnsjckjncjdnchbechbadhsd"))

    def test_average_pair(self):
        self.assertTrue(average_pair([1, 2, 3], 2.5))
        self.assertTrue(average_pair([1, 3, 3, 5, 6, 7, 10, 12, 19], 8))
        self.assertFalse(average_pair([-1, 0, 3, 4, 5, 6], 4.1))
        self.assertFalse(average_pair([], 4))