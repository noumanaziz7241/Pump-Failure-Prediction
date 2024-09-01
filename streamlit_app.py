import pandas as pd
import joblib
import warnings
import streamlit as st

# Filter warnings
warnings.filterwarnings('ignore')

# Load the model and scaler
model_filename = 'random_forest_model.pkl'
scaler_filename = 'scaler.pkl'
loaded_model = joblib.load(model_filename)
loaded_scaler = joblib.load(scaler_filename)

# Streamlit App
st.title("Pump Failure Prediction")

# Input fields for new data
vibration_level = st.number_input('Vibration Level', min_value=0.0, step=0.01)
temperature_C = st.number_input('Temperature (°C)', min_value=0.0, step=0.1)
pressure_PSI = st.number_input('Pressure (PSI)', min_value=0.0, step=0.1)
flow_rate_m3h = st.number_input('Flow Rate (m³/h)', min_value=0.0, step=0.1)

# Make prediction on button click
if st.button("Predict"):
    # Create a DataFrame for the input
    new_data = pd.DataFrame({
        'vibration_level': [vibration_level],
        'temperature_C': [temperature_C],
        'pressure_PSI': [pressure_PSI],
        'flow_rate_m3h': [flow_rate_m3h]
    })

    # Normalize the new data using the loaded scaler
    new_data_scaled = loaded_scaler.transform(new_data)

    # Make prediction
    prediction = loaded_model.predict(new_data_scaled)

    # Output dictionary
    output = {0: "No Failure", 1: "Failure"}

    # Display result
    st.write(f"Given data points indicate: **{output.get(prediction[0])}** in pump")

