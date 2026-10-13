import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Load model
model = tf.keras.models.load_model("brain_tumor_classifier.keras")

# Class names
class_names = [
    "glioma",
    "meningioma",
    "notumor",
    "pituitary"
]

st.set_page_config(
    page_title="Brain Tumor Detection",
    page_icon="🧠",
    layout="centered"
)

st.title("🧠 Brain Tumor Detection System")
st.write("Upload an MRI image to predict the tumor type.")

uploaded_file = st.file_uploader(
    "Choose an MRI image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_container_width=True)

    # Resize according to your model input size
    image = image.resize((224, 224))

    img_array = np.array(image)
    img_array = img_array / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)

    predicted_class = np.argmax(prediction)
    confidence = np.max(prediction)

    st.success(
        f"Prediction: {class_names[predicted_class]}"
    )

    st.info(
        f"Confidence: {confidence*100:.2f}%"
    )