import datetime
from aiogram import Router
from aiogram.filters import (Command,CommandStart)
from aiogram.fsm.context import FSMContext
from aiogram import types
from aiogram.types import CallbackQuery
from database.session import new_session
from database.repository import HumanRepository
from handlers.states.human import FormAddBirthday
from ..keyboards.birthday import main_kb
from utlis.human import download_photo , get_next_birthday , read_file_as_text
from config import config , mainmenu_path, start_path 
router = Router()

@router.message(Command("menu"))
async def help(message : types.Message):

    await message.answer(read_file_as_text(mainmenu_path),reply_markup=main_kb)

@router.message(CommandStart())
async def help(message : types.Message):

    await message.answer(read_file_as_text(start_path),reply_markup=main_kb)



@router.callback_query(lambda c: c.data == "allbirthday")
async def start_adding_birthday(callback: CallbackQuery, state: FSMContext):
    
     async with new_session() as session:

        all = await HumanRepository(session).get_all()

     mesg = ""
    
     for human in all:
        mesg += f"{human.name} {human.surname}: лет родился {human.birthday_date}\n"

     await callback.message.answer(mesg)
 

@router.callback_query(lambda c: c.data == "nearirthday")
async def start_adding_birthday(callback: CallbackQuery, state: FSMContext):
    
     async with new_session() as session:

        all = await HumanRepository(session).get_all()

     human , date , f_date=  get_next_birthday(all)
    
     mesg = f"Ближайший день рождения у {human.name} {human.surname} {f_date} "

     await callback.message.answer(mesg)
 
    
@router.callback_query(lambda c: c.data == "addbirthday")
async def start_adding_birthday(callback: CallbackQuery, state: FSMContext):
    
    await callback.message.answer("Введите имя:")

    await state.set_state(FormAddBirthday.name) 

    await callback.answer()

@router.message(FormAddBirthday.name)
async def process_name(message: types.Message, state: FSMContext):
    
    await state.update_data(name=message.text)

    await message.answer("Введите фамилию:")

    await state.set_state(FormAddBirthday.surname) 

    
@router.message(FormAddBirthday.surname)
async def process_surname(message: types.Message, state: FSMContext):
    
    await state.update_data(surname=message.text)

    await message.answer("Введите дату рождения: (формат: YYYY-MM-DD например: 2024-11-11):")

    await state.set_state(FormAddBirthday.birthday_date)  

@router.message(FormAddBirthday.birthday_date)
async def process_birthday(message: types.Message, state: FSMContext):
    try:
       
        datetime.datetime.strptime(message.text, "%Y-%m-%d")
        await state.update_data(birthday_date=message.text)

        await message.answer("Пришлите фото:")
        await state.set_state(FormAddBirthday.photo)

    except ValueError:
        await message.answer("❌ Неверный формат даты. Пожалуйста, введите в формате YYYY-MM-DD (например: 2024-11-11):")
     
@router.message(FormAddBirthday.photo)
async def process_photo(message: types.Message, state: FSMContext):
   
    photo_id = message.photo[-1].file_id

    await state.update_data(photo=photo_id)

   
    user_data = await state.get_data()

    user_data["photo"] = await download_photo(message)

    async with new_session() as session:

        await HumanRepository(session).add_human(user_data)
    
    await state.clear() 

    await message.answer("Ваши данные сохранены!")
