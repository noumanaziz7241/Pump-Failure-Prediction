import pandas as pd
import joblib
import warnings

# Filter warnings
warnings.filterwarnings('ignore')
model_filename = 'random_forest_model.pkl'
scaler_filename = 'scaler.pkl'

# Example unknown data point (you need to replace this with your actual unknown data)
vibration_level = float(input("Please enter the value of vibration level for prediction: "))
temperature_C = float(input("Please enter the value of temperature in C for prediction: "))
pressure_PSI = float(input("Please enter the value of pressure PSI for prediction: "))
flow_rate_m3h = float(input("Please enter the value of flow rate m3h for prediction: "))

new_data = pd.DataFrame({
    'vibration_level': [vibration_level],
    'temperature_C': [temperature_C],
    'pressure_PSI': [pressure_PSI],
    'flow_rate_m3h': [flow_rate_m3h]
})

# Load the model from the file
loaded_model = joblib.load(model_filename)
loaded_scaler = joblib.load(scaler_filename)

# Load the scaler and model from the files
loaded_scaler = joblib.load(scaler_filename)
loaded_model = joblib.load(model_filename)

# Normalize the new data using the same scaler
new_data_scaled = loaded_scaler.transform(new_data)

# Make predictions
prediction = loaded_model.predict(new_data_scaled)

output = {0: "No Failure",
          1: "Failure"}
print(f"Given Data points indicates: {output.get(prediction[0])} in pump")  # 0 or 1
