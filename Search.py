import json
import requests
import time
import os
import phonenumbers
from phonenumbers import carrier, geocoder, timezone
from sys import stderr

Bl = '\033[30m'  # Переменная для цвета текста
Re = '\033[1;31m'
Gr = '\033[1;32m'
Ye = '\033[1;33m'
Blu = '\033[1;34m'
Mage = '\033[1;35m'
Cy = '\033[1;36m'
Wh = '\033[1;37m'


# утилиты

# декоратор для прикрепления run_banner к функции
def is_option(func):
    def wrapper(*args, **kwargs):
        run_banner()
        func(*args, **kwargs)


    return wrapper


# ФУНКЦИИ ДЛЯ МЕНЮ
@is_option
def IP_Track():
    ip = input(f"{Wh}\n Введите целевой IP : {Gr}")  # ВВОД IP-АДРЕСА
    print()
    print(f' {Wh}============= {Gr}Инфа по IP {Wh}=============')
    req_api = requests.get(f"http://ipwho.is/{ip}")  # API IPWHOIS.IS
    ip_data = json.loads(req_api.text)
    time.sleep(2)
    print(f"{Wh}\n Целевой IP       :{Gr}", ip)
    print(f"{Wh} Тип IP           :{Gr}", ip_data["type"])
    print(f"{Wh} Страна           :{Gr}", ip_data["country"])
    print(f"{Wh} Код страны       :{Gr}", ip_data["country_code"])
    print(f"{Wh} Город            :{Gr}", ip_data["city"])
    print(f"{Wh} Континент        :{Gr}", ip_data["continent"])
    print(f"{Wh} Код континента   :{Gr}", ip_data["continent_code"])
    print(f"{Wh} Регион           :{Gr}", ip_data["region"])
    print(f"{Wh} Код региона      :{Gr}", ip_data["region_code"])
    print(f"{Wh} Широта           :{Gr}", ip_data["latitude"])
    print(f"{Wh} Долгота          :{Gr}", ip_data["longitude"])
    lat = int(ip_data['latitude'])
    lon = int(ip_data['longitude'])
    print(f"{Wh} Карты            :{Gr}", f"https://www.google.com/maps/@{lat},{lon},8z")
    print(f"{Wh} ЕС               :{Gr}", ip_data["is_eu"])
    print(f"{Wh} Почтовый индекс :{Gr}", ip_data["postal"])
    print(f"{Wh} Код страны      :{Gr}", ip_data["calling_code"])
    print(f"{Wh} Столица         :{Gr}", ip_data["capital"])
    print(f"{Wh} Границы         :{Gr}", ip_data["borders"])
    print(f"{Wh} Флаг страны     :{Gr}", ip_data["flag"]["emoji"])
    print(f"{Wh} ASN             :{Gr}", ip_data["connection"]["asn"])
    print(f"{Wh} ORG             :{Gr}", ip_data["connection"]["org"])
    print(f"{Wh} ISP             :{Gr}", ip_data["connection"]["isp"])
    print(f"{Wh} Домен           :{Gr}", ip_data["connection"]["domain"])
    print(f"{Wh} ID              :{Gr}", ip_data["timezone"]["id"])
    print(f"{Wh} Аббревиатура    :{Gr}", ip_data["timezone"]["abbr"])
    print(f"{Wh} Летнее время    :{Gr}", ip_data["timezone"]["is_dst"])
    print(f"{Wh} Смещение        :{Gr}", ip_data["timezone"]["offset"])
    print(f"{Wh} Время UTC       :{Gr}", ip_data["timezone"]["utc"])
    print(f"{Wh} Текущее время   :{Gr}", ip_data["timezone"]["current_time"])


