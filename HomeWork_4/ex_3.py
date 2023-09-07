# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции. 
# Дополнительно сохраняйте все операции поступления и снятия средств в список.
from datetime import datetime


header = (''' - БАНКОМАТ -\nПополнение счета - 1 | Снятие денег со счета - 2 | Выход - q\n 
''')

summ = 0
count_add = 0
count_out = 0
operation_history = []
now = datetime.now()

def add_money(amount, count, lst):
    amount = richbitch(amount)
    money_add = int(input("Внести сумму (кратную 50): "))
    while money_add % 50 != 0:
        print("Сумма пополнения должна быть кратна 50")
        money_add = int(input("Внести сумму (кратную 50): "))
    amount += money_add
    lst.append(['Пополнение', now.strftime("%H:%M:%S")])
    count += 1
    print(count)
    amount = bonus(amount, count)
    return amount, count, lst
  
    
def withdraw_money(amount, count, lst):
    amount = richbitch(amount)
    money_wd = int(input("Снять сумму (кратную 50): "))
    while money_wd % 50 != 0:
        print("Сумма снятия должна быть кратная 50")
        money_wd = int(input("Снять сумму (кратную 50: "))
    percent = money_wd * 0.015
    if percent < 30:
        percent = 30
    elif percent > 600:
        percent = 600
    if money_wd + percent > amount:
        print("Недостаточно средств")
    else:
        amount -= money_wd + percent
        lst.append(['Снятие', now.strftime("%H:%M:%S")])
        count += 1
        print(count)
        amount = bonus(amount, count)
        return amount, count, lst
    
def bonus(amount, count):
    if count % 3 == 0:
        amount *=1.03
    return amount


def richbitch(amount):
    if amount > 5000000:
        print("Налог на богатство", summ * 0.1)
        amount -= amount * 0.1
    return amount

action = None
while action != 'q':
    action = input(f'{header}').lower()
    if action == '1':
        summ, count_add, operation_history = add_money(summ, count_add, operation_history)
        print(f"Текущий счет: {summ}")
        print(f"История операций: {operation_history}\n")
    elif action == '2':
        summ, count_out, operation_history = withdraw_money(summ, count_out, operation_history)
        print(f"Текущий счет: {summ}")
        print(f"История операций: {operation_history}\n")