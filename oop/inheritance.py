class shape:
    def __init__(self,color,is_filled):
        self.color = color
        self.is_filled = is_filled
    def describe(self):
        print(f"{self.color} is {'filled' if self.is_filled else 'not filled' }")
        
class Circle(shape):
    def __init__(self,color,is_filled,radius):
        super().__init__(color,is_filled)
        self.radius = radius
        
    def describe(self):
        print(f"the area of circle is {3.14*self.radius*self.radius: .2f}")
        super().describe()
        
class Square(shape):
    def __init__(self,color,is_filled,width):
        super().__init__(color,is_filled)
        self.width = width
        
    def describe(self):
        print(f"the area of square is {self.width * self.width}")
        super().describe()
    
class Rectangle(shape):
    def __init__(self,color,is_filled,width,height):
        super().__init__(color,is_filled)
        self.width = width
        self.height = height
        
    def describe(self):
            print(f"the area of square is {self.width * self.height}")
            super().describe()
    
circle = Circle(color="red",is_filled=True,radius=6)
square = Square(color="blue",is_filled=False,width=6)
rectangle = Rectangle(color="pink",is_filled=True,width=6,height=4)
circle.describe()
square.describe()
rectangle.describe()
