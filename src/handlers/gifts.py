from TikTokLive.events import GiftEvent
import pyautogui

async def on_gift(event: GiftEvent):
   # print(f"{event.user.unique_id} sent a {event.gift.name}")

    if event.gift.name == "Rose":
        pyautogui.press("space")

    elif event.gift.name == "Finger Heart":
        pyautogui.press("enter")

    elif event.gift.name == "Rosa":
        pyautogui.press("delete")

    elif event.gift.name == "Capybara":
        pyautogui.write("Capybara")    
