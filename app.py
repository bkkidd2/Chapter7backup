print("\nChapter 7.2 Creating Classes")


class Point:
    def draw(self):
        print("draw")


point = Point()
print(type(point))
print(isinstance(point, int))


# Chapter 7.3 Constructors
print("\nChapter 7.3 Constructors")


class Point3:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"point ({self.x}, {self.y})")


point = Point3(1, 2)
point.draw()


# Chapter 7.4 Class vs Instance Attributes
print("\Chapter 7.4 Class vs instance Attributes")


class Point4:
    # class attribute
    default_color = "red"

    def __init__(self, x, y):
        # instance attribute
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point({self.x}, {self.y})")


Point4.default_color = "yellow"


point = Point4(1, 2)

print(point.default_color)

print(Point4.default_color)
point.draw()

# insantiate another object of class point()
another = Point4(3, 4)
print(another.default_color)
another.draw()


# chapter 7.5 class vs instance methods
print("Chapter 7.5 Class vs Instance Methods")


class Point5:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def zero(cls):
        return cls(0, 0)

    def draw(self):
        print(f"point ({self.x}, {self.y}")


point = Point5.zero()
point.draw()

# Chapter 7.6
print("\Chapter 7.6 Magic Methods")


class Point6:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point6(1, 2)
print(str(point))

# Chapter 7.7 - 7.11. Nothing to code


# Chapter 7.12 Inheritance
print("Chapter 7.12 Inheritance")


class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):
    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print('swim')


m = Mammal()
m.eat()
print(m.age)

f = Fish()
f.eat()
f.age = 3
print(f.age)
