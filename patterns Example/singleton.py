class singleton : 
    def __new__(cls) :
        return cls 
    

    def __init__(self) -> None:
        self.name = None


singleton1 = singleton() 
singleton1.name='Magdy'
singleton2 = singleton() 


print(singleton1.name)
print(singleton2.name)
print(singleton1 is singleton2)



