from re import*

with open('24.23_19887.txt') as file:
    data = file.readline()

pattern1 = r'([13579][02468])+[13579]?|([02468][13579])+[02468]?'
pattern2 = r'[02468]?([13579][02468])+[13579]?'
matches1 = finditer(pattern1, data)
matches2 = finditer(pattern2, data)

print(max(len(i.group()) for i in matches1))
print(max(len(i.group()) for i in matches2))