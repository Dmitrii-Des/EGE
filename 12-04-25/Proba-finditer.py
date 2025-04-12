import re

string = 'ABBAACABAABABCA'
pattern = r'AB'

matches = re.finditer(pattern, string)

for match in matches:
    print(f'Найдено совпадение: {match.group()}')
    print(f'Позиция: {match.span()}')
