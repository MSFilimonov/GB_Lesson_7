from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, fab_quantity):
        self.fab_quantity = fab_quantity

    @abstractmethod
    def my_method_1(self):
        print("Тип одежды:", end=' ')

    @abstractmethod
    def my_method_2(self):
        print("Расход ткани:", end=' ')


class Coat(Clothes):
    def my_method_1(self):
        super().my_method_1()
        print("Пальто")

    def my_method_2(self):
        super().my_method_2()
        return float(self.fab_quantity) / 6.5 + 0.5


class Suit(Clothes):
    def my_method_1(self):
        super().my_method_1()
        print("Костюм")

    def my_method_2(self):
        super().my_method_2()
        return 2 * float(self.fab_quantity) + 0.3


class Total:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        return (self.a / 6.5 + 0.5) + (2 * self.b + 0.3)


size_coat = 3
size_suit = 4

print(" ")
c = Coat(size_coat)
c.my_method_1()
print("%.2f" % c.my_method_2())

print(" ")
s = Suit(size_suit)
s.my_method_1()
print("%.2f" % s.my_method_2())

t = Total(size_coat, size_suit)
print("Сумарный расход ткани: %.2f" % t.sum())
