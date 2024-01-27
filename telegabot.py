import telebot
from telebot import types
import webbrowser

bot = telebot.TeleBot('6914629685:AAEkAlswi6Q-28TRbQzR2XshjU540IL1iv4') #создаем оброщение к боту

#===================================================Кнопки======================================================
markup = types.InlineKeyboardMarkup() # создаем кнопку
markup.add(types.InlineKeyboardButton('перейти на сайт'))
#===================================================ДЕКОРАТОРЫ===================================================
@bot.message_handler(commands=['start', 'main'])  # говорим какая команда будет запускать функцию
def start(message):                               # говорим, что будет делать функция
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}')


@bot.message_handler(commands=['help']) 
def help(message): 
    bot.send_message(message.chat.id, 'There is not help')


@bot.message_handler(commands=['info']) 
def info(message):   
    bot.send_message(message.chat.id, message)



@bot.message_handler(commands=['site'])
def site(message):
    webbrowser.open('https://www.youtube.com/channel/UC8fBvI-1z29e2wSzLfkAl6A')

@bot.message_handler(content_types=['photo'])
def get_photo(message):
    bot.reply_to(message.chat.id,'it is so beautiful!')


#========================================ПРИЕМ===================================================================
@bot.message_handler()  # дикоратор (принимает ввод данных от user)
def letter(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}')
    
    elif message.text.lower() == 'id':
        bot.send_message(message.chat.id, f'{message.from_user.id}')

#================================================================================================================
#================================================================================================================

bot.polling(non_stop=True)  # зацикливаем работу