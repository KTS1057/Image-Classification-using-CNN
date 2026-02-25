import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import os

st.set_page_config(page_title="Cat vs Dog Classifier")

st.title("🐱🐶 Cat vs Dog Image Classifier")

@st.cache_resource
def load_model():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(BASE_DIR,"CAT_DOG_MODEL.keras")
    return tf.keras.models.load_model(model_path)

model = load_model()

uploaded_file = st.file_uploader("Upload an image", type=["jpg","png","jpeg"])

if uploaded_file is not None:

    image = Image.open(uploaded_file)
    st.image(image, width="stretch")

    img = image.resize((160,160))  # ✅ must match training size
    img_array = np.array(img)/255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)
    confidence = float(prediction[0][0])

    model_accuracy = 92  # replace with your real accuracy

    if confidence > 0.5:
        st.success(f"🐶 Dog | Confidence: {confidence*100:.2f}% | Accuracy: {model_accuracy}%")
    else:
        st.success(f"🐱 Cat | Confidence: {(1-confidence)*100:.2f}% | Accuracy: {model_accuracy}%")