# ENPM 701 - Homework 1 

## Overview
This repository contains **Homework 1 for ENPM 701**, focusing on **processing IMU data from an ADXL327 3-axis accelerometer**. The goal is to analyze and visualize **pitch angle data**, compute moving averages, and evaluate sensor calibration.

### **Tasks Completed**
- Load and parse **IMU sensor data** from `imudata.txt`
- Extract **pitch angle (5th column)** and visualize **raw data**
- Implement a **custom moving average function** (without built-in smoothing)
- Compute **moving averages** for different window sizes **(2, 4, 8, 16, 64, 128 points)**
- Overlay **moving averages** on the **raw data plots**
- Compute and display **mean and standard deviation** on plots
- Save **all plots in PNG and PDF formats** for analysis
- Write a **detailed LaTeX report** (`report.tex`) with explanations and figures

---

## Repository Structure
```plaintext
ENPM_701_Homework_1/
│── README.md               # Project documentation
│── ENPM701__Homework1_NeerajLaul_120518973.tex               # LaTeX report source file
│── ENPM701__Homework1_NeerajLaul_120518973.pdf               # Final compiled report with plots
│── imudata.txt              # IMU accelerometer data
│── solution.py              # Python script for data processing & plotting
│── plots/                   # Folder containing generated plots
│   ├── pitch_analysis_2pt.png
│   ├── pitch_analysis_4pt.png
│   ├── pitch_analysis_8pt.png
│   ├── pitch_analysis_16pt.png
│   ├── pitch_analysis_64pt.png
│   ├── pitch_analysis_128pt.png
│── pitch_analysis_2pt.pdf   # 2-pt Moving Average plot
│── pitch_analysis_4pt.pdf   # 4-pt Moving Average plot
│── pitch_analysis_8pt.pdf   # 8-pt Moving Average plot
│── pitch_analysis_16pt.pdf  # 16-pt Moving Average plot
│── pitch_analysis_64pt.pdf  # 64-pt Moving Average plot
│── pitch_analysis_128pt.pdf # 128-pt Moving Average plot
