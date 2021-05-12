import unittest
from construct_note import construct_note

class testCountersPointers(unittest.TestCase):
    def test_construct_note(self):
        self.assertFalse(construct_note('aa', 'abc'))
        self.assertTrue(construct_note('abc', 'dcba'))
        self.assertTrue(construct_note('aabbcc', 'bcabcaddff'))

        