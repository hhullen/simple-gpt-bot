import logging
import asyncio

from aiogram import Bot, Dispatcher
from config import Config, load_configuration, set_main_menu
from handlers import other_handlers, user_handlers

logger = logging.getLogger(__name__)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s '
               u'[%(asctime)s] - %(name)s - %(message)s')

    config: Config = load_configuration("config/.env")
    print("Configuration:\n", config.tg_bot, "\n", config.db)
    bot: Bot = Bot(config.tg_bot.token, parse_mode="HTML")
    dp: Dispatcher = Dispatcher()

    dp.startup.register(set_main_menu)
    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot crushed")
