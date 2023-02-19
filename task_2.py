# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

number = input("Введите трехзначное число: ")
result = 0

for dig in number:
    result += int(dig)

print(result)

