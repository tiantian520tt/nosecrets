import time
import ctypes, sys
from colorama import Back, Fore, init
import random
import threading
import keyboard
import requests
import json
import os
init()
# green
def printGreen(mess):
    #set_cmd_text_color(FOREGROUND_GREEN)
    print(Fore.GREEN,end='')
    sys.stdout.write(mess)
    print(Fore.RESET)


# red
def printRed(mess):
    #set_cmd_text_color(FOREGROUND_RED)
    print(Fore.RED,end='')
    sys.stdout.write(mess)
    print(Fore.RESET)


# yellow
def printYellow(mess):
    #set_cmd_text_color(FOREGROUND_YELLOW)
    print(Fore.YELLOW,end='')
    sys.stdout.write(mess)
    print(Fore.RESET)


def printColor(mess, color, END):
    exec('print(Fore.'+str(color).upper()+',end=\'\')')
    sys.stdout.write(mess)
    print(Fore.RESET,end=END)




loaded_modules = {}
module_helps = {}

for module in os.listdir('./mods/'):
    try:
        with open('./mods/'+str(module),'r',encoding='utf-8') as mod:
            tmp = mod.read()
    except:
        printRed('[-] Loaded mod '+str(module)+' failed. Encode Error.')
    try:
        exec(tmp)
        loaded_modules.update({str(module).replace('.py',''):str(module).replace('.py','')+'_main'})
        module_helps.update({str(module).replace('.py',''):[Auther,Date,EN_Description,CN_Description]})
        printGreen('[*] Loaded mod '+str(module)+'.')
    except:
        printRed('[-] Loaded mod '+str(module)+' failed. The mod had been broken.')

with open('loader.py','r') as f:
    exec(f.read())