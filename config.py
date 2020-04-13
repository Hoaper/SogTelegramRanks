token = '1089289084:AAH-8be_N7d0gLlO0V9WZsSGGyUILQxDse8'

ranksColors = {
    'ryad': 'grey',
    'effr': 'grey2',
    '_ser': 'darkred',
    'ser': 'red',
    '+ser': 'lime',
    'prap': 'darkblue',
    '+pra': 'blue',
    '_lei': 'orchid',
    'leit': 'purple',
    '+lei': 'orchid',
    'capt': 'lime',
    'mayo': 'red',
    '_pol': 'yellow',
    'polk': 'green',
    'geni': 'gold',
    'mars': 'gold'
}
ranks = {
    'Рядовой': 'ryad',
    'Еффрейтор': 'effr',
    'Мл.Сержант': '_ser',
    'Сержант': 'ser',
    'Ст.Сержант': '+ser',
    'Прапорщик': 'prap',
    'Ст.Прапорщик': '+pra',
    'Мл.Лейтенант': '_lei',
    'Лейтенант': 'leit',
    'Ст.Лейтенант': '+lei',
    'Капитан': 'capt',
    'Майор': 'mayo',
    'Мл.Полковник': '_pol',
    'Полковник': 'polk',
    'Генерал': 'geni',
    'Маршал' : 'mars'
}

allowed_pswd = [
    '23lkJjksana',
    '26784807'
]

host = '46.174.55.215'
user = 'server909'
pswd = '26784807'

#Exception
class AuthError(Exception):
    pass
