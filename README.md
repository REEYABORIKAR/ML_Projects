---
title: Student Exam Performance Predictor
emoji: 📊
colorFrom: blue
colorTo: green
sdk: gradio
sdk_version: "4.44.0"
app_file: app.py
pinned: false
---


## END to END Machine Learning Project
Based on the structure and content of your repository, here is a comprehensive `README.md` file designed for your end-to-end Machine Learning project.

# Student Performance Prediction (End-to-End ML Project)

## Project Overview

This project is an end-to-end machine learning application designed to predict student performance based on various demographic and academic factors. It includes a complete pipeline from data ingestion and transformation to model training and deployment via a Flask web application.

## Features

* **Data Ingestion:** Automatically splits raw data into training and testing sets.
* **Data Transformation:** Handles categorical encoding and numerical scaling using `StandardScaler`.
* **Model Training:** Utilizes multiple algorithms, including **CatBoost**, to find the best performing model.
* **Prediction Pipeline:** A dedicated pipeline to process new user input and generate predictions.
* **Web Interface:** A Flask-based web application for users to input data and view results in real-time.

## Dataset

The project uses student performance data (e.g., `stud.csv`) containing the following features:

* **Demographics:** Gender, Race/Ethnicity.
* **Background:** Parental level of education, Lunch type.
* **Academic Preparation:** Test preparation course completion.
* **Scores:** Reading and writing scores (used to predict the target performance metric).

## Project Structure

```text
├── artifacts/              # Contains saved model, preprocessor, and data CSVs
├── notebook/               # Jupyter notebooks for EDA and Model Training
├── src/                    # Source code for the ML pipeline
│   ├── components/         # Data ingestion, transformation, and trainer modules
│   ├── pipeline/           # Training and prediction pipelines
│   ├── logger.py           # Logging configuration
│   └── exception.py        # Custom exception handling
├── templates/              # HTML templates for the web app
├── app.py                  # Flask application entry point
├── setup.py                # Project packaging and metadata
└── requirements.txt        # Project dependencies

```


## Installation & Setup

1. **Clone the repository:**
```bash
git clone <repository-url>
cd ML_Projects

```

2. **Create a virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

```

3. **Install dependencies:**
The `setup.py` file is configured to install requirements automatically from `requirements.txt`.
```bash
pip install -r requirements.txt

```


## Usage

### Running the Web Application

To start the Flask server, run:

```bash
python app.py

```

Open your browser and navigate to `http://127.0.0.1:5000/`. You can use the `/predictdata` route to input student details and get a performance prediction.

### Training the Model

If you wish to re-train the model, you can execute the data ingestion component:

```bash
python src/components/data_ingestion.py

```

## Technologies Used

* **Python**
* **Pandas & NumPy** (Data manipulation)
* **Scikit-Learn** (Preprocessing and Modeling)
* **CatBoost** (Gradient Boosting)
* **Flask** (Web Framework)
* **Matplotlib & Seaborn** (Visualization)

## Author

**Reeya**
Email: reeyaborikar02@gmail.com