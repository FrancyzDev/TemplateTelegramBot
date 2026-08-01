from aiogram import Router
from .user import user_menu_router
from .admin import admin_menu_router

user_routers = [user_menu_router,]
admin_routers = [admin_menu_router,]

