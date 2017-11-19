from Framework.ClassProperty import ClassProperty
#クラスプロパティを実装するためのメタクラス
class ClassPropertyMeta(type):
    def __new__(cls, name, bases, namespace):
        props = [(k, v) for k, v in namespace.items() if type(v) == ClassProperty]
        for k, v in props:
            setattr(cls, k, v)
            del namespace[k]
        return type.__new__(cls, name, bases, namespace)

