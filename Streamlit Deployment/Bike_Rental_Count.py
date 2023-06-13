# -*- coding: utf-8 -*-
"""
Created on Thu May 18 15:01:28 2023

@author: imjma
"""

import pickle
import pandas as pd
import numpy as np 
import streamlit as st

# Load the model
model = pickle.load(open('rf.pkl', 'rb'))

# Load the dataframe
df = pd.read_csv("bike_rent.csv")

def predict(mnth, hr, weekday, temp, hum, windspeed, casual, season_fall, season_springer, season_summer, season_winter, holiday_No, holiday_Yes, workingday_No_work, workingday_Working_Day, weathersit_Clear, weathersit_HeavyRain, weathersit_LightSnow, weathersit_Mist):
    # Create an input array
    input_data = np.array([[mnth, hr, weekday, temp, hum, windspeed, casual, season_fall, season_springer, season_summer, season_winter, holiday_No, holiday_Yes, workingday_No_work, workingday_Working_Day, weathersit_Clear, weathersit_HeavyRain, weathersit_LightSnow, weathersit_Mist]])

    # Make the prediction using the trained model
    prediction = model.predict(input_data)

    # Return the prediction
    return prediction[0]


def main():
    # Price Calculator page
    st.title("Bike Sharing Prediction App")
    st.write("Enter the values for the features to get a prediction")

    month_names = {1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr", 5: "May", 6: "Jun", 7: "Jul", 8: "Aug", 9: "Sep", 10: "Oct", 11: "Nov", 12: "Dec"}
    weekday_names = {0: "Sun", 1: "Mon", 2: "Tue", 3: "Wed", 4: "Thu", 5: "Fri", 6: "Sat"}

    mnth = st.selectbox("Month", options=list(month_names.values()), index=0)
    hr = st.number_input("Hour", min_value=0, max_value=23, value=12)
    weekday = st.selectbox("Weekday", options=list(weekday_names.values()), index=0)
    temp = st.number_input("Temperature (in Celsius)", value=25.0)
    hum = st.number_input("Humidity (in %)", min_value=0, max_value=100, value=50)
    windspeed = st.number_input("Wind Speed (in km/h)", value=25.0)
    casual = st.number_input("Casual", value=0)
    "Select Season"
    season_fall = st.checkbox("Fall")
    season_springer = st.checkbox("Spring")
    season_summer = st.checkbox("Summer")
    season_winter = st.checkbox("Winter")
    "Type of day"
    holiday_No = st.checkbox("No Holiday")
    holiday_Yes = st.checkbox("Holiday")
    "Type of working Day"
    workingday_No_work = st.checkbox("No Working Day")
    workingday_Working_Day = st.checkbox("Working Day")
    "Weather Situation"
    weathersit_Clear = st.checkbox("Clear")
    weathersit_HeavyRain = st.checkbox("Heavy Rain")
    weathersit_LightSnow = st.checkbox("Light Snow")
    weathersit_Mist = st.checkbox("Mist")

    # Map the selected values back to numerical values
    mnth = list(month_names.keys())[list(month_names.values()).index(mnth)]
    weekday = list(weekday_names.keys())[list(weekday_names.values()).index(weekday)]

    # Make the prediction using the predict() function
    prediction = predict(mnth, hr, weekday, temp, hum, windspeed, casual, season_fall, season_springer, season_summer, season_winter, holiday_No, holiday_Yes, workingday_No_work, workingday_Working_Day, weathersit_Clear, weathersit_HeavyRain, weathersit_LightSnow, weathersit_Mist)

    # Display the prediction
    st.write("The predicted number of bikes rented is:", round(prediction))

if __name__ == '__main__':
    main()
