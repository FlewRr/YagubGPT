from aiogram import Bot, Dispatcher
from aiogram import types
from aiogram.dispatcher import FSMContext
from utils.settings import BotSettings
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import time


st = time.time()

settings = BotSettings()
bot = Bot(token=settings.config.token)
dp = Dispatcher(bot, storage=MemoryStorage())

fn = time.time()
print(f"EVERYTHING SUCCESSFULLY BUILDED IN {fn-st}")

