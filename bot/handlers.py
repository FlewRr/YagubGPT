from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp, settings
from utils.states import States
from ml.yagubgpt import YagubGPT

ygpt = YagubGPT("tinkoff-ai/ruDialoGPT-small", "/home/sfleur/YagubGPT/YagubGPT/bot/ml/statedicts/model-epoch-4.bin")

@dp.message_handler(commands=["start"], state="*")
async def welcome(message: types.Message, state: FSMContext):
    print(1)
    await States.work.set()
    await message.answer(settings.messages.welcome)

@dp.message_handler(state=States.work)
async def start(message: types.Message, state):
    print(2)
    if message.text is not None:
        ans = " ".join(ygpt.answer(message.text)[1][1:]).replace("<pad>", '').strip()
        if ans == '':
            ans = 'Я хз че ответить'

        await message.answer(ans)