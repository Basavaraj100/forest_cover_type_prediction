# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 16:12:25 2021

@author: HP
"""


import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn  as sns
import sklearn
 
import streamlit.components.v1 as stc 
import pickle
import base64 
import time
from csv_file_downloader import FileDownloader
timestr = time.strftime("%Y%m%d-%H%M%S")


original_columns=['Id', 'Elevation', 'Aspect', 'Slope',
   'Horizontal_Distance_To_Hydrology', 'Vertical_Distance_To_Hydrology',
   'Horizontal_Distance_To_Roadways', 'Hillshade_9am', 'Hillshade_Noon',
   'Hillshade_3pm', 'Horizontal_Distance_To_Fire_Points',
   'Wilderness_Area1', 'Wilderness_Area2', 'Wilderness_Area3',
   'Wilderness_Area4', 'Soil_Type1', 'Soil_Type2', 'Soil_Type3',
   'Soil_Type4', 'Soil_Type5', 'Soil_Type6', 'Soil_Type7', 'Soil_Type8',
   'Soil_Type9', 'Soil_Type10', 'Soil_Type11', 'Soil_Type12',
   'Soil_Type13', 'Soil_Type14', 'Soil_Type15', 'Soil_Type16',
   'Soil_Type17', 'Soil_Type18', 'Soil_Type19', 'Soil_Type20',
   'Soil_Type21', 'Soil_Type22', 'Soil_Type23', 'Soil_Type24',
   'Soil_Type25', 'Soil_Type26', 'Soil_Type27', 'Soil_Type28',
   'Soil_Type29', 'Soil_Type30', 'Soil_Type31', 'Soil_Type32',
   'Soil_Type33', 'Soil_Type34', 'Soil_Type35', 'Soil_Type36',
   'Soil_Type37', 'Soil_Type38', 'Soil_Type39', 'Soil_Type40']


def validate_file(file):
    original_columns=['Id', 'Elevation', 'Aspect', 'Slope',
       'Horizontal_Distance_To_Hydrology', 'Vertical_Distance_To_Hydrology',
       'Horizontal_Distance_To_Roadways', 'Hillshade_9am', 'Hillshade_Noon',
       'Hillshade_3pm', 'Horizontal_Distance_To_Fire_Points',
       'Wilderness_Area1', 'Wilderness_Area2', 'Wilderness_Area3',
       'Wilderness_Area4', 'Soil_Type1', 'Soil_Type2', 'Soil_Type3',
       'Soil_Type4', 'Soil_Type5', 'Soil_Type6', 'Soil_Type7', 'Soil_Type8',
       'Soil_Type9', 'Soil_Type10', 'Soil_Type11', 'Soil_Type12',
       'Soil_Type13', 'Soil_Type14', 'Soil_Type15', 'Soil_Type16',
       'Soil_Type17', 'Soil_Type18', 'Soil_Type19', 'Soil_Type20',
       'Soil_Type21', 'Soil_Type22', 'Soil_Type23', 'Soil_Type24',
       'Soil_Type25', 'Soil_Type26', 'Soil_Type27', 'Soil_Type28',
       'Soil_Type29', 'Soil_Type30', 'Soil_Type31', 'Soil_Type32',
       'Soil_Type33', 'Soil_Type34', 'Soil_Type35', 'Soil_Type36',
       'Soil_Type37', 'Soil_Type38', 'Soil_Type39', 'Soil_Type40']
    if len(set(original_columns))==len(set(file.columns)):
        return 'valid'
    else:
        return 'Not valid'
def pred_from_csv():
   
    file=st.file_uploader('Drop the csv file here',type=['csv'])
    if file:
        df_test=pd.read_csv(file.name)
        if validate_file(df_test)=='valid':
            if st.button('Predict'):
                # =============== removing id column=============
                df_test.drop('Id',axis=1,inplace=True)
                
                # ============removing hillshade_9am<40==================
                df_test=df_test[df_test['Hillshade_9am']>40]
                
            
                # =========== selecting features========================
                selected_features=['Elevation', 'Horizontal_Distance_To_Roadways',
                                    'Horizontal_Distance_To_Fire_Points',
                                    'Horizontal_Distance_To_Hydrology',
                                    'Vertical_Distance_To_Hydrology', 'Hillshade_9am', 'Aspect',
                                    'Hillshade_Noon', 'Hillshade_3pm', 'Slope',
                                    'Wilderness_Area3', 'Wilderness_Area1',
                                    'Soil_Type10', 'Soil_Type38',
                                    'Soil_Type3', 'Soil_Type39']
                final_test_df=df_test[selected_features]
                
                #  ===========predict for the test data=========
                model = pickle.load(open('Forest_cover_type_prediction.pkl', 'rb'))
                
                output=model.predict(final_test_df)
                # ============== attach output to original input file==============
                d1={1: 'Spruce/Fir',
                      2: 'Lodgepole Pine',
                      3: 'Ponderosa Pine',
                      4: 'Cottonwood/Willow',
                      5: 'Aspen',
                      6: 'Douglas-fir',
                      7: 'Krummholz'}
                # final_test_df['Labels']=output
                # final_test_df['Labels']=final_test_df['Labels'].map(d1)
                result_df=pd.DataFrame({'Labels':output})
                result_df['Labels']=result_df['Labels'].map(d1)
                
                # =================asking to download the results============
                download = FileDownloader(result_df.to_csv(),file_ext='csv').download()
        else:
            st.markdown('**Please enter valid file**')
    else:
        st.markdown('First enter the valid file')
                
    
    
    
    
    
    
    
    
    
    
    
    
    
if __name__=='__main__':
    pred_from_scv()