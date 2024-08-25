# app/main.py
import streamlit as st
from app.utils import load_data, process_data, create_visualizations

st.title("Multi-Dataset Data Insights Dashboard")

# Sidebar for dataset selection
st.sidebar.header("Select Dataset")
dataset_choice = st.sidebar.selectbox(
    "Choose a dataset:",
    ("Dataset 1", "Dataset 2", "Dataset 3")
)

# Load the selected dataset
data = load_data(dataset_choice)

# Interactive Widgets
st.sidebar.header("Customize your view")
slider_value = st.sidebar.slider("Select a range", 0, 100, (25, 75))

# Process and filter data based on user input
filtered_data = process_data(data, slider_value)

# Create visualizations
create_visualizations(filtered_data, dataset_choice)
