
class Bird:

    def __init__(self, name) -> None:
        self.name = name

    def fly(self) -> None:
        print(f"{self.name} bird can fly")

    def walk(self) -> None:
        print(f"{self.name} bird can walk")

    def __str__(self) -> str:
        return f"{self.name} can fly, walk"

class FlyingBird(Bird):

    def __init__(self, name, ration = "grains") -> None:
        super().__init__(name)
        self.ration = ration

    def eat(self) -> None:
        print(f"{self.name} eats mostly {self.ration}")

    def __str__(self) -> str:
        return super().__str__() + ", eat"

class NonFlyingBird(Bird):

    def __init__(self, name, ration = "fish") -> None:
        super().__init__(name)
        self.ration = ration

    def swim(self) -> None:
        print(f"{self.name} bird can fly")

    def eat(self) -> None:
        print(f"{self.name} eats mostly {self.ration}")

    def __str__(self) -> str:
        return super().__str__() + ", eat, swim"

class SuperBird(NonFlyingBird, FlyingBird):

    def __init__(self, name) -> None:
        super().__init__(name)

aboba = SuperBird("javoh")
aboba.eat()
print(aboba)

print(SuperBird.__mro__)