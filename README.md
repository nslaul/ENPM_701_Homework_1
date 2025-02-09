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
├── pitch_analysis_2pt.png
├── pitch_analysis_4pt.png
├── pitch_analysis_8pt.png
├── pitch_analysis_16pt.png
├── pitch_analysis_64pt.png
├── pitch_analysis_128pt.png

```
###Installation And Dependancies
##Requirements
Ensure you have Python 3.x installed with the following libraries:

- NumPy (for numerical operations)
- Matplotlib (for plotting)
##Install Dependencies
If not already installed, run:
### Install Dependencies
If not already installed, run:
```bash
pip install numpy matplotlib
```

---

## Running the Code
### Clone the Repository
```bash
git clone https://github.com/nslaul/ENPM_701_Homework_1.git
cd ENPM_701_Homework_1
```

### Execute the Script
Run the following command to generate and save the plots:
```bash
python solution.py
```

This will:
- Read and process **`imudata.txt`**.
- Generate **six plots** (PNG & PDF) with moving averages.
- Display each figure one by one.

---

## Output Files
After running the script, the following files will be created:
- **Six PNG plots** (`pitch_analysis_2pt.png`, `pitch_analysis_4pt.png`, etc.)
- **Six PDF plots** (same as PNG but in PDF format)

These files will be saved in the `plots/` directory.

---

## LaTeX Report
The **LaTeX report (`report.tex`)** contains:
- Code explanations
- Figures of generated plots
- Moving average analysis
- Conclusion on data smoothing & noise reduction

### Compiling the Report
To generate `report.pdf` from the LaTeX source:
```bash
pdflatex report.tex
```
Alternatively, open and compile `report.tex` in **Overleaf**.

---

## References
- **ADXL327 Datasheet**: [Analog Devices Documentation](https://www.analog.com/media/en/technical-documentation/data-sheets/adxl327.pdf)
- **Python Libraries Used**: NumPy, Matplotlib
