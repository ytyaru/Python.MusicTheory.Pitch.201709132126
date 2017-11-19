"""
変化記号から相対半音数を取得する。
"""
class Accidental:
    #将来_Accidentalsを定数化したい（_Accidentalsをreadonlyにし、immutableな辞書にしたい）
    _Accidentals = {None: 0, '':0, '♯': 1, '#': 1, '+': 1, '♭': -1, 'b': -1, '-': -1}
    @classmethod
    def Get(cls, accidental:str):
        cls.__CheckParameter(accidental)
        return sum([cls._Accidentals[c] for c in accidental])
    @classmethod
    def __CheckParameter(cls, accidental):
        if None is accidental or 0 == len(accidental): return
        if not isinstance(accidental, str): raise Exception(f'引数accidentalは次のような文字列のみ許されます。: {cls._Accidentals.keys()}')
        cls.__IsSameChars(accidental)
        if accidental[0] not in cls._Accidentals.keys(): raise Exception(f'引数accidentalに使える文字は次のものだけです。: {cls._Accidentals.keys()}')
    @classmethod
    def __IsSameChars(cls, accidental):
        for c in accidental:
            if c != accidental[0]: raise Exception(f'引数accidentalは同じ文字のみ連続使用を許されます。異なる文字を混在させることはできません。: {accidental}')
        return True
