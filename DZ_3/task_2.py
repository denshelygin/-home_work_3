# 2-Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

def com_index(lst):
    number = len(lst)
    lst2 = []
    for i in range (len(lst)):
        while i < len(lst)/2 and number > len(lst)/2: 
            number = number - 1
            a = lst[i] * lst[number]  
            lst2.append(a)  
            i += 1
    print(lst2)

lst = [6, 3, 4, 9, 5, 7, 6, 9, 3]
com_index(lst)



