from re import*

with open('24_17756.txt') as file:
    data = file.readline()

pattern1 = r'[0-9]+([+|*][0-9]+)*'
pattern2 = r'([+|*]?[0-9]+)*[+|*]?'
matches1 = finditer(pattern1, data)
matches2 = finditer(pattern2, data)

print(max(len(i.group()) for i in matches1))
print(max(len(i.group()) for i in matches2))