from TikTokLive.events import GiftEvent
import pyautogui

one_to_four_coins = ["Rose" , "GG" , "Ice Cream Cone" , "White Rose" , "You're awesome" ,
            "Clap Clap" , "TikTok" , "Guardian Wings" , "Community Heart" , "Love you so much" ,
            "Freestyle" , "A Shard of Hope" , "Glow Stick" , "It's corn" , "Pop" , "Good Job" ,
            "Wink wink" , "Cake Slice" , "Maracas" , "Oldies" , "It's Match Time"]

five_to_nine_coins = ["Finger Heart" , "Wave Firework" , "Spinning Soccer" , "Divine Finger" , "Overreact" , "Name shoutout"]

ten_to_nineteen_coins = [
    "Rosa", "Friendship Necklace", "Slow motion", "Journey Pass", "FANDOM Fan",
    "Chocolate", "LIVE Ranking Ticket", "Sing Together", "League Ball", "Lucky Pony",
    "Heart", "EWC", "Style Me Up", "Banana Peel", "Heart Gaze", "Intimacy",
    "Mind Blown", "Gold Boxing Gloves", "ASMR Time", "Cherry Blossom Bunny",
    "DJ Vinyl", "I Love You", "Ice Lolly", "Tiny Diny", "Shepherd", "LIVE Island",
    "Whistle", "Potato with Ice Cream", "LIVE Star", "Panther", "Gutab", "Football",
    "You're the Best!", "Balloons", "Lucky Pig", "Shamrock", "Drip Brewing",
    "Fried Chicken", "Hi Bear", "Dolphin", "New York Cab", "Beach Radio",
    "Meowthumbs Up", "Pork Rice Bowl", "Northern Zongzi", "Southern Zongzi",
    "Udon-nou", "Fukkachan", "Nebaarukun", "Courage Potion", "Koala", "Dragon Egg",
    "Furious Fire", "Love Piggy", "Boo", "Pumpkin Latte", "Nightshade Seal",
    "Whitewind Seal", "Firelight Seal", "Crocodile", "Azura Card Fiery",
    "Azura Card Tranquil", "Minecraft", "Watermelon", "Koala Refuel", "Little Ghost",
    "Baby Hippo", "Sakura Mochi", "Go Go Go", "Takatanoyumechan", "Easy Victory",
    "Kuruppa", "DJ Cactus", "Magnifying Glass",
    "Bravo!", "Romanian Polenta", "Flower Garland", "Woody",
    "Buzz Light Year", "Tiny Diny in Love", "My Melody & Kuromi",
]

twenty_to_twentynine_coins = ["Baby Fox" , "Perfume" , "Applause" , "Cry Laugh" , "Love" , "Made My Day" , "OMG" , "Plus One" , "Hilarious" , "Party"]

async def on_gift(event: GiftEvent):
    print(f"{event.user.unique_id} sent a {event.gift.name}")

    for i in one_to_four_coins:
        if i == event.gift.name:
            pyautogui.press("space")
            print(f"The gift is {event.gift.name} and it worked")
        else:
            break

    for e in five_to_nine_coins:
        if e == event.gift.name:
            pyautogui.press("enter")

    for a in ten_to_nineteen_coins:
        if a == event.gift.name:
            pyautogui.press("delete")
    
