from aiogram import Bot
from aiogram import Dispatcher
from loguru import logger

from config import BOT_TOKEN


bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)

logger.add('log_info.log',
           format="{time} - {level} - {message}",
           level='DEBUG')
