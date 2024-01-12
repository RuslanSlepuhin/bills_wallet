from igmToText import tess_OCR as tesseract_ocr
from igmToText.bill_cutter import Cutter


if __name__ == "__main__":
    products_list, text = tesseract_ocr.text_from_tesseract_ocr("./media/pictures/bill0.jpg")
    for i in products_list:
        print(f"{i}\n")
    cutter = Cutter()
    sum, no_sum = cutter.summ_cost(products_list)
    print("------------------BILL Summ ", sum)

    print(text)
    pass

