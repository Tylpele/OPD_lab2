import random

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


TOKEN_API = ""
bot = Bot(TOKEN_API)
dp =Dispatcher(bot)

a={"Count": 0}


quest =["Вопрос №1: Какой сегодня день?","Вопрос №2: Кто автор «Сказки о попе и работнике его Балде»?","Вопрос №3: Что способствовало поражению ливонских рыцарей во время Ледового побоища?",
       "Вопрос №4: Что находилось в сердцевине волшебной палочки Гарри Поттера?","Вопрос №5: Под каким названием известна единица с последующими ста нулями?"]
answ =[["Сегодня","Вчера","Завтра", "Среда"], ["Гололь","Достоевский","Пушкин", "Крылов"], ["Началась пурга","Затупились коньки","Провалился лёд","Пропустили шайбу"],
       ["Перо феникса","Волос единорога","Сердичная жила дракона","Цветок папоротника"],["Мегатрон","Гигадрон","Наномоль", "Гугол"]]


zipped = list(zip(answ, quest))
random.shuffle(zipped)
answ_v2, quest_v2 = zip(*zipped)


@dp.message_handler(commands=['start'], state=None)
async def intro(message: types.Message): # асинхоронная функция
      markup = InlineKeyboardMarkup()
      but_1 = InlineKeyboardButton("Играть", callback_data="but_1")
      markup.add(but_1)
      a["Count"]= 0
      await bot.send_message(message.chat.id, "Добро пожаловать в 'Как стать миллионером'", reply_markup=markup)





@dp.callback_query_handler(lambda c: c.data == "but_1" or c.data == "Сегодня" or c.data == "Пушкин" or c.data == "Провалился лёд" or c.data == "Перо феникса" or c.data == "Гугол")
async def first_quest(call: types.callback_query):
    if (a["Count"]<= 4):
        await  bot.answer_callback_query(call.id)
        markup = InlineKeyboardMarkup()
        but_answ_1 = InlineKeyboardButton(answ_v2[a["Count"]][0], callback_data=answ_v2[a["Count"]][0])
        but_answ_2= InlineKeyboardButton(answ_v2[a["Count"]][1], callback_data=answ_v2[a["Count"]][1])
        but_answ_3= InlineKeyboardButton(answ_v2[a["Count"]][2], callback_data=answ_v2[a["Count"]][2])
        but_answ_4 = InlineKeyboardButton(answ_v2[a["Count"]][3],  callback_data=answ_v2[a["Count"]][3])
        markup.add(but_answ_1, but_answ_2)
        markup.add(but_answ_3, but_answ_4)
        await bot.send_message(call.message.chat.id, quest_v2[a["Count"]], reply_markup=markup)
        a["Count"] += 1
    else:
        await bot.send_message(call.message.chat.id, "Подравляем, вы миллионер!")
        markup = InlineKeyboardMarkup()
        but_return_yes = InlineKeyboardButton("Да", callback_data="but_1")
        but_return_no = InlineKeyboardButton("Нет", callback_data="but_return_no")
        markup.add(but_return_yes, but_return_no)
        await bot.send_message(call.message.chat.id, "Хотите сыграть ещё раз?", reply_markup=markup)
        a["Count"] = 0

@dp.callback_query_handler(lambda c: c.data =="but_return_no")
async def Exit(call: types.callback_query):
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.message.chat.id, "Ну ладно...")
    exit(1)

@dp.callback_query_handler(lambda c: c.data != "Сегодня" or c.data != "Пушкин" or c.data != "Провалился лёд" or c.data != "Перо феникса" or c.data != "Гугол")
async def first_quest(call: types.callback_query):
    await  bot.answer_callback_query(call.id)
    await  bot.send_message(call.message.chat.id, "Вы проиграли!")
    markup = InlineKeyboardMarkup()
    but_return_yes = InlineKeyboardButton("Да", callback_data="but_1")
    but_return_no = InlineKeyboardButton("Нет", callback_data="but_return_no")
    markup.add(but_return_yes,but_return_no)
    await bot.send_message(call.message.chat.id, "Хотите сыграть ещё раз?", reply_markup=markup)
    a["Count"] = 0


@dp.callback_query_handler(lambda c: c.data =="but_return_no")
async def Exit(call: types.callback_query):
    await  bot.answer_callback_query(call.id)
    await  bot.send_message(call.message.chat.id, "Ну ладно...")
    exit(1)

def BOT():
   executor.start_polling(dp)
