from TikTokLive import TikTokLiveClient
from TikTokLive.events import LikeEvent

from handlers.likes import on_like

client = TikTokLiveClient(unique_id="@backdoor_humor")

client.on(LikeEvent)(on_like)

client.run()