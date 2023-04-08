from aiogram import Bot
from aiogram.types import BotCommand


async def set_main_menu(bot: Bot):
    main_menu = [BotCommand(command="/help", description="Справка по работе бота")]
    await  bot.set_my_commands(main_menu)
