import pytesseract
from PIL import Image
import cv2 as cv
import numpy as np
import re

pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'



def ocr_text(file_path):
    img = Image.open(file_path) 
    # img_np = np.array(img)

    # inverted_image= cv.bitwise_not(img_np)
    # cv.imwrite('temp/inverted.jpg', inverted_image)

    # gray = cv.cvtColor(inverted_image, cv.COLOR_BGR2GRAY)
    # cv.imwrite('temp/index_gray.png', gray)

    ocr_result = pytesseract.image_to_string(img)
    with open('temp/output.json', 'w') as file:
        file.write(ocr_result)

    return ocr_result

# def corrected_text_fn(ocr_result):
#     corrected_text = re.sub(r'\|', 'I', ocr_result)
#     return corrected_text
  