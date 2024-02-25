from flask import Flask, render_template, request, redirect, url_for
from flask import Flask, render_template, request, redirect, url_for
import tensorflow.keras.backend as K
from tensorflow.keras.models import load_model
from classifier import predict_class
from env_vars import model_rel_path, image_rel_path
from get_image import download_image
from query_db import get_data
import os

app = Flask(__name__)

@app.route('/imgUrl')
def query_example():
    url = request.args.get(r'url')

    print(f'url: {url}')

    # define the function to get the images from the url and predicted the class
    # Replace 'firebase_url' with your Firebase URL
    # Replace 'local_path.jpg' with your local file path
    firebase_url = "https://firebasestorage.googleapis.com/v0/b/gamifit69420.appspot.com/o/images%2F"+ str(url)
    download_image(firebase_url, 'capturedImage.jpg')


    # Make a list of images and test the trained model
    #the path is always from the user root in C:
    imagepath = ['capturedImage.jpg']
    pred_val = predict_class(model_best, imagepath, True)
    # Call the function with the value for FoodItem
    nutri_info =  get_data(pred_val)
    print(nutri_info)
    #clean the image after predicting
    os.remove("capturedImage.jpg")
    return str(nutri_info)

# use the pre-trained model
# Loading the best saved model to make predictions
K.clear_session()
model_best = load_model(model_rel_path,compile = False)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

  

