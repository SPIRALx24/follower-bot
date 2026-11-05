import os, requests

TOKEN = os.environ["TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]
USERNAME = "memfis_land"
PRE_TARGET = 1_399_950
TARGET = 1_400_000

def tg(text):
    requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage",
                  data={"chat_id": CHAT_ID, "text": text}, timeout=20)

def out(line):
    with open(os.environ["GITHUB_OUTPUT"], "a") as f:
        f.write(line + "\n")

try:
    r = requests.get(
        "https://i.instagram.com/api/v1/users/web_profile_info/",
        params={"username": USERNAME},
        headers={"User-Agent": "Instagram 219.0.0.12.117 Android",
                 "x-ig-app-id": "936619743392459"},
        timeout=20)
    n = r.json()["data"]["user"]["edge_followed_by"]["count"]
    print("followers:", n)
    if n >= TARGET:
        tg(f"🎉 پیج {USERNAME} به {n:,} فالوور رسید!")
        out("reached=true")
    elif n >= PRE_TARGET and not os.path.exists("pre_sent.txt"):
        tg(f"⚠️ پیج {USERNAME} الان {n:,} فالوور داره، خیلی نزدیکه!")
        with open("pre_sent.txt", "w") as f:
            f.write("sent")
        out("pre=true")
except Exception as e:
    print("error:", e)
