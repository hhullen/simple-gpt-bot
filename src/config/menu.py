from aiogram import Bot
from aiogram.types import BotCommand


async def set_main_menu(bot: Bot):
    main_menu = [BotCommand(command="/help", description="Bot help"),
                 BotCommand(command="/forget", description="Forget dialogue context")]
    print(main_menu)
    await bot.set_my_commands(main_menu)
