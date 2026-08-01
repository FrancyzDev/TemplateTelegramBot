from aiogram.fsm.context import FSMContext
from aiogram.filters import CommandStart, Command
from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from assets.translation import get_text
from db.user import User
from db.database import database
from keyboards.user.menu import get_start_buttons, get_check_sub_buttons
from services.callback_parser import callback_parser
from services.sub import get_membership_in_channels

router = Router()

@router.message(CommandStart())
async def handle_message(message: Message, state: FSMContext, user: User, is_admin: bool):
    await message.answer(
        text=get_text("start_text", user.language),
        reply_markup=get_start_buttons(is_admin, user.language)
    )

@router.callback_query(F.data.startswith("language"))
async def handle_callback(callback: CallbackQuery, state: FSMContext, user: User):
    command, lang_code = callback_parser(callback.data)
    user_lang = user.language if user else None
    if user_lang:
        await database.users.update_user_lang(user.user_id, lang_code)
    else:
        await database.users.create(callback.from_user.id, lang_code)
    await callback.message.edit_text(
        text=get_text("start_text", lang_code)
    )

@router.callback_query(F.data.startswith("check_sub"))
async def handle_callback(callback: CallbackQuery, state: FSMContext, user: User, is_admin: bool):
    status, need_to_subscribe_channels = await get_membership_in_channels(callback.bot, callback.from_user.id)
    if status:
        await callback.message.edit_text(
            text=get_text("start_text", user.language),
            reply_markup=get_start_buttons(is_admin, user.language)
        )
    else:
        try:
            await callback.message.edit_text(
                text=get_text("check_sub_text", user.language),
                reply_markup=get_check_sub_buttons(user.language, need_to_subscribe_channels)
            )
        except:
            pass
        await callback.answer(
            text=get_text("check_sub_error_text", user.language),
            show_alert=True
        )

@router.callback_query(F.data.startswith("close"))
async def callback_handler(callback: CallbackQuery):
    await callback.message.delete()

@router.callback_query(F.data == "start")
async def handle_callback(callback: CallbackQuery, state: FSMContext, user: User, is_admin: bool):
    await callback.message.answer(
        text=get_text("start_text", user.language),
        reply_markup=get_start_buttons(is_admin, user.language)
    )


