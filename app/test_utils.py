from utils import pointInsideRect as f1
import unittest

class TestPointInsideRect(unittest.TestCase):

    def test_values(self):
        # rwidth
        self.assertRaises(ValueError, f1, (1.5, 1), (1, 1), -3, 5)
        self.assertRaises(ValueError, f1, (1,1), (1,1), 0, 5)
        # rheight
        self.assertRaises(ValueError, f1, (1,1), (1,1), 5, 0)
        self.assertRaises(ValueError, f1, (1,1), (3.14,1), 5, -20)
        
        for wt in [(-2, 0), (0, -1), (3, -100)]:
            # point
            self.assertRaises(ValueError, f1, wt, (1,1), 3, 100)
            # corner
            self.assertRaises(ValueError, f1, (1,1), wt, 3, 100)
            
    def test_result(self):
        self.assertTrue(f1((2,2), (0,0), 5, 3))
        self.assertTrue(f1((2,2), (2,2), 3, 2))

        self.assertFalse(f1((2,2),(0,0), 1, 2))
        self.assertFalse(f1((20, 10.5), (2, 8), 9, 1))

if __name__ == '__main__':
    unittest.main()

