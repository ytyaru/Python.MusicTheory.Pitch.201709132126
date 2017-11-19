import unittest
from MusicTheory.pitch.Degree import Degree
"""
Degreeのテスト。
"""
class TestDegree(unittest.TestCase):
    def test_TestGetClassMethod(self):
        print(f'aaaaaaaaaaa: "{Degree.TestGetClassMethod}"')
        self.assertEqual(11, Degree.TestGetClassMethod)
#        self.assertEqual(11, Degree.TestGetClassMethod())#こっちだと成功する。プロパティとして見てくれない。困る。
    def test_TestGetClassProperty(self):
        print(f'bbbbbbbbbbb: "{Degree.TestGetClassProperty}"')
        self.assertEqual(11, Degree.TestGetClassProperty)


if __name__ == '__main__':
    unittest.main()
