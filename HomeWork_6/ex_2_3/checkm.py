# Модуль проверки восьми ферзей
from random import randint as rnd

# функция проверки
def check_queens(figure):
    for i in range(len(figure)):
        for j in range(i + 1, len(figure)):
            if figure[i][0] == figure[j][0] or figure[i][1] == figure[j][1] or abs(figure[i][0] - figure[j][0]) == abs(figure[i][1] - figure[j][1]):
                return False
    return True


# функция рандомной расстановки
def random_queens(num):
    count = 0
    good_pos = []
    while count < num:
        for _ in range(7):
            x = rnd(1, 8)
            y = rnd(1, 8)
            good_pos.append((x, y))

        if check_queens(good_pos):
            print(f"Правильная расстановка ферзей № {count}: {good_pos}")
            count += 1