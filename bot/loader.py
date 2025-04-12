from aiogram import types
from aiogram import (Bot, Dispatcher)
from config import config
from handlers.router import router as mainrouter
from handlers.keyboards.commands import commands

bot = Bot(token=config.TELEGRAM_TOKEN)
dp = Dispatcher()

dp.include_router(mainrouter)


