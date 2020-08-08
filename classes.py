class Point:
    # constructor. self is like this in c#
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def drow(self):
        print("drow")


point1 = Point(10, 20)
point1.drow()
point1.move()
point1.x = 12
point1.y = 13


class Person:
    # constructor. self is like this in c#
    def __init__(self, a_name):
        self.a_name = a_name

    def talk(self):
        print(f"Hi, i am {self.a_name}")


oren = Person("Oren bahar")
oren.talk()
