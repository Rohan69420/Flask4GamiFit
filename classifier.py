from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.inception_v3 import preprocess_input
import numpy as np

# mapping
#necessary vars# picking 3 food items and generating separate data folders for the same
food_list = ['samosa','pizza','omelette']

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
    return pred_value
    #we will return this value if needed, which we will need to anyway