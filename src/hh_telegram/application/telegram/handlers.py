from aiogram.filters import CommandStart, Command
from aiogram import Router
from aiogram.types import Message


router = Router()

@router.message(CommandStart())
async def start_command(message: Message):
    await message.answer(
        'Привет! Я — твой персональный помощник для поиска работы на hh.ru.\n'
        'Я могу собирать вакансии по твоим запросам и публиковать их раз в день.'
    )

@router.message(Command('help'))
async def help_command(message: Message):
    await message.answer('Чем могу помочь?')

