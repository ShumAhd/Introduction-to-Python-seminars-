#2. Напишите программу, которая найдёт произведение пар чисел списка.
#Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in
# 4
# out
# [2, 5, 8, 10]
# [20, 40]
# in
# 5
# out
# [2, 2, 4, 8, 8]
# [16, 16, 4]

from random import sample

def c_list(counter):
    if counter <= 0:
        return print("Необходимо задать положительное число!")

    r_list = []
    for i in sample(range(counter), counter):
        r_list.append(i)
    print("Рандомный список - ", r_list)
    
    p_list =[]
    if (len(r_list)) % 2 == 0:
        for i in range((len(r_list))//2):
            #print(i)
            p_list.append(r_list[i] * r_list[len(r_list)-1-i])
        print("Произведение пар чисел из списка - ", p_list)
    else:
        for i in range((len(r_list)+1)//3):
            #print(i)
            p_list.append(r_list[i] * r_list[len(r_list)-1-i])
        print("Произведение пар чисел из списка - ", p_list,
              "У последнего элемента по середине списка, нет пары",)

c_list(int(input("Задай размер списка, введи положительное число: ")))


