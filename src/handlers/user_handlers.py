from aiogram import Router
from aiogram.filters import CommandStart, Command, Text
from aiogram.types import Message
from lexicon import LEXICON_RU
from keyboards import game_kb, yes_no_kb
from services import get_winner, get_bot_choice

router: Router = Router()


@router.message(CommandStart())
async def process_command_start(message: Message):
    await message.answer(text=LEXICON_RU["/start"], reply_markup=yes_no_kb)


@router.message(Command(commands=["help"]))
async def process_command_help(message: Message):
    await message.answer(text=LEXICON_RU["/help"], reply_markup=yes_no_kb)


@router.message(Text(text=LEXICON_RU["yes_button"]))
async def process_yes_answer(message: Message):
    await message.answer(text=LEXICON_RU["yes"], reply_markup=game_kb)


@router.message(Text(text=LEXICON_RU["no_button"]))
async def process_no_answer(message: Message):
    await message.answer(text=LEXICON_RU["no"])


@router.message(Text(text=[LEXICON_RU["rock"],
                           LEXICON_RU["scissors"],
                           LEXICON_RU["paper"]]))
async def process_game_button(message: Message):
    bot_choice: str = get_bot_choice()
    await message.answer(text=f"{LEXICON_RU['bot_choice']} : {bot_choice}")

    winner: str = get_winner(message.text, bot_choice)
    await message.answer(text=LEXICON_RU[winner], reply_markup=yes_no_kb)
