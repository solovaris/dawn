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

    @commands.command(aliases=["dice"])  # Dice
    async def roll(self, ctx):
        dice_number = random.randint(1, 6)
        await ctx.send(f":game_die: Rolling... **{dice_number}**")

    @commands.command()  # Meme Feed
    async def meme(self, ctx):
        content = get("https://meme-api.com/gimme").text
        data = json.loads(content)
        meme = discord.Embed(title=f"{data['title']}", color=discord.Color.random())
        meme.set_image(url=f"{data['url']}")
        meme.set_footer(text=f'Requested by {ctx.message.author}')
        await ctx.reply(embed=meme)

    @commands.command(aliases=["pfp", "av"])  # User Avatar  NEEDS FIX!!!!
    async def avatar(self, ctx, *, member: discord.Member = None):
        if not member:
            member = ctx.message.author
        useravatar = member.avatar
        embed = discord.Embed(title=f"{member}'s Avatar", color=discord.Color.random())
        embed.set_image(url=f"{useravatar}")
        embed.set_footer(text=f'Requested by {ctx.message.author}')
        await ctx.send(embed=embed)


async def setup(client):
    await client.add_cog(Fun(client))
