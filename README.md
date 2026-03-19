# Smart Bridge Crack Detection System

## 📌 Overview
This project focuses on detecting structural cracks in bridge surfaces using image processing techniques. It demonstrates how AI and sensing technologies can be applied to infrastructure monitoring.

## 🚀 Features
- Crack detection using image processing (OpenCV)
- Edge detection and thresholding techniques
- Batch processing of multiple images
- Simple and scalable architecture

## 🧠 Approach
1. Convert image to grayscale  
2. Apply Gaussian blur  
3. Perform edge detection (Canny)  
4. Apply thresholding to highlight cracks  

## 🏗️ System Architecture
Sensor (Camera) → Image Capture → Processing (Python/OpenCV) → Crack Detection → Alert/Monitoring System

## 🛠️ Tech Stack
- Python
- OpenCV
- NumPy

## ▶️ How to Run
```bash
pip install -r requirements.txt
python main.py