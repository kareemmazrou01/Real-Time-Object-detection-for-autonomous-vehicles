# Real-Time Object Detection for Autonomous Vehicles

## Team Members
- **Kareem Yasser Mazrou** – Deployment, Real-Time Testing  
- **Shiref Ashraf** – Model Development, Evaluation  
- **Aliaa Abobakr** – MLOps, Monitoring  
- **Shehab Ahmed** – Data Collection, Preprocessing  
- **Aya Mohamed** – Data Collection, Preprocessing  

_All team members contributed to documentation and system design._

## Project Overview

We developed a real-time object detection system tailored for autonomous vehicles, capable of identifying pedestrians, vehicles, traffic signs, and obstacles from live video streams. The system utilizes YOLOv11 for high-speed inference and is deployed using a Flask web interface, integrated with Microsoft Azure and MLOps pipelines for continuous delivery and monitoring.

## Technologies Used

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Badge"/>
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask Badge"/>
  <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white" alt="PyTorch Badge"/>
  <img src="https://img.shields.io/badge/YOLOv11-FFCC00?style=for-the-badge&logo=OpenCV&logoColor=black" alt="YOLO Badge"/>
  <img src="https://img.shields.io/badge/Azure-0078D4?style=for-the-badge&logo=microsoft-azure&logoColor=white" alt="Azure Badge"/>
  <img src="https://img.shields.io/badge/MLflow-1E4C6B?style=for-the-badge&logo=mlflow&logoColor=white" alt="MLflow Badge"/>
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker Badge"/>
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5 Badge"/>
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS3 Badge"/>
</p>


## Problem Statement

Autonomous vehicles must process visual data in real-time to make safe and accurate driving decisions. This project addresses the challenges of:
- High-speed inference for real-time decision-making  
- Robust detection across various environmental conditions  
- Seamless integration with control systems  
- MLOps-driven deployment and lifecycle management

## Tech Stack

- **Model Architecture:** YOLOv11, SSD, Faster R-CNN  
- **Frameworks:** PyTorch, TensorFlow  
- **Interface:** Flask Web Application  
- **Deployment:** Microsoft Azure, Docker  
- **MLOps:** MLflow, Azure Pipelines  
- **Data Sources:** KITTI, COCO datasets  

## System Features

### Real-Time Object Detection
- Detects pedestrians, vehicles, traffic signs, and other road objects.
- Achieves real-time processing (≥30 FPS).
- Outputs bounding boxes with class labels and confidence scores.

### Web Interface
- Built using Flask to accept video input and display detection output.
- User-friendly design for testing and monitoring predictions.

### Azure Deployment
- Deployed using Azure App Services and Azure Machine Learning.
- Supports scalable, cloud-based inference with GPU acceleration.

### MLOps Integration
- MLflow integration for model tracking and retraining.
- Continuous monitoring and automatic updates upon performance drift.

## Functional Architecture

1. Video Input: Accepts video via web upload or live stream.
2. Preprocessing: Frames resized, normalized, and enhanced.
3. Model Inference: YOLOv11 detects and classifies objects in real time.
4. Output Rendering: Displays predictions via bounding boxes and labels.
5. Monitoring: Tracks metrics like mAP, IoU, and FPS for performance.

## Functional Requirements

| Feature                          | Description |
|----------------------------------|-------------|
| Real-Time Inference              | ≥30 FPS with low latency (≤100ms per frame) |
| Video Stream Support             | Accepts multiple camera feeds or uploaded video |
| Scalable Deployment              | Cloud-ready, edge-compatible |
| Integration-Ready                | Exposes RESTful API for vehicle control systems |
| Model Retraining                 | Automated via MLOps pipelines |
| Logging & Alerts                 | Logs inference stats, errors, and sends alerts on anomalies |

## Model Evaluation Results

| Metric         | Value   |
|----------------|---------|
| Recall         | 0.8188  |
| mAP@50         | 0.8975  |
| Box Precision  | 0.9295  |

These results demonstrate strong object detection performance, especially in terms of bounding box accuracy and classification precision, supporting real-time deployment in dynamic driving environments.

## Performance Metrics

- **mAP (mean Average Precision):** Measures detection accuracy  
- **IoU (Intersection over Union):** Assesses bounding box precision  
- **FPS (Frames Per Second):** Gauges real-time capability  
- **Latency:** Time per frame (target ≤100ms)  

## Non-Functional Highlights

- **Reliability:** 99.999% uptime, error tolerance, fail-safe modes  
- **Security:** Data encryption, role-based access, cyber threat detection  
- **Scalability:** Modular components support future expansion  
- **Compliance:** Designed with ISO 26262 and ASIL guidelines in mind  
- **Portability:** Runs on cloud, edge devices, or local simulation setups  
- **Energy Efficiency:** Optimized for low-power embedded systems  

## Future Work

- Support for additional sensor fusion (LiDAR, Radar)
- Fine-tuning YOLOv11 for night and adverse weather conditions
- Expanding MLOps capabilities with model drift detection and alerting
- Vehicle simulation testing using CARLA or similar environments

## Get Started

To run locally:
```bash
git clone https://github.com/your-repo/realtime-object-detection.git
cd realtime-object-detection
pip install -r requirements.txt
python app.py
