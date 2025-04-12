from datetime import datetime
from aiogram.types import Message
from database.models import Human
import locale
from io import BytesIO


async def download_photo(message: Message) -> bytes:

    from loader import bot
    
    file_id = message.photo[-1].file_id

    
    file = await bot.get_file(file_id)

    photo_io = await bot.download_file(file.file_path)

    
    photo_bytes = photo_io.getvalue()

    return photo_bytes

def convert_bytes_to_input_file(photo_bytes: bytes, filename: str = "photo.jpg") -> BytesIO:

    photo = BytesIO(photo_bytes)

    photo.name = filename 
    
    return photo


def read_file_as_text(file_path: str, encoding: str = "utf-8") -> str:
    with open(file_path, "r", encoding=encoding) as file:
        return file.read()
    

# you can change into your lang months
month_names = {
    1: "января", 2: "февраля", 3: "марта", 4: "апреля", 5: "мая", 6: "июня",
    7: "июля", 8: "августа", 9: "сентября", 10: "октября", 11: "ноября", 12: "декабря"
}

def get_next_birthday(humans: list):
    current_date = datetime.now().date()
    closest_birthday = None
    closest_person = None

    for human in humans:
        original_birthday = datetime.strptime(human.birthday_date, "%Y-%m-%d").date()
        this_year_birthday = original_birthday.replace(year=current_date.year)

        if this_year_birthday < current_date:
            next_birthday = this_year_birthday.replace(year=current_date.year + 1)
        else:
            next_birthday = this_year_birthday

        if closest_birthday is None or next_birthday < closest_birthday:
            closest_birthday = next_birthday
            closest_person = human

    if closest_birthday:
        month_name = month_names[closest_birthday.month]
        formatted_birthday = f"{closest_birthday.day} {month_name} {closest_birthday.year} года"
    else:
        formatted_birthday = None

    return closest_person, closest_birthday, formatted_birthday