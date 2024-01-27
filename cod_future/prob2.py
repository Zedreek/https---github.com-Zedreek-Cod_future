class Animal:
    def __init__(self,name,old):
        self.name = name
        self.old = old
    def get_name(self):
        return f'{self.name}'
    
class Cat(Animal):
        def __init__(self, name, old, color, weight):
            super().__init__(name,old)
            self.color = color
            self.weight = weight
        def info(self):
            return f'{self.name} {self.old} {self.color} {self.weight}'
        
s = Cat(input('имя '),input('возраст '),input('цвет '),input('вес '))
a = s.info()
print(a)