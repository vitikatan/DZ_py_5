# Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.

def f(a, b):
    if b == 0:
        return 1
    return f(a, b-1) * a

print ('Введите A')
n = int(input())
print ('Введите B')
m = int(input())
print(f(n, m))