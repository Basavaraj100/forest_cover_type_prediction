


import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn  as sns
import sklearn

import streamlit.components.v1 as stc 
import pickle


html_temp = """
		<div style="background-color:#3872fb;padding:10px;border-radius:10px">
		<h1 style="color:white;text-align:center;">Forest Area Cover Type Prediction App </h1>
		</div>
		"""

 
    
        
def main():
    # -------------wilderness_area_type------
    Wilderness_area_type_Comanche_Peak=0
    Wilderness_area_type_Rawah=0
    Wilderness_area_other=0


   # soil_type
    soil_type_10=0
    soil_type_3=0
    soil_type_38=0
    soil_type_39=0
    
    model = pickle.load(open('Forest_cover_type_prediction.pkl', 'rb'))
    stc.html(html_temp)
    
    
    
    with st.form(key='form1'):
        col1,col2=st.beta_columns(2)
        
        
        with col1:
            # --------------elevarion-------1
            elev=st.number_input('Enter elevation in meters')
            #  Horizontal distance to roadway
            h_d_road=st.number_input('Enter horizontal distance to raodway')
            
            # -----Horizontal distance to firepoint------
            h_d_fire_point=st.number_input('Enter horizontal distance to fire point')
            
            
            #  horizontal distance to hydrology
            
            h_d_hydrology=st.number_input('Enter horizontal distance to hydrology')
            
            # vertical distance to hydrology
            v_d_hydroplogy=st.number_input('Enter vertical distance to hydrology')
            
            # ------wilderness area type------
            wilderness_opt=['Comanche Peak','Rawah','Other']
            wilderness=st.selectbox('Select wilderness area type',wilderness_opt)
            if wilderness=='Comanche Peak':
                Wilderness_area_type_Comanche_Peak=1
            if wilderness=='Rawah':
                Wilderness_area_type_Rawah=1
            if wilderness=='Other':
                pass
           
                
            
            
            
            
            
            
            
            
        with col2:
            
         
            
            
            # ------hillshade 9am----
            hillshade_9am=st.number_input('Enter hillshade at 9 am in summer solistice')
            
            # -------aspect--------
            aspect=st.number_input('Enter aspect in degree azimuthal')
            
        
            
            
            # ------Hillshade_Noon---------
            hillshade_noon=st.number_input('Enter hillshade at noon in summer solistice')
            
            # ----------Hillshade_3pm---------
            hillshade_3pm=st.number_input('Enter hillshade at 3 pm in summer solistice')
            
            # --------Slope-------
            slope=st.number_input('Enter slope in degree')
            
            # ------------soil type-----
            num=[3,10,38,39,'Other']
            
            soil_type_=st.selectbox('Select soil type',num)
            if soil_type_==10:
                soil_type_10=1
            if soil_type_==3:
                soil_type_3=1
            
            if soil_type_==38:
                soil_type_38=1
            if soil_type_==39:
                soil_type_39=1
            
                
         
            
                
                
            
            
        inputs=[elev,h_d_road,h_d_fire_point,h_d_hydrology,
                v_d_hydroplogy,hillshade_9am,aspect,hillshade_noon,
                hillshade_3pm,slope,Wilderness_area_type_Comanche_Peak,Wilderness_area_type_Rawah,
                soil_type_10,soil_type_38,soil_type_3,soil_type_39]   
            
            
            
        if st.form_submit_button('Predict forest cover type'):
            ans=model.predict([inputs])[0]
            d={1:'Spruce/Fir',2:'Lodgepole Pine',3:'Ponderosa Pine',4:'Cottonwood/Willow',5:'Aspen',6:'Douglas-fir',7:'Krummholz'}
            f_ans=d[ans]
            
            st.success('The forest cover type is "{}"'.format(f_ans))
        
     





if __name__=='__main__':
    main()