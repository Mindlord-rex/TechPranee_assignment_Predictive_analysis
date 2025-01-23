# Predictive Analysis API for Manufacturing Operations

## Overview
A RESTful API built with FastAPI to predict machine downtime using manufacturing data. Supports data upload, model training, and predictions.

## Table of Contents
- [Features](#features)
- [Setup](#setup)
- [API Endpoints](#api-endpoints)
- [Dataset](#dataset)
- [Model Details](#model-details)

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
