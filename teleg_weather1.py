import telebot
from telebot import types
import webbrowser

bot = telebot.TeleBot('6914629685:AAEkAlswi6Q-28TRbQzR2XshjU540IL1iv4') #создаем оброщение к боту

#==============================================================================================================
#===================================================ДЕКОРАТОРЫ===================================================
@bot.message_handler(commands=['start'])  # говорим какая команда будет запускать функцию
def start(message):                               # говорим, что будет делать функция
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}\nЯ - бот, который показывает погоду\nнапиши мне название населенного пункта, погоду которого вы хотите узнать.')




#========================================ПРИЕМ===================================================================
@bot.message_handler()  # дикоратор (принимает ввод данных от user)
def letter(message):

    if message.text.lower() == 'тимашевск':

        markup = types.InlineKeyboardMarkup() # создаем кнопку
        markup.add(types.InlineKeyboardButton('Перейти на сайт', url='https://www.gismeteo.ru/weather-timashevsk-5133/')) #указываем что она будет делать
        bot.reply_to(message, 'Вот что я нашел:', reply_markup=markup) #отправлсяем

    elif message.text.lower() == 'москва':

        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Перейти на сайт', url='https://www.gismeteo.ru/weather-moscow-4368/')) 
        bot.reply_to(message, 'Вот что я нашел:', reply_markup=markup)


    
    elif message.text.lower() == 'помоги':
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}\nЯ - бот, который показывает погоду\nнапиши мне название населенного пункта, погоду которого вы хотите узнать.')


    elif message.text.lower() == 'пискуновское':

        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Перейти на сайт', url='https://www.gismeteo.ru/weather-piskunovskoye-156154/')) 
        bot.reply_to(message, 'Вот что я нашел:', reply_markup=markup)

    
    else:
        bot.send_message(message.chat.id,'Извините я не знаю такой населенный пункт\nвозможно вы могли ввести название неправильно\nВАЖНО! Указывайте название в иминительном падеже\n<Если вы не знаете, что делать, то напишите\'помоги\'>')

#================================================================================================================
#================================================================================================================

bot.polling(non_stop=True)  # зацикливаем работу