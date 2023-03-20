import requests
import datetime
from data import TOKEN, open_weather_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("Привет! Напиши мне название города и я пришлю сводку погоды!")


@dp.message_handler()
async def get_weather(message: types.Message):

    code_to_smile = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Облачно \U00002601",
        "Rain": "Дождь \U00002614",
        "Drizzle": "Дождь \U00002614",
        "Thunderstorm": "Гроза \U000026A1",
        "Snow": "Снег \U0001F328",
        "Mist": "Туман \U0001F32B"
    }

    try:
        c = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={message.text}&limit={1}&appid={open_weather_token}')
        data_c = c.json()
        lat = data_c[0]['lat']
        lon = data_c[0]['lon']

        r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={open_weather_token}&units=metric")
        data_r = r.json()
        city = data_r['name']
        cur_weather = data_r["main"]["temp"]

        weather_description = data_r["weather"][0]["main"]
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = " "

        humidity = data_r["main"]["humidity"]
        pressure = data_r["main"]["pressure"]
        wind = data_r["wind"]["speed"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data_r["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data_r["sys"]["sunset"])
        length_of_the_day = datetime.datetime.fromtimestamp(data_r["sys"]["sunset"]) - datetime.datetime.fromtimestamp(
            data_r["sys"]["sunrise"])

        await message.reply(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
              f"Погода в городе: {city}\nТемпература: {cur_weather}C° {wd}\n"
              f"Влажность: {humidity}%\nДавление: {pressure} мм.рт.ст\nВетер: {wind} м/с\n"
              f"Восход солнца: {sunrise_timestamp}\nЗакат солнца: {sunset_timestamp}\nПродолжительность дня: {length_of_the_day}\n"
              f"Хорошего дня!"
              )

    except:
        await message.reply('\U00002620 Проверьте название города \U00002620')


if __name__ == '__main__':
    executor.start_polling(dp)
