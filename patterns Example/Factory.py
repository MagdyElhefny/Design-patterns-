# from abc import ABC , abstractmethod
# class shape(ABC) :
#     @abstractmethod
#     def draw (self) :
#         return  
    
class concreteFactoryRectangle  : 
    def __init__(self):
        self.name1 = "Rectangle is drawed"

class concreteFactorySquare : 
    def __init__(self):
        self.name1 = "Square is drawed"       

class concreteFactorycircle  : 
    def __init__(self):
        self.name1 = "circle is drawed"


class  ShapeFactory :   
    def create_object ( some_property ) :
        if (some_property == "circle") :
            return concreteFactorycircle()

        if (some_property == "ractangle") :
            return concreteFactoryRectangle() 

        if (some_property == "square ") :
            return concreteFactorySquare()  
         
         
        return None 

if __name__ == "__main__" :
   A= ShapeFactory.create_object("ractangle")
   print(A.name1)        