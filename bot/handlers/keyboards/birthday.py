from aiogram import types

main_kb = [
    [types.InlineKeyboardButton(text="❓ У кого ближайший день рождения ?", callback_data=f"nearirthday")],
    [types.InlineKeyboardButton(text="📋 Все дни рождения", callback_data=f"allbirthday")],
    [types.InlineKeyboardButton(text="💬 Добавить день рождения", callback_data=f"addbirthday")]
]

main_kb = types.InlineKeyboardMarkup(inline_keyboard=main_kb)