@is_option
def phoneGW():
    User_phone = input(
        f"\n {Wh}Введите номер телефона {Gr}Пример [+380xxxxxxxxx] {Wh}: {Gr}")  # ВВОД НОМЕРА ТЕЛЕФОНА
    default_region = "ID"

    parsed_number = phonenumbers.parse(User_phone, default_region)  # ПАРСИНГ НОМЕРА ТЕЛЕФОНА
    region_code = phonenumbers.region_code_for_number(parsed_number)
    jenis_provider = carrier.name_for_number(parsed_number, "en")
    location = geocoder.description_for_number(parsed_number, "id")
    is_valid_number = phonenumbers.is_valid_number(parsed_number)
    is_possible_number = phonenumbers.is_possible_number(parsed_number)
    formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
    formatted_number_for_mobile = phonenumbers.format_number_for_mobile_dialing(parsed_number, default_region,
                                                                                with_formatting=True)
    number_type = phonenumbers.number_type(parsed_number)
    timezone1 = timezone.time_zones_for_number(parsed_number)
    timezoneF = ', '.join(timezone1)

    print(f"\n {Wh}========== {Gr}Информация по номеру {Wh}==========")
    print(f"\n {Wh}Местоположение             :{Gr} {location}")
    print(f" {Wh}Код региона          :{Gr} {region_code}")
    print(f" {Wh}Часовой пояс             :{Gr} {timezoneF}")
    print(f" {Wh}Оператор             :{Gr} {jenis_provider}")
    print(f" {Wh}Действительный номер         :{Gr} {is_valid_number}")
    print(f" {Wh}Возможный номер      :{Gr} {is_possible_number}")
    print(f" {Wh}Международный формат :{Gr} {formatted_number}")
    print(f" {Wh}Мобильный формат        :{Gr} {formatted_number_for_mobile}")
    print(f" {Wh}Оригинальный номер      :{Gr} {parsed_number.national_number}")
    print(
        f" {Wh}E.164 формат         :{Gr} {phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)}")
    print(f" {Wh}Код страны         :{Gr} {parsed_number.country_code}")
    print(f" {Wh}Местный номер         :{Gr} {parsed_number.national_number}")
    if number_type == phonenumbers.PhoneNumberType.MOBILE:
        print(f" {Wh}Тип                 :{Gr} Это мобильный номер")
    elif number_type == phonenumbers.PhoneNumberType.FIXED_LINE:
        print(f" {Wh}Тип                 :{Gr} Это стационарный номер")
    else:
        print(f" {Wh}Тип                 :{Gr} Это другой тип номера")


@is_option
def TrackLu():
    try:
        username = input(f"\n {Wh}Введите имя пользователя : {Gr}")
        results = {}
        social_media = [
            {"url": "https://www.facebook.com/{}", "name": "Facebook"},
            {"url": "https://www.twitter.com/{}", "name": "Twitter"},
            {"url": "https://www.instagram.com/{}", "name": "Instagram"},
            {"url": "https://www.linkedin.com/in/{}", "name": "LinkedIn"},
            {"url": "https://www.github.com/{}", "name": "GitHub"},
            {"url": "https://www.pinterest.com/{}", "name": "Pinterest"},
            {"url": "https://www.tumblr.com/{}", "name": "Tumblr"},
            {"url": "https://www.youtube.com/{}", "name": "Youtube"},
            {"url": "https://soundcloud.com/{}", "name": "SoundCloud"},
            {"url": "https://www.snapchat.com/add/{}", "name": "Snapchat"},
            {"url": "https://www.tiktok.com/@{}", "name": "TikTok"},
            {"url": "https://www.behance.net/{}", "name": "Behance"},
            {"url": "https://www.medium.com/@{}", "name": "Medium"},
            {"url": "https://www.quora.com/profile/{}", "name": "Quora"},
            {"url": "https://www.flickr.com/people/{}", "name": "Flickr"},
            {"url": "https://www.periscope.tv/{}", "name": "Periscope"},
            {"url": "https://www.twitch.tv/{}", "name": "Twitch"},
            {"url": "https://www.dribbble.com/{}", "name": "Dribbble"},
            {"url": "https://www.stumbleupon.com/stumbler/{}", "name": "StumbleUpon"},
            {"url": "https://www.ello.co/{}", "name": "Ello"},
            {"url": "https://www.producthunt.com/@{}", "name": "Product Hunt"},
            {"url": "https://www.snapchat.com/add/{}", "name": "Snapchat"},
            {"url": "https://www.telegram.me/{}", "name": "Telegram"},
            {"url": "https://www.weheartit.com/{}", "name": "We Heart It"}
        ]
        for site in social_media:
            url = site['url'].format(username)
            response = requests.get(url)
            if response.status_code == 200:
                results[site['name']] = url
            else:
                results[site['name']] = (f"{Ye}Имя пользователя не найдено {Ye}!")
    except Exception as e:
        print(f"{Re}Ошибка : {e}")
        return

    print(f"\n {Wh}========== {Gr}Информация о пользователе {Wh}==========")
    print()
    for site, url in results.items():
        print(f" {Wh}[ {Gr}+ {Wh}] {site} : {Gr}{url}")


