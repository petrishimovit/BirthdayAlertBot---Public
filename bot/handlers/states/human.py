from aiogram.fsm.state import StatesGroup , State

class FormAddBirthday(StatesGroup):

    name : State = State()

    surname : State = State()

    birthday_date : State = State()

    photo : State = State()



