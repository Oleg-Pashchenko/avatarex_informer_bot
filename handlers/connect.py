from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message


router = Router()


@router.message(Command("connect"))
async def cmd_connect(message: Message):
    await message.answer("Хочу к вам!")
