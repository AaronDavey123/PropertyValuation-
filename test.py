from price_to_sell import valuation

import unittest
from statistics import mean

# Assuming `valuation` function is defined elsewhere in the repo
# from your_module import valuation
class TestValuation(unittest.TestCase):

    def setUp(self):
        print("\nStarting new test...\n")

    def tearDown(self):
        print("Test completed.\n")

    def test_case_1(self):
        reqArea = 1500
        area = [1000, 1500, 1500, 1000, 1500, 2000]
        price = [200000, 300000, 290000, 210000, 310000, 500000]
        expected = 262000
        result = valuation(reqArea, area, price)
        
        if result == expected:
            print(f"test_case_1 passed with result: {result}")
        else:
            print(f"test_case_1 failed: Expected {expected}, but got {result}")
        
        self.assertEqual(result, expected)

    def test_case_2(self):
        reqArea = 1000
        area = [1000, 1000, 1000, 1000, 1000]
        price = [150000, 150000, 150000, 150000, 150000]
        expected = 150000
        result = valuation(reqArea, area, price)
        
        if result == expected:
            print(f"test_case_2 passed with result: {result}")
        else:
            print(f"test_case_2 failed: Expected {expected}, but got {result}")
        
        self.assertEqual(result, expected)

    def test_case_3(self):
        reqArea = 2000
        area = [1500, 2000, 2000, 2000, 1500, 2000, 1500, 1500]
        price = [250000, 400000, 500000, 600000, 240000, 450000, 235000, 250000]
        expected = 365625
        result = valuation(reqArea, area, price)
        
        if result == expected:
            print(f"test_case_3 passed with result: {result}")
        else:
            print(f"test_case_3 failed: Expected {expected}, but got {result}")
        
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
