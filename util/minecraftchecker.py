import requests
import string
import random
import time
import json
from colorama import Fore, Back, Style, init
from os import system, name

t = 80

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(f'    {Fore.RED}[{Fore.WHITE}TIMER{Fore.RED}] {Fore.YELLOW}' + timer, end="\r")
        time.sleep(1)
        t -= 1

available = 0
taken = 0
banned = 0

def reset():
    global available
    global taken
    global banned
    notinuse = 0
    taken = 0
    banned = 0

def counter():
    global available
    global taken
    global banned
    while True:
        system(f'title Username Checker v2 By Hereafter#6615 ^| Checker: Tiktok ^| Available: {available} ^| Taken: {taken} ^| Banned: {banned}')

def checker():
    global available
    global taken
    global banned
    print('')
    with open("util\config.json", 'r') as j:
        contents = json.loads(j.read())

        bearer = contents['bearer']
        amount = contents['amount of usernames to check']
        amount = int(amount)
        dictwords = contents['dictwords']
        length = contents['username length']
    headers = {
        'Authorization': f'Bearer {bearer}'
    }
    for x in range(amount):
        if dictwords == 'n':
            letters = string.ascii_letters + string.digits + "_"
            username = ''.join(random.choice(letters) for i in range(length))
        if dictwords == 'y':
            f = open('util/data/dictionarywords.txt', 'r').read().splitlines()
            username = random.choice(f)

        r = requests.get(f'https://api.minecraftservices.com/minecraft/profile/name/{username}/available', headers=headers)
        html = r.text

        if "NOT_ALLOWED" in html:
            banned = banned + 1
            print(Style.NORMAL + f'    {Fore.RED}[{Fore.WHITE}Not-Allowed{Fore.RED}]{Fore.RED} {username}')
            f = open('util/data/not_allowed.txt', 'a')
            f.write(f'{username}\n')
            f.close()
        if "AVAILABLE" in html:
            available = available + 1
            print(f'    {Fore.RED}[{Fore.WHITE}Available{Fore.RED}]{Fore.LIGHTGREEN_EX} {username}')
            f = open('util/data/available.txt', 'a')
            f.write(f'{username}\n')
            f.close()
        ####################################################################################################
            #Webhook
            with open("util/config.json", 'r') as j:
                contents = json.loads(j.read())

                webhook = contents['webhook']
                togglewebhook = contents['toggle-webhook']

            if togglewebhook == "y":
                url = webhook

                data = {
                    "username" : "Username Checker v2 - Hereafter#6615"
                }

                data["embeds"] = [
                    {
                        "type": "rich",
                        "title": "New Possible Available Username!",
                        "description": f"Username: **{username}**",
                        "color": 0x73ff00,
                    "thumbnail": {
                        "url": "https://cdn.discordapp.com/attachments/968914394689990677/968961514071543888/tiktok_tik_tok_logo_icon_134936.png",
                        "height": 0,
                        "width": 0
                    },
                    "footer": {
                        "text": "Thanks for using Hereafter#6615's username checker! If you have any questions, feel free to dm me.",
                        "icon_url": "https://cdn.discordapp.com/attachments/968914394689990677/968961514071543888/tiktok_tik_tok_logo_icon_134936.png"
                    }
                    }
                ]

                data["components"] = [
                    {
                        "type": 1,
                        "components": [
                            {
                                "style": "5",
                                "label": "Join Discord Server",
                                "url": "https://discord.gg/sFHQu3EPY9",
                                "disabled": "false",
                                "type": 2
                            }
                        ]
                    }
                ]

                result = requests.post(url, json = data)

                try:
                    result.raise_for_status()
                except requests.exceptions.HTTPError as err:
                    print(f'    {Fore.RED}[{Fore.WHITE}ERROR{Fore.RED}] {Fore.YELLOW} There Might Be An Error With Your Webhook! Make Sure All Settings Are Correct.', flush=True)
                ######################################################################################################################################################
        if "DUPLICATE" in html:
            taken = taken + 1
            print(Style.BRIGHT + f'    {Fore.RED}[{Fore.WHITE}Taken{Fore.RED}]{Fore.LIGHTRED_EX} {username}')
            f = open('util/data/Taken.txt', 'a')
            f.write(f'{username}\n')
            f.close()
        if r.status_code == 429:
            print(f'    {Fore.RED}[{Fore.WHITE}ERROR{Fore.RED}] {Fore.YELLOW}Too Many Requests, Activating Timer!')
            countdown(int(t))
            print(f'    {Fore.RED}[{Fore.WHITE}TIMER{Fore.RED}] {Fore.YELLOW}Continuing..')
        if r.status_code == 401:
            print(f'    {Fore.RED}[{Fore.WHITE}ERROR{Fore.RED}] {Fore.YELLOW}Invalid Bearer Token!')
            time.sleep(3)
            from minecraftui import minecraftui