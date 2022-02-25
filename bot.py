import discord
from discord.ext import commands
from config import settings
import requests
import asyncio


bot = commands.Bot(command_prefix = settings["prefix"]) 

@bot.event
async def on_ready():
    while True:
        a = requests.get("https://mcapi.us/server/status?ip=" + settings["ip"], "&port=" + settings["port"])
        b = a.json()
        if b["online"] == True:
            online = b["players"]["now"]
            maxonline = b["players"]["max"]
            core = b["server"]["name"]
            print("------------------------------------\nSERVER ONLINE\n------------------------------------\nАйпи:" + settings["ip"] + f"\nОнлайн: {online}/{maxonline}" + f"\nЯдро: {core}")         
            await bot.change_presence(activity=discord.Game(f'Онлайн: {online}/{maxonline} | Статистика обновляется раз в минуту'))
        elif b["online"] == False:
            print("Сервер Оффлайн")
            await bot.change_presence(activity=discord.Game('Сервер офлайн'))
        await asyncio.sleep(settings["time"])



bot.run(settings["token"])

