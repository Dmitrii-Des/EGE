# Если в условии задания просят найти кол-во каких-то символов идущих подряд,
# то заменяем интересующие нас последовательности на какой-то отстраненный символ
# и все оставшиеся символы из исходного алфавита заменяем на пробелы
with open('24_3228.txt') as file:
    data = file.readline()

data = data.replace('AC', '*')
data = data.replace('AB', '*')

for i in 'ABC':
    data = data.replace(i, ' ')
data = data.split()

print(len(max(data, key=len)))