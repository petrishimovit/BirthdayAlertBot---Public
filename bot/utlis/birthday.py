from aiogram import Bot, types
from aiogram.types import InputFile
import os
from datetime import datetime
from database.repository import HumanRepository
from aiogram.types import FSInputFile
import asyncio
from config import BASE_DIR




async def check_birthdays_and_send_congratulations(bot: Bot, sessionmaker, group_id: str):
    while True:
        now = datetime.now()

   
        print(f"[{now}] Проверка ближайших дней рождения началась...")

        async with sessionmaker() as session:
           
            all_birthdays = await HumanRepository(session).get_all()  
            upcoming_birthdays = [person for person in all_birthdays if is_upcoming_birthday(person.birthday_date, now)]
            
           
            for person in upcoming_birthdays:
                message = f"🎉 Сегодня день рождения у {person.name}! Мои поздравления :)"

                
                try:
                  
                    photo_path = f"{BASE_DIR}/birthday_photo.jpg"  

                    with open(photo_path, "wb") as f:
                        f.write(person.photo) 

                   
                    photo_input = FSInputFile(photo_path)

                    
                    await bot.send_photo(group_id, photo=photo_input, caption=message)  # Отправка поздравления в группу
                    
                    
                    os.remove(photo_path)

                except Exception as e:
                    print(f"Ошибка при отправке фото: {e}")


        print(f"[{now}] Проверка дней рождения завершена.")

        
        await asyncio.sleep(86450)


def is_upcoming_birthday(birthday_date: str, current_time: datetime):
  
    birthday = datetime.strptime(birthday_date, "%Y-%m-%d")  #
    birthday_this_year = birthday.replace(year=current_time.year)  
    
    
    if birthday_this_year < current_time:
        birthday_this_year = birthday_this_year.replace(year=current_time.year) 
    
   
    return (birthday_this_year - current_time).days < 7