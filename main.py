import os
import string
from unittest import async_case
import discord as dc
import time
import pyautogui as auto
from dotenv import load_dotenv
from discord.ext import commands
import win32api, win32con

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intent = dc.Intents.all()

bot = commands.Bot(intents = intent, command_prefix="$")

def pressKeys(coord):
    keys = list(map(int, str(coord)))
    for key in keys:
        match key:
            case 1:
                time.sleep(0.3)
                auto.keyDown('1')
                time.sleep(0.3)
            case 2:
                time.sleep(0.3)
                auto.keyDown('2')
                time.sleep(0.3)
            case 3:
                time.sleep(0.3)
                auto.keyDown('3')
                time.sleep(0.3)
            case 4:
                time.sleep(0.3)
                auto.keyDown('4')
                time.sleep(0.3)
            case 5:
                time.sleep(0.3)
                auto.keyDown('5')
                time.sleep(0.3)
            case 6:
                time.sleep(0.3)
                auto.keyDown('6')
                time.sleep(0.3)
            case 7:
                time.sleep(0.3)
                auto.keyDown('7')
                time.sleep(0.3)
            case 8:
                time.sleep(0.3)
                auto.keyDown('8')
                time.sleep(0.3)
            case 9:
                time.sleep(0.3)
                auto.keyDown('9')
                time.sleep(0.3)
            case 0:
                time.sleep(0.3)
                auto.keyDown('0')
                time.sleep(0.3)
    

def goToCoords(x, y):
    #click coords
    win32api.SetCursorPos((359, 18))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.2)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    #insert coordinate x
    time.sleep(2)
    win32api.SetCursorPos((948, 317))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.2)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(1)
    pressKeys(x)
    time.sleep(1)

    #insert coordinate y
    time.sleep(2)
    win32api.SetCursorPos((1110, 315))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.2)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(1)
    pressKeys(y)
    time.sleep(1)

    #search
    win32api.SetCursorPos((1217, 317))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.2)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(3)

    #click on village
    win32api.SetCursorPos((956, 543))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.2)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


@bot.command()
async def duke(ctx, x, y):
    time.sleep(3)
    goToCoords(x, y)
    #TODO: click on 

@bot.command()
async def architect(ctx, x, y):
    time.sleep(3)
    goToCoords(x, y)
    #TODO: click on

@bot.command()
async def scientist(ctx, x, y):
    time.sleep(3)
    goToCoords(x, y)
    #TODO: click on

bot.run(TOKEN)