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

async def employees(occupation):
    all_employees = await get_employees_by_occupation()
    keyboard = InlineKeyboardBuilder()
    for employee in all_employees:
        words = employee.split()
        if words[2] == occupation:
            keyboard.add(InlineKeyboardButton(text = f'{words[0]} {words[1]}',callback_data=f'+{employee}'))
    return keyboard.adjust(2).as_markup()


async def action(employee):
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text = 'fire',callback_data=f'fire_{employee}'))
    keyboard.add(InlineKeyboardButton(text = 'promote',callback_data=f'promote_{employee}'))
    return keyboard.adjust(2).as_markup()
