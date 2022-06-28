
class Counter:

    def __init__(self, *, start = None, stop = None) -> None:
        
        self.start = start
        self.stop = stop

        if start == None:
            self.start = 0
        
        if stop == None:
            self.stop = float("inf")

        self.count = self.start

    def increment(self):
        if self.count >= self.stop:
            # Change to exception raise
            print("Maximal value is reached")
        else:
            self.count += 1
        
        return self.count

    def get(self):
        return self.count

c = Counter(start=42)

c.increment()
print(c.get())
c.increment()
print(c.get())

b = Counter(stop=2)
print(b.get())
b.increment()
print(b.get())
b.increment()
print(b.get())
b.increment()
print(b.get())