# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 15:58:18 2021

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





    
def EDA():
    
    st.header('**Data Understanding**')
    st.write('''In this section we will try to understand what each and 
             every feature indicates, what are their datatypes and their units of measurment.''')
    st.write('**Lets import the data**')
    st.write('The imported data is stored in "df" variable')
    df=pd.read_csv(r'train.csv')
    st.success("df=pd.read_csv(r'train.csv')")
    st.write('Reading first 5 observations from the data')
    st.success("df.head()")
    st.write(df.head())
    st.write(' and the last five observations are')
    st.success("df.tail()")
    st.write(df.tail())
    st.write('In the dataset Id column is there which is not important to classify the target so lets drop the id column from the data')
    df.drop('Id',axis=1,inplace=True)
    st.success("df.drop('Id',axis=1,inplace=True)")
    st.write('The information of each feature is explained in below dataframe')
    st.write(pd.read_csv(r'Data_info.csv',index_col='Unnamed: 0'))
    st.write('''From the above data frame we can observe that there are 40 columns related to soil types
             which are encoded with 0 and 1. The target column "Cover type" is label encoded from 1 to 7
             (each label are given in about section). And there are four binary columns related to Wilderness areas. 
             _All features are in numeric datatype_''')
    st.write('**Shape of the data**')
    st.success('df.shape')
    st.write(df.shape)
    st.write('There are  55 features including target and  15120   observations in the data')
    st.write('Desciption of the data')
    st.write('df.describe()')
    st.write(df.describe())
    st.write('''From the above description one can notice that
             "Vertical_Distance_to_Hydrology" column contains negative values,
             it might be because the the vertical distance of the water
             source is below from the point of consideration ''')
    # ======================EDA===============================================
    st.header('**Exploratory Data Anlysis**')
    st.write('_Here onwards we will use eda_df which is copy of original dataframe(df)_')
    eda_df=df.copy()
    st.success('eda_df=df.copy()')
    st.write('''Before continuing with EDA we will convert all 40 columns related to soil type into one column, and
             4 wilderness columns into one columns, meanwhile map the target column to its original names
             which will help in EDA''')
   # ============================= soil type ===================================================
    st.write('Converting all soil type binary columns into single column. Before that we found some columns are with all values 0 only')
    st.write('**Columns with zero No information are:**')
    st.write()
    soil_type_cols=[i for i in eda_df.columns if 'Soil_Type' in i]
    st.success('''for i in soil_type_cols:
                     \n    a=eda_df[i].unique()
                     \n    if len(a)==1:
                     \n        print(i,eda_df[i].unique())''')
    for i in soil_type_cols:
        a=eda_df[i].unique()
        if len(a)==1:
            st.write(i,eda_df[i].unique())
    st.write('We will drop these columns and convert other soil types columns into one column')
    eda_df.drop(['Soil_Type7','Soil_Type15'],axis=1,inplace=True) # droping columns
    soil_type_cols_rem=list(eda_df.columns)[14:-1] # soil type columns after dropping
    
    soil_type=[]
    soil_type_df=eda_df[soil_type_cols_rem]
    for i in range(len(soil_type_df)):
        l=soil_type_df.iloc[i,:].to_list()
        ind=l.index(1)
        if ind>=0:
            soil_type.append(soil_type_cols_rem[ind])
        else:
            soil_type.append('Soil_Type41')
    eda_df.drop(soil_type_cols_rem,axis=1,inplace=True)
    eda_df['soil_type']=soil_type 
    st.write('After converting all binary soil type columns into one column the soil type column looks like:')
    st.success("eda_df['soil_type']")
    st.write(eda_df['soil_type'])
    # ==============wilderness area===============
    
    st.write('**Mapping wilderness columns into one column**')
    wilderness_cols=[i for i in eda_df.columns if 'Wilderness_Area' in i]
    wilderness_d={1:'Rawah',2:'Neota',3:'Comanche Peak',4:'Cache la Poudre'}
    st.write(wilderness_d)
    wilderness_area_type=[]
    wilderness_area_type_df=eda_df[wilderness_cols]
    for i in range(len(wilderness_area_type_df)):
        l=wilderness_area_type_df.iloc[i,:].to_list()
        ind=l.index(1)
        wilderness_area_type.append(wilderness_d[ind+1])
        
    eda_df.drop(wilderness_cols,axis=1,inplace=True)
    eda_df['Wilderness_area_type']=wilderness_area_type
    st.write('After mapping wilderness columns the column looks like:')
    st.success("eda_df['Wilderness_area_type']")
    st.write(eda_df['Wilderness_area_type'])
    
    st.write('**mapping target columns to its original names**')
    d={1:'Spruce/Fir',2:'Lodgepole Pine',3:'Ponderosa Pine',4:'Cottonwood/Willow',5:'Aspen',6:'Douglas-fir',7:'Krummholz'}
    st.write(d)
    st.success("df_train['Cover_Type']=df_train['Cover_Type'].map(d)")
    eda_df['Cover_Type']=eda_df['Cover_Type'].map(d)
    st.write('**After mapping required columns the data set looks like:**')
    st.write(eda_df.head())
    
                           
                          
    
    st.write('**In this section we will deal with following steps:**')
    st.write('''- Missing values
              \n- Outliers
              \n- Balance of data
              \n- Relationship between categorical and numerical features and target
              \n- Relationship between numerical features and target''')
    st.write('**Missing vlaues**')
    st.success('df.isna().sum()')
    st.write(df.isna().sum())
    st.write('Data is free of missing values')
    st.write('**Outliers**')
    
    st.write('_The box plot for all numerical features shown below_')
    cols=df.columns
    for i in cols:
        if 'Soil' in i:
            continue 
        if 'Wild' in i: 
            continue
        if 'Cover' in i:
            continue
        
        fig=plt.figure()
        sns.boxplot(df[i])
        plt.title(i)
        st.pyplot(fig)
        
    st.write('''Data contains outliers. Only Vertical_distance_to_Hydrology and Hillshade_9am column contains very few observations apart from the group
             .we droped only those observations which are away from crowd''')
    
    st.write('''**Relationship between categorical features and target**''')
    cat_features=eda_df.select_dtypes(np.object).columns
    st.write('''To check whether categorical features related to target we used chi_sqruare test, 
             from the chisquare test we found that all categorical features are related to target''')
    st.write('Value counts of soil_type')
    soil_type_freq=eda_df['soil_type'].value_counts()
    st.write(soil_type_freq)
    st.write('From the above table we can see that there are some soil types which occured less than 100 times we considered these as rare soil types')
    rare_soil_type=soil_type_freq[soil_type_freq<100].index.to_list()
    st.write('Rare soil types are:')
    st.write(rare_soil_type)
    eda_df['soil_type']=eda_df['soil_type'].replace(to_replace=rare_soil_type,value='rare_soil_type')
    st.write('After replacing rare soil type')
    st.write(eda_df['soil_type'])
    wild_area_vs_c_type=pd.crosstab(eda_df['Cover_Type'],eda_df['Wilderness_area_type'])
    st.write('**Count of Wilderness areas among different cover Types**')
    st.write(wild_area_vs_c_type)
    st.write('''Cottonwood/Willow cover type is completely covered with "Cache la Poudre" wilderness area
            . "Krummholz" and "Spruce/Fir" cover type are free of "Cache la Poundre" wilderness_area_tyep
            . All four wilderness_area type are avilable only in "Lodgepole Pine" cover type only. 
            From the observation of above atble wilderness area type will help to segregate cover type to some extent''')
                    
    st.write("**Relationship between numerical and target**")
    num_features=eda_df.select_dtypes(np.number).columns
    for i in num_features:
        f=plt.figure()
        sns.boxplot(data=eda_df,x='Cover_Type',y=i)
        plt.title(f'{i} distribution for different cover types')
        plt.xticks(rotation=45)
        st.pyplot(f)
        
    st.write('Observations from above boxplots')
    st.write('''**Elevation**

            \n- For different cover types elevation is less overlapped
            \n- Krummhalz cover_type is at highest elevation among all cover_types
            \n- Cottonwood/willow cover_type is at lowest elevation as compared to other Cover_types
            \n- Elevation is the good feature to segregate different cover_types
            \n**Aspect**
            
            \n- Aspect for different cover types is more overlapping hence its difficult to group the cover_types bases on aspect
            \n**Slope**
            
            \n- The mean slope for Lodgepole pine, Spruce/fir and Keummholz is lower as compared to the mean slope of other cover types
            \n**Horizontal Distance to Hydrology**
            
            \n- Mean horizontal distance for Cottonwood/willow cover type is lowest among all other cover types indicates Cottonwood/willow cover type forest is always lies near to the water surface
            \n**Vertical_Distance_to_Hydrology**
            
            \n- Mean vertical distance for willow cover type is least among other cover types which agin tells that willow cover type forest lies near to water source
            \n- High overlapping of vertical distance to hydrology for different cover types.
            \n**Vertical distance to roadway**
            
            \n- Mean vertical distance for Ponderosa Pine, Douglass-fir and willow cover type is less among all cover types 
            indicates they are at lower elevation, 
            where as Lodgepole pine, spruce/fir and krummholz have high mean vertical distance to roadway 
            indicates they found at higher elevations.
            \n**Hillshade_9am**
            
            \n- Mean hillshade_9am is highest for willow cover type
            \n**Hillshade_noon**
            
            \n- more overlapping of hillshade_noon among different cover types
            \n**Hillshade_3am**
            
            \n- Except Aspen and willow cover types all other cover types have high and similar mean hillshade_3am
            \n**Horizontal distance to fire points**
            
            \n- Ponderosa Pine, willow and Douglass-fir have low mean horizontal distance to fire points as compared to other cover types indicates these cover types are more prone to fire''')
                                                
    st.write('**Encoding and splitting the data**')   
    st.write('We encoded the remainig categorical features using one hot encoded and map the target columns to numbers 1 to 7')
    y=eda_df['Cover_Type']
    x=eda_df.drop('Cover_Type',axis=1) 
    x_encoded=pd.get_dummies(x,drop_first=True)  
    d={1:'Spruce/Fir',2:'Lodgepole Pine',3:'Ponderosa Pine',4:'Cottonwood/Willow',5:'Aspen',6:'Douglas-fir',7:'Krummholz'}
    d1=dict(zip(d.values(),d.keys()))
    y_encoded=y.map(d1)    
    df_final=pd.concat([x_encoded,y_encoded],axis=1)
    st.write('After encoded the data looks like:')
    st.write(df_final.head())
    
    st.header('Model building')
    st.write('We select the Decision tree as Base model followed by hyperparamter tuning, But finally we select the random forest with selected features and hyperparameter tuning')
    st.write('_The work flow model building and selection followed is shown in below figure_')
    im = Image.open(r"model_building_flowchart.png")    
    st.image(im)
    st.write('**The final selected features are**')
    f_features= Image.open(r"selected_features.PNG")
    st.image(f_features)
    
    
    st.write('**Confusion matrix for test data from final model**')
    c_mat= Image.open(r"confussion_matrix.PNG")
    st.image(c_mat)
    
    st.write('**Classification report for test data from final model**')
    c_report=Image.open(r"classification_report.PNG")
    st.image(c_report)
    
    st.info('To run the model to predict test data use "Run app" section')
    
    
    
    
    
    
    
    
    
    
if __name__=='__main__':
    EDA()