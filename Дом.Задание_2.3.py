month = int(input("Введите номер месяца: "))
if 2<month<6:
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
elif 8<month<12:
    print("Осень")
    if month == 9:
        print("Сентябрь")
    elif month == 10:
        print("Октябрь")
    else: print("Ноябрь")
elif 11<month<3: 
    print("Зима")
    if month == 1:
        print("Январь")
    elif month == 2:
        print("Февраль")
    else: print("Декабрь")
else: print("Ошибка, такого месяца нет")
