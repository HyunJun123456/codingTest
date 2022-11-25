"""
import cv2

img_source = cv2.imread("C:/Users/easypick/Desktop/input11.jpg")
cv2.imshow("original", img_source)
"""

from PIL import Image
import pytesseract

filePath = "C:/Users/easypick/Desktop/input11.jpg"



img = Image.open(filePath)
print(img.size[0])
print(img.size[1])
new_image = img.resize((150, 150))

new_image.save(filePath)

pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"

str = pytesseract.image_to_string(Image.open(filePath), lang='kor')
print(str)