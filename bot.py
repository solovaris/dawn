import discord
from discord.ext import commands
import os
import asyncio


client = commands.Bot(command_prefix=">", intents=discord.Intents.all())  # Creating connection to interact with Discord API
with open("bot_token.txt", "r") as f:  # Token
    token = f.readline()


@client.event  # Status and Turning the bot on
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.streaming, name='>help', url='https://www.youtube.com/watch?v=dMXJHw2z8s4'))
    print('\x1b[1;32;4m' + str(client.user) + ' is now up and running' + '\x1b[0m')


dad_on = True


@client.command()  # Dad reply config
async def imdad(ctx, dadstate: str = "on"):
    global dad_on  # Global variable to keep the state of the dad joke feature

    if dadstate.lower() == "on":
        if dad_on is False:
            dad_on = True
            await ctx.send("Dad joke feature enabled.")
        elif dad_on is True:
            await ctx.send(":x: This feature has already been enabled!")

    elif dadstate.lower() == "off":
        if dad_on is True:
            dad_on = False
            await ctx.send("Dad joke feature disabled.")
        elif dad_on is False:
            await ctx.send(":x: This feature has already been disabled!")


@client.event  # Plaintext commands - Message log + dawn + Dad reply
async def on_message(message):
    if message.author == client.user:
        return

    username = message.author.name
    user_message = message.content
    channel = message.channel

    print(f'{username} said: "{user_message}" in {channel}.')

    await client.process_commands(message)  # process commands first

    # "dawn"
    if user_message.lower() == "dawn":
        await message.channel.send(f"Hello {message.author.mention}, I'm Dawn! Type `>help` for more info.")

    # Dad reply
    elif user_message.lower().startswith(("i'm", "im", "i am")) and dad_on:
        dadjoke_message = user_message.lower().split()
        possible_joke = False
        while True:
            if "im" in dadjoke_message or "IM" in dadjoke_message:
                dadjoke_message.remove("im")
                possible_joke = True
            elif "i" in dadjoke_message and "am" in dadjoke_message:
                dadjoke_message.remove('i')
                dadjoke_message.remove('am')
                possible_joke = True
            elif "i'm" in dadjoke_message or "I'M" in dadjoke_message:
                dadjoke_message.remove("i'm")
                possible_joke = True
            else:
                break
        if possible_joke is True and "@everyone" not in dadjoke_message and dad_on is True:
            await message.channel.send(f"Hi {' '.join(dadjoke_message)}, I'm dad!")


# COGS
@client.event
async def load():
    for filename in os.listdir("cogs"):
        if filename.endswith(".py"):
            await client.load_extension(f"cogs.{filename[:-3]}")


# Start the bot
async def main():
    async with client:
        await load()
        await client.start(token)

asyncio.run(main())
