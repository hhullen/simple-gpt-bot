from aiogram import Router
from aiogram.filters import CommandStart, Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from storage import users_contexts


router: Router = Router()


async def set_clean_user_context(id):
    users_contexts[id] = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]


@router.message(CommandStart())
async def process_command_start(message: Message):
    await set_clean_user_context(message.from_user.id)
    await message.answer(text="Hi, I'm chatGPT API bot. Lets try to talk! I can handle with text messages only))", reply_markup=ReplyKeyboardRemove())


@router.message(Command(commands=["help"]))
async def process_command_help(message: Message):
    await message.answer(text="God helps you.\nSo, nobody helps you.")


@router.message(Command(commands=["forget"]))
async def process_command_help(message: Message):
    await set_clean_user_context(message.from_user.id)
    await message.answer(text="Ok, lets start with a clean slate")
