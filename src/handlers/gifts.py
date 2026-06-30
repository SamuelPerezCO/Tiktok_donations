from TikTokLive.events import GiftEvent

one_coin = ["Rose" , "GG" , "Ice Cream Cone" , "White Rose" , "You're awesome" ,
            "Clap Clap" , "TikTok" , "Guardian Wings" , "Community Heart" , "Love you so much" ,
            "Freestyle" , "A Shard of Hope" , "Glow Stick" , "It's corn" , "Pop" , "Good Job" ,
            "Wink wink" , "Cake Slice" , "Maracas" , "Oldies" , "It's Match Time"]

async def on_gift(event: GiftEvent):
    print(f"{event.user.unique_id} sent a {event.gift.name}")

    for i in one_coin:
        if i == event.gift.name:
            print(f"The gift is {event.gift.name} and it worked")
"""
    if event.gift.name == "Rose":
        pyautogui.press('space')
        print ("Space key pressed due to Rose gift!")
"""