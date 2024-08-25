# app/utils.py
import pandas as pd
import streamlit as st

def load_data(dataset_choice):
    if dataset_choice == "Benin":
        data = pd.read_csv("/home/kali/Desktop/git/Streamlit_Dashboard/data/benin-malanville.csv")
    elif dataset_choice == "Sierraleone":
        data = pd.read_csv("/home/kali/Desktop/git/Streamlit_Dashboard/data/sierraleone-bumbuna.csv")
    elif dataset_choice == "Togo":
        data = pd.read_csv("/home/kali/Desktop/git/Streamlit_Dashboard/data/togo-dapaong_qc.csv")
    else:
        st.error("Invalid dataset choice!")
        return None
    return data

def process_data(data, range_values):
    # Example: Filter data based on range values
    return data[(data['value'] >= range_values[0]) & (data['value'] <= range_values[1])]

def create_visualizations(data, dataset_choice):
    st.subheader(f"Visualizations for {dataset_choice}")
    
    # Example: Create a simple line chart
    st.line_chart(data)

    # Example: Add more custom visualizations based on dataset_choice
    if dataset_choice == "Dataset 1":
        st.bar_chart(data)
    elif dataset_choice == "Dataset 2":
        st.area_chart(data)
    elif dataset_choice == "Dataset 3":
        st.write("Additional visualizations can be added here.")
