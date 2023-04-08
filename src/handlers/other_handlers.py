from aiogram.types import Message
from aiogram import Router
import openai
import os

router: Router = Router()


async def gpt(message: Message):

    openai.api_key = os.environ['OPEN_AI_KEY']
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0301",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message.text}
        ]
    )
    answer = response['choices'][0]['message']['content']
    if answer:
        await message.answer(text=answer)


@router.message()
async def send_answer(message: Message):
    if message.text:
        await gpt(message)
        # await message.answer(text=answer)
