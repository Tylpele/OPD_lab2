import type



# a={"stop": False }
# @dp.message_handler(commands=['start'], state=None)
# async def intro(message: types.Message): # асинхоронная функция
#     if a["stop"] == False:
#         markup = InlineKeyboardMarkup()
#         but_1 = InlineKeyboardButton("Играть", callback_data="but_1")
#         markup.add(but_1)
#         await bot.send_message(message.chat.id, "Добро пожаловать в 'Как стать миллионером'", reply_markup=markup)
#
#
#
# @dp.callback_query_handler(lambda c: c.data == "but_1")
# async def first_quest(call: types.callback_query):
#     if a["stop"] == False:
#         await  bot.answer_callback_query(call.id)
#         markup = InlineKeyboardMarkup()
#         but_answ_11 = InlineKeyboardButton("Сегодня", callback_data="but_answ_11")
#         but_answ_21= InlineKeyboardButton("Вчера", callback_data="but_answ_21")
#         but_answ_31= InlineKeyboardButton("Завтра", callback_data="but_answ_31")
#         but_answ_41 = InlineKeyboardButton("Среда",  callback_data="but_answ_41")
#         markup.add(but_answ_11, but_answ_21)
#         markup.add(but_answ_31, but_answ_41)
#         await bot.send_message(call.message.chat.id, "Вопрос №1: Какой сегодня день", reply_markup=markup)
#
#
# @dp.callback_query_handler(lambda c: c.data == "but_answ_21" or c.data == "but_answ_31" or c.data == "but_answ_41")
# async def first_answ_fail(call: types.callback_query):
#     await bot.send_message(call.message.chat.id, "Не правильно! Конец игры")
#     a["stop"] = True
#
#
# @dp.callback_query_handler(lambda c: c.data == "but_answ_11")
# async def second_quest(call: types.callback_query):
#     if a["stop"] == False:
#         await bot.send_message(call.message.chat.id, "Правильно!")
#         await bot.answer_callback_query(call.id)
#         markup = InlineKeyboardMarkup()
#         but_answ_12 = InlineKeyboardButton("Гололь", callback_data="but_answ_12")
#         but_answ_22= InlineKeyboardButton("Достоевский", callback_data="but_answ_12")
#         but_answ_32= InlineKeyboardButton("Пушкин", callback_data="but_answ_32")
#         but_answ_42 = InlineKeyboardButton("Крылов",  callback_data="but_answ_42")
#         markup.add(but_answ_12, but_answ_22)
#         markup.add(but_answ_32, but_answ_42)
#         await bot.send_message(call.message.chat.id, "Вопрос №2: Кто автор «Сказки о попе и работнике его Балде»?", reply_markup=markup)
#
#
# @dp.callback_query_handler(lambda c: c.data == "but_answ_22" or c.data == "but_answ_12" or c.data == "but_answ_42")
# async def third_quest_fail(call: types.callback_query):
#     await bot.send_message(call.message.chat.id, "Не правильно! Конец игры")
#     a["stop"] = True
#
#
#
# @dp.callback_query_handler(lambda c: c.data == "but_answ_32")
# async def third_quest(call: types.callback_query):
#     if a["stop"] == False:
#         await bot.send_message(call.message.chat.id, "Правильно!")
#         await bot.answer_callback_query(call.id)
#         markup = InlineKeyboardMarkup()
#         but_answ_13 = InlineKeyboardButton("Началась пурга", callback_data="but_answ_13")
#         but_answ_23= InlineKeyboardButton("Затупились коньки", callback_data="but_answ_23")
#         but_answ_33= InlineKeyboardButton("Провалился лёд", callback_data="but_answ_33")
#         but_answ_43 = InlineKeyboardButton("Пропустили шайбу",  callback_data="but_answ_43")
#         markup.add(but_answ_13, but_answ_23)
#         markup.add(but_answ_33, but_answ_43)
#         await bot.send_message(call.message.chat.id, "Вопрос №3: Что способствовало поражению ливонских рыцарей во время Ледового побоища?", reply_markup=markup)
#
#
# @dp.callback_query_handler(lambda c: c.data == "but_answ_23" or c.data == "but_answ_13" or c.data == "but_answ_43")
# async def third_quest_fail(call: types.callback_query):
#     await bot.send_message(call.message.chat.id, "Не правильно! Конец игры")
#     a["stop"] = True
#
#
# @dp.callback_query_handler(lambda c: c.data == "but_answ_33")
# async def third_quest(call: types.callback_query):
#     if a["stop"] == False:
#         await bot.send_message(call.message.chat.id, "Правильно!")
#         await bot.answer_callback_query(call.id)
#         markup = InlineKeyboardMarkup()
#         but_answ_14 = InlineKeyboardButton("Перо феникса", callback_data="but_answ_14")
#         but_answ_24= InlineKeyboardButton("Волос единорога", callback_data="but_answ_24")
#         but_answ_34= InlineKeyboardButton("Сердичная жила дракона", callback_data="but_answ_34")
#         but_answ_44 = InlineKeyboardButton("Цветок папоротника",  callback_data="but_answ_44")
#         markup.add(but_answ_14, but_answ_24)
#         markup.add(but_answ_34, but_answ_44)
#         await bot.send_message(call.message.chat.id, "Вопрос №4: Что находилось в сердцевине волшебной палочки Гарри Поттера?", reply_markup=markup)
#
#
# @dp.callback_query_handler(lambda c: c.data == "but_answ_24" or c.data == "but_answ_34" or c.data == "but_answ_44")
# async def third_quest_fail(call: types.callback_query):
#     await bot.send_message(call.message.chat.id, "Не правильно! Конец игры")
#     a["stop"] = True
#
#
# @dp.callback_query_handler(lambda c: c.data == "but_answ_14")
# async def third_quest(call: types.callback_query):
#     if a["stop"] == False:
#         await bot.send_message(call.message.chat.id, "Правильно!")
#         await bot.answer_callback_query(call.id)
#         markup = InlineKeyboardMarkup()
#         but_answ_15 = InlineKeyboardButton("Мегатрон", callback_data="but_answ_15")
#         but_answ_25= InlineKeyboardButton("Гигадрон", callback_data="but_answ_25")
#         but_answ_35= InlineKeyboardButton("Наномоль", callback_data="but_answ_35")
#         but_answ_45 = InlineKeyboardButton("Гугол",  callback_data="but_answ_45")
#         markup.add(but_answ_15, but_answ_25)
#         markup.add(but_answ_35, but_answ_45)
#         await bot.send_message(call.message.chat.id, "Вопрос №5: Под каким названием известна единица с последующими ста нулями?", reply_markup=markup)
#
#
# if a["stop"] == False:
#     @dp.callback_query_handler(lambda c: c.data == "but_answ_25" or c.data == "but_answ_35" or c.data == "but_answ_15")
#     async def third_quest_fail(call: types.callback_query):
#         await bot.send_message(call.message.chat.id, "Не правильно! Конец игры")
#         a["stop"] = True
#
#
# @dp.callback_query_handler(lambda c: c.data == "but_answ_45")
# async def third_quest(call: types.callback_query):
#     if a["stop"] == False:
#         await bot.send_message(call.message.chat.id, "Правильно!")
#         await bot.answer_callback_query(call.id)
#         markup = InlineKeyboardMarkup()
#         but_final = InlineKeyboardButton("Ееее. Я победил!", callback_data="but_final")
#         markup.add(but_final)
#         await bot.send_message(call.message.chat.id, "Вы выиграли!", reply_markup=markup)
#
#
#
#
# @dp.callback_query_handler(lambda c: c.data == "but_final")
# async def third_quest(call: types.callback_query):
#     if a["stop"] == False:
#         await bot.answer_callback_query(call.id)
#         markup = InlineKeyboardMarkup()
#         but_return_yes = InlineKeyboardButton("Да", callback_data="but_return_yes")
#         but_return_no = InlineKeyboardButton("Нет", callback_data="but_return_no")
#         markup.add(but_return_yes,but_return_no)
#         await bot.send_message(call.message.chat.id, "Сыграть ещё?", reply_markup=markup)
#
#
# @dp.callback_query_handler(lambda c: c.data == "but_return_yes")
# async def third_quest(call: types.callback_query):
#     await bot.send_message(call.message.chat.id, "Хороший выбор!")
#     await bot.answer_callback_query(call.id)
#     a["stop"] = False
#
# @dp.callback_query_handler(lambda c: c.data == "but_return_no")
# async def third_quest(call: types.callback_query):
#     await bot.send_message(call.message.chat.id, "Очень жаль")
#     await bot.answer_callback_query(call.id)
#     a["stop"] = True
#
# @dp.message_handler(commands=['start'])
# async def intro(message: types.Message): # асинхоронная функция
#     if a["stop"] == False:
#         markup = InlineKeyboardMarkup()
#         but_1 = InlineKeyboardButton("Играть", callback_data="but_1")
#         markup.add(but_1)
#         await bot.send_message(message.chat.id, "Добро пожаловать в 'Как стать миллионером'", reply_markup=markup)
#
#
#
#
#
#
#
#
#







if __name__=="__main__":
    type.BOT()
