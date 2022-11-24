
import cv2
from PIL import Image
import pytesseract

"""
image = cv2.imread("C:/Users/easypick/Desktop/input11.jpg", cv2.IMREAD_GRAYSCALE)

print(image.shape)
"""

#resized_image_1 = cv2.resize(image, (130,227))

#print(resized_image_1.shape)

"""
pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"

str = pytesseract.image_to_string(Image.open(image), lang='kor')
print(str)
"""



#cv2.imshow("resized_image_1", resized_image_1)


imagePath = "C:/Users/easypick/Desktop/input11.jpg"
image = cv2.imread(imagePath, cv2.IMREAD_GRAYSCALE)

print(image)
resized_image_1 = cv2.resize(image, (227, 227))

cv2.imshow("origin", resized_image_1)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(resized_image_1)

cv2.imwrite("original", resized_image_1)
pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"

#str = pytesseract.image_to_string(Image.open(image), lang='kor')
#print(str)

#print(image.shape)

