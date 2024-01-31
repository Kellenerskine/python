# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv()

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run("NzU3OTc1NDc4NDYzMjM0MTA4.X2oNrA.MR0ZAfD_HukFxTRtXl98slXLBTM")