import discord

client = discord.Client()

@client.event
async def on_message(message):
    message.content.lower()
    if message.author == client.user:
        return
    if message.content.startswith("time?"):

        if str(message.author) == "iwillbehere#0798":
            await message.channel.send("hello " + str(message.author))
        else:
            await message.channel.send("It is 2 am somewhere in the world right now...")

client.run("NzU3OTc1NDc4NDYzMjM0MTA4.X2oNrA.wjCm9PaXNzBgmW-lr9Z0iz57BVk")
