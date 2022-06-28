
class Sun:
    _instance = None

    @classmethod
    def inst(cls):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
        
        return cls._instance

a = Sun.inst()
b = Sun.inst()

print(a is b)