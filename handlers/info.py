from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message


router = Router()


@router.message(Command("info"))
async def cmd_info(message: Message):
    await message.answer("Да что тут происходит !?")
