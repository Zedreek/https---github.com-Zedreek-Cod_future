class market():
    def __init__(self,name,age,col_persens):
        self.name = name
        self.age = int(age)
        self.col_persens = int(col_persens)
    def show_info(self):
        return(f'Имя - {self.name}\nВозрост - {self.age}\nПерсонал-{self.col_persens}')
    def __str__(self):
        return(f'Имя - {self.name}\nВозрост - {self.age}\nПерсонал-{self.col_persens}')

class shop():
    def __init__(self,name,age,col_persens,col_towara):
        super().__init__(self,name,age,col_persens)
        self.col_towara = col_towara
    def __str__(self):
        return(f'Имя - {self.name}\nВозрост - {self.age}\nПерсонал-{self.col_persens}')
sh1 = shop('Дружба','12','20')
#print(sh1.show_info())
print(sh1)








#float - дробное число
#int - число 
#str - строка