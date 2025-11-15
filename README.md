# **Flexible PCB Defect Detection using YOLOv5 + FlexSim Augmentation**
### *AI-Based Defect Detection Tailored for Flexible Electronics*

## **Project Overview**
Flexible Printed Circuit Boards (FPCBs) are critical components in flexible electronics. This project develops a YOLOv5-based defect detection system adapted for flexible PCBs using a custom FlexSim augmentation pipeline.

## Key Contributions
- FlexSim augmentation simulating bending, warping, lighting artifacts.
- Flexible-PCB dataset generation.
- YOLOv5 model training on FlexPCB dataset.
- End-to-end ready pipeline.

## Why Flexible PCB Detection is Hard
- Geometric deformation due to bending.
- Shadowing and lighting changes.
- Wrinkles/creases unique to FPCBs.
- Parallax distortion while imaging.

## Repository Structure
```
Flexible-PCB-Defect-Detection/
├── README.md
├── requirements.txt
├── flexsim_augmentation.py
├── prepare_dataset.py
├── train.py
├── infer.py
├── data/
│   ├── deepPCB/
│   ├── flexPCB/
│   └── data.yaml
├── yolov5/
└── results/
```

## How to Run
### 1. Install
```
pip install -r requirements.txt
```

### 2. Prepare Dataset
```
python prepare_dataset.py
```

### 3. Train YOLO
```
python train.py
```

### 4. Inference
```
python infer.py image.jpg
```

## Defect Classes
- Missing hole  
- Mousebite  
- Open circuit  
- Short  
- Spur  
- Spurious copper  

## Conclusion
This project provides a domain-adapted PCB defect detector designed for flexible electronics using synthetic augmentation to simulate bending and lighting variations.

