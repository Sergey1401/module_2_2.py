# Домашняя работа по уроку "Условная конструкция. Операторы if, elif, else."
first = int(input("Введите первое число: "))
second = int(input("Введите второе значение: "))
third = int(input("Введите третье значение: "))
if first==second==third:
    print(3)
elif first==second or second==third or first==third:
    print(2)
else:
    print(0)