# 1) Вычислить и вывести на экран длину окружности и площадь круга одного и того же заданного радиуса R, 
#    который необходимо ввести с клавиатуры в сантиметрах. Результаты должны округляться до сотых.

import math
r = int(input("Введите, в сантиметрах, размер радиуса акружности: "))
print("размер окружности: ",round(2*math.pi*r, 3))

# 2) Даны две переменные x = 10 и y = 55. Поменяйте их значения местами. Выведите значения переменных на экран до и после замены.

x = 10
y = 55
print("Первичные значения: \n", "x = ", x, "\n y = ", y)
c = x
x = y
y = c
print("Новые значение: \n", "x = ", x, "\n y = ", y)

# 3) Вычислить и вывести на экран период колебания маятника длиной L с точностью до сотых. 
#    Для рассчетов использовать формулу T = 2π√(L/g), где g – ускорение свободного падения (9.81 м/c2). 
#    Значение длины маятника в метрах необходимо ввести с клавиатуры.

import math
L = int(input("Введите длинну маятника: "))
print("Период колебания маятника равен: ", round(2*math.pi*L/9.81,3))
