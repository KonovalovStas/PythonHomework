#
# Найдите сумму цифр трехзначного числа.

# 1 пример нахождения суммы числа
print('сумма цифр техзначного числа')
x = 756
print(x)

print('равна')

a = 7
b = 5
c = 6
sum = (a + b + c)
print(sum)

#2 пример нахождения суммы числа

n = 756
summa = 0
while n > 0:
    x = n % 10
    summa = summa + x
    n = n // 10
print(summa)

# 3  пример нахождения суммы числа

n = input("Введите трехзначное число: ")
n = int(n)

a = n % 10
b = n % 100 // 10
c = n // 100

print("Сумма цифр числа:", a + b + c)
