import streamlit as st
import tensorflow as tf
from tensorflow import keras
import numpy as np
from tensorflow.keras.preprocessing import image
from PIL import Image
import io

# Title
st.title("Date Classification")
st.write("Ajwa or Medjool, This Model Shows you the Date is Ajwa or Medjool")
# Load model
@st.cache_resource
def load_model():
    model = tf.keras.models.load_model('Date_Mode.h5')
    return model

with st.spinner("Loading Model...."):
    model = load_model()

# Classes for CIFAR-10 dataset
classes = ["Ajwa", "Medjool"]

# Image preprocessing
def load_image(uploaded_image):
    img = Image.open(uploaded_image)
    img = img.resize((256, 256))  # Resize image to match the model's input
    img_array = np.array(img)
    img_array = np.expand_dims(img_array, 0)  # Add batch dimension
    return img_array

# File uploader widget for image upload
uploaded_image = st.file_uploader("Choose an image (ONLY JPG)...", type=["jpg"])

# Predict when an image is uploaded
if uploaded_image is not None:
    st.image(uploaded_image, caption="Uploaded Image.",  use_container_width=True)
    st.write("Predicting Class...")

    # Preprocess the image and make a prediction
    with st.spinner("Classifying..."):
        img_tensor = load_image(uploaded_image)
        pred = model.predict(img_tensor)
        predicted_class = 'Ajwa' if pred[0][0] > pred[0][1] else 'Medjool'
        
        st.write(f"Predicted Class: {predicted_class}")