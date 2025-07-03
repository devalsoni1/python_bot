import requests
from aiogram import Bot, Dispatcher, executor, types

bot = Bot(token='')
dp = Dispatcher(bot)

API_KEY = ""

@dp.message_handler(commands=['start', 'help'])
async def welcome(message: types.Message):
    await message.reply("Hello! I am a Weather Bot by Deval. Type any city name to get current weather.")

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        description = data["weather"][0]["description"]
        city_name = data["name"]

        report = (
            f"📍 City: {city_name}\n"
            f"🌤 Weather: {description}\n"
            f"🌡 Temperature: {temperature}°C\n"
            f"💧 Humidity: {humidity}%\n"
            f"💨 Wind Speed: {wind_speed} m/s"
        )
        return report

    except requests.exceptions.RequestException as e:
        return f"Somegthing went wrong {e}"

@dp.message_handler(content_types=['text'])
async def city_name(message: types.Message):
    city = message.text.strip()
    report = get_weather(city)
    await message.reply(report)

executor.start_polling(dp, skip_updates=True)
