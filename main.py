from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel
import pandas as pd
from model import train_save_model, load_model


app = FastAPI()
df = None

class PredictRequest(BaseModel):
    Temperature: float
    Run_Time: float
    

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    global df
    try:
        df = pd.read_csv(file.file)
        required_columns = ['Machine_ID', 'Temperature', 'Run_Time', 'Downtime_Flag']
        if not all(col in df.columns for col in required_columns):
            raise HTTPException(status_code=400, detail="Missing required columns")
        return {"message": "Data uploaded successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    
@app.post("/train")
async def train():
    global df
    if df is None:
        raise HTTPException(status_code=400, detail="Upload data first")
    
    try:
        metrics = train_save_model(df)
        return metrics
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    
@app.post("/predict")
async def predict(request: PredictRequest):
    model = load_model()
    if not model:
        raise HTTPException(status_code=400, detail="Trail model first")
    
    try:
        data = [[request.Temperature, request.Run_Time]]
        prediction = model.predict(data)[0]
        confidence = model.predict_proba(data)[0][1]
        return {
            "Downtime": "Yes" if prediction == 1 else "No",
            "Confidence": float(confidence)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
