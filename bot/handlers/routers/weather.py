from aiogram import Router
from aiogram.filters import Command
from aiogram import types
from config import config
from utlis.weather import get_weather

router = Router()

@router.message(Command("weather"))
async def help(message : types.Message):
    await message.answer(await get_weather(config.WEATHER_API_KEY))
