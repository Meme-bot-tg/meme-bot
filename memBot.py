import telebot;
import pandas as pd
bot = telebot.TeleBot('5641796619:AAHcrwsw169q69zif1JM0d30bmJlHVxX4SA');
data = pd.read_excel('img\\data.xlsx')
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет")
    else:
        findMem(message)

def findMem(message):
    flag = True
    for i in range(data.shape[0]):
        if data.iloc[i,1].find(message.text)!=-1:
            flag = False
            img = open(f'img\\{data.iloc[i, 0]}.jpg', 'rb')
            bot.send_photo(message.chat.id, img)
    if flag:
        bot.send_message(message.from_user.id, f"Такой мем не найден( Напиши /help.")
bot.polling(none_stop=True, interval=0)
