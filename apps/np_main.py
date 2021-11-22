import streamlit as st
from datetime import date
import pandas as pd
import pandas_datareader as data
import pickle
import numpy as np
from plotly import graph_objs as go
import matplotlib.pyplot as plot
from neuralprophet import NeuralProphet
from neuralprophet import set_random_seed
from sklearn.metrics import mean_squared_error

def app():
    global data
    global st
    
    START = '2000-01-01'
    TODAY = date.today().strftime('%Y-%m-%d')

    user_input = st.text_input('Enter Stock Ticker', '^KS11')
    df = data.DataReader(user_input,"yahoo", START, TODAY)

    st.subheader('Data from 2000 - 2021')
    st.write(df.describe())

    st.subheader('현재 주가 차트')
    fig = plot.figure(figsize = (12,6))
    plot.plot(df.Close)
    st.pyplot(fig)

    data = df.reset_index()
    prcp_data = data.rename(columns={'Date': 'ds', 'Close': 'y'})[['ds', 'y']]
    

    m = NeuralProphet(
        n_forecasts=60,
        n_lags=60,
        n_changepoints=100,
        changepoints_range=0.95,
        yearly_seasonality=True,
        weekly_seasonality=True,
        daily_seasonality=True,
        batch_size=64,
        epochs=50,
        learning_rate=1.0,)
    metrics = m.fit(prcp_data, freq='5d')


    st.subheader('주가 예측')
    future = m.make_future_dataframe(prcp_data, n_historic_predictions=True)
    forecast = m.predict(future)
    fig = m.plot(forecast)
    plot.xlabel('Time')
    plot.ylabel('Price')
    plot.legend()
    plot.show();
    st.pyplot(fig)
    """
    st.subheader('추세, 변동성, 자기회귀 그래프')
    m = m.highlight_nth_step_ahead_of_each_forecast(1) # temporary workaround to plot actual AR weights
    fig_param = m.plot_parameters()
    plot.legend()
    plot.show();
    st.pyplot(fig_param)
    """
