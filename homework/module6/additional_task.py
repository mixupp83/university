class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__sides = list(sides)
        self.__color = color
        self.filled = False

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if 255 >= r >= 0 and 255 >= g >= 0 and 255 >= b >= 0:
            return True
        else:
            return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b) is True:
            self.__color = (r, g, b)

    def __is_valid_sides(self, *new_sides):
        if len(new_sides) == self.sides_count and all(side > 0 for side in new_sides):
            return True
        else:
            return False

    def get_sides(self):
        if self.sides_count == 12:
            return [self.__sides[0]] * self.sides_count
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides) is True:
            self.__sides = list(new_sides)

class Circle(Figure):
    sides_count = 1

    def __init__(self, color, radius):
        super().__init__(color, radius)
        self.__radius = radius
    def get_square(self):
        return 3.14 * (self.__radius ** 2)

class Triangle(Figure):
    sides_count = 3
    def __init__(self, color, height):
        super().__init__(color, height)
        self.__height = height
    def get_square(self):
        return 0.5 * self.__height * sum(self.__sides)


class Cube(Figure):
    sides_count = 12
    def __init__(self, color, side):
        super().__init__(color, side)
        self.__side = side
    def get_volume(self):
        return self.__side ** 3


circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)

circle1.set_color(55, 66, 77)
print(circle1.get_color())
cube1.set_color(300, 70, 15)
print(cube1.get_color())

cube1.set_sides(5, 3, 12, 4, 5)
print(cube1.get_sides())
circle1.set_sides(15)
print(circle1.get_sides())

print(len(circle1))

print(cube1.get_volume())