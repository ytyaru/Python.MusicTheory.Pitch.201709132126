import re
#import MusicTheory.pitch.PitchClass
#import MusicTheory.pitch.Accidental
from MusicTheory.pitch.PitchClass import PitchClass
from MusicTheory.pitch.Accidental import Accidental
from Framework.ClassProperty import ClassProperty
from Framework.ClassPropertyMeta import ClassPropertyMeta
"""
音度から半音数を取得する。
"""
class Degree(metaclass=ClassPropertyMeta):
    _Pattern = re.compile(r'[1-9][0-9]*')
    _Degrees = ((1,0),(2,2),(3,4),(4,5),(5,7),(6,9),(7,11))
    
    @classmethod
    def TestGetClassMethod(cls): return PitchClass.MaxPitchClass
    @ClassProperty
    def TestGetClassProperty(cls): return PitchClass.MaxPitchClass
    
    @classmethod
    def Get(cls, name:str):
        d, a = cls.__Split(name)
        degree = cls.__GetDegree(d)
        accidental = Accidental.Accidental.Get(a)
        return degree + accidental
        
    @classmethod
    def __Split(cls, name):
        match = cls._Pattern.search(name)
        if not(match): raise Exception('引数nameに数字が含まれていません。1〜14までの自然数を含めてください。')
        return (name[match.start():match.end()+1], name[:match.start()])

    @classmethod
    def __GetDegree(cls, degree_str):
        degree = int(degree_str)
        if 0 < degree and degree < 8: return cls.__GetDefaultHalfToneNum(degree)
        elif 7 < degree and degree < 15: return cls.__GetDefaultHalfToneNum(degree - 7) + 12
        else: raise Exception(f'degreeは1〜14までの自然数のみ有効です。degree={degree}')

    #定数のようにしたい: readonlyにしたい。クラス・プロパティにして()不要にし、名前を"Degrees"にしたい。
    #(音度,半音数(PitchClass))
    @classmethod
    def GetList(cls): return cls._Degrees
    
    @classmethod
    def __GetDefaultHalfToneNum(cls, degree):
        for d in cls.GetList():
            if d[0] == degree: return d[1]
        raise Exception('引数degreeは1〜7までの自然数のみ有効です。')


if __name__ == '__main__':
    print(Degree.GetList())
    for degree in range(1, 8):
        for accidental in Accidental.Accidental._Accidentals.keys():
            if None is accidental: continue
            degreeName = accidental+str(degree)
            print(degreeName, Degree.Get(degreeName))
    
    print('----- エラー確認 -----')
    for degreeName in ['無効な音度名', '無効な音度名1', '無無無無1', '#b1']:
        try: print(degreeName, Degree.Get(degreeName))
        except Exception as e: print(degreeName + ':', e)
    
    """
#    degreeName = '無効な音度名'#Exception: 引数nameに数字が含まれていません。1〜14までの自然数を含めてください。
#    degreeName = '無効な音度名1'#Exception: 引数accidentalは同じ文字のみ連続使用を許されます。異なる文字を混在させることはできません。: 無効な音度名
    degreeName = '無無無無1'#Exception: 引数accidentalに使える文字は次のものだけです。: dict_keys([None, '', '♯', '#', '+', '♭', 'b', '-'])
    print(degreeName, Degree.Get(degreeName))
    """
