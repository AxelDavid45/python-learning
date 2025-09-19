class Square:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height


square = Square(20, 20)
# update directly
square.height = 40
print(square.get_area())


class Figure:
    """Inheritance"""

    def __init__(self, width, height):
        self.width = width
        self.height = height


class Square2(Figure):
    """Inheritance"""

    def __init__(self, width):
        super().__init__(width, width)

    def get_area(self):
        return self.height * self.height


new_square = Square2(20)

print(new_square.get_area())
