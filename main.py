from igmToText import tess_OCR as tesseract_ocr

if __name__ == "__main__":
    products_list, text = tesseract_ocr.text_from_tesseract_ocr("./media/pictures/bill5.jpg")
    for i in products_list:
        print(f"{i}\n")
    products_list = tesseract_ocr.get_dict(products_list)