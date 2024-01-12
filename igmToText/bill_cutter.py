from variables import variables
import re

class Cutter:
    def __init__(self):
        pass

    # def cut_bill(self, text) -> list:
    #     preview_text = text
    #     text = text.replace("\n", " ")
    #     bill_products = []
    #     if type(text) is str:
    #         code_match = re.findall(variables.code, text)
    #         for code in code_match:
    #             if code =='4600682003212 ':
    #                 pass
    #             if text.startswith(code) and len(re.findall(code, text)) > 1:
    #                 split_text = text.split(code)
    #                 bill_products.append(f"{code} {split_text[1]}")
    #                 text = code + code.join(split_text[2:])
    #                 pass
    #             else:
    #                 split_text = text.split(code, 1)
    #                 text = f"{code} {split_text[1]}"
    #                 if re.findall(r"\*[ ]?[0-9.]{2,}", split_text[0]):
    #                     bill_products.append(split_text[0])
    #             pass
    #         text = self.find_end_of_product_value(text)
    #         bill_products.append(text)
    #     # products_value_list = self.product_values(bill_products)
    #     pass
    #     return bill_products, preview_text

    def cut_bill(self, text) -> list:
        products_list = []
        text = " ".join(text.split("\n"))
        raw_text = text
        separators_list = re.findall(variables.separate_products_throw_text, text)
        for separator in separators_list:
            # print(separator)
            separated_text = text.split(separator)
            i = 1 if not separated_text[0] else 0
            text = f"{separator} {separator.join(separated_text[i+1:])}"
            products_list.append(separated_text[i].strip()) if i ==0 else products_list.append(f"{separator.strip()} {separated_text[i].strip()}")
            pass
        return products_list, raw_text

    def find_end_of_product_value(self, text):
        for invalid_value in  variables.invalid_value:
            if invalid_value in text:
                print(invalid_value)
                text = text.split(invalid_value)[0]
                break
            else:
                pass
        return text

    def get_products_dict(self, bill_products:list, file_path:str=None) -> list:
        products_value_list = []
        for product in bill_products:
            product_dict = {}
            product_dict['code'] = re.findall(variables.code, product)[0].strip()
            product = product.replace(product_dict['code'], "")
            product_dict['quantity'] = re.findall(variables.quantity, product)[0].strip()
            product = product.replace(product_dict['quantity'], "")
            product = re.sub(variables.bonus, "", product).strip()
            product_dict['cost'] = re.findall(variables.price_and_cost, product)[-1]
            product_dict['price'] = re.findall(variables.price_and_cost, product)[-2]
            product_dict['product'] = product.replace(product_dict['cost'], "").replace(product_dict['price'], "")

            products_value_list.append(product_dict)
            pass
        return(products_value_list)
