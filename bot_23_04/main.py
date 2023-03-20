import os
import sys
import telebot
import time
from selenium import webdriver

from data import TOKEN, list

bot = telebot.TeleBot(TOKEN)

class Kanal:
    name: str = list[0]
    stpage: int = list[1]
    embaded: str = "?embed=1"


driver = webdriver.Chrome()
counter = 0
counter2 = 1

while True:
    clear = lambda: os.system('cls')
    clear()
    print()
    print('(0_0 )')
    time.sleep(2)
    clear = lambda: os.system('cls')
    clear()
    print()
    print('( 0_0)')
    time.sleep(2)
    driver.get(Kanal.name + str(Kanal.stpage) + Kanal.embaded)
    pg_not_fnd = driver.find_elements('name', "tgme_widget_message_error")
    # pg_not_fnd = driver.find_elements_by_class_name("tgme_widget_message_error")
    if len(pg_not_fnd) > 0:
        counter = counter + 2
        counter2 = counter2 + 2
        Kanal.name = list[counter]
        Kanal.stpage = list[counter2]
        stop = len(list) - 2
        if counter == stop:
            driver.quit()
            break
    else:
        for a in driver.find_elements('name', 'tgme_widget_message_date'):
        # for a in driver.find_elements_by_class_name('tgme_widget_message_date'):
            link = a.get_atribute('href')
            list[counter2] = int(list[counter2]) + 1
            bot.send_message(chat_id=6217940788, text=link)
            output = open('data.py', 'w')
            print("TOKEN = '6217940788:AAG9DruoXHjyXD8XYYhizWyk1Pq_wt32oK8'", file=output)
            print("list =", list, file=output)
            output.close()
        Kanal.stpage = str(Kanal.stpage + 1)

for i in reversed(range(1, 500)):
    time.sleep(1)
    clear = lambda: os.system('cls')
    clear()
    print()
    print('-_-')
    sys.stderr.write(f"{i:2d}\r")
    time.sleep(1)

os.startfile('main.py')
