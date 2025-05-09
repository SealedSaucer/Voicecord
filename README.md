<div id="SealedSaucer" align="center">
    <h1>Voicecord</h1>
    <p>Make Your Discord Account 24/7 On Voice Channels!</p>
    <a href="https://github.com/SealedSaucer/Voicecord/blob/main/LICENSE"><img src="https://img.shields.io/github/license/SealedSaucer/Voicecord?style=for-the-badge"></a>
    <a href="https://sealedsaucer.sell.app"><img src="https://img.shields.io/badge/SHOP-CLICK HERE-5e40e4?style=for-the-badge"></a>
    <a href="https://phantom.fr.to/verify"><img src="https://img.shields.io/badge/contact-click me-05babf?style=for-the-badge"></a>
    <br>
    <img src="https://i.imgur.com/Pzu4u0S.png" height="100">
</div>

---

<p align="center">
If you want to connect tokens to a voice channel in bulk, consider checking out my store: <b><a href="https://sealedsaucer.sell.app">click here</a></b>! ☄️
<br>
⭐ Feel free to star the repository if this helped you!
</p>

## Disclaimer
By using this code, you are automating your Discord Account. This is against Discord's Terms of Service and Community Guidelines. If not used properly, your account(s) might get suspended or terminated by Discord. I, the developer, is not responsible for any consequences that may arise from the use of this code. Use this software at your own risk and responsibility. Learn more about <a href="https://discord.com/terms">Discord's Terms of Service</a> and <a href="https://discord.com/guidelines">Community Guidelines</a> here.
#### This repository is in no way affiliated with, authorized, maintained, sponsored or endorsed by Discord Inc. (discord.com) or any of its affiliates or subsidiaries.

## Warning
**DO <ins>NOT</ins> GIVE YOUR DISCORD TOKENS TO ANYONE.**
#### Giving your token to someone else will give them the ability to log into your account without the password or 2FA.

## Features:
- 🔒 Secure
- Supports Stage Channels
- Account will stay 24/7 online and connected (if you set it up correctly)
- Supports all three status modes (Online, Idle, Do Not Disturb)
- Can be used almost on any platform that supports [Python](https://python.org)

## Installation
### · Replit
#### The code inside the repository was originally made to be hostable on [Replit](https://replit.com), but due to a recent ban on all repositories that are against Discord's ToS, you won't be able to import this repository directly to Replit anymore.
#### Here's a workaround to solve that issue:
1. Click [here](https://github.com/SealedSaucer/Voicecord/archive/refs/heads/main.zip) to download the latest version of this code.
2. Unzip the file
3. Create a new Python repl on [Replit](https://replit.com)
4. Upload the files into the repl (Just drag and drop it into the files sidebar)
5. Overwrite the files if a prompt pops-up
6. Add your token inside Secrets ([Guide](https://docs.replit.com/programming-ide/workspace-features/storing-sensitive-information-environment-variables)) with `TOKEN` as the key and your token as the value ([Video](https://youtu.be/sYGdDLLu8cU))
7. Add your Guild (Server) ID and Channel ID
8. Modify the status mode or mute/deaf option (`True` or `False`), if you want to make any adjustments
9. Run the repl
10. Add your repl url to an uptime monitor ([Video](https://youtu.be/dVIjpCqnZXE))

### · Local Installation
1. Install [Python](https://python.org/downloads) on your machine (Make sure you add it to [PATH](https://i.imgur.com/Ukl6HdQ.png))
2. Copy the code below
<details>
<summary> Click here to view the code, click again to close it</summary>
<br>

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
</details>

3. Create a new Python file and paste the code into it
4. Add your Guild (Server) ID and Channel ID
5. Modify the status mode or mute/deaf option (`True` or `False`), if you want to make any adjustments
6. Save the file
7. Create a `requirements.txt` file and copy paste the file contents inside [requirements.txt](https://github.com/SealedSaucer/Voicecord/blob/main/requirements.txt) without the `Flask` module
8. Save the file
8. Open command prompt where both the files are present and run `pip install -r requirements.txt`
9. Once the packages are downloaded, either double click the python file inorder to run it or open command prompt where the python file is present and run `python filename.py`

## Known Errors And How To Fix Them
### [Replit] This repository could not be accessed, try again later/This repository possibly violates our Terms of Service. Contact support if you believe this is a mistake.
<details>
<summary>Click here to view the explanation and fix</summary>
<br>
As I mentioned before, due to a recent ban on all repositories that are against Discord's ToS, you won't be able to import this repository directly to Replit anymore. Follow <a href="https://github.com/SealedSaucer/Voicecord#heres-a-workaround-to-solve-that-issue">this</a> workaround to host the code on Replit.
</details>

### [Replit] sh: line 1: python3: command not found
<details>
<summary>Click here to view the explanation and fix</summary>
<br>
You cloned it into a bash repl. Make sure you select "Python" from the languages list when you create the repl.
</details>

### [Replit] Cloudflare Error/Temporarily banned from accessing Discord's API
<details>
<summary>Click here to view the explanation and fix</summary>
<br>
This happens because repls have Shared Public IP Addresses, and some Replit Users abuse the platform to spam (through selfbots or nukers). Whenever Discord sees lots of invalid requests coming from a single IP address, they will use Cloudflare to temporarily block any incoming requests.

#### Fix:
- Go to shell
- Enter <code>kill 1</code>
- Wait for the repl to reload
- Run the repl again
</details>

### [Replit] ModuleNotFoundError: No module named 'websocket'
<details>
<summary>Click here to view the explanation and fix</summary>
<br>
Run <code>pip install websocket</code> in the shell
</details>

### [Replit] TypeError: WebSocket.__init() missing 3 required positional arguments: 'environ', 'socket', and 'rfile'
<details>
<summary>Click here to view the explanation and fix</summary>
<br>
Run <code>pip install websocket-client</code> in the shell
</details>

## Help and Support
If you have any issues or doubts regarding this, feel free to [contact me](https://phantom.fr.to/verify).

---

<p align="center">❤️ Voicecord is licensed under GNU General Public License.</p>
