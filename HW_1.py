# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
# in
# 5
# out
# [10, 2, 3, 8, 9]
# 22
# in
# 4
# out
# [4, 2, 4, 9]
# 8
from random import sample

def find_num(count):
    if count < 0: # проверка на отрецательное число
        return print("Negative value of the number of numbers!")

    list_nums = sample(range(count*2), count) #Создаём список из рандомных чисел
    print("out", list_nums)

    sum = 0
    for i in range(0, count, 2): #выбираем нечётные позиции
        sum += list_nums[i]      #суммируем нечётные позиции
    print("sum of odd positions = ", sum)

find_num(int(input("in: ")))


