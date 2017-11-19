import unittest
from MusicTheory.pitch.PitchClass import PitchClass
"""
PitchClassのテスト。
"""
class TestPitchClass(unittest.TestCase):
    def test_MaxPitchClass(self):
        self.assertEqual(11, PitchClass.MaxPitchClass)
    def test_MinPitchClass(self):
        self.assertEqual(0, PitchClass.MinPitchClass)
    def test_PitchClass(self):
        pitch_class = PitchClass.Get(0)
        self.assertTrue(hasattr(pitch_class, 'PitchClass'))
        self.assertTrue(hasattr(pitch_class, 'RelativeOctave'))
        #名前は変更されるかもしれない。この名前が最適か判断つかない。仮名である。（テストになっていない）
    def test_Get(self):
        for halfToneNum in range(12):
            self.assertEquals((halfToneNum, 0), PitchClass.Get(halfToneNum))
    def test_Get_Plus(self):
        self.assertEquals((11, 0), PitchClass.Get(11))
        self.assertEquals((0, 1), PitchClass.Get(12))
        self.assertEquals((1, 1), PitchClass.Get(13))
        self.assertEquals((11, 1), PitchClass.Get(23))
        self.assertEquals((0, 2), PitchClass.Get(24))
        for halfToneNum in range(12, 12*3):
            self.assertEquals((halfToneNum % 12, halfToneNum // 12), PitchClass.Get(halfToneNum))
    def test_Get_Minus(self):
        self.assertEquals((11, -1), PitchClass.Get(-1))
        self.assertEquals((10, -1), PitchClass.Get(-2))
        self.assertEquals((0, -1), PitchClass.Get(-12))
        self.assertEquals((11, -2), PitchClass.Get(-13))
        self.assertEquals((0, -3), PitchClass.Get(-12*3))
        for halfToneNum in range(-12*3, 0):
            expect = halfToneNum % 12
            if expect < 0: expect += 12
            self.assertEquals((expect, halfToneNum // 12), PitchClass.Get(halfToneNum))
    def test_Get_str(self):
        with self.assertRaises(TypeError) as e: #TypeError: not all arguments converted during string formatting
            PitchClass.Get('無効値')
            self.assertEquals(e.message, '')


if __name__ == '__main__':
    unittest.main()
