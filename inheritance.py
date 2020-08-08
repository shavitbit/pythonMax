class Mammal:
    def walk(self):
        print("walk. i am a mammal")


class Dog(Mammal):
    def bark(self):
        print('bark')


class Cat(Mammal):
    def be_annoing(self):
        print("annoying")


dog1 = Dog()
dog1.walk()
dog1.bark()

cat1 = Cat()
cat1.walk()
cat1.be_annoing()
