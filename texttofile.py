import os
from aiogram import Bot,Dispatcher,executor,types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

bot = Bot(token='')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start','help'])
async def welcome(message: types.Message):
    await message.reply("Hello!, I am Text to File Bot By Deval\n'/go'")

button1 = InlineKeyboardButton(text="Fiile Mode", callback_data="text_in")
button2 = InlineKeyboardButton(text="Close", callback_data="close")

button_inline = InlineKeyboardMarkup().add(button1,button2)

@dp.message_handler(commands=['go'])
async def execute(message: types.Message):
    await message.reply("Get Your Job Done",reply_markup=button_inline)

@dp.callback_query_handler(lambda c:c.data == 'text_in')
async def process_text_in(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.edit_message_reply_markup(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,
        reply_markup=None
    )
    await bot.send_message(callback_query.from_user.id, "Please Send The You Want To Convert To Text File")

@dp.callback_query_handler(text = ["close"])
async def Inline_key(call: types.CallbackQuery):
    if call.data == "close":
        await call.answer()
        await bot.edit_message_reply_markup(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        reply_markup=None
    )
        await call.message.answer("Visit again~~")

@dp.message_handler(content_types=['text'])
async def save_text_to_file(message: types.Message):
    user_text = message.text
    filename = f"{message.from_user.id}_text.txt"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(user_text)

    with open(filename, "rb") as f:
        await bot.send_document(message.chat.id, f, caption="Here’s your file!")
        await message.reply("Thanks! for using Bot")


    os.remove(filename)

executor.start_polling(dp, skip_updates=True)
