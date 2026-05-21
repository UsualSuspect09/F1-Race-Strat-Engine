import joblib
import pandas as pd

model = joblib.load("models/ridge_model.pkl")

def predict_stint_length(gp, compound, stint):
    gp_stint = f"{gp}_S{stint}"
    compound_stint = f"{compound}_S{stint}"
    
    input_data = pd.DataFrame({
        'GP': [gp],
        'Compound': [compound],
        'Stint': [stint],
        'GP_Stint': [gp_stint],
        'Compound_Stint': [compound_stint]
    })
    
    predicted_length = model.predict(input_data)[0]
    return (predicted_length)