from aiogram import Bot, Dispatcher
from assets.config import BOT_TOKEN
from middlewares.user import UserMiddleware
from middlewares.ban import BanMiddleware
from middlewares.language import LanguageMiddleware
from middlewares.sub import SubMiddleware
from routers import user_routers, admin_routers

dp = Dispatcher()
dp.include_routers(*[*user_routers, *admin_routers])
dp.message.middleware(UserMiddleware())
dp.callback_query.middleware(UserMiddleware())
dp.message.middleware(BanMiddleware())
dp.callback_query.middleware(BanMiddleware())
dp.message.middleware(LanguageMiddleware())
dp.callback_query.middleware(LanguageMiddleware())
dp.message.middleware(SubMiddleware())
dp.callback_query.middleware(SubMiddleware())
bot = Bot(token=BOT_TOKEN)
