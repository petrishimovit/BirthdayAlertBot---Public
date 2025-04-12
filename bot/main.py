import asyncio
from loader import (bot,dp,commands)
import logging
from database.session import init_db
from  database.models import Human
from utlis.birthday import check_birthdays_and_send_congratulations
from database.session import new_session as sessionmaker
from config import config
logging.basicConfig(level=logging.INFO)


async def main():

    asyncio.create_task(check_birthdays_and_send_congratulations(bot, sessionmaker, config.WORKGROUP_CHAT_ID))

    await init_db()

    await bot.set_my_commands(commands)
    
    await dp.start_polling(bot)
    

if __name__ == "__main__":
    asyncio.run(main())