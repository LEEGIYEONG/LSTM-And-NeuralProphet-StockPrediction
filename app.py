import streamlit as st
from multiapp import MultiApp
from apps import main_home, LSTM_main, np_main

app = MultiApp()

st.markdown("""
# 주가지수 예측 프로그램
""")

# Add all your application here
app.add_app("메인", main_home.app)
app.add_app("LSTM", LSTM_main.app)
app.add_app("NeuralProphet", np_main.app)
# The main app
app.run()