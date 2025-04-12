import re

string = 'Написал(а) ЕГЭ на 100'

pattern = r'ЕГЭ'

res = re.search(pattern, string)


print(f'Найдена подстрока: {res.group()}')  #Как с match, но с search. Search ищет во всей строке,\
                                            # match - первое вхождение
print(f'Начало вхождения: {res.start()}')
print(f'Конец вхождения: {res.end()}')
