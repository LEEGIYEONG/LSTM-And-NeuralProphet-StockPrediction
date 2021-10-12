import streamlit as st
from multiapp import MultiApp
from apps import first1, forth1, third1

app = MultiApp()

st.markdown("""
# 메인 홈페이지
This multi-page app is using the [streamlit-multiapps](https://github.com/upraneelnihar/streamlit-multiapps) framework developed by [Praneel Nihar](https://medium.com/@u.praneel.nihar). Also check out his [Medium article](https://medium.com/@u.praneel.nihar/building-multi-page-web-app-using-streamlit-7a40d55fa5b4).
""")

# Add all your application here
app.add_app("메인", first1.app)
app.add_app("LSTM", forth1.app)
app.add_app("NeuralProphet", third1.app)
# The main app
app.run()