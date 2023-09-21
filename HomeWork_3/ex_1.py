# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. 
# В результирующем списке не должно быть дубликатов. 

lst = [3, 3, 4, 5, 1, "про", 0.345, "z", "z"]

new_lst = []
temp_lst = []
for el in lst:
    if el in temp_lst:
        new_lst.append(el)
    else:
        temp_lst.append(el)
        
print(f"Список дубликатов (без дубликатов): {list(set(new_lst))}")