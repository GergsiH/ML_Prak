#test_range.py
import unittest
from range import Range

class TestRange(unittest.TestCase):

    def test_create_range(self):
        r = Range(1, 5)
        self.assertEqual(r.start, 1)
        self.assertEqual(r.end, 5)

    def test_is_empty(self):
        r1 = Range(5, 3)  # Empty range
        r2 = Range(1, 5)
        self.assertTrue(r1.is_empty())
        self.assertFalse(r2.is_empty())

    def test_contains(self):
        r = Range(1, 5)
        self.assertTrue(r.contains(3))
        self.assertFalse(r.contains(6))

    def test_intersect(self):
        r1 = Range(1, 5)
        r2 = Range(4, 7)
        intersection = r1.intersect(r2)
        self.assertEqual(str(intersection), "[4; 5]")

        r3 = Range(6, 8)
        intersection_empty = r1.intersect(r3)
        self.assertEqual(str(intersection_empty), "[0; -1]")  # Empty range

    def test_union(self):
        r1 = Range(1, 5)
        r2 = Range(4, 7)
        union = r1.union(r2)
        self.assertEqual(str(union), "[1; 7]")

        r3 = Range(8, 10)
        union_non_intersecting = r1.union(r3)
        self.assertEqual(str(union_non_intersecting), "[1; 10]")

if __name__ == "__main__":
    unittest.main()
