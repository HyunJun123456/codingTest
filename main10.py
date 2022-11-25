from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"

str = pytesseract.image_to_string(Image.open("C:/Users/easypick/Desktop/input12.jpg"), lang='kor')
print(str)