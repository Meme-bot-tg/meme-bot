# Весь код

<pre><code>import telebot;
import pandas as pd
bot = telebot.TeleBot('5641796619:AAHcrwsw169q69zif1JM0d30bmJlHVxX4SA');
data = pd.read_excel('img\\data.xlsx')
finde = False

@bot.message_handler(content_types=['text'])
<strong>def get_text_messages(message):
</strong>    global finde
    if finde:
        findMem(message)
        finde=False
    elif message.text == "/start":
        bot.send_message(message.from_user.id, "Привет, я помогу тебе разобраться в глубоком внутреннем мире Леонида В."
                                               "и найти мем из его группы в телеге по описанию"
                                               "(все права и разрешения получены у него лично)")
        bot.send_message(message.from_user.id, "Чтобы приступить к поиску напиши /find")
    elif message.text == "/find":
        bot.send_message(message.from_user.id, "Вводи слово или фразу, а я попробую найти мем по ней")
        finde = True
    else:
        bot.send_message(message.from_user.id, "Чтобы начать напиши /start")

def findMem(message):
    flag = True
    for i in range(data.shape[0]):
        if data.iloc[i,1].find(message.text)!=-1:
            flag = False
            img = open(f'img\\{data.iloc[i, 0]}.jpg', 'rb')
            bot.send_photo(message.chat.id, img)
    if flag:
        bot.send_message(message.from_user.id, f"Такой мем не найден( Напиши /help.")
bot.polling(none_stop=True, interval=0)</code></pre>
