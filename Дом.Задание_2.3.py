month = int(input("Введите номер месяца: "))
if month<3: 
    print("Зима")
    if month == 1:
        print("Январь")
    else: print("Февраль")
elif 2<month<6:
    print("Весна")
    if month == 3:
        print("Март")
    elif month == 4:
        print("Апрель")
    else: print("Май")
elif 5<month<9:
    print("Лето")
    if month == 6:
        print("Июнь")
    elif month == 7:
        print("Июль")
    else: print("Август")
elif month>8:
    print("Осень")
    if month == 9:
        print("Сентябрь")
    elif month == 10:
        print("Октябрь")
    elif month == 11:
        print("Ноябрь")
    else: print("Декабрь")
else: print("Ошибка, такого месяца нет")
