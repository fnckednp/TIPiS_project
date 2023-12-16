import telebot
import config
import prediction
import start_message

type_errors = []
errors = [] 

def is_number(n):
    is_number = True
    try:
        num = float(n)
        is_number = num == num   # Проверка на 'NaN'
    except ValueError:
        is_number = False
    return is_number

bot = telebot.TeleBot(config.TOKEN)
@bot.message_handler(content_types=['text'])

def bot_answer(message):
    if(message.text == '/start'):
        bot.send_message(message.chat.id, start_message.START_MSG, parse_mode='html')
        return
    
    arr = message.text.split(',')
    if len(arr) == 8 and all(is_number(value) for value in arr):
        arr = [arr]
        output = prediction.check_data(arr)
    else:
        output = [2]
    

    if output[0] == 1:
        ans = "Вы, вероятно, болеете диабетом"
    elif output[0] == 0:
        ans = "Вы, вероятно, не болеете диабетом"
    elif output[0] == 2:
        ans = "Неверные данные"


    bot.send_message(message.chat.id, ans,
                     parse_mode='html')
    print(f"Введённое сообщение: {message.text} ; Отправленное сообщение : {ans}")

bot.polling(non_stop=True)