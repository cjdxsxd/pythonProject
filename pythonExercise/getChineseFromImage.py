# _*_ coding: utf _*_



from PIL import Image
import pytesseract

img = Image.open("D:\\02python\\youzhengimage.jpg")
data = pytesseract.image_to_string(img, lang='chi_sim')
print(data)