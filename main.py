import sys
import json
import time
import requests
import websocket
from websocket._core import create_connection
from websocket._exceptions import WebSocketConnectionClosedException

status = "online"

GUILD_ID = "1358108404182159451"
CHANNEL_ID = "1358133795156656421"
SELF_MUTE = True
SELF_DEAF = False

usertoken = "NzAzMjI2MTc4NTQxOTc3NjAw.8pT1sx--iy1VoJAwE4gqVMlpPG0"

headers = {"Authorization": usertoken, "Content-Type": "application/json"}

validate = requests.get('https://discordapp.com/api/v9/users/@me', headers=headers)
if validate.status_code != 200:
    print("[ERROR] Invalid token. Check your token and try again.")
    sys.exit()

userinfo = validate.json()
username = userinfo["username"]
discriminator = userinfo["discriminator"]
userid = userinfo["id"]

def connect_to_voice():
    while True:
        try:
            ws = create_connection('wss://gateway.discord.gg/?v=9&encoding=json')
            print("Connected to Discord Gateway.")

            hello = json.loads(ws.recv())
            heartbeat_interval = hello['d']['heartbeat_interval'] / 1000

            auth_payload = {
                "op": 2,
                "d": {
                    "token": usertoken,
                    "properties": {
                        "$os": "Windows",
                        "$browser": "Chrome",
                        "$device": "PC"
                    },
                    "presence": {
                        "status": status,
                        "afk": False
                    }
                }
            }
            ws.send(json.dumps(auth_payload))

            voice_payload = {
                "op": 4,
                "d": {
                    "guild_id": GUILD_ID,
                    "channel_id": CHANNEL_ID,
                    "self_mute": SELF_MUTE,
                    "self_deaf": SELF_DEAF
                }
            }
            ws.send(json.dumps(voice_payload))
            print(f"Joined voice channel {CHANNEL_ID} in guild {GUILD_ID}.")

            last_heartbeat = time.time()
            while True:
                try:
                    event = json.loads(ws.recv())
                    print("Event:", event)

                    if time.time() - last_heartbeat > heartbeat_interval:
                        ws.send(json.dumps({"op": 1, "d": None}))
                        last_heartbeat = time.time()

                except WebSocketConnectionClosedException:
                    print("WebSocket connection closed. Reconnecting...")
                    time.sleep(5)
                    break

        except Exception as e:
            print(f"Error: {e}. Reconnecting in 5 seconds...")
            time.sleep(5)
            continue

if __name__ == "__main__":
    print(f"Logged in as {username}#{discriminator} ({userid}).")
    connect_to_voice()
