from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
from app.database.connection import get_departments,get_occupations,get_employees_by_occupation
from aiogram.utils.keyboard import InlineKeyboardBuilder
main = ReplyKeyboardMarkup(keyboard = [
    [KeyboardButton(text = 'Departments')]
])

async def departments():
    all_departments = await get_departments()
    keyboard = InlineKeyboardBuilder()
    for department in all_departments:
        keyboard.add(InlineKeyboardButton(text = department,callback_data = f':{department}'))
    return keyboard.adjust(2).as_markup()

async def occupations():
    all_occupations = await get_occupations()
    keyboard = InlineKeyboardBuilder()
    for occupation in all_occupations:
        keyboard.add(InlineKeyboardButton(text = occupation,callback_data = f'-{occupation}'))
    return keyboard.adjust(2).as_markup()

async def employees():
    all_employees = await get_employees_by_occupation()
    keyboard = InlineKeyboardBuilder()
    for employee in all_employees:
        keyboard.add(InlineKeyboardButton(text = employee,callback_data=f'+{employee}'))
    return keyboard.adjust(2).as_markup()