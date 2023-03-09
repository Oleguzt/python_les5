#  Напишите программу, которая на вход принимает два числа A и B, и возводит 
# число А в целую неотрицательную степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8

def degree(a, b):
    if b == 0:
        return 1
    if b > 0:
        return a * degree(a, b - 1)
    
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

print(degree(a, b)) 
