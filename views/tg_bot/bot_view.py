import asyncio
import logging
import sys
from datetime import datetime
from igmToText import tess_OCR as tesseract_ocr
from igmToText.bill_cutter import Cutter

from aiogram import Router, F
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold

from variables import variables

TOKEN = "6163884294:AAGConcnLAXf-5PHJV6EnIX_8ErsazemKh8"



class BotHandlers:

    def __init__(self):
        self.bot = Bot("6163884294:AAGConcnLAXf-5PHJV6EnIX_8ErsazemKh8", parse_mode=ParseMode.HTML)
        self.dp = Dispatcher()
        self.router = Router(name=__name__)

    async def handlers(self):

        @self.dp.message(CommandStart())
        async def command_start_handler(message: Message) -> None:
            await self.bot.send_message(message.chat.id, "Пожалуйста, введите новый текст", reply_markup=types.ForceReply())

            await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")

        @self.dp.message(F.photo)
        async def echo_handler(message: types.Message) -> None:
            photo = message.photo[-1]  # Последний элемент списка - наибольший размер фото
            file_id = photo.file_id

            file = await self.bot.get_file(file_id)

            # Скачайте файл
            result = await self.bot.download_file(file.file_path)

            # Сохраните файл
            file_name = f"./media/pictures/bill_{datetime.now().strftime('%H-%M')}.jpg"
            with open(file_name, 'wb') as f:
                f.write(result.read())

            products_list, text = tesseract_ocr.text_from_tesseract_ocr(file_name)
            cutter = Cutter()
            sum, no_sum = cutter.summ_cost(products_list)

            text = ""
            for item in products_list:
                for key in variables.keys:
                    text += f"{key}: {item[key]}\n"
                text += "--------\n"
            text += f"Bill Summ: {sum}"
            await self.bot.send_message(message.chat.id, text)

        await self.dp.start_polling(self.bot)




if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    bot = BotHandlers()
    asyncio.run(bot.handlers())

