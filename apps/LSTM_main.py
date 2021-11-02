import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader as data
from keras.models import load_model
from datetime import date
import streamlit as st

def app():
    START = '2000-01-01'
    TODAY = date.today().strftime('%Y-%m-%d')

    user_input = st.text_input('Enter Stock Ticker', '^KS11')
    df = data.DataReader(user_input,"yahoo", START, TODAY)
    
    st.subheader('Data from 2000 - 2021')
    st.write(df.describe())
    

    st.subheader('현재 주가 차트')
    fig = plt.figure(figsize = (12,6))
    plt.plot(df.Close)
    st.pyplot(fig)

    data_training = pd.DataFrame(df['Close'][0:int(len(df)*0.70)])
    data_testing = pd.DataFrame(df['Close'][int(len(df)*0.70): int(len(df))])

    from sklearn.preprocessing import MinMaxScaler
    scaler = MinMaxScaler(feature_range=(0,1))

    data_training_array = scaler.fit_transform(data_training)

    x_train = []
    y_train = []

    for i in range(100, data_training_array.shape[0]):
        x_train.append(data_training_array[i-100: i])
        y_train.append(data_training_array[i, 0])
    
    x_train, y_train = np.array(x_train), np.array(y_train)    

    model = load_model('LSTM_model.h5')

    past_100_days = data_training.tail(100)
    final_df = past_100_days.append(data_testing, ignore_index=True)
    input_data = scaler.fit_transform(final_df)

    x_test = []
    y_test = []

    for i in range(100, input_data.shape[0]):
        x_test.append(input_data[i-100: i])
        y_test.append(input_data[i, 0])

    x_test, y_test = np.array(x_test), np.array(y_test)
    y_predicted = model.predict(x_test)
    scaler.scale_

    scale_factor = 1/0.00042257
    y_predicted = y_predicted * scale_factor
    y_test = y_test * scale_factor


    
    st.subheader('주가 예측')
    fig2, ax = plt.figure(figsize=(12,6))
    ax.plot(y_test, 'b', label = 'Actual Price')
    ax.plot(y_predicted, 'r', label = 'Predicted Price')
    ax.xlabel('TIME', fontsize = 20)
    ax.ylabel('Price', fontsize = 20)
    leg = ax.legend()
    st.pyplot(fig2)