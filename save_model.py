import cv2
import os
import numpy as np
from PIL import Image
import re
import os.path

def get_images_and_labels():
    print('save models start...')

    trainPath = './img/raccoon'

    # Haar-like特徴分類器
    cascadePath = './haarcascade_frontalface_alt.xml' # 正面から見た人の顔のルール
    faceCascade = cv2.CascadeClassifier(cascadePath)
    recognizer = cv2.face.LBPHFaceRecognizer_create()

    # 画像を保存する配列
    images = []
    # ラベルを保存する配列
    labels = []
    for f in os.listdir(trainPath):
        imagePath = os.path.join(trainPath, f)
        imagePil = Image.open(imagePath).convert('L') # 8bitグレースケール
        image = np.array(imagePil, 'uint8')
        faces = faceCascade.detectMultiScale(image) # 顔の検知

        for(x, y, w, h) in faces:
            # 200*200にリサイズ
            roi = cv2.resize(image[y: y+h, x: x+w],
                             (200, 200), interpolation=cv2.INTER_LINEAR)
            # 画像の保存処理
            images.append(roi)
            intNumber = re.findall('\d+', f) #'\d'は数字の正規表現
            for number in intNumber:
                labels.append(int(number))

    recognizer.train(images, np.array(labels)) # カスケード分類機のトレーニング機能
    recognizer.write('sample-model.yml')

    print('save models complete...')

get_images_and_labels()