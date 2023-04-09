from aiogram.types import Message
from aiogram import Router
import openai
import os

router: Router = Router()


async def gpt(message: Message):

    openai.api_key = os.environ['OPEN_AI_KEY']
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0301",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                # {"role": "system", "content": "You are my best friend."},
                {"role": "user", "content": message.text}
            ]
        )
        answer = response['choices'][0]['message']['content']
        if answer:
            await message.answer(text=answer)
        else:
            message.answer(text="Smt went wrong, try to ask again")
    except:
        message.answer(
            text="I amfucking overloaded, probably. Try ask me the question later.")


@router.message()
async def send_answer(message: Message):
    if message.text:
        await gpt(message)
    else:
        await message.reply("It is not a text message 🙊")
