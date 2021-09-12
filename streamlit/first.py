import forth
import third
import streamlit as st
PAGES = {
    "NeuralProphet": third,
    "LSTM": forth
}
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()