from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

import data

TOKEN_API = ""
bot = Bot(TOKEN_API)
dp =Dispatcher(bot)

#счётчик текущего вопроса и номер максильного вопроса
counts={"Count": 0, "Count_max": 9}

#что высвечивается при нажатии старта
@dp.message_handler(commands=['start'], state=None)
async def begin(message: types.Message):
      markup = InlineKeyboardMarkup()
      start = InlineKeyboardButton("Играть", callback_data="start")
      markup.add(start)
      counts["Count"]= 0
      await bot.send_message(message.chat.id, "Добро пожаловать в 'Как стать миллионером'", reply_markup=markup)


#проверка на правильные ответы
@dp.callback_query_handler(lambda c: c.data == "start" or c.data == "Сегодня" or c.data == "Пушкин" or c.data == "Провалился лёд" or c.data == "Перо феникса" or c.data == "Гугол" or
                           c.data == "Билл Гейтс" or c.data == "Elk Cloner" or c.data == "Глубинное обучение" or c.data == "Айзек Азимов" or c.data == "12 сентября" or c.data == "HDD")
async def game(call: types.callback_query):
    if (counts["Count"]<= counts["Count_max"]): #вывод вопросов и ответов
        await  bot.answer_callback_query(call.id)
        markup = InlineKeyboardMarkup()
        but_answ_1 = InlineKeyboardButton(data.answ_v2[counts["Count"]][0], callback_data=data.answ_v2[counts["Count"]][0])
        but_answ_2= InlineKeyboardButton(data.answ_v2[counts["Count"]][1], callback_data=data.answ_v2[counts["Count"]][1])
        but_answ_3= InlineKeyboardButton(data.answ_v2[counts["Count"]][2], callback_data=data.answ_v2[counts["Count"]][2])
        but_answ_4 = InlineKeyboardButton(data.answ_v2[counts["Count"]][3],  callback_data=data.answ_v2[counts["Count"]][3])
        markup.add(but_answ_1, but_answ_2)
        markup.add(but_answ_3, but_answ_4)
        await bot.send_message(call.message.chat.id, data.quest_v2[counts["Count"]], reply_markup=markup)
        counts["Count"] += 1
    else: #объявление победы и приглашение сыграть заново
        await bot.send_message(call.message.chat.id, "Подравляем, вы миллионер!")
        markup = InlineKeyboardMarkup()
        but_return_yes = InlineKeyboardButton("Да", callback_data="start")
        but_return_no = InlineKeyboardButton("Нет", callback_data="but_return_no")
        markup.add(but_return_yes, but_return_no)
        await bot.send_message(call.message.chat.id, "Хотите сыграть ещё раз?", reply_markup=markup)
        counts["Count"] = 0


#выход
@dp.callback_query_handler(lambda c: c.data =="but_return_no")
async def Exit(call: types.callback_query):
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.message.chat.id, "Ну ладно...")
    exit(1)


#обработка неправильных ответов и приглашение на повторную игру
@dp.callback_query_handler()
async def first_quest(call: types.callback_query):
    await  bot.answer_callback_query(call.id)
    await  bot.send_message(call.message.chat.id, "Вы проиграли!")
    markup = InlineKeyboardMarkup()
    but_return_yes = InlineKeyboardButton("Да", callback_data="start")
    but_return_no = InlineKeyboardButton("Нет", callback_data="but_return_no")
    markup.add(but_return_yes,but_return_no)
    await bot.send_message(call.message.chat.id, "Хотите сыграть ещё раз?", reply_markup=markup)
    counts["Count"] = 0


def BOT():
   executor.start_polling(dp)
