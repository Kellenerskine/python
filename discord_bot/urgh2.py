import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print("Bot is ready.")

client.run('NzU3OTc1NDc4NDYzMjM0MTA4.X2oNrA.wjCm9PaXNzBgmW-lr9Z0iz57BVk')