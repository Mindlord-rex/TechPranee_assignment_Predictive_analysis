from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score
import joblib

def train_save_model(data):
    
    required_columns = ['Temperature', 'Run_Time','Downtime_Flag']
    if not all(col in data.columns for col in required_columns):
        missing_columns = [col for col in required_columns if col not in data.columns]
        raise ValueError(f"Missing required columns in dataset: {missing_columns}")
    
    
    X = data[['Temperature','Run_Time']]
    Y = data['Downtime_Flag']
    
    X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.2, random_state=42)
    
    model = LogisticRegression()
    model.fit(X_train, Y_train)
    
    Y_pred = model.predict(X_test)
    metrics = {
        "accuracy": accuracy_score(Y_test,Y_pred),
        "f1_score": f1_score(Y_test,Y_pred)
    }
    
    joblib.dump(model, 'trained_model.pkl')
    
    return metrics

def load_model():
    
    try:
        return joblib.load('trained_model.pkl')
    except FileNotFoundError:
        return None
    