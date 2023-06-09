import random

#воспросы и ответы
quest = ["Какой сегодня день?", "Вопрос №2: Кто автор «Сказки о попе и работнике его Балде»?",
         "Что способствовало поражению ливонских рыцарей во время Ледового побоища?",
         "Что находилось в сердцевине волшебной палочки Гарри Поттера?",
         "Под каким названием известна единица с последующими ста нулями?",
         "Кто является основателем компании Microsoft?",
         "Как назывался первый вирус?", "Вопрос №8: Что появилось позже остальных?",
         "Кто придумал 3 закона робототехники?",
         "Какого числа отмечается День программиста (256 день в году) в високосный год?",
         "Какому устройству дал имя винтовочный патрон американского происхождения?"]
answ = [["Сегодня", "Вчера", "Завтра", "Среда"], ["Гололь", "Достоевский", "Пушкин", "Крылов"],
        ["Началась пурга", "Затупились коньки", "Провалился лёд", "Пропустили шайбу"],
        ["Перо феникса", "Волос единорога", "Сердичная жила дракона", "Цветок папоротника"],
        ["Мегатрон", "Гигадрон", "Наномоль", "Гугол"], ["Марк Цукерберк", "Билл Гейтс", "Стив Джобс","Билл Клинтон"],
        ["Elk Cloner", "Brain", "Jerusalem", "Windows"], ["Машинное обучение","Обучение с подкреплением", "Перебор", "Глубинное обучение"],
        ["Айзек Азимов", "Евгений Замятин", "Жюль Верн", "Карл Маркс"], ["13 сентября", "4 декабря", "12 сентября", "3 декабря"],
        ["RAM", "HDD", "CPU", "ROM"]]

#перетасовка списков так, чтобы на вопрос были корректные варианты ответа к нему
zipped = list(zip(answ, quest))
random.shuffle(zipped)
answ_v2, quest_v2 = zip(*zipped)
