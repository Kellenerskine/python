import discord
from discord.ext import commands

client = commands.Bot(command_prefix=">")

@client.event
async def on_ready():
    print("Bot is ready")

@client.command()
async def hello(ctx):
    await ctx.send("Hi")

client.run("NzU3OTc1NDc4NDYzMjM0MTA4.X2oNrA.QqtkFTGHZasUYyBaUzHmTn-PRT4")