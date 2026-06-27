from TikTokLive import TikTokLiveClient
from TikTokLive.events import GiftEvent
import pyautogui

client = TikTokLiveClient(unique_id="@unaneaprogramadora")

@client.on(GiftEvent)
async def on_gift(event: GiftEvent):
    gift_name = event.gift.name
    print(f"{event.user.nickname} sent: {gift_name}")

    if gift_name == "Rose":
        pyautogui.write("Si funciono")
        print("Text written!")

client.run()