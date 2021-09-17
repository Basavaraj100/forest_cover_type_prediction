# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 16:06:21 2021

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



def about():
    st.subheader('**About**')
    st.write('''Project is based on a famous data set in the machine learning community 
    and known as [Forest Cover Type](https://archive.ics.uci.edu/ml/datasets/covertype)
     available for download in the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/index.php)''')
    st.write('''**The goal of the Project :** To predict seven different cover types in four different
    wilderness areas of the  [Roosevelt National Forest](https://en.wikipedia.org/wiki/Roosevelt_National_Forest)
    of Northern Colorado with the best [accuracy](https://miro.medium.com/max/1064/1*5XuZ_86Rfce3qyLt7XMlhw.png).''')
    
    st.write('''**The four wilderness areas are:**''')
    st.write('''1). Rawah
             \n2).Neota
                \n3). Comanche Peak
                \n4). Cache la Poudre''')
    st.write('**Seven categories numbered from 1 to 7 in the "Cover_Type" column, to be classified:**')
    st.write('''
             1). Spruce/Fir
            \n2). Lodgepole Pine
            \n3). Ponderosa Pine
            \n4). Cottonwood/Willow
            \n5). Aspen
            \n6). Douglas-fir
            \n7). Krummholz''')
    st.subheader('Machine Learning Workflow Steps')
    st.write('In this project we will follow the below steps:')
    st.write('''- Data Understanding
             \n- Exploratory Data Analysis
             \n- Feature Engineering
             \n- Model building
             \n- App building''')
             
    st.markdown('''You can find "Data undestanding","Exploratory data analysis",
                "Feature Engineering" and "Model building" in EDA and model building section. To use the app go for "Run app" section ''')
    st.write('**The libraries used in this project are:**')
    st.write('''- Pandas
             \n- Numpy
             \n- Matplotlib
             \n- Seaborn
             \n- Sklearn
             \n- Klib''')
             
             
             
if __name__=='__main__':
    about()           
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    