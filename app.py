import streamlit as st 
import pickle as pkl

# Correct way to load the model
with open("model.pkl", "rb") as model_file:
    model = pkl.load(model_file)

def predict_diabetes(glucose, bloodpressure):
    glucose = float(glucose)
    bloodpressure = float(bloodpressure)

    # Make a prediction using the trained model
    prediction = model.predict([[glucose, bloodpressure]])
    return "Non-Diabetic" if prediction[0] == 0 else "Diabetic"
   
# Streamlit UI
st.title("Diabetes Prediction App")
st.write("This app predicts whether a person is diabetic or non-diabetic based on glucose and blood pressure levels.")

# Input fields for glucose and blood pressure levels
glucose_input = st.text_input("Enter glucose level:")
bloodpressure_input = st.text_input("Enter blood pressure level:")

if st.button("Predict"):
    if glucose_input and bloodpressure_input:
        try:
            prediction = predict_diabetes(glucose_input, bloodpressure_input)
            st.success(f"Prediction: {prediction}")
        except ValueError:
            st.error("Please enter valid numeric values for glucose and blood pressure.")
    else:
        st.warning("Please fill in both glucose and blood pressure levels.")
