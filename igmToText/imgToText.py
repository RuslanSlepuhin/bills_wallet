import re

import easyocr

from variables import variables


def get_text(path):
   # Инициализация readers для английского языка
   reader = easyocr.Reader(['ru'])
   # Чтение текста с изображения
   result = reader.readtext(path)
   product_dict = []

   collected_data = collect_data(result)
   data = get_data(collected_data)
   pass

   # for i in range(0, len(result)):
   #    if re.findall("^\*[ ]?[0-9]+", result[i][1]):
   #       data = get_product(result[i-4:i+2], raw_list=result[i-4:i+2])
   #       product_dict.append(correct_data(result[i-4:i+2], **data))

def get_product(raw_data:list, raw_list:list) -> dict:
   expressions = {
      "=": "cost",
      "[0-9]{5,}": "product",
      "^[\d.,]+$": "price",
      "\^[^a-zA-Zа-яА-Я\n *]+": "price_before",

   }
   data = {}
   index_quantity = len(raw_data)-2
   data['quantity'] = raw_data[index_quantity][1].replace("*", "")
   raw_data.pop(index_quantity)
   for expression in expressions:
      for item in reversed(raw_data):
         if 'product' in data and "МУЧН" in data['product']:
            pass
         match = re.findall(expression, item[1])
         if match:
            data[expressions[expression]] = item[1]
            index = raw_data.index(item)
            raw_data.pop(index)

            break
      if expressions[expression] == 'cost' and re.findall("[0-9]{5,}", raw_data[-1][1]):
         raw_data.pop(-1)

   if data.get('price_before') and data['product'] == data['price_before']:
      data.pop('price_before')
   pass
   return data

def correct_data(*args, **kwargs):
   data = {}
   for key in kwargs:
      match key:
         case "product":
            data["product_code"] = kwargs['product'].split(" ", 1)[0]
            data[key] = kwargs['product'].replace(data["product_code"], "").replace(";", "").strip()
         case "quantity":
            data[key] = clear_digital(kwargs[key])
         case "price":
            data[key] = clear_digital(kwargs[key])
         case "price_before":
            data["price"] = clear_digital(kwargs["price_before"]) + "." + data['price'] if "." not in data['price'] else data['price']
         case "cost":
            data[key] = clear_digital(kwargs[key])
            pass
   [print(f"{i}: {data[i]}") for i in data]
   print("---------------\n")
   return data

def clear_digital(text):
   preview = text
   for key in variables.replace_dict:
      text = text.replace(key, variables.replace_dict[key])
   return text.strip()

def collect_data(result:list):
   input = False
   product = ""
   products_list = []
   for item in result:
      print(item[1])
      match = re.findall(r"^[ ]?[0-9]{5,14}[^.]", item[1])
      if match:
         input = True
         if product:
            products_list.append(product)
         product = f"{item[1]} "
      else:
         if input:
            if not valid_value_item(item[1]):
               products_list.append(product)
               break
            product += f"{item[1]} "
   products_list.append(product)
   return products_list

def get_data(collected_data):
   for item in collected_data:
      for i in variables.clear_item_list:
         item = item.replace(i, "")

      code = re.findall(variables.code_text_start, item)[0]
      item = item.replace(code, "")
      pass

def valid_value_item(item):
   for i in variables.invalid_value:
      if i in item:
         return False
   return True

if __name__ == "__main__":
   get_text(path="../media/pictures/bill2.jpg")