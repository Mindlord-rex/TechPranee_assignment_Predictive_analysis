# Predictive Analysis API for Manufacturing Operations

## Overview
A RESTful API built with FastAPI to predict machine downtime using manufacturing data. Supports data upload, model training, and predictions.

## Table of Contents
- [Features](#features)
- [Setup](#setup)
- [API Endpoints](#api-endpoints)
- [Dataset](#dataset)
- [Model Details](#model-details)
- [Testing](#testing)

## Features
- Upload manufacturing data via CSV
- Train logistic regression model
- Predict downtime with confidence scores
- Persistent model storage using `joblib`

## Setup

### Prerequisites
- Python 3.8+
- pip

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/machine-downtime-api.git
   cd machine-downtime-api


2. Install dependencies:
   ```bash
      pip install -r requirements.txt
   ```
   
###Run the API:
    ```bash
   uvicorn main:app --reload
     ```

   Access the API at [http://localhost:8000](http://localhost:8000) 
   
## **API Endpoints** 

### 1. **Upload Data** (POST `/upload`)
   **Purpose:** Upload a CSV dataset for training. 
   **Request Example:** 
   ```bash   
   curl -X POST -F "file=@sample_data.csv" http://localhost:8000/upload
 ```
   **Success Response:**
   ```json
   { "message": "Data uploaded successfully" }
   ```
### 2. **Train Model** (POST `/train`) 
   **Purpose:** Train the model on the uploaded dataset. 
   **Request Example:** 
    ```bash
    curl -X POST http://localhost:8000/train
    ``` 
**Success Response (example):** 
```json
{ "accuracy": 0.92, "f1_score": 0.89 }
 ```
 ### 3. **Predict Downtime** (POST `/predict`) 
   **Purpose:** Predict machine downtime based on input features. 
   **Request Example:**
    ```bash
    curl -X POST -H "Content-Type: application/json" -d '{"Temperature": 80, "Run_time": 120}' http://localhost:8000/predict
    ```
   **Success Response:**
   ```json 
   { "Downtime": "Yes", "Confidence": 0.85 }
 ```

## **Dataset** 
### **Format** The dataset should be in CSV format with the following columns:
   - `Machine_ID`
   - `Temperature`
   - `Run_time`
   - `Downtime_Flag`

### **Dummy Code Generator** Generate a dummy dataset for given features with random values
```Code
import pandas as pd
import numpy as np

data = {
    'Machine_ID': [f'M{i}' for i in range(100)],
    'Temperature': np.random.randint(50, 100, 100),
    'Run_Time': np.random.randint(60, 300, 100),
    'Downtime_Flag': np.random.choice([0, 1], 100)
}
df = pd.DataFrame(data)
df.to_csv('sample_data.csv', index=False)
```

### **Sample Data** 
```csv 
Machine_ID,Temperature,Run_time,Downtime_Flag
M0,72,150,0 M1,85,200,1
```

## **Model Details** 
   - **Algorithm:** Logistic Regression (scikit-learn)
   - **Input Features:** `Temperature`, `Run_time`
   - **Output:** Binary classification (`0 = No Downtime`, `1 = Downtime`)
   - **Persistence:** The trained model is saved as `trained_model.pkl`.
     
## Testing 
1. **Upload Data**
   ```bash
   curl -X POST -F "file=@sample_data.csv" http://localhost:8000/upload
   ```
2. **Train Model**
   ```bash
    curl -X POST http://localhost:8000/train
    ```
3. **Get Prediction**
   ```bash
   curl -X POST -H "Content-Type: application/json" -d "{\"Temperature\": 75, \"Run_Time\": 180}" http://localhost:8000/predict
    ```
