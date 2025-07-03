from aiogram import Bot,Dispatcher,executor,types
# from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = Bot(token='')
dp = Dispatcher(bot)

# b1 = KeyboardButton('Hello dalle')
# b2 = KeyboardButton('Another dalle')
b1 = InlineKeyboardButton(text="let seee", callback_data="letsee")
b2 = InlineKeyboardButton(text="ja ja", callback_data="jaja")

# keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(b1, b2)
keyboard1_inline = InlineKeyboardMarkup().add(b1, b2)

@dp.callback_query_handler(text = ["letsee", "jaja"])
async def Inline_key(call: types.CallbackQuery):
    if call.data == "letsee":
        await call.message.answer("What see")
    elif call.data == "jaja":
        await call.message.answer("kha ja aukat mein")
    await call.answer()


@dp.message_handler(commands=['start','help'])
async def welcome(message: types.Message):
    await message.reply("Hello!, I am Wether Checker Bot by Deval")

# @dp.message_handler(commands=['kill'])

# async def kill(message:  types.Message):
#     await message.reply("Choose an Button!!", reply_markup=keyboard1)

@dp.message_handler(commands='pls')
async def pls(message: types.Message):
    await message.reply("Choose kaar jldi", reply_markup=keyboard1_inline)


# @dp.message_handler()
# async def echo(message: types.Message):
#     await message.answer(message.text)

executor.start_polling(dp, skip_updates=True)