# 🌴 Date Classification Project

## 📖 Overview

This intelligent **Date Classification System** leverages state-of-the-art deep learning techniques to accurately distinguish between two premium date varieties: **Ajwa** and **Medjool**. The project combines machine learning with an intuitive web interface, making date identification accessible to consumers, retailers, and agricultural professionals.

### 🎯 Purpose & Use Cases

- **Consumer Education**: Help consumers identify authentic date varieties when shopping
- **Quality Control**: Assist retailers and distributors in verifying date authenticity
- **Agricultural Research**: Support researchers studying date fruit characteristics
- **Educational Tool**: Demonstrate practical applications of computer vision in agriculture
- **Food Industry**: Aid in automated sorting and quality assessment processes

## 🚀 Features

- **High-Accuracy Classification**: AI-powered image recognition with trained CNN model
- **User-Friendly Web Interface**: Interactive Streamlit application for easy image upload
- **Real-Time Predictions**: Instant classification results with confidence scores
- **Educational Content**: Detailed information about both date varieties
- **Mobile-Friendly**: Responsive design works on desktop and mobile devices
- **Sample Images**: Pre-loaded test images for trying the system immediately

## 🛠️ Technologies & Requirements

### Core Technologies
- **Python 3.x**: Primary programming language
- **TensorFlow**: Deep learning framework for CNN model
- **Streamlit**: Web application framework for the interactive interface
- **NumPy**: Numerical computing library
- **PIL (Pillow)**: Python Imaging Library for image processing
- **Jupyter Notebook**: Development environment for model training

### Model Specifications
- **Architecture**: Convolutional Neural Network (CNN)
- **Framework**: TensorFlow/Keras
- **Input Size**: 256x256x3 (RGB images)
- **Model File**: `Date_Mode.h5` (pre-trained model)
- **Classes**: Binary classification (Ajwa vs Medjool)

### Dependencies
```
streamlit
tensorflow
numpy
pillow
```

## 📊 Dataset

The model is trained on the **UCI Machine Learning Repository** dataset:
- **Dataset Name**: Ajwa or Medjool Date Classification
- **Source**: [UCI ML Repository](https://archive.ics.uci.edu/static/public/879/ajwa+or+medjool.zip)
- **Classes**: 2 (Ajwa and Medjool dates)
- **Format**: High-resolution JPG images
- **Split**: 80% training, 20% validation

## 🏗️ Model Architecture

The classification model is a **Convolutional Neural Network (CNN)** optimized for date fruit recognition:

```
Input Layer (256x256x3)
    ↓
Conv2D (32 filters, 3x3) + ReLU + MaxPooling2D
    ↓
Conv2D (64 filters, 3x3) + ReLU + MaxPooling2D
    ↓
Conv2D (128 filters, 3x3) + ReLU + MaxPooling2D
    ↓
Flatten Layer
    ↓
Dense Layer (128 neurons, ReLU)
    ↓
Output Layer (2 neurons, Softmax)
```

### Training Configuration
- **Epochs**: 10
- **Optimizer**: Adam
- **Loss Function**: Sparse Categorical Crossentropy
- **Metrics**: Accuracy
- **Batch Size**: 32

## 🚀 Installation & Usage

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Quick Start
1. **Clone the repository**
   ```bash
   git clone https://github.com/0M3REXE/Date-Classification.git
   cd Date-Classification
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run streamlit_app.py
   ```

4. **Open your browser** and navigate to `http://localhost:8501`

### Using the Application
1. Upload a clear JPG image of a date fruit
2. Wait for the AI analysis to complete
3. View the classification result with confidence score
4. Learn more about the identified date variety

## 🌐 Live Demo

**Try the live application**: [https://date-classification.streamlit.app/](https://date-classification.streamlit.app/)

*Use the provided sample images or upload your own date pictures to test the classifier!*

## 📈 Performance & Results

- **Model Accuracy**: Trained for optimal performance on date classification
- **Real-time Processing**: Fast inference suitable for web applications
- **Confidence Scoring**: Provides prediction confidence for reliability assessment

## 📁 Project Structure

```
Date-Classification/
├── streamlit_app.py           # Main web application
├── Date_Mode.h5              # Pre-trained CNN model
├── Dates.ipynb               # Model training notebook
├── requirements.txt          # Python dependencies
├── sample Images/            # Test images
│   ├── AJWA/                # Ajwa date samples
│   └── Medjool/             # Medjool date samples
├── README.md                # Project documentation
└── LICENSE                  # Apache License 2.0
```

## 🥭 Date Varieties Information

### Ajwa Dates
**Origin**: Medina, Saudi Arabia
- Soft, dark brown appearance with a distinctive wrinkled texture
- Rich, complex flavor with hints of honey and caramel
- Highly valued for their religious and cultural significance
- Premium quality dates often consumed during Ramadan
- Known for their nutritional benefits and antioxidant properties

### Medjool Dates  
**Origin**: Morocco (now cultivated worldwide)
- Large, plump dates often called the "King of Dates"
- Golden-brown color with a glossy, smooth skin
- Sweet, caramel-like flavor with chewy texture
- Popular in Western markets and gourmet applications
- Excellent source of fiber, potassium, and natural sugars

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues, fork the repository, and create pull requests for any improvements.

### Areas for Contribution
- Model accuracy improvements
- Additional date varieties
- UI/UX enhancements
- Performance optimizations
- Documentation improvements

## 📄 License

This project is licensed under the **Apache License 2.0** - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- UCI Machine Learning Repository for providing the dataset
- TensorFlow and Streamlit communities for their excellent frameworks
- Contributors and users who help improve this project

---

**⭐ If you find this project helpful, please give it a star on GitHub!**
