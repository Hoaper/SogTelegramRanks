token = 'api_telegram_token'

# Rank keys ( Do not Change )
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

# Passwords For access in a bot
allowed_pswd = [
    'password'
]

# FTP Data
host = 'hostname'
user = 'username'
pswd = 'password'

#Exception
class AuthError(Exception):
    pass
