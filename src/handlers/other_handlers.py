from aiogram.types import Message
from aiogram import Router
from storage import users_contexts
import openai
import os

router: Router = Router()


async def is_user_exists(id) -> bool:
    return users_contexts.get(id) is not None


async def add_message_to_context(id, message, role):
    users_contexts[id].append(
        {"role": role, "content": message})


async def gpt(message: Message):

    openai.api_key = os.environ['OPEN_AI_KEY']
    try:
        await add_message_to_context(message.from_user.id, message.text, "user")
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0301",
            messages=users_contexts[message.from_user.id]
        )
        answer = response['choices'][0]['message']['content']
        if answer:
            await add_message_to_context(message.from_user.id, answer, "assistant")
            await message.answer(text=answer)
        else:
            await message.answer(text="Smt went wrong, try to ask again")
    except:
        await message.answer(
            text="I amfucking overloaded, probably. Try ask me the question later.")


@router.message()
async def send_answer(message: Message):
    if not await is_user_exists(message.from_user.id):
        await message.reply("Bot have been restarted probably. You need to get your id to database. Please send /start command.")
        return
    if message.text:
        await gpt(message)
    else:
        await message.reply("It is not a text message 🙊")
