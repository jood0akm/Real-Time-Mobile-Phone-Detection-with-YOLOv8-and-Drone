# Real-Time-Mobile-Phone-Detection-with-YOLOv8-and-Drone
Real-time mobile phone detection using a custom-trained YOLOv8 model integrated with a DJI Tello drone. 
Overview

This project uses artificial intelligence to detect mobile phones in real time, integrated with a flying drone that performs the detection while airborne.

Key Stages
1. Data Collection

A set of mobile phone images was captured from various angles and positions to build a diverse dataset for training.

2. Data Labeling

Using labelme, each phone's location within the images was marked with a bounding box, preparing the data for training.

3. Model Training

A YOLOv8 (Nano) model was trained from scratch on the labeled dataset using the Ultralytics library.

Results:

Metric	Score
mAP50	99.5%
Precision	98%
Recall	97.4%
4. Testing

The trained model was first tested using a laptop camera to verify detection accuracy before deployment.

5. Drone Integration

The trained model was integrated with a DJI Tello drone using the djitellopy library. The drone takes off, flies, and analyzes its live video feed in real time, drawing a bounding box around any detected mobile phone during flight.

Result

A complete system combining AI (machine learning and computer vision) with aerial robotics, capable of accurately detecting mobile phones in real time during flight.

Tech Stack
Python
YOLOv8 (Ultralytics)
OpenCV
labelme / labelme2yolo
DJI Tello + djitellopy
