from TikTokLive import TikTokLiveClient
from TikTokLive.events import LikeEvent , GiftEvent

from handlers.likes import on_like
from handlers.gifts import on_gift

client = TikTokLiveClient(unique_id="@1abestia")

client.on(LikeEvent)(on_like)
client.on(GiftEvent)(on_gift)

client.run()