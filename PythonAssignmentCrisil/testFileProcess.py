import unittest
import os


class MyTestCase(unittest.TestCase):
    def test_main(self):
        result = os.system("python FileProcessUtil.py test1.txt")
        print("return :"+str(result))
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()
