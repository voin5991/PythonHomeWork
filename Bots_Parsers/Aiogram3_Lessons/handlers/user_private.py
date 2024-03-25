from aiogram import types, Router
from aiogram.filters import CommandStart, Command

user_private_router = Router()


@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer('Привет, я виртуальный помощник')


@user_private_router.message(Command('menu'))
async def echo(message: types.Message):
    await message.answer('Вот меню:')


@user_private_router.message(Command('about'))
async def abot_cmd(message: types.Message):
    await message.answer('О нас')


@user_private_router.message(Command('payment'))
async def payment_cmd(message: types.Message):
    await message.answer('Варианты оплаты:')


@user_private_router.message(Command('shipping'))
async def shipping_cmd(message: types.Message):
    await message.answer('Варианты доставки:')