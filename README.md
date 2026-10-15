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

## Execution Process

Follow these steps in order to run the project successfully.

### 1. Prerequisites

Make sure you have Python 3.9 or later installed on your machine.

You should also have access to:

- Git
- A terminal or PowerShell window
- Internet access for installing Python packages if needed

### 2. Clone the Repository

```bash
git clone <repository-url>
cd Human-Action
```

If you are working inside the project folder already, skip this step.

### 3. Create a Virtual Environment

It is recommended to create an isolated environment before installing dependencies.

#### Windows (PowerShell)

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

#### Linux or macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies

Install the required libraries:

```bash
pip install streamlit pandas scikit-learn
```

If the environment is missing other packages, you can also install them as needed, but the app is designed around these three libraries.

### 5. Verify the Project Structure

Before running the app, confirm that the required files are present:

```text
Human-Action/
├── app.py
├── model.pkl
├── README.md
├── data/
│   ├── mHealth_subject1.csv
│   └── ...
├── streamlit/
│   └── config.toml
└── Human Action Detection (1).ipynb
```

The app loads the trained model from `model.pkl` and reads sample data from the `data/` folder.

### 6. Start the Streamlit Application

From the project root, run:

```bash
streamlit run app.py
```

This starts the local Streamlit server. The terminal will display a URL such as:

```text
Local URL: http://localhost:8501
```

Open that address in your browser to view the app.

### 7. App Workflow

The application has three main tabs:

#### Home

- Displays the project title and summary
- Shows basic information such as model type, activity count, and project purpose
- Serves as the landing page

#### Prediction

This is the main functionality of the application.

1. Click `Load Sample Data` to automatically populate the sensor values using a sample row from the dataset.
2. Alternatively, paste your own sensor readings manually in the text box.
3. Enter exactly 23 numeric values separated by commas.
4. Click `Predict Activity`.
5. The app sends the values to the trained model and displays the predicted class.

Example format:

```text
-9.8184,0.009971,0.29563,0.0041863,0.0041863,2.1849,-9.6967,0.63077,0.1039,-0.84053,-0.68762,-0.37,-0.36327,0.29963,-8.6499,-4.5781,0.18776,-0.44902,-1.0103,0.034483,-2.35,-1.6102,-0.030899
```

The app expects the input to match the dataset feature order used in training.

#### About

- Explains the objective of the project
- Summarizes dataset details
- Describes the model and supported classes

### 8. Model Execution Flow in the App

When the app starts, it does the following:

```python
model = pickle.load(open("model.pkl", "rb"))
```

Then during prediction:

1. Reads the sensor values from the text area
2. Converts the values into floats
3. Checks whether there are exactly 23 inputs
4. Sends the list to the model using `model.predict([values])`
5. Converts the result into a readable activity name
6. Displays the predicted activity on the dashboard

### 9. How the Data Is Used

The project uses sensor readings from the mHealth dataset, including:

- acceleration values from the chest sensor
- ECG signals
- acceleration, gyroscope, and magnetometer readings from the left ankle
- acceleration, gyroscope, and magnetometer readings from the right lower arm

Each input row contains 23 sensor features plus a label column. The model learns from these values to classify the activity performed by the subject.

### 10. Common Issues and Fixes

#### Error: model.pkl not found

Make sure you run the project from the root folder where `model.pkl` is located.

#### Error: expected 23 values but got X

The input box must contain exactly 23 comma-separated numeric values. Remove extra values or add missing values before predicting.

#### Streamlit does not start

Check whether dependencies are installed in the active virtual environment:

```bash
pip list
```

If needed, reinstall them:

```bash
pip install streamlit pandas scikit-learn
```

#### Browser does not open automatically

Open the following URL manually:

```text
http://localhost:8501
```

### 11. Best Practice for Local Development

- Use a virtual environment for dependency isolation
- Run the app from the project root
- Keep `model.pkl` and `data/` in the same folder structure as expected by the code
- Re-train or replace the model only after confirming the data distribution remains consistent

## Notes

- The project is designed for local experimentation and demonstration.
- It is ideal for learning how an ML classification pipeline can be exposed through a Streamlit interface.
- For production, it is recommended to add preprocessing validation, model monitoring, and better deployment controls.

## License

This project is intended for educational and research purposes.
