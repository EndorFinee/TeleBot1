import telebot,sqlite3,config,os,sys,time,SQLighter,random
from telebot import types
from SQLighter import SQLighter
bot = telebot.TeleBot(config.token)
path = "C:/EndorFine/University/Diplom/"
mu = types.ReplyKeyboardMarkup(resize_keyboard=True)
mu.row('Еще!')

#global a
#sql = "SELECT * FROM Games"
#cursor.execute(sql)
@bot.message_handler(content_types=["text"])
def any_msg(message):
            bot.send_message(message.chat.id,"Привет!", reply_markup=mu)
            keyboard = types.InlineKeyboardMarkup()
            button = types.InlineKeyboardButton(text="6-9", callback_data="kids")
            button1 = types.InlineKeyboardButton(text="10-13", callback_data="keys")
            button2 = types.InlineKeyboardButton(text="14-17", callback_data="keep")
            keyboard.add(button,button1,button2)
            bot.send_message(message.chat.id,"Выбери возраст!", reply_markup=keyboard)
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == "kids":
            global a
            a = 1
            keyboard=types.InlineKeyboardMarkup()
            callback_button = types.InlineKeyboardButton(text="На взаимодействие", callback_data="inter")
            callback_button1 = types.InlineKeyboardButton(text="Уличные", callback_data="street")
            callback_button2 = types.InlineKeyboardButton(text="Шутки", callback_data="joke")
            callback_button3 = types.InlineKeyboardButton(text="На снятие напряжения", callback_data="relax")
            callback_button4 = types.InlineKeyboardButton(text="Быстрые", callback_data="quick")
            callback_button5 = types.InlineKeyboardButton(text="Тактильные", callback_data="touch")
            callback_button6 = types.InlineKeyboardButton(text="На знакомство", callback_data="know")
            keyboard.add(callback_button)
            keyboard.add(callback_button3)
            keyboard.add(callback_button1,callback_button2,callback_button4,callback_button5)
            keyboard.add(callback_button6)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Выбери тип игры!", reply_markup=keyboard)
        if call.data == "keys":
            a = 2
            keyboard=types.InlineKeyboardMarkup()
            callback_button = types.InlineKeyboardButton(text="На взаимодействие", callback_data="inter")
            callback_button1 = types.InlineKeyboardButton(text="Уличные", callback_data="street")
            callback_button2 = types.InlineKeyboardButton(text="Шутки", callback_data="joke")
            callback_button3 = types.InlineKeyboardButton(text="На снятие напряжения", callback_data="relax")
            callback_button4 = types.InlineKeyboardButton(text="Быстрые", callback_data="quick")
            callback_button5 = types.InlineKeyboardButton(text="Тактильные", callback_data="touch")
            callback_button6 = types.InlineKeyboardButton(text="На знакомство", callback_data="know")
            keyboard.add(callback_button)
            keyboard.add(callback_button3)
            keyboard.add(callback_button1,callback_button2,callback_button4,callback_button5)
            keyboard.add(callback_button6)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Выбери тип игры!", reply_markup=keyboard)
        if call.data == "keep":
            a = 3
            keyboard=types.InlineKeyboardMarkup()
            callback_button = types.InlineKeyboardButton(text="На взаимодействие", callback_data="inter")
            callback_button1 = types.InlineKeyboardButton(text="Уличные", callback_data="street")
            callback_button2 = types.InlineKeyboardButton(text="Шутки", callback_data="joke")
            callback_button3 = types.InlineKeyboardButton(text="На снятие напряжения", callback_data="relax")
            callback_button4 = types.InlineKeyboardButton(text="Быстрые", callback_data="quick")
            callback_button5 = types.InlineKeyboardButton(text="Тактильные", callback_data="touch")
            callback_button6 = types.InlineKeyboardButton(text="На знакомство", callback_data="know")
            keyboard.add(callback_button)
            keyboard.add(callback_button3)
            keyboard.add(callback_button1,callback_button2,callback_button4,callback_button5)
            keyboard.add(callback_button6)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Выбери тип игры!", reply_markup=keyboard)
        if call.data == "inter":
            r=random.randint(1,59)
            db_worker = SQLighter(config.database_name)
            row = db_worker.select_single_inter(r, a)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text=row)
        if call.data == "street":
            r=random.randint(1,59)
            db_worker = SQLighter(config.database_name)
            row = db_worker.select_single_street(r, a)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text=row)
        if call.data == "joke":
            r=random.randint(1,59)
            db_worker = SQLighter(config.database_name)
            row = db_worker.select_single_joke(r, a)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text=row)
        if call.data == "relax":
            r=random.randint(1,59)
            db_worker = SQLighter(config.database_name)
            row = db_worker.select_single_relax(r, a)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text=row)
        if call.data == "quick":
            r=random.randint(1,59)
            db_worker = SQLighter(config.database_name)
            row = db_worker.select_single_quick(r, a)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text=row)
        if call.data == "touch":
            r=random.randint(1,59)
            db_worker = SQLighter(config.database_name)
            row = db_worker.select_single_touch(r, a)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text=row)
        if call.data == "know":
            r=random.randint(1,59)
            db_worker = SQLighter(config.database_name)
            row = db_worker.select_single_know(r, a)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text=row)
#@bot.callback_query_handler(func=lambda call: True)
#def callback_inline(call):
    #if call.message:

if __name__ == '__main__':
    random.seed()
    bot.polling(none_stop=True)
