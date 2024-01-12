import asyncio

from igmToText import tess_OCR as tesseract_ocr
from igmToText.bill_cutter import Cutter
from views.tg_bot.bot_view import BotHandlers

if __name__ == "__main__":
    bot = BotHandlers()
    asyncio.run(bot.handlers())
    # products_list, text = tesseract_ocr.text_from_tesseract_ocr("./media/pictures/bill3.jpg")
    # for i in products_list:
    #     print(f"{i}\n")
    # cutter = Cutter()
    # sum, no_sum = cutter.summ_cost(products_list)
    # print("------------------BILL Summ ", sum)
    #
    # print(text)
    # pass

