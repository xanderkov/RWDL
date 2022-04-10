from operator import imod
import cv2
import numpy as np
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.layers import BatchNormalization, Conv2D, MaxPooling2D, Input, Conv2DTranspose
import matplotlib.pyplot as plt
from keras.preprocessing.image import save_img
import PIL
from cv2 import dnn_superres

H = 128
W = 128

def createPixelArr(files, width, height):
    data = []
    for image in files:
        try:
            img_arr = cv2.imread(image, cv2.IMREAD_COLOR)
            resized_arr = cv2.resize(img_arr, (width, height))
            data.append(resized_arr)
        except Exception as e:
            print(e)
    return np.array(data)


def baseAutoencoder(width, height):
    minWeight = W
    maxWeight = W * 2
    shape=(width, height, 3)
    img_input = Input((shape))

    x = Conv2D(minWeight, (3, 3), padding='same', activation='relu')(img_input)
    x = BatchNormalization()(x)
    x = Conv2D(minWeight, (3, 3), padding='same', activation='relu')(x)
    x = BatchNormalization()(x)
    x = MaxPooling2D()(x)

    x = Conv2D(maxWeight, (3, 3), padding='same', activation='relu')(x)
    x = BatchNormalization()(x) 
    x = Conv2D(maxWeight, (3, 3), padding='same', activation='relu')(x)
    x = BatchNormalization()(x) 
    z = MaxPooling2D()(x)


    x = Conv2DTranspose(maxWeight, (2, 2), strides=(2, 2), padding='same', activation='relu')(z) # слой разжимает данные(с 28*20 на 56*40)
    x = BatchNormalization()(x)

    x = Conv2D(maxWeight, (3, 3), padding='same', activation='relu')(x)
    x = BatchNormalization()(x) 
    x = Conv2D(maxWeight, (3, 3), padding='same', activation='relu')(x)
    x = BatchNormalization()(x) 

    x = Conv2DTranspose(minWeight, (2, 2), strides=(2, 2), padding='same', activation='relu')(x) # слой разжимает данные(с 56*40 на 112*80)
    x = BatchNormalization()(x) 
    x = Conv2D(minWeight, (3, 3), padding='same', activation='relu')(x) 
    x = BatchNormalization()(x) 
    x = Conv2D(minWeight, (3, 3), padding='same', activation='relu')(x)
    x = BatchNormalization()(x) 

    x = Conv2D(shape[-1], (3, 3), activation='sigmoid', padding='same')(x)

    model = Model(img_input, x) # указываем модель, с оригинальным изображением на входе в сеть и сжатым-разжатым на выходе из сети
    model.compile(optimizer=Adam(lr=0.0001), loss='mean_squared_error') 

    return model

def delWatermarkFormImage(width, height, name):
    files = ['mnt/img/' + 'photo.jpeg']
    img = createPixelArr(files, H, W)
    img = img / 255
    modelAutoEncoder = baseAutoencoder(H, W)
    modelAutoEncoder.load_weights('./weights/128.h5')
    res = modelAutoEncoder.predict(img)
    modelAutoEncoder.evaluate(img, res)
    src = 'mnt/img/' + name
    sr = dnn_superres.DnnSuperResImpl_create()
    path = './weights/EDSR_x3.pb'
    sr.readModel(path)
    sr.setModel("edsr", 3)
    
    save_img(src, cv2.cvtColor(res[0], cv2.COLOR_BGR2RGB))
    image = cv2.imread(src)
    result = sr.upsample(image)
    cv2.imwrite(src, result)

def delWatermark():
    originalImage = PIL.Image.open('mnt/img/' + 'photo.jpeg')
    width, height = originalImage.size
    delWatermarkFormImage(width, height, 'photo.jpeg')

    

if __name__ == '__main__':
    delWatermark()