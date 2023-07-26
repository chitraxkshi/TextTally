import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def perform_ocr(image_path):
    
    image = Image.open(image_path)

    
    extracted_text = pytesseract.image_to_string(image)

    return extracted_text

def count_words(text):
    
    words = text.strip().split()

    word_count = len(words)

    word_count_str = str(word_count)

    return word_count_str


# import pytesseract
# from PIL import Image

# pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# def perform_ocr(file_path):

#     img = Image.open(file_path)  #loading image in memory

#     ocr_result = pytesseract.image_to_string(img)
#     with open('temp/output.json2', 'w') as file:
#         file.write(ocr_result)


#     return ocr_result

# def count_words():
    
#     with open('temp/output.json2', 'r') as file:
#         words = file.read()
#         word_count = len(words)
#         word_count_str = str(word_count)

#     return word_count_str








