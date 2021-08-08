# Voicecord
Make your Discord Account Online 24/7 on Voice Channels!

----

A Code written in Python that helps you to keep your account 24/7 on Voice Channels.

# Installation

• Fork the repo

• Clone it to replit

• Install the Self-Bot Package : `pip install discord.py-self`

• Install PyNaCl using the Package Manager

> I would really suggest you to watch [this video](https://youtu.be/gvSgnPER6Kw) before installing.

---

The [main.py](https://github.com/SealedSaucer/Voicecord/blob/main/main.py) is the main file. [keep_alive.py](https://github.com/SealedSaucer/Voicecord/blob/main/keep_alive.py) prevents your repl from going to sleep. (If you have a replit hacker plan, then you can delete [this file](https://github.com/SealedSaucer/Voicecord/blob/main/keep_alive.py) and paste this code inside the [main.py](https://github.com/SealedSaucer/Voicecord/blob/main/main.py) file : 

</br>

```py
import discord
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

bot.add_cog(Music(bot))
bot.run(os.getenv("TOKEN"))
```

This Code is from [this tutorial](https://youtu.be/gvSgnPER6Kw). If you have any doubts regarding this, feel free to [contact me](https://dsc.gg/phantom).

**DO NOT GIVE YOUR TOKEN TO OTHERS!**

Use [uptimerobot.com](https://uptimerobot.com) to make your repl online 24/7.

</br>

> ⭐ Feel free to Star the Repository if this helped you! ;)

----

> Voicecord © 2021 by SealedSaucer is licensed under Attribution 4.0 International 
