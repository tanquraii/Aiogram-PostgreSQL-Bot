from aiogram.types import Message, CallbackQuery
from aiogram import F,Router
from aiogram.filters import CommandStart
import app.keyboard as kb

router = Router()

@router.message(CommandStart())
async def start(message:Message):
    await message.answer('Welcome to TanqurAI corporation.Please press the departments button and choose the one you are interested in:',reply_markup = kb.main)

@router.message(F.text == 'Departments')
async def department(message:Message):
    await message.answer('Choose a department',reply_markup=await kb.departments())

@router.callback_query(F.data.startswith(':'))
async def occupation(callback:CallbackQuery):
    await callback.message.answer('Choose an occupation to get data about the employees',reply_markup=await kb.occupations())

@router.callback_query(F.data.startswith('-'))
async def employee(callback:CallbackQuery):
    await callback.message.answer('Choose an employee',reply_markup=await kb.employees())