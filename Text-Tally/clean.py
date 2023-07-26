import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def perform_ocr(image_path):
    
    image = Image.open(image_path)

    
    extracted_text = pytesseract.image_to_string(image)

    return extracted_text

def RemoveCharacter(text):
    special_characters = "!@#$%^&*()[]{};:,<>/?\\|`~“”‘©¢\""
    cleaned_text = ''.join(char for char in text if char not in special_characters)
    return cleaned_text









# def RemoveCharacter(input_file, output_file):
#     special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '<', '>', '?', ':', ',', ';', '|', '{', '}', '[', ']', '-', '=', "'", '"', '\\', '/', '`', '~', '“', '”']
        
#     with open('temp/output.json', 'r') as f1:
#         data = f1.read()
#         cleaned_data = ''.join(char for char in data if char not in special_characters)

#     with open('temp/cleaned_data.json', 'w') as f2:
#         f2.write(cleaned_data)

#     return cleaned_data    