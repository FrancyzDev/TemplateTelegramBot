from aiogram import BaseMiddleware
from aiogram.types import CallbackQuery, Message
from typing import Callable, Dict, Any, Awaitable
from assets.translation import LANGUAGES_SELECT_TEXT, LANGUAGES_SELECT_BUTTONS


class LanguageMiddleware(BaseMiddleware):
    def __init__(self):
        super().__init__()

    async def __call__(
        self,
        handler: Callable[[Message | CallbackQuery, Dict[str, Any]], Awaitable[Any]],
        event: Message | CallbackQuery,
        data: Dict[str, Any]
    ) -> Any:
        user = data.get("user")
        if not user:
            if type(event) is CallbackQuery:
                callback_data = data["event_update"].callback_query.data
                if not callback_data.startswith("language"):
                    await event.message.edit_text(
                        text=LANGUAGES_SELECT_TEXT,
                        reply_markup=LANGUAGES_SELECT_BUTTONS
                    )
                else:
                    return await handler(event, data)
            else:
                await event.answer(
                    text=LANGUAGES_SELECT_TEXT,
                    reply_markup=LANGUAGES_SELECT_BUTTONS
                )
                return None
        else:
            return await handler(event, data)