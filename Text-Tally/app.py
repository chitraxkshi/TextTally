from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from ocr import ocr_text
# from ocr import corrected_text_fn
from count import count_words
from clean import RemoveCharacter
from count import perform_ocr
from clean import perform_ocr
import os


app = Flask(__name__, static_folder='static')

@app.route('/')
def home():
    
    return render_template('index2.html')





@app.route('/uploaded_ocr', methods=['POST'])
def upload_ocr():
    file = request.files['file']
    if file:
        
        file_path = 'temp/' + file.filename
        file.save(file_path)

        extracted_text = ocr_text(file_path)
        # correct_text= corrected_text_fn(extracted_text)
       
        return render_template('Uocr.html', extracted_text=extracted_text)
    else:
        extracted_text=''
        return render_template('Uocr.html', extracted_text=extracted_text)


@app.route('/uploaded_WordCount', methods=['POST'])
def upload_WC():
    file = request.files['file']
    if file:
        
        file_path = 'temp/' + file.filename
        file.save(file_path)
        text = perform_ocr(file_path)

        Word_count = count_words(text)
        return render_template('Ucount.html', Word_count=Word_count)
    else:
        Word_count=''
        return render_template('Ucount.html', Word_count=Word_count)
    

@app.route('/uploaded_CleanData', methods=['POST'])
def upload_CD():
    file = request.files['file']
    if file:
        
        file_path = 'temp/' + file.filename
        file.save(file_path)
        text = perform_ocr(file_path)

        Clean_Data = RemoveCharacter(text)
        return render_template('Uclean.html', Clean_Data=Clean_Data)

    else:

        Clean_Data=''
        return render_template('Uclean.html', Clean_Data=Clean_Data) 


if __name__ == "__main__":
    app.run(debug=True)

