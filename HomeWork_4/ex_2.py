# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, 
# где ключ — значение переданного аргумента, а значение — имя аргумента. 
# Если ключ не хешируем, используйте его строковое представление. 


def func(**kwargs):
    dict = {}
    for key, value in kwargs.items():
        if not isinstance(key, (int, float, bool, tuple)):
            key = str(key)
        dict[value] = key
    return dict

params = func(number='1', vegetable='Тыква', tool='топор')
print(params)