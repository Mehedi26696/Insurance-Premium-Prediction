import pandas as pd
import streamlit as st
import pickle

import warnings
warnings.filterwarnings('ignore')

# Custom CSS
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .stButton button {
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 12px;
    }
    .stButton button:hover {
        background-color: #45a049;
    }
    .stTitle {
        color: #4CAF50;
        font-size: 36px;
        font-weight: bold;
    }
    .center-button {
        display: flex;
        justify-content: center;
    }
    .result {
        background-color: rgba(255, 255, 255, 0.5);
        padding: 10px;
        border-radius: 5px;
        font-size: 20px;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

st.title('Insurance Premium Prediction')

id = st.number_input('ID', min_value=1, max_value=1000000, value=1)
age = st.number_input('Age', min_value=1, max_value=100, value=25)
gender = st.selectbox('Gender', ['Female', 'Male'])

if gender == 'Female':
    gender = 0
else:
    gender = 1

annual_income = st.number_input('Annual Income', min_value=0, max_value=1000000, value=50000)
marital_status = st.selectbox('Marital Status', ['Single', 'Married', 'Divorced'])

if marital_status == 'Single':
    marital_status = 2
elif marital_status == 'Married':
    marital_status = 1
else:
    marital_status = 0

number_of_dependents = st.number_input('Number of Dependents', min_value=0, max_value=10, value=0)
education_level = st.selectbox('Education Level', ['High School', 'Bachelors', 'Masters', 'PhD'])

if education_level == 'High School':
    education_level = 1
elif education_level == 'Bachelors':
    education_level = 0
elif education_level == 'Masters':
    education_level = 2
else:
    education_level = 3

occupation = st.selectbox('Occupation', ['Employed', 'Unemployed', 'Self-Employed'])

if occupation == 'Employed':
    occupation = 3
elif occupation == 'Unemployed':
    occupation = 2
else:
    occupation = 1

health_score = st.number_input('Health Score', min_value=0, max_value=100, value=50)
location = st.selectbox('Location', ['Urban', 'Suburban', 'Rural'])

if location == 'Urban':
    location = 2
elif location == 'Suburban':
    location = 1
else:
    location = 0

policy_type = st.selectbox('Policy Type', ['Premium', 'Comprehensive', 'Basic'])

if policy_type == 'Premium':
    policy_type = 2
elif policy_type == 'Comprehensive':
    policy_type = 1
else:
    policy_type = 0

previous_claims = st.number_input('Previous Claims', min_value=0, max_value=100, value=0)
vehicle_age = st.number_input('Vehicle Age', min_value=0, max_value=50, value=5)
credit_score = st.number_input('Credit Score', min_value=0, max_value=850, value=700)
insurance_duration = st.number_input('Insurance Duration (years)', min_value=1, max_value=50, value=1)
policy_start_date = st.date_input('Policy Start Date')
customer_feedback = st.selectbox('Customer Feedback', ['Good', 'Average', 'Poor'])

if customer_feedback == 'Good':
    customer_feedback = 1
elif customer_feedback == 'Average':
    customer_feedback = 0
else:
    customer_feedback = 2

smoking_status = st.selectbox('Smoking Status', ['Non-Smoker', 'Smoker'])

if smoking_status == 'Non-Smoker':
    smoking_status = 0
else:
    smoking_status = 1

exercise_frequency = st.selectbox('Exercise Frequency', ['Daily', 'Weekly', 'Monthly', 'Rarely'])

if exercise_frequency == 'Daily':
    exercise_frequency = 0
elif exercise_frequency == 'Weekly':
    exercise_frequency = 3
elif exercise_frequency == 'Monthly':
    exercise_frequency = 1
else:
    exercise_frequency = 2

property_type = st.selectbox('Property Type', ['House', 'Apartment', 'Condo'])

if property_type == 'House':
    property_type = 2
elif property_type == 'Apartment':
    property_type = 0
elif property_type == 'Condo':
    property_type = 1

# model load
model = pickle.load(open('model.pkl', 'rb'))

# prediction
if st.button('Predict', key='predict_button'):
    data = [[age, gender, annual_income, marital_status, number_of_dependents, education_level, occupation, health_score, location, policy_type, previous_claims, vehicle_age, credit_score, insurance_duration, customer_feedback, smoking_status, exercise_frequency, property_type]]
    prediction = model.predict(data)
    st.markdown(f'<div class="result">The predicted insurance premium is: {prediction[0]:.2f}</div>', unsafe_allow_html=True)