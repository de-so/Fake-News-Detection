import sklearn
import joblib
import cleaningInput as cd


def predict(user_data):
    input_data = cd.clear_input(user_data)
    text_vector = joblib.load('models/vectorizer.joblib')
    model = joblib.load('models/trained_model.joblib')

    v_text = text_vector.transform([input_data])
    prediction = model.predict(v_text)
    return prediction[0]
