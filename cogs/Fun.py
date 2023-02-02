import discord
from discord.ext import commands
import random
import json
from requests import get


class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Fun commands are ready!")

    @commands.command(aliases=["8ball", "eightball"])  # Magic 8 ball
    async def magic8ball(self, ctx, *, question=None):
        if not question:
            await ctx.send(':x: The magic 8 ball needs a question to answer.')
            return
        with open("magic8ball_responses.txt", "r") as f:
            magic8ball_random = f.readlines()
            magic8ball_response = random.choice(magic8ball_random).strip()

            mentions = ctx.message.mentions
            for mention in mentions:
                question = question.replace(mention.mention, mention.name)

            await ctx.send(f'> :8ball: {question}\n *"{magic8ball_response}"*')

    @commands.command(aliases=["penis", "peen"])  # Peen
    async def cock(self, ctx):
        pp_length = random.randint(1, 8)
        pp = "=" * pp_length
        await ctx.send(f"{ctx.author.name}'s peen:\n8{pp}D")

    @commands.command(aliases=["dice"])
    async def roll(self, ctx):
        dice_number = random.randint(1, 6)
        await ctx.send(f":game_die: Rolling... **{dice_number}**")

    @commands.command()
    async def meme(self, ctx):
        content = get("https://meme-api.com/gimme").text
        data = json.loads(content, )
        meme = discord.Embed(title=f"{data['title']}", color=discord.Color.random())
        meme.set_image(url=f"{data['url']}")
        await ctx.reply(embed=meme)


async def setup(client):
    await client.add_cog(Fun(client))
