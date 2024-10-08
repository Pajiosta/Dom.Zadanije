s=input("Введите строчку: ").split()
for i in s:
    if i[0]=="а" and i[-1]=="я":
        print("Слова: ", i)