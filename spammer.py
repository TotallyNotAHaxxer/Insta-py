from instabot import Bot
import os 
import sys 
import time as t 
from datetime import datetime
from colorama import init 
from colorama import Fore, Back, Style
import requests 
import platform
from requests import get 

#win colors 
init()

#node/sys name 
uname = platform.uname()


# FETCH IP FOR RESPONSE 
ip = get('https://api.ipify.org').text


def CS(X):
    t.sleep(X)
    if sys.platform == 'win32':
        os.system('cls')
    if sys.platform == 'linux':
        os.system('clear')
    if sys.platform == 'darwin':
        os.system('clear') #depending on system platfrom commands transit


def send_image():
    bot = Bot()
    bot.login(username=f"{user}", password=f"{password}")
    t.sleep(1)
    image   = str(input(" Image   >>> "))
    t.sleep(1)
    caption = str(input(" Caption >>> "))
    t.sleep(1)
    print("")
    bot.upload_photo(f"{image}", password=f"{password}")


def send_message():
    t.sleep(1)
    bot = Bot()
    bot.login(username=f"{user}", password=f"{password}")
    t.sleep(1)
    user2 = str(input(" User To Send To   >>> "))
    message = str(input(" Message To Send >>> "))
    print("")
    bot.send_message(f"{message}", [f'{user}',f'{user2}'])

def spam_message():
    t.sleep(1)
    bot = Bot()
    bot.login(username=f"{user}", password=f"{password}") # use f string 
    t.sleep(1)
    user2 = str(input(" User To Send To   >>> ")) # add a optional message 
    message = str(input(" Message To Send >>> ")) # optional user fuck i- nevermind 
    print("")
    while True: # when in a while true loop, it stays constant and will continue to send the message back and fourth 
        bot.send_message(f"{message}", [f'{user}',f'{user2}'])

def follow():
    t.sleep(1)
    bot = Bot()
    bot.login(username=f"{user}", password=f"{password}")
    t.sleep(1)
    who = str(input(" User TO Follow >>> "))
    bot.follow(f"{who}")






def check():
    r = requests.get('https://www.google.com') # test response 
    t.sleep(2)
    if r.status_code == 200: # if code = 200 dont do nothign and continue if it doesnt exit script 
        print("")
    else:
        print("o(╥﹏╥)o ~ i failed you...")
        print ('[!] Connection refused Try Again later......')
        sys.exit()    

def banner():
    CS(2)
    print(Fore.MAGENTA+"""

          _              _                  _               _                _                            _       _        _   
         /\ \           /\ \     _         / /\            /\ \             / /\                         /\ \    /\ \     /\_\ 
         \ \ \         /  \ \   /\_\      / /  \           \_\ \           / /  \                       /  \ \   \ \ \   / / / 
         /\ \_\       / /\ \ \_/ / /     / / /\ \__        /\__ \         / / /\ \                     / /\ \ \   \ \ \_/ / /  
        / /\/_/      / / /\ \___/ /     / / /\ \___\      / /_ \ \       / / /\ \ \       ____        / / /\ \_\   \ \___/ /   
       / / /        / / /  \/____/      \ \ \ \/___/     / / /\ \ \     / / /  \ \ \    /\____/\     / / /_/ / /    \ \ \_/    
      / / /        / / /    / / /        \ \ \          / / /  \/_/    / / /___/ /\ \   \/____\/    / / /__\/ /      \ \ \     
     / / /        / / /    / / /     _    \ \ \        / / /          / / /_____/ /\ \             / / /_____/        \ \ \    
 ___/ / /__      / / /    / / /     /_/\__/ / /       / / /          / /_________/\ \ \           / / /                \ \ \   
/\__\/_/___\    / / /    / / /      \ \/___/ /       /_/ /          / / /_       __\ \_\         / / /                  \ \_\  
\/_________/    \/_/     \/_/        \_____\/        \_\/           \_\___\     /____/_/         \/_/                    \/_/  
                                                                                                                               
                                                                                                 V 1.0 
""")



def menu():
    print(Fore.RED+"───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
    print(f" [RUNNING-NODE] ==> {uname.node} ",f"[USER-NAME] ~~> {user} [PASSWORD] ~~> {password} ""[PUBLIC-ADDRESS] ==> {}".format(ip))
    print("")
    print("                                                                          (҂‾ ▵‾)︻デ═一                (˚▽˚’!)/ ")
    print(Fore.RED+"───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
    print(" [1] ~~> Post A Image          | [2]  ~~>   Follow Someone     | [3] ~~> Send A Message        |   [4] Spam A Message     ")
    print("")
    print("")
    insta = str(input(" >>> "))

    if '1' == insta:
        print(" [+] Running Mods.... ")
        send_image() # send the image 
    
    elif '2' == insta:
        print(" [!] Running.... ")
        follow()
    
    elif '3' == insta:
        print(" [=] Please Wait.... ")
        send_message()
    
    elif '4' == insta:
        print(" [+] Running mod ")
        spam_message()
    
    else:
        banner()
        menu()






def bot():
    bot = Bot()
    bot.login(username=f"{user}", password=f"{password}")

    ######  upload a picture #######
    bot.upload_photo("yoda.jpg", caption="biscuit eating baby")

    #follow someone 
    bot.follow("elonrmuskk")

    ######send a message 
    bot.send_message("Hello from Dhaval", ['user1','user2'])

    #get follower info 
    my_followers = bot.get_user_followers("dhavalsays")
    for follower in my_followers:
        print(follower)

    bot.unfollow_everyone()

if __name__ == "__main__": # if name in main for better organization 
    banner()
    user     = str(input(" Username >>> "))
    t.sleep(1)
    password = str(input(" Password >>> "))
    CS(3)
    banner()
    menu()