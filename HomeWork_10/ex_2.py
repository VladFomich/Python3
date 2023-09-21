# Возьмите 1-3 любые задания из прошлых семинаров (например сериализация данных), которые вы уже решали. 
# Превратите функции в методы класса, а параметры в свойства. 
# Задания должны решаться через вызов методов экземпляра

# из домашки 8:

# def get_directory_size(path):  # Функция для получения размера директории или файла в байтах.

#     if os.path.isfile(path):

#         return os.path.getsize(path)

#     elif os.path.isdir(path):

#         total_size = 0

#         for dirpath, dirnames, filenames in os.walk(path):

#             for filename in filenames:

#                 filepath = os.path.join(dirpath, filename)

#                 total_size += os.path.getsize(filepath)

#         return total_size


# print(get_directory_size("../"))


import os


class Get_Dict_Sze:


    def __init__(self, directory):
        self.directory = directory

    def get_directory_size(self):  

        if os.path.isfile(self.directory):

            return os.path.getsize(self.directory)

        elif os.path.isdir(self.directory):

            total_size = 0

            for dirpath, dirnames, filenames in os.walk(self.directory):

                for filename in filenames:

                    filepath = os.path.join(dirpath, filename)

                    total_size += os.path.getsize(filepath)

            return total_size


getter = Get_Dict_Sze("../")
print(getter.get_directory_size())    