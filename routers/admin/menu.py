from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.filters import Command
from aiogram import F, Router
from aiogram.types import Message, CallbackQuery

router = Router()

class AdminStates(StatesGroup):
    mailing_state = State()

@router.callback_query(F.data == "admin_menu")
async def handle_callback(callback: CallbackQuery, state: FSMContext):
    pass

@router.callback_query(F.data.startswith("make_mailing"))
async def callback_handler(callback: CallbackQuery, state: FSMContext):
    pass

@router.message(AdminStates.mailing_state)
async def message_handler(message: Message, state: FSMContext):
    pass

@router.callback_query(F.data.startswith("manage_block"))
async def callback_handler(callback: CallbackQuery, state: FSMContext):
    pass

@router.message(Command("ban"))
async def message_handler(message: Message, state: FSMContext):
    pass

@router.message(Command("unban"))
async def message_handler(message: Message, state: FSMContext):
    pass