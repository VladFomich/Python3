# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла. 
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.


from os import path 


def my_file_info(the_path):
    f_dir = path.dirname(the_path)
    f_name = path.splitext(path.basename(the_path))[0]
    f_ex = path.splitext(the_path)[1]
    return f_dir, f_name, f_ex


i_know_the_way = r"C:\Windows\user\vlad\my_shit\pass.txt" 
print(my_file_info(i_know_the_way))