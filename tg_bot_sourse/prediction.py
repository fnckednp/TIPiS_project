import joblib
import numpy as np
from sklearn.preprocessing import StandardScaler


def check_data(arr) -> np.ndarray:
    model = joblib.load('input/diabetes_prediction_model.joblib')

    scaler = StandardScaler()
    scaler.fit(arr)
    normalized_arr = scaler.transform(arr)
    output = model.predict(normalized_arr)

    return output
