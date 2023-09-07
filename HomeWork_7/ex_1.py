# Напишите функцию группового переименования файлов. Она должна:
#     принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется 
#         порядковый номер.
#     принимать параметр количество цифр в порядковом номере.
#     принимать параметр расширение исходного файла. Переименование должно работать только для этих 
#         файлов внутри каталога.
#     принимать параметр расширение конечного файла.
#     принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы 
#         с 3 по 6 из исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано. 
#         Далее счётчик файлов и расширение. 
import os


def files_rename(new_name, number_of_digits, old_ext, new_ext, name_range, the_path):
    count = 1
    for filename in os.listdir(the_path):
        if filename.endswith(old_ext):
            old_name = filename.split('.')[0]
            old_name_sub = old_name[name_range[0] - 1:name_range[1]] if name_range else ""
            new_filename = f'{old_name_sub}{new_name}{str(count).zfill(number_of_digits)}.{new_ext}'
            os.rename(os.path.join(the_path, filename), os.path.join(the_path, new_filename))
            count += 1


files_rename('new_file', 3, 'doc', 'txt', [1, 3], './newfolder')