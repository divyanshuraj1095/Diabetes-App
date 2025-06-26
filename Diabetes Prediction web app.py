# -*- coding: utf-8 -*-
"""
Created on Wed Jun 25 13:08:19 2025

@author: divya
"""

import numpy as np 
import pickle
import streamlit as st

loaded_model = pickle.load(open('E:/ML-DL projects/Deploying model/trained_model.sav', 'rb'))
loaded_scalar = pickle.load(open('E:/ML-DL projects/Deploying model/scalar.sav', 'rb'))
#creating a function for prediction


def diabetes_prediction(input_data):

    #changing to numpy array

    input_data_as_numpy = np.asarray(input_data)

    #reshape the array as we are predicting the one instance

    input_data_reshaped = input_data_as_numpy.reshape(1,-1)

    # standarize the input data
    std_data = loaded_scalar.transform(input_data_reshaped)
    # print(std_data)

    prediction = loaded_model.predict(std_data)#the output we get from the classifier is a list not an integer
    print(prediction)

    if(prediction[0] == 0): ## we are taking the first value of the list (prediction[0])
        return "The person is non-diabetic !"

    else :
        return "The person is diabetic !"
    
    
def main():
    
    #giving a title
    st.title('Diabetes Prediction Web App')
    
    #getting input data from the user
    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Glucose level')  
    BloodPressure = st.text_input('Blood Pressure value')
    SkinThickness = st.text_input('Skin Thickness Value')
    Insulin = st.text_input('Insulin Level')
    BMI = st.text_input('Bmi Value')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value')
    Age = st.text_input('Age of the person ')
    
    #code for prediction
    diagnosis = ''
    
    #creating a button for prediction
    
    if st.button('Diabetes test result'):
        diagnosis = diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
    
    st.success(diagnosis)
    
    
    
if __name__ == '__main__':
    main()
    
    