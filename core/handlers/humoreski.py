from aiogram import Router, F, types
from aiogram.filters import Command
from mysql.connector import connect, Error
dict_of_brothers = dict()

try:
    with connect(
        host="localhost",
        user="root",
        password="1234",
        database="mydb",
    ) as connection:
        print(connection)
        select_users_query = """
                                SELECT FIO, text
                                FROM users
                                INNER JOIN anecdots
                                    ON users.id = anecdots.id
                                GROUP BY users.id
                              """
        with connection.cursor() as cursor:
            cursor.execute(select_users_query)
            for i in cursor.fetchall():
              dict_of_brothers[i[0]] = i[1]
              print(i)
except Error as e:
    print(e)

bratva = dict_of_brothers.keys()

router = Router()



@router.message(Command(commands = 'humour'))
async def process_start_command(message: types.Message):
    await message.answer(
        'Привет!\nДавайте посмеёмся\n\n'
        'Чтобы получить список доступных '
        'команд - отправьте команду /helphumour'
    )


# Этот хэндлер будет срабатывать на команду "/helphumour"
@router.message(Command(commands='helphumour'))
async def process_help_command(message: types.Message):
    await message.answer(
        f'Есть тюремная камера, в которой живут 20 зэков'
        f'Написав имя зэка, можно прочитать его любимый анекдот'
        f'Чтобы узнать список имён, напишите /names'
    )


# Этот хэндлер будет срабатывать на команду "/names"
@router.message(Command(commands='names'))
async def process_names_command(message: types.Message):
    await message.answer(
        f'Всего зэков: {len(dict_of_brothers)}\n'
        f'Их имена: {bratva}'
    )


# Этот хэндлер будет срабатывать на отправку пользователем имени
@router.message(F.text)
async def process_numbers_answer(message: types.Message):
    await message.reply(dict_of_brothers.get(F.text))