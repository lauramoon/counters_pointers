import unittest
from construct_note import construct_note
from average_pair import average_pair
from two_array_object import two_array_object
from same_frequency import same_frequency
from separate_positive import separate_positive
from is_subsequence import is_subsequence
from count_pairs import count_pairs

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

    def test_two_array_object(self):
        self.assertEqual(two_array_object(["a", "b", "c"], [1, 2, 3]), {"a": 1, "b": 2, "c": 3})
        self.assertEqual(two_array_object(["a", "b", "c"], [1, 2, 3, 4]), {"a": 1, "b": 2, "c": 3})
        self.assertEqual(two_array_object(["a", "b", "c", "d"], [1, 2, 3]), {"a": 1, "b": 2, "c": 3, "d": None})

    def test_same_frequency(self):
        self.assertTrue(same_frequency(182, 281))
        self.assertTrue(same_frequency(3589578, 5879385))
        self.assertFalse(same_frequency(34, 14))
        self.assertFalse(same_frequency(22, 222))

    def test_separate_positive(self):
        self.assertEqual(separate_positive([1, 2, 3]), [1, 2, 3])
        self.assertEqual(separate_positive([-1, -2, -3]), [-1, -2, -3])
        self.assertEqual(separate_positive([2, -1, -3, 6, -8, 10]), [2, 10, 6, -3, -8, -1])
        self.assertEqual(separate_positive([5, 10, -15, 20, 25]), [5, 10, 25, 20, -15])

    def test_is_subsequence(self):
        self.assertTrue(is_subsequence("hello", "hello world"))
        self.assertTrue(is_subsequence("sing", "sting"))
        self.assertTrue(is_subsequence("abc", "abracadabra"))
        self.assertFalse(is_subsequence("abc", "acb"))
        self.assertFalse(is_subsequence("notasubstring", "banana"))
        self.assertFalse(is_subsequence("almost", "almossssss"))

    def test_count_pairs(self):
        self.assertEqual(count_pairs([1, 2, 3, 4, 5], 10), 0)
        self.assertEqual(count_pairs([1, 2, 3, 4, 5], 10), 0)
        self.assertEqual(count_pairs([4, 6, 2, 7], 10), 1)
        self.assertEqual(count_pairs([0, -4], -4), 1)
        self.assertEqual(count_pairs([3, 1, 5, 4, 2], 6), 2)
        self.assertEqual(count_pairs([1, 2, 3, 0, -1, -2], 0), 2)
        self.assertEqual(count_pairs([10, 4, 8, 2, 6, 0], 10), 3)
