import streamlit as st
import pickle
import numpy as np



# Load the saved model (replace 'your_model_path.pkl' with the path to your saved model)
model = pickle.load(open('Fertclass.pkl','rb'))


# Streamlit UI
st.title("Fertilizer Recommendation System")

# User input fields
temperature = st.slider("Temperature", min_value=0, max_value=100, value=25)
humidity = st.slider("Humidity", min_value=0, max_value=100, value=50)
moisture = st.slider("Moisture", min_value=0, max_value=100, value=60)
nitrogen = st.slider("Nitrogen", min_value=0, max_value=100, value=30)
phosphorous = st.slider("Phosphorous", min_value=0, max_value=100, value=40)
potassium = st.slider("Potassium", min_value=0, max_value=100, value=20)
soil_num = st.slider("Soil Number", min_value=1, max_value=5, step=1)
crop_num = st.slider("Crop Number", min_value=1, max_value=11, step=1)



# Button to trigger the prediction
if st.button("Get Fertilizer Recommendation"):
    # Prepare input data
    input_data = np.array([[temperature, humidity, moisture, nitrogen, phosphorous, potassium, soil_num, crop_num]])

    # Make prediction using the loaded model
    prediction = model.predict(input_data)

    # Display the result
    st.subheader("Recommended Fertilizer:")
    st.write(prediction[0])