@is_option
def showIP():
    respone = requests.get('https://api.ipify.org/')
    Show_IP = respone.text

    print(f"\n {Wh}========== {Gr}Информация по IP {Wh}==========")
    print(f"\n {Wh}[{Gr} + {Wh}] Ваш IP-адрес : {Gr}{Show_IP}")
    print(f"\n {Wh}==============================================")

# ВАРИАНТЫ
options = [
    {
        'num': 1,
        'text': 'Отслеживание IP',
        'func': IP_Track
    },
    {
        'num': 2,
        'text': 'Показать ваш IP',
        'func': showIP

    },
    {
        'num': 3,
        'text': 'Отслеживание номера телефона',
        'func': phoneGW
    },
    {
        'num': 4,
        'text': 'Отслеживание имени пользователя',
        'func': TrackLu
    },
    {
        'num': 0,
        'text': 'Выход',
        'func': exit
    }
]

def clear():
    # для Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # для Mac и Linux
    else:
        _ = os.system('clear')


def call_option(opt):
    if not is_in_options(opt):
        raise ValueError('Опция не найдена')
    for option in options:
        if option['num'] == opt:
            if 'func' in option:
                option['func']()
            else:
                print('Функция не найдена')


def execute_option(opt):
    try:
        call_option(opt)
        input(f'\n{Wh}[ {Gr}+ {Wh}] {Gr}Нажмите Enter, чтобы продолжить')
        main()
    except ValueError as e:
        print(e)
        time.sleep(2)
        execute_option(opt)
    except KeyboardInterrupt:
        print(f'\n{Wh}[ {Re}! {Wh}] {Re}Выход')
        time.sleep(2)
        exit()


def option_text():
    text = ''
    for opt in options:
        text += f'{Wh}[ {opt["num"]} ] {Gr}{opt["text"]}\n'
    return text


def is_in_options(num):
    for opt in options:
        if opt['num'] == num:
            return True
    return False


def option():
    # БАННЕР ИНСТРУМЕНТОВ
    clear()
    stderr.writelines(f"""
       ________               __      ______                __  
      / ____/ /_  ____  _____/ /_    /_  __/________ ______/ /__
     / / __/ __ \/ __ \/ ___/ __/_____/ / / ___/ __ `/ ___/ //_/
    / /_/ / / / / /_/ (__  ) /_/_____/ / / /  / /_/ / /__/ ,<   
    \____/_/ /_/\____/____/\__/     /_/ /_/   \__,_/\___/_/|_| 

              {Wh}[ + ] Разработчик: Admt_450 [ + ]
    """)

    stderr.writelines(f"\n\n\n{option_text()}")


def run_banner():
    clear()
    time.sleep(1)
    stderr.writelines(f"""{Wh}
         .-.
       .'   `.          {Wh}--------------------------------
       :g g   :         {Wh}| {Gr}GHOST - TRACKER - IP ADDRESS {Wh}|
       : o    `.        {Wh}|       {Gr}@Разработчик Admt_450      {Wh}|
      :         ``.     {Wh}--------------------------------
     :             `.
    :  :         .   `.
    :   :          ` . `.
     `.. :            `. ``;
        `:;             `:'
           :              `.
            `.              `.     .
              `'`'`'`---..,___`;.-'
        """)
    time.sleep(0.5)


def main():
    clear()
    option()
    time.sleep(1)
    try:
        opt = int(input(f"{Wh}\n [ + ] {Gr}Выберите опцию : {Wh}"))
        execute_option(opt)
    except ValueError:
        print(f'\n{Wh}[ {Re}! {Wh}] {Re}Пожалуйста, введите номер')
        time.sleep(2)
        main()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(f'\n{Wh}[ {Re}! {Wh}] {Re}Выход')
        time.sleep(2)
        exit()
