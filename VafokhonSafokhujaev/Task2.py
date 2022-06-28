
class HistoryDict():

    def __init__(self, iterable = None, /, **kwargs) -> None:
        self.dict = {}
        self.index = 0
        self.history = []

        if iterable is not None:
            if not isinstance(iterable, dict):
                print("Dictionary is expected")
            else:
                for key, val in iterable.items():
                    self.dict[key] = val

        for key, val in kwargs.items():
            self.dict[key] = val

    def set_value(self, key, val):
        self.dict[key] = val
        
        if self.index >= len(self.history):
            self.history.append(None)

        self.history[self.index] = key
        self.index += 1
        if self.index >= 10:
            self.index = 0

        return self.dict[key]

    def get_history(self) -> list:
        return self.history[self.index - 1::-1] + self.history[:self.index - 1:-1]

d = HistoryDict({"foo": 123})
d.set_value("bar", 43)
d.set_value("abab", 4443)
d.set_value("dBABBA", 41233)
d.set_value("adwawdw", 41233)
print(d.get_history())