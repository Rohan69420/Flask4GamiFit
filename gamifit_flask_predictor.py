# importing the required libaries
from flask import Flask, render_template, request, redirect, url_for

import tensorflow as tf

import tensorflow.keras.backend as K
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

from tensorflow import keras
from tensorflow.keras import models
from tensorflow.keras.applications.inception_v3 import preprocess_input

import numpy as np
from env_vars import model_rel_path, image_rel_path

app = Flask(__name__)

# mapping
#necessary vars# picking 3 food items and generating separate data folders for the same
food_list = ['samosa','pizza','omelette']

# use the pre-trained model
# Loading the best saved model to make predictions
K.clear_session()
model_best = load_model(model_rel_path,compile = False)


# define the function to get the images from the url and predicted the class



#prediction function
#resuming with the model trained on google colaboratory
def predict_class(model, images, show = True):
  for img in images:
    img = image.load_img(img, target_size=(299, 299))
    img = image.img_to_array(img)                    
    img = np.expand_dims(img, axis=0)         
    img = preprocess_input(img)                                      

    pred = model.predict(img)
    index = np.argmax(pred)
    food_list.sort()
    pred_value = food_list[index]
    #print(pred)

    #printing what the model predicted
    print(pred_value) 
    #we will return this value if needed, which we will need to anyway

# Make a list of images and test the trained model
#the path is always from the user root in C:
images = []
imagepath = image_rel_path
images.append(imagepath+'samosa.jpg')
#images.append(imagepath+'pizza.jpg')
#images.append(imagepath+'omelette.jpg')
predict_class(model_best, images, True)