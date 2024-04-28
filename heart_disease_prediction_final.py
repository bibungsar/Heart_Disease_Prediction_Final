# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 14:07:37 2024

@author: bibun
"""

import numpy as np
import pickle
import streamlit as st



heart_disease_model = pickle.load(open('heart_disease_model_final.sav', 'rb'))


st.title('Heart Disease Prediction using ML')

col1, col2, col3 = st.columns(3)
  
with col1: 
    Age = st.text_input("Age")

with col2:
    Gender = st.text_input("Gender")
    
with col3:  
    Chest_Pain = st.text_input("Chest Pain Type")
    
with col1:
    Blood_Pressure = st.text_input("Blood Pressure")
with col2:
    Cholestoral = st.text_input("Cholestoral")

with col3:
    Blood_Sugar = st.text_input("Blood Sugar")

with col1:
    ECG = st.text_input("ECG")

with col2:
    Heart_Rate = st.text_input("Maximum Heart Rate ")


    

# Convert input data to numeric values
input_data = np.array([float(Age) if Age else 0,    # Use 0 as default if age is empty
                       float(Gender) if Gender else 0,    # Use 0 as default if sex is empty
                       float(Chest_Pain) if Chest_Pain else 0,      # Use 0 as default if cp is empty
                       float(Blood_Pressure) if Blood_Pressure else 0,  # Use 0 as default if trtbps is empty
                       float(Cholestoral) if Cholestoral else 0,
                       float(Blood_Sugar) if Blood_Sugar else 0,
                       float(ECG) if ECG else 0,
                       float( Heart_Rate) if Heart_Rate else 0,
                       ])

heart_disease_diagnosis = ''

if st.button("Heart Disease Test Result"):
    heart_disease_prediction = heart_disease_model.predict(input_data.reshape(1, -1))
    
    
    if(heart_disease_prediction[0] == 1):
        heart_disease_diagnosis = 'The Person has heart disease'
    else:
        heart_disease_diagnosis = 'The Person doesnot have heart disease'
    
st.success(heart_disease_diagnosis)