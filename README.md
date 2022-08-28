# Voicecord
Make your discord account 24/7 online on voice channels!

----

A Code written in Python that helps you to keep your account 24/7 on discord voice channels.

---

The [main.py](https://github.com/SealedSaucer/Voicecord/blob/main/main.py) is the main file. [keep_alive.py](https://github.com/SealedSaucer/Voicecord/blob/main/keep_alive.py) prevents your repl from going to sleep. (If you have a replit hacker plan, then you can delete [this file](https://github.com/SealedSaucer/Voicecord/blob/main/keep_alive.py) and paste this code inside the [main.py](https://github.com/SealedSaucer/Voicecord/blob/main/main.py) file : 

</br>

```py
import discord
import os
from discord.ext import commands

client=commands.Bot(command_prefix=':', self_bot=True, help_command=None)

GUILD_ID = YOUR_GUILD_ID_HERE
CHANNEL_ID = YOUR_CHANNEL_ID_HERE

@client.event
async def on_ready():
    os.system('clear')
    print(f'Logged in as {client.user} ({client.user.id})')
    vc = discord.utils.get(client.get_guild(GUILD_ID).channels, id = CHANNEL_ID)
    await vc.guild.change_voice_state(channel=vc, self_mute=False, self_deaf=False)
    print(f"Successfully joined {vc.name} ({vc.id})")

client.run(os.getenv("TOKEN"))
```

This code is from [this tutorial](https://youtu.be/u9P2K2pNNJQ). If you have any doubts regarding this, feel free to [contact me](https://dsc.gg/phantom).

**DO NOT GIVE YOUR TOKEN TO OTHERS!**

Use [uptimerobot.com](https://uptimerobot.com) to make your repl online 24/7.

</br>

> ⭐ Feel free to star the repository if this helped you! ;)

----

> Voicecord by SealedSaucer is licensed under Attribution 4.0 International 
