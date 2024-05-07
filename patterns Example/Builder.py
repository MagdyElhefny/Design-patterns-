from abc import ABC , abstractmethod
class House : 
    def __init__(self) -> None:
         self.foundation=None 
         self.roof=None 
         self.doors=None 
         self.windows=None
         self.swimpool=None

class House_Builder(ABC) :
      def foundation (self) :
           pass
      def roof(self ) : 
           pass
      def doors (self) :
           pass  
      def swimpool (self ) :
           pass 
      def windows (self ) :
           pass 
      
class concrete_Builder(House_Builder) : 
        #def __init__(self) -> None:
          #   self.house = House() 
          
        def foundation(self):
             print("Home Founded")

        def roof (self) : 
             print("Roof is Founded") 

        def doors (self) : 
             print("Create doors")  

        def windows(self):
            print("Windows created") 

        def swimpoll(self) : 
             print("Pool is created ")


class Builder_Diractor  :
     def create_House (self , home ):
          home.roof()
          home.doors()

          return home 
     

     
if __name__ == "__main__" :
    c1 = concrete_Builder() 
    D1=Builder_Diractor() 

    house = D1.create_House(c1)