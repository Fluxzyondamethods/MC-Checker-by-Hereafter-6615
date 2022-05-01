import os
from os import system, name
from colorama import Fore, Back, Style, init
import json
import time
import threading
from minecraftchecker import counter
from minecraftchecker import reset

def minecraftui():
    system(f'title Username Checker v2 By Hereafter#6615')
    os.system('cls')
    banner = f"""{Fore.RED}
    
    $$\      $$\  $$$$$$\         $$$$$$\  $$\                           $$\                           
    $$$\    $$$ |$$  __$$\       $$  __$$\ $$ |                          $$ |                          
    $$$$\  $$$$ |$$ /  \__|      $$ /  \__|$$$$$$$\   $$$$$$\   $$$$$$$\ $$ |  $$\  $$$$$$\   $$$$$$\  
    $$\$$\$$ $$ |$$ |            $$ |      $$  __$$\ $$  __$$\ $$  _____|$$ | $$  |$$  __$$\ $$  __$$\ 
    $$ \$$$  $$ |$$ |            $$ |      $$ |  $$ |$$$$$$$$ |$$ /      $$$$$$  / $$$$$$$$ |$$ |  \__|
    $$ |\$  /$$ |$$ |  $$\       $$ |  $$\ $$ |  $$ |$$   ____|$$ |      $$  _$$<  $$   ____|$$ |      
    $$ | \_/ $$ |\$$$$$$  |      \$$$$$$  |$$ |  $$ |\$$$$$$$\ \$$$$$$$\ $$ | \$$\ \$$$$$$$\ $$ |      
    \__|     \__| \______/        \______/ \__|  \__| \_______| \_______|\__|  \__| \_______|\__|      
                                                                                                                         
    {Fore.LIGHTRED_EX}Made by Hereafter#6615 -> https://discord.gg/h9SuzYa3aP                                                                                                                               

    """

    ALTERNATIVES = f"""
          Menu                  Settings                                 Webhooks
    ------------------     ------------------                       ------------------
    [{Fore.RED}1{Fore.YELLOW }] Start              [{Fore.RED}3{Fore.YELLOW }] Insert Bearer                        [{Fore.RED}7{Fore.YELLOW }] Toggle Webhook
    [{Fore.RED}2{Fore.YELLOW }] Exit               [{Fore.RED}4{Fore.YELLOW }] Dictionary Words (y/n)               [{Fore.RED}8{Fore.YELLOW }] Insert Webhook
                           [{Fore.RED}5{Fore.YELLOW }] Username Length
                           [{Fore.RED}6{Fore.YELLOW }] Amount Of Usernames To Check
    """
    print(banner)
    print(Fore.YELLOW + Style.BRIGHT + ALTERNATIVES)

    choice = input(Style.BRIGHT + f'\n    {Fore.RED}[{Fore.WHITE}CONSOLE{Fore.RED}]{Fore.YELLOW } -> ')

    if choice == "1":
        thread1 = threading.Thread(target=counter)
        thread1.start()
        from minecraftchecker import checker
        checker()
        print(Style.BRIGHT + f'\n    {Fore.RED}[{Fore.WHITE}CHANGELOG{Fore.RED}]{Fore.YELLOW} Script Ended Succsessfully!')
        input(Style.BRIGHT + f'    {Fore.RED}[{Fore.WHITE}CONSOLE{Fore.RED}]{Fore.YELLOW} Press ENTER To Return To Main Menu...')
        thread2 = threading.Thread(target=reset)
        thread2.start()
        minecraftui()
    if choice == '2':
        print(Style.BRIGHT + f'\n    {Fore.RED}[{Fore.WHITE}CHANGELOG{Fore.RED}]{Fore.YELLOW} Exited Program Succsessfully!')
        exit()
    if choice == '3':
        with open("util/config.json", 'r') as j:
            contents = json.loads(j.read())

            currentsetting = contents['bearer']
        print(Style.BRIGHT + f'\n    {Fore.RED}[{Fore.WHITE}CONSOLE{Fore.RED}]{Fore.YELLOW} Currently Set To: {Fore.RED}{currentsetting}\n')
        bearer = input(Style.BRIGHT + f'    {Fore.RED}[{Fore.WHITE}CONSOLE{Fore.RED}]{Fore.YELLOW} Bearer Token: ')
        with open("util/config.json", "r") as jsonFile:
            data = json.load(jsonFile)

            data["bearer"] = bearer

            with open("util/config.json", "w") as jsonFile:
                json.dump(data, jsonFile)
                jsonFile.close()
                print(Style.BRIGHT + f'    {Fore.RED}[{Fore.WHITE}CHANGELOG{Fore.RED}]{Fore.YELLOW} Succsessfully updated Bearer!')
                time.sleep(3)
                minecraftui()
    if choice == '4':
        with open("util/config.json", 'r') as j:
            contents = json.loads(j.read())

            currentsetting = contents['dictwords']
        print(Style.BRIGHT + f'\n    {Fore.RED}[{Fore.WHITE}CONSOLE{Fore.RED}]{Fore.YELLOW} Currently Set To: {Fore.RED}{currentsetting}\n')
        yn = input(Style.BRIGHT + f'    {Fore.RED}[{Fore.WHITE}CONSOLE{Fore.RED}]{Fore.YELLOW} Dictionary Words (y/n): ')
        x = yn in ["y", "n"]
        if not x:
            print(f'    {Fore.RED}[{Fore.WHITE}ERROR{Fore.RED}]{Fore.YELLOW} Invalid Character! (y/n)')
            time.sleep(3)
            minecraftui()
        with open("util/config.json", "r") as jsonFile:
            data = json.load(jsonFile)

            data["dictwords"] = yn

            with open("util/config.json", "w") as jsonFile:
                json.dump(data, jsonFile)
                jsonFile.close()
                print(Style.BRIGHT + f'    {Fore.RED}[{Fore.WHITE}CHANGELOG{Fore.RED}]{Fore.YELLOW} Succsessfully changed Dictionary Words to {Fore.RED}{yn}')
                time.sleep(3)
                minecraftui()
    if choice == '5':
        with open("util/config.json", 'r') as j:
            contents = json.loads(j.read())

            currentsetting = contents['username length']
        print(Style.BRIGHT + f'\n    {Fore.RED}[{Fore.WHITE}CONSOLE{Fore.RED}]{Fore.YELLOW} Currently Set To: {Fore.RED}{currentsetting}\n')
        amount = input(Style.BRIGHT + f'    {Fore.RED}[{Fore.WHITE}CONSOLE{Fore.RED}]{Fore.YELLOW} Username Length: ')
        isnumeric = amount.isnumeric()
        
        if not isnumeric:
            print(f'    {Fore.RED}[{Fore.WHITE}ERROR{Fore.RED}]{Fore.YELLOW} Variable Must Be Numeric!')
            time.sleep(3)
            minecraftui()
        amount = int(amount)
        if amount >= 25:
            print(f'    {Fore.RED}[{Fore.WHITE}ERROR{Fore.RED}]{Fore.YELLOW} Usernames have to be between 2 and 24 characters')
            time.sleep(3)
            minecraftui()
        if amount <= 1:
            print(f'    {Fore.RED}[{Fore.WHITE}ERROR{Fore.RED}]{Fore.YELLOW} Usernames have to be between 2 and 24 characters')
            time.sleep(3)
            minecraftui()
        with open("util/config.json", "r") as jsonFile:
            data = json.load(jsonFile)

            data["username length"] = amount

            with open("util/config.json", "w") as jsonFile:
                json.dump(data, jsonFile)
                jsonFile.close()
                print(Style.BRIGHT + f'    {Fore.RED}[{Fore.WHITE}CHANGELOG{Fore.RED}]{Fore.YELLOW} Succsessfully changed Username Length to {Fore.RED}{amount}')
                time.sleep(3)
                minecraftui()
    if choice == '6':
        with open("util/config.json", 'r') as j:
            contents = json.loads(j.read())

            currentsetting = contents['amount of usernames to check']
        print(Style.BRIGHT + f'\n    {Fore.RED}[{Fore.WHITE}CONSOLE{Fore.RED}]{Fore.YELLOW} Currently Set To: {Fore.RED}{currentsetting}\n')
        amount = input(Style.BRIGHT + f'    {Fore.RED}[{Fore.WHITE}CONSOLE{Fore.RED}]{Fore.YELLOW} Amount Of Usernames To Check: ')
        isnumeric = amount.isnumeric()
        
        if not isnumeric:
            print(f'    {Fore.RED}[{Fore.WHITE}ERROR{Fore.RED}]{Fore.YELLOW} Variable Must Be Numeric!')
            time.sleep(3)
            minecraftui()

        with open("util/config.json", "r") as jsonFile:
            data = json.load(jsonFile)

            data["amount of usernames to check"] = amount

            with open("util/config.json", "w") as jsonFile:
                json.dump(data, jsonFile)
                jsonFile.close()
                print(Style.BRIGHT + f'    {Fore.RED}[{Fore.WHITE}CHANGELOG{Fore.RED}]{Fore.YELLOW} Succsessfully changed Amount Of Usernames To Check to {Fore.RED}{amount}')
                time.sleep(3)
                minecraftui()
    if choice == '7':
        with open("util/config.json", 'r') as j:
            contents = json.loads(j.read())

            webhook = contents['webhook']
            currentsetting = contents['toggle-webhook']
        print(Style.BRIGHT + f'\n    {Fore.RED}[{Fore.WHITE}CONSOLE{Fore.RED}]{Fore.YELLOW} Currently Set To: {Fore.RED}{currentsetting}\n')
        yn = input(Style.BRIGHT + f'    {Fore.RED}[{Fore.WHITE}CONSOLE{Fore.RED}]{Fore.YELLOW} Toggle Webhook (y/n): ')
        with open("util/config.json", 'r') as j:
            contents = json.loads(j.read())

            webhook = contents['webhook']

        if webhook == "":
            if yn == "y":
                print(f"    {Fore.RED}[{Fore.WHITE}ERROR{Fore.RED}]{Fore.YELLOW} Couldn't Toggle Due To Webhook Not Inserted!")
                time.sleep(3)
                minecraftui()
        x = yn in ["y", "n"]
        if not x:
            print(f'    {Fore.RED}[{Fore.WHITE}ERROR{Fore.RED}]{Fore.YELLOW} Invalid Character! (y/n)')
            time.sleep(3)
            minecraftui()

        with open("util/config.json", "r") as jsonFile:
            data = json.load(jsonFile)

            data["toggle-webhook"] = yn

            with open("util/config.json", "w") as jsonFile:
                json.dump(data, jsonFile)
                jsonFile.close()
                print(Style.BRIGHT + f'    {Fore.RED}[{Fore.WHITE}CHANGELOG{Fore.RED}]{Fore.YELLOW} Succsessfully changed Toggle Webhook to {Fore.RED}{yn}')
                time.sleep(3)
                minecraftui()
    if choice == '8':
        webhook = input(Style.BRIGHT + f'\n    {Fore.RED}[{Fore.WHITE}CONSOLE{Fore.RED}]{Fore.YELLOW} Insert Webhook: ')

        if "discord.com/api/webhooks/" not in webhook:
            print(f'    {Fore.RED}[{Fore.WHITE}ERROR{Fore.RED}]{Fore.YELLOW} Please Insert A Discord WEBHOOK!')
            time.sleep(3)
            minecraftui()

        with open("util/config.json", "r") as jsonFile:
            data = json.load(jsonFile)

            data["webhook"] = webhook

            with open("util/config.json", "w") as jsonFile:
                json.dump(data, jsonFile)
                jsonFile.close()
                print(Style.BRIGHT + f'    {Fore.RED}[{Fore.WHITE}CHANGELOG{Fore.RED}]{Fore.YELLOW} Succsessfully updated Webhook')
                time.sleep(3)
                minecraftui()
minecraftui()