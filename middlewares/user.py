from aiogram import BaseMiddleware
from aiogram.types import CallbackQuery, Message
from typing import Callable, Dict, Any, Awaitable
from assets.config import BOT_ADMIN_IDS
from db.database import database

class UserMiddleware(BaseMiddleware):
    def __init__(self):
        super().__init__()

    async def __call__(
            self,
            handler: Callable[[Message | CallbackQuery, Dict[str, Any]], Awaitable[Any]],
            event: Message | CallbackQuery,
            data: Dict[str, Any]
    ) -> Any:
        user_id = event.from_user.id
        user = await database.users.get(user_id)
        data.update(user=user)
        data.update(is_banned=await database.bans.is_user_banned(user_id))
        data.update(is_admin=user_id in BOT_ADMIN_IDS)
        return await handler(event, data)