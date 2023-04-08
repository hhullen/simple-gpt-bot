from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from lexicon import LEXICON_RU

btn_y: KeyboardButton = KeyboardButton(text=LEXICON_RU["yes_button"])
btn_n: KeyboardButton = KeyboardButton(text=LEXICON_RU["no_button"])

yes_no_kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
yes_no_kb_builder.row(btn_y, btn_n, width=2)
yes_no_kb: ReplyKeyboardMarkup = yes_no_kb_builder.as_markup(on_time_keyboard=True,
                                                             resize_keyboard=True)

btn_rock: KeyboardButton = KeyboardButton(text=LEXICON_RU["rock"])
btn_scissors: KeyboardButton = KeyboardButton(text=LEXICON_RU["scissors"])
btn_paper: KeyboardButton = KeyboardButton(text=LEXICON_RU["paper"])
game_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=[[btn_rock,
                                                              btn_scissors,
                                                              btn_paper]],
                                                   resize_keyboard=True)
