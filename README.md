# Human Action Recognition

A machine learning project for recognizing human activities from wearable sensor data. This application uses a trained classifier to predict activity labels such as walking, running, cycling, standing, and more based on 23 sensor features collected from the mHealth dataset.

## Overview

This project combines:

- A Streamlit web application for interactive prediction
- Sensor-based human activity data from the mHealth dataset
- A trained machine learning model saved as `model.pkl`
- A simple interface for loading sample data or entering raw sensor values

The app predicts one of 12 activity classes from input sensor readings collected from chest, left ankle, and right lower arm sensors.

## Features

- Predict activity from 23 comma-separated sensor values
- Load a sample sensor record from the dataset with one click
- View the predicted activity label in a clean dashboard
- Support for 12 human activities
- Lightweight web app built with Streamlit

## Supported Activities

The model classifies the following activities:

1. Standing still
2. Sitting and relaxing
3. Lying down
4. Walking
5. Climbing stairs
6. Waist bends forward
7. Frontal elevation of arms
8. Knees bending (crouching)
9. Cycling
10. Jogging
11. Running
12. Jump front and back

## Dataset

The project uses the mHealth dataset, which contains wearable sensor readings across multiple body locations. The input features include:

- Chest acceleration and ECG signals
- Left-ankle acceleration, gyro, and magnetometer readings
- Right-lower-arm acceleration, gyro, and magnetometer readings

Each row contains 23 sensor measurements plus a `Label` column.

## Project Structure

```text
Human-Action/
├── app.py                  # Streamlit application
├── model.pkl               # Trained activity recognition model
├── README.md               # Project documentation
├── data/
│   ├── mHealth_subject1.csv
│   ├── mHealth_subject2.csv
│   └── ...
├── streamlit/
│   └── config.toml
├── Human Action Detection (1).ipynb
└── .git/
```

## Setup

1. Clone the repository.
2. Create a virtual environment (optional but recommended).
3. Install the required dependencies:

```bash
pip install streamlit pandas scikit-learn
```

## Run the App

From the project root, start the Streamlit app:

```bash
streamlit run app.py
```

Then open the local URL shown in the terminal, usually:

```text
http://localhost:8501
```

## How to Use

### Prediction tab

- Click `Load Sample Data` to populate the sensor values from a sample row
- Or manually enter 23 comma-separated numeric values
- Click `Predict Activity`
- The app will display the predicted activity class

### Home tab

- Shows a project summary and model overview

### About tab

- Describes the objective, dataset, model, and supported activities

## Model Information

The trained classifier is loaded with:

```python
model = pickle.load(open("model.pkl", "rb"))
```

The app expects 23 numeric feature values for prediction and maps the output label to a human-readable activity name.

## Notes

- The application is designed for quick demonstrations and local experimentation.
- For production use, it is recommended to add validation, preprocessing, and retraining pipelines.
- The dataset and model are stored in the project root and data folder for easy offline use.

## License

This project is intended for educational and research purposes.
