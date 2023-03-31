# Voicecord
Make your discord account 24/7 online on voice channels!

----

A code written in Python that helps you to keep your account 24/7 on discord voice channels.

#### Please check out this if you want to add multiple tokens with just one file: [phantom.sellix.io/product/6359655010aec](https://phantom.sellix.io/product/6359655010aec)

---

The [main.py](https://github.com/SealedSaucer/Voicecord/blob/main/main.py) is the main file. [keep_alive.py](https://github.com/SealedSaucer/Voicecord/blob/main/keep_alive.py) prevents your repl from going to sleep. (If you have a replit hacker plan or want to run the script locally, then you can delete [this file](https://github.com/SealedSaucer/Voicecord/blob/main/keep_alive.py) and paste this code inside the [main.py](https://github.com/SealedSaucer/Voicecord/blob/main/main.py) file : 

</br>

```py
import sys
import json
import time
import requests
import websocket

status = "online"

GUILD_ID = ADD_YOUR_SERVER_ID_HERE
CHANNEL_ID = ADD_YOUR_CHANNEL_ID_HERE
SELF_MUTE = True
SELF_DEAF = False

usertoken = "Add your token here"

headers = {"Authorization": usertoken, "Content-Type": "application/json"}

validate = requests.get('https://discordapp.com/api/v9/users/@me', headers=headers)
if validate.status_code != 200:
  print("[ERROR] Your token might be invalid. Please check it again.")
  sys.exit()

userinfo = requests.get('https://discordapp.com/api/v9/users/@me', headers=headers).json()
username = userinfo["username"]
discriminator = userinfo["discriminator"]
userid = userinfo["id"]

def joiner(token, status):
    ws = websocket.WebSocket()
    ws.connect('wss://gateway.discord.gg/?v=9&encoding=json')
    start = json.loads(ws.recv())
    heartbeat = start['d']['heartbeat_interval']
    auth = {"op": 2,"d": {"token": token,"properties": {"$os": "Windows 10","$browser": "Google Chrome","$device": "Windows"},"presence": {"status": status,"afk": False}},"s": None,"t": None}
    vc = {"op": 4,"d": {"guild_id": GUILD_ID,"channel_id": CHANNEL_ID,"self_mute": SELF_MUTE,"self_deaf": SELF_DEAF}}
    ws.send(json.dumps(auth))
    ws.send(json.dumps(vc))
    time.sleep(heartbeat / 1000)
    ws.send(json.dumps({"op": 1,"d": None}))

def run_joiner():
  print(f"Logged in as {username}#{discriminator} ({userid}).")
  while True:
    joiner(usertoken, status)
    time.sleep(30)

run_joiner()
```

This code is from [this tutorial](https://youtu.be/u9P2K2pNNJQ). If you have any doubts regarding this, feel free to [contact me](https://dsc.gg/phantom).

---

> **Warning**
> : Self-bots are discouraged by Discord and is against Discord's ToS. You might get banned for this if not used properly.

> **Note**
> : Discord's Terms of Service: [discord.com/terms](https://discord.com/terms)

#### This repository is in no way affiliated with, authorized, maintained, sponsored or endorsed by Discord Inc. (discord.com) or any of its affiliates or subsidiaries.

---

### DO NOT GIVE YOUR TOKEN TO OTHERS!

#### Giving your token to someone else will give them the ability to log into your account without the password or 2FA.

---

> ⭐ Feel free to star the repository if this helped you! ;)
