https://image-classification-using-cnn-3eh4freqpk3gkrieycp5tz.streamlit.app/
# 🐶🐱 Dog vs Cat Image Classification using CNN
![Python](https://img.shields.io/badge/Python-3.10-blue)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.15-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-WebApp-red)
![Status](https://img.shields.io/badge/Status-Deployed-brightgreen)


## 📌 Overview

This project implements an Image Classification system using a Convolutional Neural Network (CNN) to classify images of dogs and cats. The model learns visual features automatically from images and predicts whether the input image belongs to a dog or a cat class.

Convolutional Neural Networks are widely used in computer vision tasks because they can automatically detect important features such as edges, shapes, and textures without manual feature extraction.

This project covers the full deep learning pipeline including data preprocessing, model building, training, evaluation, and prediction.

---

## 🎯 Objectives

- Build a CNN model for binary image classification
- Understand convolution, pooling, and dense layers
- Learn image preprocessing techniques
- Train and evaluate deep learning models
- Perform predictions on new images
- Save and reuse trained models

---

## 🧠 CNN Explanation

A Convolutional Neural Network consists of multiple layers:

### Convolution Layer
Extracts important features using filters.

Example:
- edges
- textures
- shapes

### Activation Function
ReLU is used to introduce non-linearity.

Formula:
f(x) = max(0, x)

### Pooling Layer
Reduces image size and computation.

Example:
MaxPooling 2×2

### Flatten Layer
Converts 2D feature maps into a 1D vector.

### Dense Layer
Performs classification.

### Output Layer
Sigmoid activation is used for binary classification.

Output range:
0 to 1

---

## 📂 Dataset Structure

dataset/
│
├── train/
│   ├── dogs/
│   └── cats/
│
├── validation/
│   ├── dogs/
│   └── cats/
│
└── test/
    ├── dogs/
    └── cats/

Each folder contains images corresponding to its label.

---

## ⚙️ Technologies Used

Python  
TensorFlow  
Keras  
NumPy  
Matplotlib  
Pillow  

---

## 🧹 Data Preprocessing

Steps performed:

- Resize images to 160 × 160
- Normalize pixel values
- Convert images into arrays
- Generate batches

Normalization formula:

pixel = pixel / 255.0

Benefits:

- Faster training
- Better convergence

---

## 🏗️ Model Architecture

Layer 1  
Conv2D  
Filters: 32  
Kernel: 3×3  
Activation: ReLU  

Layer 2  
MaxPooling  

Layer 3  
Conv2D  
Filters: 64  
Activation: ReLU  

Layer 4  
MaxPooling  

Layer 5  
Conv2D  
Filters: 128  
Activation: ReLU  

Layer 6  
MaxPooling  

Layer 7  
Flatten  

Layer 8  
Dense  
Units: 128  
Activation: ReLU  

Layer 9  
Dense  
Units: 1  
Activation: Sigmoid  

---

## ⚡ Compilation

Optimizer:
Adam

Loss function:
Binary Crossentropy

Metric:
Accuracy

---

## 🏋️ Training

Steps:

1 Load dataset  
2 Preprocess images  
3 Build CNN model  
4 Compile model  
5 Train model  
6 Validate model  
7 Save model  

Example:

Epochs: 10  
Batch size: 32  

---

## 📊 Evaluation

Metrics used:

Accuracy  
Loss  

Example result:

Training Accuracy: 95%  
Validation Accuracy: 92%  

---

## 🔍 Prediction

Steps:

1 Load trained model  
2 Load image  
3 Resize image  
4 Normalize image  
5 Predict using model  

Output:

Dog  
or  
Cat  

---

## 💾 Model Saving

Model is saved as:

dog_cat_model.keras

This allows reuse without retraining.

---

## ▶️ How to Run

Install dependencies:

pip install tensorflow numpy matplotlib pillow

Train model:

python train.py

Predict image:

python predict.py

---

## 📈 Advantages

Automatic feature extraction  
High accuracy  
Efficient image classification  

---

## ⚠️ Limitations

Requires large dataset  
Training can be slow  
Needs GPU for faster performance  

---

## 🚀 Future Improvements

Use Transfer Learning  
Use MobileNetV2  
Improve accuracy  
Deploy using Streamlit  

---

## 📚 Learning Outcomes

Understanding CNN architecture  
Image preprocessing  
Model training  
Model evaluation  
Image prediction  

---

## 👨‍💻 Author

Kratarth Srivastava  
B.Tech Computer Science Engineering  

---

## ⭐ Support

Star this repository if you found it useful.
