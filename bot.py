import telebot
from telebot import types
import config as cfg
import ftp
bot = telebot.TeleBot(cfg.token)

#MarkUp for welcome message
mainMU = types.InlineKeyboardMarkup()
act_add = types.InlineKeyboardButton('✍ ️Добавить пользователя', callback_data='add')
mainMU.add(act_add)

#All passwords MarkUp
pswdsMU = types.InlineKeyboardMarkup()
for i in cfg.allowed_pswd:
    pswdsMU.add(types.InlineKeyboardButton(i, callback_data=f'pswd,{i}'))

#Ranks MarkUp
rankMU = types.InlineKeyboardMarkup()

@bot.message_handler(commands=['start'])
def auth(message):
    bot.send_message(message.chat.id, 'Прошу, введите пароль...')
    bot.register_next_step_handler(message, welcome)

def welcome(message):
    try:
        tmp = 0
        for i in cfg.allowed_pswd:
            if i != message.text:
                tmp += 1
            else:
                bot.send_message(message.chat.id, 'Приветствую! \n Я - бот для добавления рангов\n Вот всё что я могу:', reply_markup=mainMU)
        if tmp == len(cfg.allowed_pswd):
            raise cfg.AuthError('Have no password')

    except cfg.AuthError as e:
        bot.send_message(message.chat.id, 'Вы не авторизированы!')
@bot.message_handler(commands=['passwords'])
def all_pswds(message):
    bot.send_message(message.chat.id, 'Доступные пароли...', reply_markup=pswdsMU)

@bot.callback_query_handler(func=lambda call: call.text.split(',')[0] == 'pswd')
def manage_pswds(call):
    pswd = call.text.split(',')[1]



@bot.message_handler(commands=['addpassword'])
def changePswd(message):
    bot.send_message(message.chat.id, 'Введите пароль...')
    bot.register_next_step_handler(message, confirmPwsd)

def confirmPwsd(message):
    try:
        tmp = 0
        for i in cfg.allowed_pswd:
            if i != message.text:
                tmp += 1
            else:
                bot.send_message(message.chat.id, 'Введите пароль, который хотите добавить...')
                bot.register_next_step_handler(message, addPswd)
        if tmp == len(cfg.allowed_pswd):
            raise cfg.AuthError('Wrong Password')

    except cfg.AuthError as e:
        bot.send_message(message.chat.id, 'Пароль не верный, введите занова...')
        bot.register_next_step_handler(message, confirmPwsd)

def addPswd(message):
    cfg.allowed_pswd.append(message.text)
    pswdsMU.add(types.InlineKeyboardButton(message.text, f'pswd, {message.text}'))
    bot.send_message(message.chat.id, 'Пароль добавлен!')




@bot.callback_query_handler(func= lambda call: call.data == 'add')
def add_user(call):
    steam = bot.send_message(call.message.chat.id, 'Введите STEAMID пользователя:')
    bot.register_next_step_handler(call.message, rank, call, steam)

def rank(message, call, steam):
    # RankUp rankMu
    for key, value in cfg.ranks.items():
        rankMU.add(types.InlineKeyboardButton(key, callback_data='cfg,' + value + ',' + key+','+message.text))

    bot.send_message(message.chat.id, 'Введите ранг пользователя: ', reply_markup=rankMU)

@bot.callback_query_handler(func=lambda call: call.data.split(',')[0] == 'cfg')
def addToCfg(call):
    key, name = call.data.split(',')[1:2][0], call.data.split(',')[2:3]
    steam_id = call.data.split(',')[3:][0]
    bot.send_message(call.message.chat.id, '♨️STEAM_ID: {0}\n🎉Ранг: {1}\n🎈Цвет: {2}\nВведите 123 для подтверждения...'.format(steam_id, name[0], cfg.ranksColors[key]))
    bot.register_next_step_handler(call.message, confirm, steam_id, key, name)

def confirm(message, steam, key, name):
    if message.text == '123':
        f = ftp.FtpControl('46.174.55.215', 'server909', '26784807')
        if f.edit(steam, name, cfg.ranksColors[key]):
            f.quit()
            bot.send_message(message.chat.id, '✔️Пользователь успешно добавлен!')

bot.polling()