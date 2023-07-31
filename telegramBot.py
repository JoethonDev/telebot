import telebot
import sqlite3


# Replace 'YOUR_BOT_TOKEN' with the token you obtained from BotFather
TOKEN = '1156662740:AAEWzSmMZkdRiwlBX_fmLxdMeUuPQgE3ETM'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    id = message.text.split(',')
    for seat in id:
        try :
            seat = int(seat)
            cursor.execute(f'SELECT * FROM results_results WHERE seat_no = {seat} ')
            result = cursor.fetchone()
            text = f"""
Name : {result[3]}
Seat_Number : {result[1]}
Degree : {result[2]}
State : {result[4]}
            """
            bot.reply_to(message, text)

        except :
            print(f'Error with {seat}')


bot.infinity_polling()