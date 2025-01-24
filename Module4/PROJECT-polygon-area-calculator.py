class Rectangle:
    def __init__(self, width, height):
        self.set_width(width)
        self.set_height(height)

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        return ('*' * self.width + '\n') * self.height

    def get_amount_inside(self, other):
        amount_inside_width = self.width // other.width
        amount_inside_height = self.height // other.height
        return amount_inside_width * amount_inside_height

    def __str__(self):
        return f'{self.__class__.__name__}(width={self.width}, height={self.height})'


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(width=side, height=side)
        self.set_side(side)

    def set_side(self, side):
        self.side = side
        super().set_width(side)
        super().set_height(side)

    def set_width(self, side):
        self.set_side(side)

    def set_height(self, side):
        self.set_side(side)

    def __str__(self):
        return f'{self.__class__.__name__}(side={self.side})'


rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
