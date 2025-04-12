from aiogram import Router
from handlers.routers.weather import router as weather_router
from handlers.routers.birthday import router as birthday_router



router = Router()
router.include_router(weather_router)
router.include_router(birthday_router)


