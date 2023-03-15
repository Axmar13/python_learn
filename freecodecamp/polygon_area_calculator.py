class Rectangle:
    
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height

    def __str__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"
    
    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self) -> int:
        return self.width * self.height

    def get_perimeter(self) -> int:
        return (2 * self.width + 2 * self.height)

    def get_diagonal(self) -> int:
        return ((self.width ** 2 + self.height ** 2) ** .5)

    def get_picture(self) -> str:
       if self.width > 50 or self.height > 50:
           return "Too big for picture."
       string = (("*" * self.width) + "\n") * self.height
       return string

    def get_amount_inside(self, Rectangle) -> int:
        return int(self.get_area()) // int(Rectangle.get_area()) 


class Square(Rectangle):
  
    def __init__(self, side):
        super().__init__(side, side)   # llama a __init__ de Rectangle y setea width = side, height = side.
    
    def __str__(self) -> str:
        return f"Square(side={self.width})"
    
    def set_side(self, side):
        self.set_height(side)          # aca podes cambiar super() por self, ya que Square hereda set_height y set_width de Rectangle.
        self.set_width(side)    


rec = Rectangle(10, 10)
print(rec.get_picture())

sqr = Square(3)
print(sqr.get_picture())
print(sqr.get_picture())


