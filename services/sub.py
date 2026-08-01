from aiogram import Bot
from assets.config import BOT_MUST_HAVE_CHANNELS

async def get_membership_in_channels(bot: Bot, user_id: int):
    try:
        memberships = [await get_membership_in_channel(bot, user_id, channel_id) for channel_id in BOT_MUST_HAVE_CHANNELS.keys()]
        need_to_subscribe_channels = dict(zip(BOT_MUST_HAVE_CHANNELS.keys(), memberships))
        return (all(memberships), need_to_subscribe_channels) if BOT_MUST_HAVE_CHANNELS else (True, {})
    except Exception as err:
        return False, {}

async def get_membership_in_channel(bot: Bot, user_id: int, channel_id: int):
    try:
        membership = await bot.get_chat_member(chat_id=channel_id, user_id=user_id)
        return membership.status in ["creator", "administrator", "member"]
    except Exception as err:
        print(str(err))
        return False