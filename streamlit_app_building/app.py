# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 10:20:54 2021

@author: HP
"""


# importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from sklearn.model_selection import train_test_split
import streamlit.components.v1 as stc 
import pickle
import streamlit as st
import pandas as pd
from scipy import stats
import klib
from PIL import Image
from model_building import model_building_func
from eda_app import EDA
from About_section import about
from predict_from_csv_file import pred_from_csv

# Utils
import base64 
import time
timestr = time.strftime("%Y%m%d-%H%M%S")


# ===============================LOGGING SECTION===============================
import logging

# Save to File
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Formatter
formatter = logging.Formatter("%(levelname)s %(asctime)s.%(msecs)03d -%(message)s")


# File
file_handler = logging.FileHandler('activity.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)



# =============================HEADING=========================================
Heading="""
		<div >
		<h1 style="text-align:center;"><b>Predicting Forest Cover Types with the Machine Learning Workflow</b> </h1>
		</div>
		"""
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

# ==============================================================================       
def main():
    
     
# ====================Skeleton of app=======================
    stc.html(Heading)
    menu=['About','EDA and Model building','Run app']
    s_bar=st.sidebar.selectbox('Menu' ,menu)
    
# ====================ABOUT SECTION======================   
    if s_bar=='About':
        logger.info('About section')
        about()
        
          
# ===========================EDA AND MODEL BUILDING SECTION==================       
    
    if s_bar=='EDA and Model building':
        logger.info('EDA and model building section')
        EDA()
        
    
        
# ===================== RUN APP SECTION===================================                                                                                
        
    if s_bar=='Run app':
        logger.info('Run app section')
        with st.beta_expander('Predict single observations'):
            logger.info('Run app section-Predicting for given observation')
            model_building_func()
        with st.beta_expander('How the csv file should be'):
            
            st.write('- No missing values should be there in any column')
            st.write('- The column name should follow proper names as given below')
            st.write('- The features names are:')
            st.write(original_columns)
        with st.beta_expander('Predict from the csv file'):
            logger.info('Run app section-Predicting for given csv file')
            pred_from_csv()
            
            
            
              
                
            
        
    
    
    
    
    
    
    
    
    
    
if __name__=='__main__':
    main()
