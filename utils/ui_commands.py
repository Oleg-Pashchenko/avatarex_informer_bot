from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_bot_commands(bot: Bot):
    commands = [
            BotCommand(command="start", description='Запуск бота'),
            BotCommand(command="info", description='Получить информацию о состоянии'),
            BotCommand(command="stop", description='Отсановить уведомления'),
            BotCommand(command="connect", description='Соединить бота и Avatarex'),
            BotCommand(command='disconnect', description='Отсоединить бота от Avatarex'),
            BotCommand(command="help", description='Помощь')
        ]

    await bot.set_my_commands(commands=commands, scope=BotCommandScopeDefault())
