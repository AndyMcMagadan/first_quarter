from aiogram.dispatcher.filters import Command, Text
from aiogram.types import CallbackQuery, Message

from db_work import add_entry
from db_work import del_entry
from db_work import edit_entry
from db_work import find_entry
from db_work import read_all
from keyboards.inline.callback_data import action_callback
from keyboards.inline.choise_buttons import choise_main
from loader import bot
from loader import dp
from loader import logger

mode_operating = "add"


def import_export_menu():
    pass


def edit_menu():
    pass


@dp.message_handler(Command('Start'))
async def start_com(message: Message):
    await message.answer(text="Welcome to the Phone Book!",
                         reply_markup=choise_main)


@dp.callback_query_handler(action_callback.filter(item_name=["show_all", "find", "add",
                                                             "edit", "delete", "imp_exp", "exit"]))
async def main_menu(call=CallbackQuery, callback_data=dict):
    global mode_operating
    print(callback_data)
    match callback_data[item_name]:
        case "show_all":
            logger.info("Show all phone book")
            await call.message.edit_text(read_all(), reply_markup=choise_main)
        case "find":
            read_all()
            find_entry(input("Enter surname or phone number: "))
            logger.info("Find record")
        case "add":
            logger.info("Add record")
            pass
        case "edit":
            logger.info("Edit record")
            pass
        case "delete":
            logger.info("Delete record")
            pass
        case "imp_exp":
            logger.info("Import/export record")
            pass
        case "exit":
            logger.info("Exit from programm")
            exit()
