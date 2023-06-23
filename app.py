import joblib
import streamlit as st
import pandas as pd
import xgboost

def app():
    model = joblib.load('Final_Model.h5')
    st.set_page_config(page_title=" Airline Price Prediction ")
    st.title(" Airline Price Based on Features ")
    st.header(" Epsilon Training Project ")

    st.write("This project predicts Airline Prices based on some features")

    Airline = st.radio('Select Airline Company', ['IndiGo','Air India','Jet Airways', 'SpiceJet','Multiple carriers','GoAir', 'Vistara', 'Air Asia','Vistara Premium economy','Jet Airways Business','Multiple carriers Premium economy','Trujet'])
    Source = st.radio('Select Source', ['Banglore', 'Kolkata', 'Delhi', 'Chennai', 'Mumbai'])
    Destination = st.radio('Select Destination', ['New Delhi','Banglore','Cochin','Kolkata','Delhi','Hyderabad'])
    Total_Stops = st.selectbox('How Many Stops before reaching Destination', ['0','1','2','3','4'])
    Journey_Year = st.number_input("2019", value=0)
    Journey_Month = st.number_input("Month 1 - 12", value=0)
    Journey_Day = st.number_input("Day 1 - 31", value=0)
    Total_Hops = st.selectbox('How Much Country to Pass Through to reach Destination', ['1','2','3','4','5'])
    Arrive_in_Different_Day = st.selectbox('The arrival is in Other Day or Not', ['Yes', 'No'])
    Duration_Hour = st.number_input("Length of Flight in Hours 1 - 24", value=0)
    Duration_Minute  = st.number_input("Length of Flight in Minutes 1 - 60", value=0)
    
    
    predict = st.button("Predict")
    if predict:
        df = pd.DataFrame.from_dict(
            {
                'Airline':[0 if Airline == 'IndiGo' else (1 if Airline == 'Air India' else  (2 if Airline =='Jet Airways'else  (3 if Airline ==  'SpiceJet' else  (4 if Airline == 'Multiple carriers' else  (5 if Airline == 'GoAir' else  (6 if Airline == 'Vistara' else  (7 if Airline == 'Air Asia' else  (8 if Airline == 'Vistara Premium economy' else (9 if Airline == 'Jet Airways Business' else (10 if Airline =='Multiple carriers Premium economy' else 11))))))))))],
                'Source':[0 if Source == 'Banglore' else (1 if Source == 'Kolkata' else  (2 if Source =='Delhi' else  (3 if Source ==  'Chennai' else  4 )))],
                'Destination':[0 if Destination == 'New Delhi' else (1 if Destination == 'Banglore' else  (2 if Destination =='Cochin' else  (3 if Destination ==  'Kolkata' else  (4 if Destination == 'Delhi' else 5 ))))],
                'Total_Stops':[0 if Total_Stops == '0' else (1 if Total_Stops == '1' else  (2 if Total_Stops =='2' else  (3 if Total_Stops ==  '3' else  4 )))],
                'Journey_Year':[Journey_Year],
                'Journey_Month':[Journey_Month],
                'Journey_Day':[Journey_Day],
                'Total_Hops':[0 if Total_Hops == '1' else (1 if Total_Hops == '2' else  (2 if Total_Hops =='3' else  (3 if Total_Hops ==  '4' else  (4 ))))],
                'Arrive_in_Different_Day':[0 if Arrive_in_Different_Day == 'No' else 1],
                'Duration_Hour':[Duration_Hour],
                'Duration_Minute':[Duration_Minute],            
            }
        )

        st.write("Input Data: ")
        st.dataframe(df)

        predict = model.predict(df)
    
app()
