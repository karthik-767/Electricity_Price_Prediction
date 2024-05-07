import streamlit as st
import numpy as np 
import pickle
import warnings

# Suppress warnings
warnings.filterwarnings("ignore")

# Load model
with open('elec_state.sav_1.sav', 'rb') as f:
    model = pickle.load(f)

# Set title and page layout
st.title("Electricity Price Change Prediction App")
st.markdown("---")
st.header("Enter Standardized Input Values")

# Input fields for standardized values with styling
with st.form("my_form"):
    date = st.text_input("Date", help="Enter the date")  # Example of text input with help text
    day = st.text_input("Day", help="Enter the day")
    period = st.text_input("Period", help="Enter the period")
    nsw_price = st.text_input("NSW Price", help="Enter the NSW price")
    nsw_demand = st.text_input("NSW Demand", help="Enter the NSW demand")
    vic_price = st.text_input("VIC Price", help="Enter the VIC price")
    vic_demand = st.text_input("VIC Demand", help="Enter the VIC demand")
    transfer = st.text_input("Transfer", help="Enter the transfer")

    # Prediction button
    predict_button = st.form_submit_button("Predict")

# Make prediction and display result
if predict_button:
    try:
        a = float(date)
        b = float(day)
        c = float(period)
        d = float(nsw_price)
        e = float(nsw_demand)
        f = float(vic_price)
        g = float(vic_demand)
        h = float(transfer)
        
        pred = model.predict(np.array([a,b,c,d,e,f,g,h]).reshape(1,-1))[0]
        if pred == 0:
            st.success("The price will go down.")
        else:
            st.success("The price will go up.")
    except ValueError:
        st.error("Please enter valid numeric values in all input fields.")

# Footer with background color and padding
st.markdown("---")
st.markdown(
    """<div style='background-color: #f0f0f0; padding: 10px; border-radius: 5px;'>
       Made by Karthik Gadam
       </div>
    """, unsafe_allow_html=True
)
