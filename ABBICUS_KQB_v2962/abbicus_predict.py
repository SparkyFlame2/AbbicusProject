
# abbicus_predict.py

drift_value = None
predicted_answer = None

def store_drift(val):
    global drift_value
    drift_value = val

def get_drift():
    return drift_value

def set_prediction(value):
    global predicted_answer
    predicted_answer = value

def get_prediction():
    return predicted_answer

def clear_prediction():
    global predicted_answer
    predicted_answer = None
