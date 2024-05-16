import pickle
import streamlit as st
import pandas as pd

# Page Config
st.set_page_config(
    page_title='Failure Classifier',
)

# Page Title
st.title('Maintenance - Failure Prediction')
st.image('./image.png')
st.write("\n\n")

# Page Description
st.markdown(
    """
    This app aims to assist in classifying failures, thereby reducing the time required to analyze machine problems. It enables the analysis of sensor data to classify failures swiftly and expedite the troubleshooting process.
    """
)

# Load the model
with open('./model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

#  Streamlit interface to input data
col1, col2 = st.columns(2)

with col1:
    air = st.number_input(label='Air Temperature [K]')
    process = st.number_input(label='Process Temperature [K]')
    rpm = st.number_input(label='Rotational Speed [rpm]')

with col2:
    torque = st.number_input(label='Torque [Nm]')
    tool_wear = st.number_input(label='Tool Wear [min]')
    type = st.selectbox(label='Type', options=['Low', 'Medium', 'High'])

# Function to predict the input
def prediction(air, process, rpm, torque, tool_wear, type):
    # Create a df with input data
    df_input = pd.DataFrame({
        'Air_temperature': [air],
        'Process_temperature': [process],
        'Rotational_speed': [rpm],
        'Torque': [torque],
        'Tool_wear': [tool_wear],
        'Type': [type]
    })

    prediction = model.predict(df_input)
    return prediction

# Button to predict
if st.button('Predict'):
    predict = prediction(air, process, rpm, torque, tool_wear, type)
    st.success(predict)