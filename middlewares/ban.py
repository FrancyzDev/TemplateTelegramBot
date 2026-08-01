from aiogram import BaseMiddleware
from aiogram.types import CallbackQuery, Message
from typing import Callable, Dict, Any, Awaitable

class BanMiddleware(BaseMiddleware):
    def __init__(self):
        super().__init__()

    async def __call__(
        self,
        handler: Callable[[Message | CallbackQuery, Dict[str, Any]], Awaitable[Any]],
        event: Message | CallbackQuery,
        data: Dict[str, Any]
    ) -> Any:
        if data.get('is_banned'):
            return None
        else:
            return await handler(event, data)