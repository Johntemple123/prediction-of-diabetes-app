# -*- coding: utf-8 -*-
"""
Created on Wed Aug 4 03:32:31 2021

@author: John
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Aug 4 03:32:31 2021

@author: John
"""

import streamlit as st
from PIL import Image
image = Image.open('0diabeties001.jpg')
st.image(image, caption='Nothing beats a dose of good diet, physical activity, and nature')

import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 

from PIL import Image

#app=Flask(__name__)
#Swagger(app)

pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def predict_note_authentication(VATV_L2,VATV_L3,Total_VATV,Hepatic_PDFF,Pancreatic_PDFF,Pancreatic_head_PDFF,Pancreatic_body_PDFF,Pancreatic_tail_PDFF,Gender):
    
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: VATV_L2
        in: query
        type: number
        required: true
      - name: VATV_L3
        in: query
        type: number
        required: true
      - name: Total_VATV
        in: query
        type: number
        required: true
      - name: Hepatic_PDFF
        in: query
        type: number
        required: true
      - name: Pancreatic_PDFF
        in: query
        type: number
        required: true
      - name: Pancreatic_head_PDFF
        in: query
        type: number
        required: true
      - name: Pancreatic_body_PDFF
        in: query
        type: number
        required: true
      - name: Pancreatic_tail_PDFF
        in: query
        type: number
        required: true
      - name: Gender
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
   
    prediction=classifier.predict([[VATV_L2,VATV_L3,Total_VATV,Hepatic_PDFF,Pancreatic_PDFF,Pancreatic_head_PDFF,Pancreatic_body_PDFF,Pancreatic_tail_PDFF,Gender]])
    print(prediction)
    return prediction



def main():
    st.title("Prediction of type 2 Diabetes")
    html_temp = """
    <div style="background-color:#d24dff;padding:10px">
    <h2 style="color:white;text-align:center;">A world free of diabetes is not our dream, it’s our pledge </h2>
    </div>

    <div style="background-color:#d24dff;padding:10px">
    <h3 style="color:black;text-align:left;">Result: </h3>
    </div>    
    
    <div style="background-color:#d24dff;padding:5px">
    <h4 style="color:black;text-align:left;">2-Type 2 diabetes </h4>
    </div>  

    <div style="background-color:#d24dff;padding:5px">
    <h4 style="color:black;text-align:left;">1-Prediabetes </h4>
    </div>    

    <div style="background-color:#d24dff;padding:5px">
    <h5 style="color:black;text-align:left;">0-Normal Glucose Tolerance </h5>
    </div>    
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    VATV_L2 = st.text_input("VATV_L2","Type Here")
    VATV_L3 = st.text_input("VATV_L3","Type Here")
    Total_VATV = st.text_input("Total_VATV","Type Here")
    Hepatic_PDFF = st.text_input("Hepatic_PDFF","Type Here")
    Pancreatic_PDFF = st.text_input("Pancreatic_PDFF","Type Here")
    Pancreatic_head_PDFF = st.text_input(",Pancreatic_head_PDFF","Type Here")
    Pancreatic_body_PDFF = st.text_input("Pancreatic_body_PDFF","Type Here")
    Pancreatic_tail_PDFF = st.text_input("Pancreatic_tail_PDFF","Type Here")
    Gender = st.text_input("Gender","1 for male and 0 for female")
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(VATV_L2,VATV_L3,Total_VATV,Hepatic_PDFF,Pancreatic_PDFF,Pancreatic_head_PDFF,Pancreatic_body_PDFF,Pancreatic_tail_PDFF,Gender)
    st.success('Diabetes Status is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built by John")

if __name__=='__main__':
    main()
    
    
    