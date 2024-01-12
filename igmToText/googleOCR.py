API_key = "AIzaSyBHJOXbQFFASCSYpJEShBtg1U9PaB96rCY"

from google.cloud import vision
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "goofle-drive-test-381714-35ac81751cd7.json"

client = vision.ImageAnnotatorClient()

with open('../media/pictures/bill6.jpg', 'rb') as image_file:
   content = image_file.read()

image = vision.Image(content=content)

response = client.text_detection(image=image)
texts = response.text_annotations
print('Texts:')
for text in texts:
   print('\n"{}"'.format(text.description))
