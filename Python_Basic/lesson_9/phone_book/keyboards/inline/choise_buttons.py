from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

choice_main = InlineKeyboardMarkup(
    inline_keyboar=[
        [(InlineKeyboardButton(text="Show all entries", callback_data="move:show_all"))],
        [(InlineKeyboardButton(text="Find an entries", callback_data="move:find"))],
        [(InlineKeyboardButton(text="Add an entries", callback_data="move:add"))],
        [(InlineKeyboardButton(text="Edit an entries", callback_data="move:edit"))],
        [(InlineKeyboardButton(text="Delete an entries", callback_data="move:delete"))],
        [(InlineKeyboardButton(text="Import/Export", callback_data="move:imp_exp"))],
        [(InlineKeyboardButton(text="Exit", callback_data="move:exit"))],
    ])
