<<<<<<< HEAD
# fdia
=======
# FDIA Detection System

A real-time False Data Injection Attack (FDIA) detection system for IoT telemetry data, built with Streamlit and machine learning.

## Overview

This application provides a user-friendly interface to detect potential False Data Injection Attacks in IoT telemetry data. It uses a pre-trained Random Forest model to analyze various system metrics and identify anomalies that might indicate malicious data manipulation.

## Features

- Real-time FDIA detection
- Interactive user interface
- Analysis of multiple system metrics:
  - CPU Usage
  - Memory Usage
  - Disk Usage
  - Network In/Out traffic
- Instant prediction results
- Visual feedback for normal/anomalous states

## Prerequisites

- Python 3.x
- Required Python packages:
  - streamlit
  - numpy
  - joblib
  - scikit-learn

## Installation

1. Clone this repository
2. Install the required packages:
   ```bash
   pip install streamlit numpy joblib scikit-learn
   ```

## Usage

1. Run the application:
   ```bash
   streamlit run fdia_app.py
   ```
2. Open your web browser and navigate to the provided local URL (typically http://localhost:8501)
3. Adjust the sliders and input fields to simulate different system states
4. Click "Run Prediction" to analyze the data
5. View the results indicating whether the system is operating normally or if a potential attack is detected

## Project Structure

- `fdia_app.py` - Main Streamlit application
- `fdia_rf_model.pkl` - Pre-trained Random Forest model
- `simulated_fdia_dataset.csv` - Sample dataset for training/testing

## How It Works

The application uses a machine learning model trained on simulated IoT telemetry data to detect anomalies that might indicate False Data Injection Attacks. The model analyzes various system metrics and provides real-time predictions about the system's state.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details. 
>>>>>>> 57b45c1 (Initial commit: FDIA Detection System)
