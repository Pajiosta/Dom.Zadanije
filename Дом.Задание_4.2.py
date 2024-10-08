s = input("Введите строчку: ")
for i in range(len(s)):
    if s[i] == "{" or s[i] == "[" or s[i] == "(":
        x = i
    elif s[i] == "}" or s[i] == "]" or s[i] == ")":
        y = i
print(s[x+1:y])