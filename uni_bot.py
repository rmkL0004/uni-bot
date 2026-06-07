import os
import discord
from discord.ext import commands
import re
import unicodedata
import random

TOKEN = os.environ["DISCORD_TOKEN"]

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

def contains_uni(text):
    text = unicodedata.normalize("NFKC", text)

    text = "".join(
        chr(ord(c) - 0x60)
        if "ァ" <= c <= "ヶ"
        else c
        for c in text
    )

    return (
        re.search(r"う\s*に", text)
        or re.search(r"uni", text, re.IGNORECASE)
    )

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if contains_uni(message.content):
        responses = [
            "うにだ！",
            "うに！",
            "うに発見！"
        ]

        await message.reply(random.choice(responses))

    await bot.process_commands(message)

bot.run(TOKEN)
