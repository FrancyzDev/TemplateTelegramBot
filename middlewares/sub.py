from aiogram import BaseMiddleware
from aiogram.types import CallbackQuery, Message
from typing import Callable, Dict, Any, Awaitable
from services.sub import get_membership_in_channels
from assets.translation import get_text
from keyboards.user.menu import get_check_sub_buttons

class SubMiddleware(BaseMiddleware):
    def __init__(self):
        super().__init__()

    async def __call__(
        self,
        handler: Callable[[Message | CallbackQuery, Dict[str, Any]], Awaitable[Any]],
        event: Message | CallbackQuery,
        data: Dict[str, Any]
    ) -> Any:
        is_admin = data.get("is_admin")
        status, need_to_subscribe_channels = await get_membership_in_channels(event.bot, event.from_user.id)
        if not status and not is_admin:
            user = data.get("user")
            if type(event) is CallbackQuery:
                callback_data = data["event_update"].callback_query.data
                if not callback_data.startswith("check_sub"):
                    await event.message.edit_text(
                        text=get_text("check_sub_text", user.language),
                        reply_markup=get_check_sub_buttons(user.language, need_to_subscribe_channels)
                    )
                    return None
            else:
                await event.answer(
                    text=get_text("check_sub_text", user.language),
                    reply_markup=get_check_sub_buttons(user.language, need_to_subscribe_channels)
                )
                return None
        return await handler(event, data)