import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from utils.misc import Settings
from utils.ui_commands import set_bot_commands
from handlers import default_commands, info, connect, disconnect


async def main():
    logging.basicConfig(level=logging.WARNING)
    config = Settings()

    bot = Bot(config.bot_token.get_secret_value(), parse_mode="HTML")

    storage = MemoryStorage()

    dp = Dispatcher(storage=storage, config=config)

    dp.include_router(default_commands.router)
    dp.include_router(connect.router)
    dp.include_router(disconnect.router)
    dp.include_router(info.router)

    await set_bot_commands(bot)

    try:
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(main())
