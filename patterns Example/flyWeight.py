import random
from abc import ABC , abstractmethod

# flyWeight interface
    # define the method that flyweight object must implement
class shape (ABC):
    @abstractmethod
    def draw(self) :
        pass


# flyweight concrete class
    # in concrete class represents the shared flyweight object
class Circle (shape) :
    def __init__(self , color):
        self.color=color
        self.x = 0
        self.y=0
        self.radius = 0

    def set_x (self , x) :
       self.x=x

    def set_y (self ,y) :
       self.y=y

    def set_radius (self , radius) :
        self.radius = radius

    def draw(self):
        print(f"Circle: Draw() [Color : {self.color}, x : {self.x}, y : {self.y}, radius : {self.radius}]")
# flyweight factory
    #manage and create flyweight object
class circleFactory :
    _circle = {}
    def get_circle (color) :
        circle = circleFactory._circle.get(color)
        if circle is None :
            circle = Circle(color)
            circleFactory._circle[color] = circle
            print(f"Created circle color : {color}")

        return  circle

    def  get_x_random () :
        return  random.randint(1,100)

    def  get_y_random () :
        return  random.randint(1,100)

    def get_radius () :
        return  random.randint(5 , 30)

    # Client code
if __name__ ==  "__main__" :
    colors = ['red' , 'yellow' , 'green' , 'orange']
    for _ in range (5) :
        color = random.choice(colors)
        circle = circleFactory.get_circle(color)
        circle.set_x(circleFactory.get_x_random())
        circle.set_y(circleFactory.get_y_random())
        circle.set_radius(circleFactory.get_radius())
        circle.draw()
        print("===================================================")

print("===================================================")

