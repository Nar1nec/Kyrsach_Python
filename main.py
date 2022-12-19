from selenium import webdriver
from aiogram import Bot, executor
from aiogram.dispatcher.filters import Command
import logging
from aiogram.dispatcher.filters import Text
from ThrottlingMiddleware import *
from parsing_output import *
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

buttons_AM = ["1️⃣", "2️⃣", "3️⃣", "4️⃣","Выбрать другой сайт"]
buttons_RBC = ["①", "②", "③", "④", "Выбрать другой сайт"]
buttons_SecLab = ["(1)", "(2)", "(3)", "(4)", "Выбрать другой сайт"]

bot = Bot(token = '5395562658:AAGnn6C3IYecd9M2zn8lTX4CacF_LP_BJog')

dp = Dispatcher(bot,storage = storage)

logging.basicConfig(level=logging.INFO)

#.....Начало.....
@dp.message_handler(Command('start'))
@rate_limit(limit=1.5, key = '/start')
async def start(message: types.Message):
    await message.answer("Привет, " + message.from_user.first_name + "!" + '\n'
                                            "Спасибо, что пользуешься моим ботом!")
    await message.answer("1. Выбери сайт, с которого хочешь получить новость." + '\n'+ '\n'            
                                           "2. Выбери интересующую для себя новость.     " + '\n'+ '\n'                  
                                           "3. Если тебя заинтересовала данная информация, нажми на кнопку 'Читать далее', чтобы перейти на сайт. " + '\n'+ '\n'
                                             "P.S. Используй кнопки.")

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["SecureNews", "ANTI-MALWARE", "RBC"]
    keyboard.add(*buttons)
    await message.answer("Какой сайт выберите?", reply_markup=keyboard)

#.....SecureNews......


@dp.message_handler(Text(equals="SecureNews"))
@rate_limit(limit = 1.5)
async def news_sn(message: types.Message):
    await message.reply("Сейчас что-нибудь поищу...", reply_markup=types.ReplyKeyboardRemove())
    global browser
    browser = webdriver.Chrome()

    Secure_News.parsing_Secure_news(browser)

    n = 1
    for i in range(0, len(Secure_News.news_title)):
        await message.answer(str(n) + ')' + ' ' + Secure_News.news_title[i].text)
        n += 1
        time.sleep(0.5)

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*buttons_AM)
    await message.answer("Нажмите на кнопку, чтобы выбрать номер новости.",reply_markup=keyboard)


@dp.message_handler(Text(equals="1️⃣"))
@rate_limit(limit=1.5)
async def first_answer_sn(message: types.Message):

    button = types.InlineKeyboardButton(text="Читать далее", url=search_href(0))
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(button)

    await bot.send_photo(chat_id=message.chat.id,photo = search_images(1),caption = search_text_mini(0),reply_markup=keyboard)

@dp.message_handler(Text(equals="2️⃣"))
@rate_limit(limit=1.5)
async def second_answer_sn(message: types.Message):

    button = types.InlineKeyboardButton(text="Читать далее", url = search_href(1))
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(button)

    await bot.send_photo(chat_id=message.chat.id, photo=search_images(2),caption = search_text_mini(1),reply_markup=keyboard)

@dp.message_handler(Text(equals="3️⃣"))
@rate_limit(limit=1.5)
async def third_answer_sn(message: types.Message):

    button = types.InlineKeyboardButton(text="Читать далее", url=search_href(2))
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(button)

    await bot.send_photo(chat_id=message.chat.id, photo=search_images(3),caption = search_text_mini(2),reply_markup=keyboard)

@dp.message_handler(Text(equals="4️⃣"))
@rate_limit(limit=1.5)
async def fourth_answer_sn(message: types.Message):

    button = types.InlineKeyboardButton(text="Читать далее", url=search_href(3))
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(button)

    await bot.send_photo(chat_id=message.chat.id, photo=search_images(4),caption = search_text_mini(3),reply_markup=keyboard)

#.....SecurityLab......

@dp.message_handler(Text(equals="ANTI-MALWARE"))
async def news_am(message: types.Message):
    await message.reply("Сейчас что-нибудь поищу.", reply_markup=types.ReplyKeyboardRemove())
    global browser
    browser = webdriver.Chrome()
    ANTI_MALWARE.parsing_AM(browser)

    n = 1
    for i in range(0, len(ANTI_MALWARE.news_title) - 8):
        await message.answer(str(n) + ')' + ' ' + ANTI_MALWARE.news_title[i].text)
        n += 1
        time.sleep(0.5)

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*buttons_SecLab)
    await message.answer("Введите номер новости.", reply_markup=keyboard)

