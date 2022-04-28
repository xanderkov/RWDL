from operator import imod
import cv2
import numpy as np
from model import baseAutoencoder
import matplotlib.pyplot as plt
from keras.preprocessing.image import save_img
import PIL
from cv2 import dnn_superres
from createTrain import createPixelArr



def delWatermarkFormImage(width, height, name):
    H = 128
    W = 128
    files = ['mnt/img/' + 'photo.jpeg']
    img = createPixelArr(files, W, H)
    img = img / 255
    modelAutoEncoder = baseAutoencoder(W, H)
    modelAutoEncoder.load_weights('./weights/modelAuto.h5')
    res = modelAutoEncoder.predict(img)
    modelAutoEncoder.evaluate(img, res)
    src = 'mnt/img/' + name
    resized_arr = cv2.resize(res[0], (width, height))
    
    save_img(src, cv2.cvtColor(resized_arr, cv2.COLOR_BGR2RGB))


def delWatermark():
    originalImage = PIL.Image.open('mnt/img/' + 'photo.jpeg')
    width, height = originalImage.size
    delWatermarkFormImage(width, height, 'photo.jpeg')


if __name__ == '__main__':
    delWatermark()