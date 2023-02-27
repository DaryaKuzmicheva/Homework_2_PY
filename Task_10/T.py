#Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть,
#чтобы все монетки были повернуты вверх одной и той же стороной.
#Выведите минимальное количество монет, которые нужно перевернуть

n = int(input('Введите количество монет '))
orel = 0
reshka = 0
for i in range(n):
    x = int(input("Орел(1) или решка(0)?"))
    if x == 0:
        reshka = reshka + 1
    else:
        orel = orel + 1
if orel == 0:
    print("Все монеты на стороне решка")
elif reshka == 0:
    print("Все монеты на стороне орел")
elif orel == reshka:
    print(f"Количество орлов и решек поровну. Нужно перевернуть монет: {reshka}")
elif reshka < orel:
    print(f"Монет на стороне решка меньше всего. Нужно перевернуть монет: {reshka}")
else:
    print(f"Монет на стороне орел меньше всего. Нужно перевернуть монет: {orel}")

