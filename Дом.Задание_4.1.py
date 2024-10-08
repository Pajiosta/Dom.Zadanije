s = input("Введите строчку: ")
k=m=0
for i in range(len(s)):
    if s[i]=='н':
        k += 1
    else:
        m=max(m,k)
        k=0
s=s.replace('н','!')
print("Максимальное каличество <<н>> подряд: ", m,"\n Новая строчка: ", s)