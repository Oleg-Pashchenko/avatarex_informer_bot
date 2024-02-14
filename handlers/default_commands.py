from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message


router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("Привет!")


@router.message(Command("stop"))
async def cmd_stop(message: Message):
    await message.answer('Пока!')


@router.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer('Помогите!')
