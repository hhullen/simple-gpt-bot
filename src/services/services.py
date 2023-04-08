import random
from lexicon import LEXICON_RU


def get_bot_choice() -> str:
    return random.choice([LEXICON_RU["rock"], LEXICON_RU["scissors"], LEXICON_RU["paper"]])


_rules: dict[str, str] = {LEXICON_RU["rock"]: LEXICON_RU["scissors"],
                         LEXICON_RU["scissors"]: LEXICON_RU["paper"],
                         LEXICON_RU["paper"]: LEXICON_RU["rock"]}


def get_winner(user_choice: str, bot_choice: str) -> str:
    answer: str = "bot_won"
    if _rules[user_choice] == bot_choice:
        answer = "user_won"
    elif bot_choice == user_choice:
        answer = "nobody_won"
    return answer
