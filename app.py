import streamlit as st
from multiapp import MultiApp
from apps import first1, forth1, third1

app = MultiApp()

st.markdown("""
# 주가지수 예측 프로그램
""")

# Add all your application here
app.add_app("메인", first1.app)
app.add_app("LSTM", forth1.app)
app.add_app("NeuralProphet", third1.app)
# The main app
app.run()