@dp.message_handler(Text(equals="(1)"))
@rate_limit(limit=1.5)
async def first_news_am(message: types.Message):
    button = types.InlineKeyboardButton(text="Читать далее", url=search_href_AM(63))
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(button)

    await message.answer(parsing_AM(0), reply_markup=keyboard)

@dp.message_handler(Text(equals="(2)"))
@rate_limit(limit=1.5)
async def second_news_am(message: types.Message):

    button = types.InlineKeyboardButton(text="Читать далее", url = search_href_AM(66))
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(button)

    await message.answer(parsing_AM(1),reply_markup=keyboard)

@dp.message_handler(Text(equals="(3)"))
@rate_limit(limit=1.5)
async def third_news_am(message: types.Message):

    button = types.InlineKeyboardButton(text="Читать далее", url=search_href_AM(69))
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(button)

    await message.answer(parsing_AM(2),reply_markup=keyboard)

@dp.message_handler(Text(equals="(4)"))
@rate_limit(limit=1.5)
async def fourth_news_am(message: types.Message):

    button = types.InlineKeyboardButton(text="Читать далее", url=search_href_AM(72))
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(button)

    await message.answer(parsing_AM(3),reply_markup=keyboard)

#.....RBC.....

@dp.message_handler(Text(equals="RBC"))
async def news_rbc(message: types.Message):
    await message.reply("Сейчас что-нибудь поищу.", reply_markup=types.ReplyKeyboardRemove())

    global browser
    browser = webdriver.Chrome()
    RBC_News.parsing_RBC(browser)

    n = 1
    for i in range(0, len(RBC_News.news_title) - 36):
        await message.answer(str(n) + ')' + ' ' + RBC_News.news_title[i].text + '\n' + RBC_News.time[i].text)
        n += 1
        time.sleep(0.5)


    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

    keyboard.add(*buttons_RBC)
    await message.answer("Введите номер новости.", reply_markup=keyboard)


@dp.message_handler(Text(equals="①"))
@rate_limit(limit=1.5)
async def first_news_rbc(message: types.Message):

    button = types.InlineKeyboardButton(text="Читать далее", url=search_href_RBC(0))
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(button)

    await bot.send_photo(chat_id=message.chat.id,photo = search_images_RBC(0),caption = parsing_RBC(0),reply_markup = keyboard)

@dp.message_handler(Text(equals="②"))
@rate_limit(limit=1.5)
async def second_news_rbc(message: types.Message):

    button = types.InlineKeyboardButton(text="Читать далее", url=search_href_RBC(1))
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(button)

    await bot.send_photo(chat_id=message.chat.id, photo=search_images_RBC(1), caption=parsing_RBC(1), reply_markup=keyboard)

@dp.message_handler(Text(equals="③"))
@rate_limit(limit=1.5)
async def third_news_rbc(message: types.Message):

    button = types.InlineKeyboardButton(text="Читать далее", url=search_href_RBC(2))
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(button)

    await bot.send_photo(chat_id=message.chat.id, photo=search_images_RBC(2), caption=parsing_RBC(2), reply_markup=keyboard)

@dp.message_handler(Text(equals="④"))
@rate_limit(limit=1.5)
async def fourth_news_rbc(message: types.Message):

    button = types.InlineKeyboardButton(text="Читать далее", url=search_href_RBC(3))
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(button)

    await bot.send_photo(chat_id=message.chat.id, photo=search_images_RBC(3), caption=parsing_RBC(3),
                         reply_markup=keyboard)

@dp.message_handler(Text(equals="Выбрать другой сайт"))
async def another_site(message: types.Message):
    await message.reply("Хорошо!", reply_markup=types.ReplyKeyboardRemove())
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["SecureNews", "ANTI-MALWARE", "RBC"]
    keyboard.add(*buttons)
    await message.answer("Какой сайт выберите?", reply_markup=keyboard)
    browser.close()

if __name__ == "__main__":
    # Запуск бота
    dp.middleware.setup(ThrottlingMiddleware())
    executor.start_polling(dp, skip_updates=True)