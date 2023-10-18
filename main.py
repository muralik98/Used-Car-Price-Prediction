import streamlit as st
import pandas as pd
import numpy as np
import pickle

file1 = open('best_model.pkl', 'rb')
rf = pickle.load(file1)
file1.close()

data = pd.read_csv("car_data_final.csv")

st.title("Used Car Price Predictor")

Manufacturer = st.selectbox('Brand', data['Manufacturer'].unique())

Body= st.selectbox('Type', data['Body'].unique())

Transmission = st.selectbox('Transmission', data['Transmission'].unique())

Condition= st.number_input('Condition Rating 1 to 5', min_value=0.0, max_value=5.0, value="min", step=0.1)

Odometer_Reading= st.number_input('Odometer Reading', min_value=0, max_value=1000000, value="min", step=1)

Color=st.selectbox('Color', data['Color'].unique())

Interior_Color=st.selectbox('Interior', data['Interior_Color'].unique())

MMR_Value=st.number_input('MMR_Value', min_value=0, max_value=1000000, value="min", step=1)

st.markdown('[Link to MMR Report](https://site.manheim.com/en/locations.html)')

Vehicle_Age=st.number_input('Age Of Car In Years', min_value=0, max_value=100, value="min", step=1)



if st.button('Predict Price'):

    query = pd.DataFrame([[Manufacturer, Body, Transmission, Condition, Odometer_Reading, Color, Interior_Color, MMR_Value,Vehicle_Age]],
                         columns=data.columns)


    prediction = int(np.exp(rf.predict(query)))

    price_range=f"{prediction * 1.12:.2f} to \${prediction / 1.12:.2f}"

    st.title("Predicted Price of Car is between \$" +  price_range)