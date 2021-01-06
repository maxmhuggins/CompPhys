import unittest
import module

class ModuleTester(unittest.TestCase):
    
    def test_add(self):
        result = module.add(5,2)
        # self.assertEqual(result, 7)
        # self.assertTrue(result, 7)
        self.assertAlmostEqual(result, 6.99999999999)
    def test_divide(self):
        self.assertRaises(ValueError, module.divide, 2,0)
        