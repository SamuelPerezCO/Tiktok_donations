from TikTokLive.events import LikeEvent


async def on_like(event: LikeEvent) -> None:
    print(f"❤️  {event.user.nickname} liked!")
