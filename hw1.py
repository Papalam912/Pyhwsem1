# Задача 1: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)


# num = int (input("Введите трехзначное число: "))
# sum = 0
# while num > 0:
#     x = num % 10
#     sum = sum + x
#     num = num // 10

# print ("сумма цифр равна: ", sum)


# Задача 2: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, 
# если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# 6 -> 1 4 1
# 24 -> 4 16 4
# 60 -> 10 40 10


# sum = int(input("Введите число кратное шести: "))
# k = int ((sum//3) * 2)
# p = int((sum//3) // 2)
# s = int (p)

# print(k, p, s)


# Задача 3: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no

# n = input("введите шестизначный номер билета: ")
# f = int(n[0]) + int(n[1]) + int(n[2])
# s = int(n[3]) + int(n[4]) + int(n[5])
# if f == s:
#     print ("билет счастливый")
# else:
#     print ("Не сегодня")


# Задача 4: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no


# a = int(input("значение 1: "))
# b = int(input("значение 2: "))
# c = int(input("требуемое количество долек: "))
# if a * b > c:
#     if a % c == 0 or b % c == 0:
#         print("можно делить")
#     else:
#         print("не получится")
# else:
#     print("не получится")


