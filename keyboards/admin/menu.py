from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton

async def get_admin_buttons(lang_code: str):
    ikb = InlineKeyboardBuilder()
    ikb.row(
        InlineKeyboardButton(text="Сделать рассылку" if lang_code == "ru" else "Mailing", callback_data=f"make_mailing"),
    )
    ikb.row(
        InlineKeyboardButton(text="Заблокировать/Разблокировать" if lang_code == "ru" else "Block/Unblock", callback_data=f"manage_block")
    )
    ikb.row(
        InlineKeyboardButton(text="Меню пользователя" if lang_code == "ru" else "User Menu", callback_data=f"start")
    )
    return ikb.as_markup()


async def get_make_mailing_buttons(lang_code: str):
    ikb = InlineKeyboardBuilder()
    ikb.row(
        InlineKeyboardButton(text="Отмена" if lang_code == "ru" else "Cancel", callback_data=f"admin_menu"),
    )
    return ikb.as_markup()

async def get_admin_back_buttons(lang_code: str):
    ikb = InlineKeyboardBuilder()
    ikb.row(
        InlineKeyboardButton(text="Назад" if lang_code == "ru" else "Back", callback_data=f"admin_menu"),
    )
    return ikb.as_markup()
