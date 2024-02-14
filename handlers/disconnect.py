from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message


router = Router()


@router.message(Command("disconnect"))
async def cmd_disconnect(message: Message):
    await message.answer("Отвяжитесь от меня!")
