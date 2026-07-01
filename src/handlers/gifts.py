from TikTokLive.events import GiftEvent
import pyautogui

one_to_four_coins = ["Rose" , "GG" , "Ice Cream Cone" , "White Rose" , "You're awesome" ,
            "Clap Clap" , "TikTok" , "Guardian Wings" , "Community Heart" , "Love you so much" ,
            "Freestyle" , "A Shard of Hope" , "Glow Stick" , "It's corn" , "Pop" , "Good Job" ,
            "Wink wink" , "Cake Slice" , "Maracas" , "Oldies" , "It's Match Time"]

five_to_nine_coins = ["Finger Heart" , "Wave Firework" , "Spinning Soccer" , "Divine Finger" , "Overreact" , "Name shoutout"]

async def on_gift(event: GiftEvent):
    print(f"{event.user.unique_id} sent a {event.gift.name}")

    for i in one_to_four_coins:
        if i == event.gift.name:
            pyautogui.press("space")
            print(f"The gift is {event.gift.name} and it worked")
        else:
            break

    for e in five_to_nine_coins:
        if i == event.gift.name:
            pyautogui.press("enter")
    