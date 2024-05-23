from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import numpy as np
import cv2
from datetime import datetime
import os
import string
from PIL import Image

app = Flask(__name__)

def LoadModel():
    global recognizer
    print('... Loading pre-trained model ...')
    cascadePath = './haarcascade_frontalface_alt.xml'
    faseCascade = cv2.CascadeClassifier(cascadePath)
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('sample-model.yml')
    print('... Loading end ...')

@app.route('/')
def index(): # テンプレートをレンダリングして返す
    return render_template('./flask-api-index.html')

@app.route('/result', methods=['POST']) # URLが'/result'で終わってる場合はPOSTする
def result():
    if request.files['image']:
        imagePil = Image.open(request.files['image']).convert('L')
        image = np.array(imagePil, 'uint8')

        # 類似度を出力
        label, predictConfidence = recognizer.predict(image)
        if predictConfidence > 100:
            predictConfidence = 0
        else:
            predictConfidence = 100 - predictConfidence
        predictConfidence = str(predictConfidence)
        print(predictConfidence)

        return render_template('./result.html', title='類似度', predictConfidence=predictConfidence)

if __name__ == '__main__':
    LoadModel()
    app.debug = True
    app.run(host='localhost', port=5000)