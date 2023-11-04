import tensorflow as tf
from tensorflow import keras
import cv2
import numpy as np
from PIL import Image
import os


def lowLight(filename):    
    loaded_model = keras.models.load_model("my_model")
    input_image = Image.open(f'static/input/{filename}')
    input_image = tf.image.resize(input_image, (400, 600))
    input_image = np.array(input_image) / 255.0  
    input_image = np.expand_dims(input_image, axis=0) 
    enhanced_image = loaded_model(input_image)
    enhanced_image = (enhanced_image[0].numpy() * 255).astype(np.uint8) 
    enhanced_image = Image.fromarray(enhanced_image)
    enhanced_image.save(f'{filename}')
    one  = cv2.imread(f'{filename}')
    cv2.imwrite(f'static/output/{filename}', one)
