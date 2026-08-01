from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton
from assets.config import BOT_MUST_HAVE_CHANNELS
from assets.translation import get_text

def get_start_buttons(is_admin: bool, lang_code: str):
    ikb = InlineKeyboardBuilder()
    if is_admin:
        ikb.row(
            InlineKeyboardButton(text=get_text("admin_button_text", lang_code), callback_data="admin_menu"),
        )
    return ikb.as_markup()

def get_check_sub_buttons(lang_code: str, need_to_subscribe_channels: dict[int, bool]):
    need_to_subscribe_channels = [channel_id for channel_id, status in need_to_subscribe_channels.items() if not status]
    ikb = InlineKeyboardBuilder()
    temp_counter = 0
    for channel_id in need_to_subscribe_channels:
        ikb.row(
            InlineKeyboardButton(
                text=get_text("channel_button_text", lang_code, count=temp_counter+1),
                url=BOT_MUST_HAVE_CHANNELS[channel_id]
            )
        )
        temp_counter += 1
    ikb.row(
        InlineKeyboardButton(
            text=get_text("sub_button_text", lang_code),
            callback_data="check_sub")
    )
    return ikb.as_markup()

async def get_close_buttons(lang_code: str):
    ikb = InlineKeyboardBuilder()
    ikb.row(
        InlineKeyboardButton(
            text=get_text("close_button_text", lang_code),
            callback_data=f"close"
        ),
    )
    return ikb.as_markup()