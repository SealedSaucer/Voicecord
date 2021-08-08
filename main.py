import discord
import keep_alive
import os
from discord.ext import commands

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def join(self, ctx, *, channel: discord.VoiceChannel):
        if ctx.voice_client is not None:
            return await ctx.voice_client.move_to(channel)
        await channel.connect()

    @commands.command()
    async def leave(self, ctx):
        await ctx.voice_client.disconnect()

bot = commands.Bot(command_prefix=("&"))

@bot.event
async def on_ready():
    print('Logged in as {0} ({0.id})'.format(bot.user))

keep_alive.keep_alive()
bot.add_cog(Music(bot))
bot.run(os.getenv("TOKEN"))
