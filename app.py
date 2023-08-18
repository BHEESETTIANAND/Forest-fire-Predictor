import streamlit as st
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu
import pickle



model=pickle.load(open("logreg.pkl","rb"))

st.set_page_config("wide")
selected=option_menu("Main menu",["home","forestfire predictor","info"],icons=
                     ["house","fire","book"],orientation="horizontal")



humidity_emoji = "\U0001F4A7"
wind_speed_emoji = "\U0001F4A8"
rain_emoji = "\U0001F327"



with st.sidebar:
    st.header(":blue[About Me] :man:")
    st.write("I am an AI and Data Science Student. Passionate about Data science and ML")
    github_emoji = "\U0001F680"
    github_link = f"[Github Profile {github_emoji}](https://github.com/BHEESETTIANAND)"
    st.markdown(github_link, unsafe_allow_html=True)
    gmail_emoji = "\U0001F4E7"
    st.markdown(f"email me at {gmail_emoji}")
    st.write("anandbheesetti@gmail.com")
    
    
    
if(selected=="home"):
    st.title(" :fire:  Forest Fire Predictor :fire:")
    st.image("forest-fire-2-1553010.jpg")
    st.write("With the help of this project you can know whether there is a chance of getting :fire: forest fire"
              "forest fire :fire: or not")
    
    
    
if(selected=="forestfire predictor"):
    f1=st.number_input("**Enter the Temperature** :thermometer:")
    f2=st.number_input(f"**Enter the RH value** {humidity_emoji} ")
    f3=st.number_input(f"**Enter the WS value** {wind_speed_emoji}")
    f4=st.number_input(f"**Enter the level of Rain** {rain_emoji}")
    f5=st.number_input(f"**Enter the value of FFMC**")
    f6=st.number_input(f"**Enter the value of DMC**")
    f7=st.number_input(f"**Enter the value of DC**")
    f8=st.number_input(f"**Enter the value of ISI**")
    f9=st.number_input(f"**Enter the value of BUI**")
    f10=st.number_input(f"**Enter the value of FWI**")
    
    features=np.array([f1,f2,f3,f4,f5,f6,f7,f8,f9,f10])
    pre=model.predict(features.reshape(1,-1))
    if(st.button("Predict")):
        if(pre==0):
            st.write("**There is no chance of Forest Fire**")
        if(pre==1):
            st.write("**There Is Forest Fire**")
            
            
            
if(selected=="info"):
    st.markdown("**In this project as we want to predict whether There is forest fire are not**")
    st.markdown("**For this i have used Algerian Forest Fire Data set**")
    st.markdown("**To build ML model as it is a Classification problem i had used Classification algorithms**")
    st.markdown("**Like Logistic Regression,Decision Trees,Support vecote Machines,Random Forest Classifier**")
    st.markdown("**In this for Random Forest model i had got 100% accuracy**")
    st.markdown("**And for Logistic Regression i had got 97% accuracy**")
    st.header("**The features information is as given below**")
    st.markdown(":blue[Temperature] noon (temperature max) in Celsius degrees: 22 to 42")
    st.markdown(":blue[RH] Relative Humidity in %: 21 to 90")
    st.markdown(":blue[WS] Wind speed in km/h: 6 to 29")
    st.markdown(":blue[Rain] total day in mm: 0 to 16.8")
    st.markdown(":blue[FFMC] Fine Fuel Moisture Code (FFMC) index from the FWI system: 28.6 to 92.5")
    st.markdown(":blue[DMC] Duff Moisture Code (DMC) index from the FWI system: 1.1 to 65.9")
    st.markdown(":blue[DC] Drought Code (DC) index from the FWI system: 7 to 220.4")
    st.markdown(":blue[Initial Spread Index] (ISI) index which ranges between 0 to 18")
    st.markdown(":blue[Buildup Index] (BUI) index which ranges between 1.1 to 68")
    st.markdown(":blue[Fire Weather Index] (FWI) Index which ranges between 1 to 31.1")








    
    
    



 


    




    