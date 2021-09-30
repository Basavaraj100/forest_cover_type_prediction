# forest_cover_type_prediction

## Data source: 
https://www.kaggle.com/c/forest-cover-type-prediction/data
 
## Problem statment
The goal is to predict seven different cover types in four different wilderness areas of 
the Roosevelt National Forest of Northern Colorado with the best accuracy

**The seven forest cover types are-**<br>
1: Spruce/Fir<br>
2: Lodgepole Pine<br>           
3: Ponderosa Pine<br>
4: Cottonwood/Willow<br>
5: Aspen<br>
6: Douglas-fir<br>
7: Krummholz<br>

**Four wilderness areas are-**<br>
1: Rawah<br>
2: Neota<br>
3: Comanche Peak<br>
4: Cache la Poudre<br>

# My approach


## Rare soil types
- There are 40 binary columns related to soil type but when we merge those 40 columns into one column we found that 
there are some soil types which do not occure more than 100 times, we converted all soil types of frequency less than 100 into rare soil type
```python
rare_soil_type=soil_type_freq[soil_type_freq<100].index.to_list()
eda_df['soil_type']=eda_df['soil_type'].replace(to_replace=rare_soil_type,value='rare_soil_type')
```

- Rare soil types are


![image](https://github.com/Basavaraj100/forest_cover_type_prediction/blob/main/images/rare_soil_types.PNG)



## Ml model building
- We used Decision tree as base model, becuase it need less feature engineering then we tried with random forest followed by feature selection

![image](https://github.com/Basavaraj100/forest_cover_type_prediction/blob/main/images/model_building_flowchart.png)


## Feature selection
- The feature importance technique from random forest is used to select top 16 important features
- selected features are:

![image](https://github.com/Basavaraj100/forest_cover_type_prediction/blob/main/images/selected_features.PNG)

## Final model performance
- Finally we select random forest as final model with selected features and hyperparameter tuning
- **Confusion matrix**

![image](https://github.com/Basavaraj100/forest_cover_type_prediction/blob/main/images/confussion_matrix.PNG)

- **Classification report**

![image](https://github.com/Basavaraj100/forest_cover_type_prediction/blob/main/images/classification_report.PNG)


## Model deployment in GCP
- The model is deployed in Google cloud pltform
the supported files are:

a)Dockerfile
```python
FROM python:3.9
WORKDIR /app
COPY requirements.txt ./requirements.txt

RUN pip3 install -r requirements.txt
EXPOSE 8080
COPY . /app

CMD streamlit run --server.port 8080 --server.enableCORS false app.py
```

b)app.yaml
```python
runtime: custom
env: flex
```

## Forest area cover type prediction App
- The app is divided into three sections
a) About: Here you will found the description about problem statment
b) EDA and model building: Here you will found the description about complete EDA and Model building
c) Run App: Here you can use the app to predict the forest cover type fot customised input.And also you can predict from the csv file which should follow given conditions(described in How input csv file should be)

App link: https://forest-326117.el.r.appspot.com/

