import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Page configuration
st.set_page_config(
    page_title="Date Classifier",
    page_icon="🌴",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-family: 'Arial Black', sans-serif;
        color: #5e2612;
    }
    .sub-header {
        color: #8b5a2b;
        font-style: italic;
        margin-bottom: 20px;
    }
    .instructions {
        background-color: #f5efe0;
        padding: 15px;
        border-radius: 8px;
        margin-bottom: 20px;
        color: #333333;
        border: 1px solid #dcd2bc;
    }
    .instructions ol {
        margin-top: 10px;
        margin-bottom: 10px;
    }
    .instructions li {
        color: #333333;
        padding: 3px 0;
    }
    .prediction-box {
        background-color: #f9f3e6;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #e6ccb2;
        margin-top: 20px;
    }
    .footer {
        text-align: center;
        color: #666;
        font-size: 12px;
        margin-top: 50px;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("<h1 class='main-header'>Date Classification</h1>", unsafe_allow_html=True)

# Combined "Identify dates" and "How it works" sections
st.markdown("<h3 class='sub-header'>Identify Ajwa or Medjool dates with AI</h3>", unsafe_allow_html=True)

# Instructions now directly under the subtitle with fixed background and text color
st.markdown("""
<div class="instructions">
    <strong>How it works:</strong>
    <ol>
        <li>Upload a clear image of a date</li>
        <li>The AI will analyze the image</li>
        <li>Get instant classification results</li>
    </ol>
</div>
""", unsafe_allow_html=True)

# Add a separator
st.markdown("---")

# Load model with caching
@st.cache_resource
def load_model():
    model = tf.keras.models.load_model('Date_Mode.h5')
    return model

# Two columns layout
col1, col2 = st.columns([1, 1])

with col1:
    # File uploader widget for image upload
    uploaded_image = st.file_uploader("Choose an image (JPG format)", type=["jpg"])
    
    # Add information about dates
    # Add information about dates
st.markdown("---")
with st.expander("Learn about Ajwa and Medjool dates"):
    st.write("""
    **Ajwa Dates** are soft, dark brown dates from Medina, Saudi Arabia. They're known for their distinctive taste and religious significance.
    
    **Medjool Dates** are larger, sweeter dates often called the "king of dates." They originate from Morocco and are popular worldwide for their caramel-like flavor.
    """)

with col2:
    # Image display and prediction results
    if uploaded_image is not None:
        # Open the image and resize for display
        img = Image.open(uploaded_image)
        
        # Display image with controlled size
        st.image(uploaded_image, caption="Uploaded Date", width=250)
        
        # Load model with a spinner
        with st.spinner("Loading model..."):
            model = load_model()
        
        # Preprocess the image and make a prediction
        with st.spinner("Analyzing image..."):
            # Image preprocessing
            img_resized = img.resize((256, 256))
            img_array = np.array(img_resized)
            img_array = np.expand_dims(img_array, 0)  # Add batch dimension
            
            # Make prediction
            pred = model.predict(img_array)
            predicted_class = 'Ajwa' if pred[0][0] > pred[0][1] else 'Medjool'
            confidence = pred[0][0] if predicted_class == 'Ajwa' else pred[0][1]
            
            # Display results in a styled box
            st.markdown(f"""
            <div class='prediction-box'>
                <h2 style='text-align: center; color: #000;'>Results</h2>
                <h3 style='text-align: center; color: #000;'>This appears to be a <span style='color: #5e2612; font-weight: bold;'>{predicted_class}</span> date</h3>
                <p style='text-align: center; color: #000;'>Confidence: {confidence:.2%}</p>
            </div>
            """, unsafe_allow_html=True)
    else:
        # Placeholder when no image is uploaded
        st.markdown("""
        <div style='text-align: center; padding: 30px; color: #666; border: 2px dashed #ccc; border-radius: 10px; background-color: #f9f3e6;'>
            <p style='margin: 0; font-size: 16px;'>No file chosen</p>
            <p style='margin: 0; font-size: 14px;'>Drag and drop file here</p>
            <p style='margin: 0; font-size: 12px;'>Limit 200MB per file • JPG, JPEG</p>
            <p style='margin: 10px 0 0; font-size: 14px; font-weight: bold;'>Upload an image to see the prediction</p>
        </div>
        """, unsafe_allow_html=True)
# Footer
st.markdown("<div class='footer'>Powered by TensorFlow • Date Image Classifier</div>", unsafe_allow_html=True)