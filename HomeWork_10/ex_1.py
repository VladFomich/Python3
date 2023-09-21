# Доработаем задания 5-6. Создайте класс-фабрику.
# Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
# Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики. 



class Factory:

    def create_animal(self, animal_type, name, age, breed, color):
        if animal_type == 'Dog':
            return Dog(name, age, breed, color)
        if animal_type == 'Cat':
            return Cat(name, age, breed, color)
        if animal_type == 'Pig':
            return Pig(name, age, breed, color)


class Dog:
    def __init__(self, name, age, breed, color):
        self.name = name
        self.age = age
        self.breed = breed
        self.color = color


    def info_dogs(self):
        return f'Собака {self.name}, {self.age} лет, породы {self.breed} , {self.color} окраса.'
    

    def dogs_funny(self):
        return f'\n Собаки - самый популярный вид домашнего животного в Санкт-Петербурге'



class Cat:
    def __init__(self, name, age, breed, color):
        self.name = name
        self.age = age
        self.breed = breed
        self.color = color


    def info_cats(self):
        return f'Кошка {self.name}, {self.age} лет, породы {self.breed} , {self.color} окраса.'
    

    def cats_funny(self):
        return f'\n В древнем Египте кошек почитали за богов'




class Pig:
    def __init__(self, name, age, breed, color):
        self.name = name
        self.age = age
        self.breed = breed
        self.color = color


    def info_pigs(self):
        return f'Свинка {self.name}, {self.age} лет, породы {self.breed} , {self.color} окраса.'
    

    def pigs_funny(self):
        return f'\n Домашняя свинья - довольно чистоплотное животное'


factory = Factory()


ch1 = factory.create_animal('Dog', 'Мухтар', 10, 'овчарка', 'чёрного')
ch2 = factory.create_animal('Cat', 'Мася', 8, 'сфинкс', 'серого')
ch3 = factory.create_animal('Pig', 'Пятачок', 5, 'домашняя', 'пятнистого')


choose = int(input("Создать: \n1 - Собаку , 2 - Кошку , 3 - Свинку\n"))
if choose == 1:
    print(ch1.info_dogs(),ch1.dogs_funny())
if choose == 2:
    print(ch2.info_cats(),ch2.cats_funny())
if choose == 3:
    print(ch3.info_pigs(),ch3.pigs_funny())
