from discord.ext import commands


class General(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("General commands are ready!")

    @commands.command()  # Ping
    async def ping(self, ctx):
        bot_latency = round(self.client.latency * 1000)
        await ctx.send(f'Pong!\n**{bot_latency} ms.**')

    @commands.command()  # Help
    async def dawnhelp(self, ctx):
        await ctx.send('''__**List of Commands [Prefix: >]:**__\n```ini
    [8ball] - Rolls a dice
    [cock] - Reveals your deepest insecurities... or not ¯\_(ツ)_/¯
    [help] - This
    ```''')


async def setup(client):
    await client.add_cog(General(client))
