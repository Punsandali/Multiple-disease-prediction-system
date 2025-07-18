# -*- coding: utf-8 -*-
"""
Created on Thu Jul 17 21:26:27 2025

@author: ASUS
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#loading the saved models
try:
    diabetic_model=pickle.load(open('C:/Users/ASUS/Desktop/Multiple Disease Prediction System/saved_models/diabetes_model.sav','rb'))
    scaler = pickle.load(open('C:/Users/ASUS/Desktop/Multiple Disease Prediction System/saved_models/scaler.sav','rb'))

   

except Exception as e:
    st.error(f"Failed to load diabetic model: {e}")


heart_disease_model=pickle.load(open('C:/Users/ASUS/Desktop/Multiple Disease Prediction System/saved_models/heart_disease_model.sav','rb'))


parkinson_disease_model=pickle.load(open('C:/Users/ASUS/Desktop/Multiple Disease Prediction System/saved_models/parkinsons_model.sav','rb'))
scaler2 = pickle.load(open('C:/Users/ASUS/Desktop/Multiple Disease Prediction System/saved_models/scaler2.sav','rb'))
#sidebar for the navigate
with st.sidebar:
    selected=option_menu("Multiple Disease Prediction", 
                         
                        ['Diabetics Prediction','Heart Disease Prediction','Parkinson Disease Prediction'],icons=['activity','heart','person'],default_index=0 )
    

    
    #diabetic Prediction page
if (selected == 'Diabetics Prediction'):
    st.title('Diabetics Prediction Using ML')
    
    col1, col2, col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure Value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness Value')
    with col2:
        Insulin = st.text_input('Insulin Level')
    with col3:
        BMI = st.text_input('BMI Value')
    with col1:
        DiabetesPredigreeFunction = st.text_input('Diabetes Pedigree Function Value')
    with col2:
        Age = st.text_input('Age')

    diab_diagnosis = ''

    if st.button('Diabetic Test Result'):
        try:
            input_data = [float(Pregnancies), float(Glucose), float(BloodPressure), float(SkinThickness),
                          float(Insulin), float(BMI), float(DiabetesPredigreeFunction), float(Age)]
            
            input_scaled = scaler.transform([input_data])
            diab_prediction = diabetic_model.predict(input_scaled)
            st.write("Raw prediction output:", diab_prediction)  # print raw output

            if diab_prediction[0] == 1:
                diab_diagnosis = 'The Person is Diabetic'
            else:
                diab_diagnosis = 'The Person is not Diabetic'
        except ValueError:
            diab_diagnosis = 'Please enter valid numeric values in all fields.'

        st.success(diab_diagnosis)

    
if(selected=='Heart Disease Prediction'):
    st.title('Heart Disease Prediction using ML')
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.text_input('Age')
    with col2:
        sex = st.text_input('Sex')
    with col3:
        cp = st.text_input('Chest pain Type')
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
    with col2:
        chol = st.text_input('Serum Cholestrol in mg/dl')
    with col3:
        fbs = st.text_input('Fasting Blood Sugar>120 mg/dl')
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
    with col2:
        maxRate = st.text_input('Maximum Heart rate achieved')
    with col3:
        eia=st.text_input('Exercise Included Angina')
    with col1:
        oldpeak=st.text_input('ST depression induced by exercise relative to rest')
    with col2:
        slope=st.text_input('The slope of the peak exercise ST segment')
    with col3:
        ca=st.text_input('Number of major vessels colored by floursopy')
    with col1:
        thal=st.text_input('Thal')

    heart_diagnosis = ''

    if st.button('Heart Disease Test Result'):
        try:
            input_data = [float(age), float(sex), float(cp), float(trestbps),
                          float(chol), float(fbs), float(restecg), float(maxRate),float(eia),float(oldpeak),float(slope),float(ca),float(thal)]
            
           
            heart_prediction = heart_disease_model.predict([input_data])
            st.write("Raw prediction output:", heart_prediction)  # print raw output

            if heart_prediction[0] == 1:
                heart_diagnosis = 'The Person has Heart disease'
            else:
                heart_diagnosis = 'The Person has not Heart disease'
        except ValueError:
            heart_diagnosis = 'Please enter valid numeric values in all fields.'

        st.success(heart_diagnosis)
    
    
if(selected=='Parkinson Disease Prediction'):
    st.title('Parkinson Disease Prediction using ML')
    col1, col2, col3 = st.columns(3)
    with col1:
        mdvpfo = st.text_input('MDVP:Fo')
    with col2:
        mdvpfh = st.text_input('MDVP:Fhi')
    with col3:
        mdvpfl = st.text_input('MDVP:Flo')
    with col1:
        mdvpji = st.text_input('MDVP:Jitter')
    with col2:
        mdvpjiab = st.text_input('MDVP:Jitter(abs)')
    with col3:
        mdvprap= st.text_input('MDVP:RAP')
    with col1:
        mdvpppq = st.text_input('MDVP:PPQ')
    with col2:
        jitterddp = st.text_input('Jitter:DDP')
    with col3:
         mdvpshim = st.text_input('MDVP:Shimmer')
    with col1:
         mdvpshimabs = st.text_input('MDVP:Shimmer(db)')
    with col2:
         shimmerapq=st.text_input('Shimmer:APQ3')
    with col3:
          shimmerAP= st.text_input('Shimmer:APQ5')
    with col1:
         mdvpapq= st.text_input('MDVP:APQ')
    with col2:
         shimmerdda = st.text_input('Shimmer:DDA')
    with col3:
         nhr = st.text_input('NHR')
    with col1:
        hnr= st.text_input('HNR')
    with col2:
        rpde = st.text_input('RPDE')
    with col3:
        dfa = st.text_input('DFA')
    with col1:
         spread1 = st.text_input('Spread1')
    with col2:
         spread2 = st.text_input('Spread2')
    with col3:
          d2= st.text_input('D2')
    with col1:
         ppe= st.text_input('PPE')
  

    parkinson_diagnosis = ''

    if st.button('ParkinsonTest Result'):
        try:
            input_data = [float(mdvpfo), float(mdvpfh), float(mdvpfl), float(mdvpji),
                          float(mdvpjiab), float(mdvprap), float(mdvpppq), float(jitterddp),float(mdvpshim), float(mdvpshimabs), float(shimmerapq), float(shimmerAP),
                                        float(mdvpapq), float(shimmerdda), float(nhr), float(hnr),float(rpde), float(dfa), float(spread1), float(spread2),
                                                      float(d2), float(ppe)]
            
            input_scaled = scaler2.transform([input_data])
            parkinson_prediction = parkinson_disease_model.predict(input_scaled)
            st.write("Raw prediction output:", parkinson_prediction)  # print raw output

            if parkinson_prediction[0] == 1:
                parkinson_diagnosis = 'The Person has Parkinson'
            else:
                parkinson_diagnosis = 'The Person has not Parkinson '
        except ValueError:
            parkinson_diagnosis = 'Please enter valid numeric values in all fields.'

        st.success(parkinson_diagnosis)
    
    
    

    
