n = int(input("Ввести номер: "))
sum = 0
if n>100:
    print("Ошибка: номер не должен привышать 100")
else:
    for i in range(n+1):
        sum += i**3
print("Сумма кубов равна: ", sum) 
