from TikTokLive import TikTokLiveClient
from TikTokLive.events import GiftEvent , CommentsEvent
import pyautogui

client = TikTokLiveClient(unique_id="@unaneaprogramadora")

@client.on(GiftEvent)
async def on_gift(event: GiftEvent):
    print(f"{event.user.uniqueId} sent a {event.gift.name} x{event.gift.repeatCount}")
    
    if event.gift.name == "Rose":
        pyautogui.press('space')
        print ("Space key pressed due to Rose gift!")

client.run()