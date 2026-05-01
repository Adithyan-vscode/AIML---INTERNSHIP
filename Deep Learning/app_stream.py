import streamlit as st
import numpy as np
from PIL import Image
import tensorflow as tf
from tensorflow.keras.models import load_model

# Load trained model
model = load_model('cnn_model.h5')

# CIFAR-10 class labels
class_names = [
    'Airplane',
    'Automobile',
    'Bird',
    'Cat',
    'Deer',
    'Dog',
    'Frog',
    'Horse',
    'Ship',
    'Truck'
]
# Streamlit page configuration
st.set_page_config(page_title='CNN Image Classifier')

# Title
st.title('CNN Image Classification App')

st.write('Upload an image to classify using the trained CNN model.')

# Upload image
uploaded_file = st.file_uploader(
    'Choose an image...',
    type=['jpg', 'jpeg', 'png']
)

if uploaded_file is not None:

    # Open image
    image = Image.open(uploaded_file)
    

    # Display image
    st.image(image, caption='Uploaded Image', use_container_width=True)
 # Resize image
    image = image.resize((32, 32))

    # Convert image to array
    image_array = np.array(image)

    # Normalize image
    image_array = image_array / 255.0

    # Expand dimensions
    image_array = np.expand_dims(image_array, axis=0)

    # Prediction
    prediction = model.predict(image_array)

    predicted_class = class_names[np.argmax(prediction)]

    confidence = np.max(prediction) * 100

    # Display result
    st.subheader('Prediction Result')
    st.write(f'Predicted Class: {predicted_class}')
    st.write(f'Confidence: {confidence:.2f}%')