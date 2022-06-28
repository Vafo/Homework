
import functools


@functools.total_ordering
class Money:

    exchange_rate = {
        "EUR": 1.05,
        "BYN": 0.3,
        "SUM": 9e-5,
        "WON": 7.78e-4,
        "USD": 1.0
    }

    def __init__(self, value, currency = "USD") -> None:
        self.value = value
        self.currency = currency

        if currency not in self.exchange_rate:
            print(f"Currency {currency} is not supported")
            del self

    def __str__(self):
        return f"{self.value:.2f} {self.currency}"

    def __add__(self, other):
        orig_rate = self.exchange_rate[self.currency]
        a = self.value * orig_rate

        if isinstance(other, int):
            b = other
        else:
            b = other.value * other.exchange_rate[other.currency]

        return Money( (a+b)/orig_rate, self.currency )
        
    def __sub__(self, other):
        orig_rate = self.exchange_rate[self.currency]

        a = self.value * orig_rate
        if type(other) is int:
            b = other
        else:
            b = other.value * other.exchange_rate[other.currency]

        return Money( (a-b)/orig_rate, self.currency )

    def __mul__(self, other):
        orig_rate = self.exchange_rate[self.currency]
        
        a = self.value * orig_rate
        if type(other) is int:
            b = other
        else:
            b = other.value * other.exchange_rate[other.currency]

        return Money( (a*b)/orig_rate, self.currency )

    def __truediv__(self, other):
        orig_rate = self.exchange_rate[self.currency]
        
        a = self.value * orig_rate
        if type(other) is int:
            b = other
        else:
            b = other.value * other.exchange_rate[other.currency]

        return Money( (a/b)/orig_rate, self.currency )

    def __eq__(self, other):
        orig_rate = self.exchange_rate[self.currency]
        
        a = self.value * orig_rate
        if type(other) is int:
            b = other
        else:
            b = other.value * other.exchange_rate[other.currency]

        return a == b

    def __gt__(self, other):
        orig_rate = self.exchange_rate[self.currency]
        
        a = self.value * orig_rate
        if type(other) is int:
            b = other
        else:
            b = other.value * other.exchange_rate[other.currency]

        return a > b

a = Money(3000, "WON")
k = Money(12.345, "BYN")

print(a + k + 5)

lst = [Money(10,"BYN"), Money(11), Money(12.01, "USD")]

my_money = sum(lst, Money(0))

print(Money(10, "BYN") + 1)
print(my_money)