from aiogram import F
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.enums import ParseMode
from core.games import luckycounter
from core.handlers import humoreski

logging.basicConfig(level=logging.INFO)

bot = Bot("6686600787:AAF2Bpax6fwmt5kcPRAns36uZLK5RWY9Oa8")
dp = Dispatcher()
dp.include_router(humoreski.router)
dp.include_router(luckycounter.router)





# Хэндлер на скачивание картинки
@dp.message(F.photo)
async def load_photo(message: types.Message, bot: Bot):
    file = await bot.get_file(message.photo[-1].file_id)
    destination = r"C:\Users\RGB\Desktop\Projects\Best_bot\photos\Photo.jpg"
    await bot.download_file(file.file_path, destination)
    await message.answer(f"Скачано в папку <b>photos</b>", parse_mode=ParseMode.HTML)

@dp.message(F.document)
async def load_document(message: types.Message, bot: Bot):
    file = await bot.get_file(message.document.file_id)
    destination = r"C:\Users\RGB\Desktop\Projects\Best_bot\documents\document"
    await bot.download_file(file.file_path, destination)
    await message.answer(f"Скачано в папку <b>documents</b>", parse_mode=ParseMode.HTML)


# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(f"Hello, <b>{message.from_user.full_name}</b>!",
                         parse_mode=ParseMode.HTML)

# Хэндлер на список команд
@dp.message(Command("help"))
async def cmd_start(message: types.Message):
    await message.answer(f"/help - список команд\n"
                         f"/loadfile - загрузка файлов\n"
                         f"/loadphoto - загрузка картинок боту\n"
                         f"/info - информация о боте\n"
                         f"/humour - юморески")

# Хэндлер на команду /info
@dp.message(Command("info"))
async def cmd_info(message: types.Message):
    await message.reply("Бот создан для скачивания различных материалов на компьютер, а также для создания заметок. Отправьте файл боту, и он сохранит его")

# Хэндлер на команду /loadphoto
@dp.message(Command("loadphoto"))
async def cmd_start(message: types.Message):
    await message.reply(f"Загрузите картинку")

@dp.message(Command("loadfile"))
async def cmd_start(message: types.Message):
    await message.reply(f"Загрузите файл")




# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())