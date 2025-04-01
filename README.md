# Date Classification Project

## Overview
This project uses deep learning to classify date fruits into two varieties: Ajwa and Medjool.

## Dataset
The dataset used is from the UCI Machine Learning Repository:
- **Dataset Name**: Ajwa or Medjool
- **Source**: https://archive.ics.uci.edu/static/public/879/ajwa+or+medjool.zip
- **Classes**: 2 (Ajwa and Medjool dates)
- **Format**: JPG images

## Model Architecture
The classification model is a Convolutional Neural Network (CNN) built with TensorFlow:
- 3 convolutional layers with ReLU activation and max pooling
- Flattening layer
- Dense layer with 128 neurons and ReLU activation
- Output layer with softmax activation for 2 classes

## Training
- The model is trained for 10 epochs
- Data is split into 80% training and 20% validation sets
- Uses Adam optimizer and sparse categorical crossentropy loss

## Try It Out Yourself
Use the Sample Images
https://date-classifcation.streamlit.app/

## Date Varieties Information

### Ajwa Dates
Soft, dark brown dates from Medina, Saudi Arabia. They're known for their distinctive taste and religious significance.

### Medjool Dates
Larger, sweeter dates often called the "king of dates." They originate from Morocco and are popular worldwide for their caramel-like flavor.
