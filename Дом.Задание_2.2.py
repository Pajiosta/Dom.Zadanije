Sum = float(input("Ввести сумму покупок: "))
if Sum>20:
    print("Стоймость покупок со скиткой: ", round(Sum*0.65, 2), "Скидка: ", round(Sum*0.35, 2))
else: print("Стоймость покупок со скиткой: ", round(Sum, 2), "Скидка: ", 0)
