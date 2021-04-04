import discord
import asyncio
import os
import random
import datetime

bot = discord.Client()

@bot.event
async def on_member_join(member):
    if member.id == bot.id:
        return
    channel = discord.utils.get(bot.guilds[0].channels, name="general")
    response = f"Welcome to the server, {member.name}"
    await channel.send(response)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    keywords = ["work", "workout", "push", "pushup", "up"]
    channel = message.channel
    for keyword in keywords:
        if keyword.lower() in message.content.lower():
            response = f"Did someone say {keyword.lower()}? Drop and give me 10 <@{message..}"
            await channel.send(response)

@bot.event
async def pushup_reminder():

    await 