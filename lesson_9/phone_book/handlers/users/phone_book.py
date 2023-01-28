from aiogram.dispatcher.filters import Command, Text
from aiogram.types import CallbackQuery, Message

from db_work import add_entry
from db_work import del_entry
from db_work import edit_entry
from db_work import find_entry
from db_work import read_all
from keyboards.inline.callback_data import action_callback
from keyboards.inline.choise_buttons import choice_main

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
                         reply_markup=choice_main)


@dp.callback_query_handler(action_callback.filter(item_name=["show_all", "find", "add",
                                                             "edit", "delete", "imp_exp", "exit"]))
async def main_menu(call=CallbackQuery, callback_data=dict):
    global mode_operating
    print(callback_data)
    if callback_data == "show_all":
        logger.info("Show all phone book")
        await call.message.edit_text(read_all(), reply_markup=choice_main)
    elif callback_data == "find":
        read_all()
        find_entry(input("Enter surname or phone number: "))
        logger.info("Find record")
    elif callback_data == "add":
        logger.info("Add record")
        await call.message.answer("Введите данные через пробел:\n"
                                  "id, name, surname, phone, description")
    elif callback_data == "edit":
        logger.info("Edit record")
        answer = edit_menu()
        if answer:
            edit_entry(answer)
    elif callback_data == "delete":
        logger.info("Delete record")
        mode_operating = "del"
        await call.message.edit_text(read_all(), reply_markup=choice_main)
        await call.message.answer("Enter id and surname")
    elif callback_data == "imp_exp":
        logger.info("Import/export record")
        import_export_menu()
    elif callback_data == "exit":
        logger.info("Stop programm.")
        await call.message.answer("Goodbuy! See You later.")
        # dp.stop_polling()
        # await dp.wait_closed()
        # await bot.close()


@dp.message_handler(Text(startswith=["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]))
async def mode_menu(message: Message):
    logger.info("Start and menu mode")
    list_info = message["text"].split()

    if mode_operating == "add":
        fieldnames = ["id", "name", "surname", "phone", "description"]
        add_dict = {k: v for k, v in zip(fieldnames, list_info)}
        logger.info("Stop edit menu")
        await message.edit_text(add_entry(add_dict), reply_markup=choice_main)
    elif mode_operating == "del":
        result = del_entry(list_info[0])
        if not result:
            await message.edit_text(f'Запись удалена', reply_markup=choice_main)
        else:
            await message.edit_text(result, reply_markup=choice_main)


@dp.message_handler()
async def echo(message: Message):
    logger.debug("Не верный ввод пользователя")
    await message.answer(f'{message.from_user.first_name},'
                         f' пожалуйста, кликай кнопки калькулятора!',
                         reply_markup=choice_main)
