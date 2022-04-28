from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.layers import BatchNormalization, Conv2D, MaxPooling2D, Input, Conv2DTranspose

def baseAutoencoder(width, height):
    minWeight = width
    maxWeight = width * 2
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


    x = Conv2DTranspose(maxWeight, (2, 2), strides=(2, 2), padding='same', activation='relu')(z)
    x = BatchNormalization()(x)

    x = Conv2D(maxWeight, (3, 3), padding='same', activation='relu')(x)
    x = BatchNormalization()(x) 
    x = Conv2D(maxWeight, (3, 3), padding='same', activation='relu')(x)
    x = BatchNormalization()(x) 

    x = Conv2DTranspose(minWeight, (2, 2), strides=(2, 2), padding='same', activation='relu')(x)
    x = BatchNormalization()(x) 
    x = Conv2D(minWeight, (3, 3), padding='same', activation='relu')(x) 
    x = BatchNormalization()(x) 
    x = Conv2D(minWeight, (3, 3), padding='same', activation='relu')(x)
    x = BatchNormalization()(x) 

    x = Conv2D(shape[-1], (3, 3), activation='sigmoid', padding='same')(x)

    model = Model(img_input, x)
    model.compile(optimizer=Adam(lr=0.0001), loss='mean_squared_error') 

    return model