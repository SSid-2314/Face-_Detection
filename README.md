# Project Name: Real-Time Person Recognition Model

## Overview

This project demonstrates a real-time person recognition model trained on a custom dataset. The model is designed to identify and extract information such as name, age, and ID from input data. It leverages machine learning techniques to perform these tasks efficiently.

## Dataset

The model was trained on a real-time dataset containing:

Images: Images of individuals from various angles and lighting conditions.

Annotations: Ground truth data including names, ages, and IDs associated with each individual.

Model Architecture

The model architecture used for training is a deep learning-based convolutional neural network (CNN). This architecture was chosen for its ability to extract features from images and its suitability for tasks like object detection and recognition.

Training Process

During training, the model learned to:

Detect Faces: Identify and locate faces within images.

Recognize Features: Extract information such as names, ages, and IDs associated with each detected face.

Optimize: The training process involved optimizing the model's parameters to improve accuracy and reduce errors in recognition.

Usage

To use the model:


Input: Provide an image containing a person's face.

Output: The model will output the recognized person's name, age, and ID.

Dependencies

Ensure you have the following dependencies installed:

Python 3.x

OpenCV

Other necessary libraries (specified in requirements.txt)

## important note:

create a folder name dataset to keep the data

recognizer for feeding the data to train it.
