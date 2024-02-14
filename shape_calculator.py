class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def set_width(self, width):
        self._width = width

    def set_height(self, height):
        self._height = height

    def get_area(self):
        return self._width * self._height

    def get_perimeter(self):
        return (self._width * 2) + (self._height * 2)

    def get_diagonal(self):
        return (self._width**2 + self._height**2) ** 0.5

    def get_picture(self):
        if self._width > 50 or self._height > 50:
            return "Too big for picture."
        else:
            picture = ""
            for _ in range(self._height):
                picture += f"{'*' * self._width}" + "\n"
            return picture


class Square:
    pass
