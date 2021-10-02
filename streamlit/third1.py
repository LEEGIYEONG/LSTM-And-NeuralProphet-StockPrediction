import streamlit as st
from datetime import date
import pandas as pd
import pandas_datareader as data
import yfinance as yf
from fbprophet import Prophet
from fbprophet.plot import plot_plotly
from plotly import graph_objs as go
import matplotlib.pyplot as plot
from neuralprophet import NeuralProphet
from neuralprophet import set_random_seed
from sklearn.metrics import mean_squared_error

def app():
    global data
    START = '2010-01-01'
    TODAY = date.today().strftime('%Y-%m-%d')

    user_input = st.text_input('Enter Stock Ticker', '^KS11')
    df = data.DataReader(user_input,"yahoo", START, TODAY)

    data = df.reset_index()
    prcp_data = data.rename(columns={'Date': 'ds', 'Close': 'y'})[['ds', 'y']]
    
    st.subheader('Data from 2010 - 2021')
    st.write(df.describe())

    model = NeuralProphet(n_changepoints=100,
                      trend_reg=0.05,
                      yearly_seasonality=False,
                      weekly_seasonality=False,
                      daily_seasonality=False)
    metrics = model.fit(prcp_data, validate_each_epoch=True, 
                    valid_p=0.2, freq='D', 
                    plot_live_loss=True, 
                    epochs=300)
    future = model.make_future_dataframe(prcp_data, periods=365, n_historic_predictions=len(df)) 
    forecast = model.predict(future)

def plot_forecast(model, data, periods, historic_pred=True, highlight_steps_ahead=None):    
    future = model.make_future_dataframe(data, 
                                         periods=periods, 
                                         n_historic_predictions=historic_pred)
    forecast = model.predict(future)
    
    if highlight_steps_ahead is not None:
        model = model.highlight_nth_step_ahead_of_each_forecast(highlight_steps_ahead)
        mbodel.plot_last_forecast(forecast)
    else:    
        model.plot(forecast)

    st.subheader('Predictions vs Actual')
    fig, ax = plot.subplots(figsize=(14, 10)) 
    model.plot(forecast, xlabel="Date", ylabel="Price", ax=ax)
    ax.set_title("KOSPI INDEX", fontsize=28, fontweight="bold")