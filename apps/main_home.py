import streamlit as st

def app():
    st.title('페이지마다 적용된 예측 알고리즘의 설명')

    st.write('LSTM : KOSPI 주가지수의 종가를 수집하고 딥러닝 기법인 LSTM모델을 사용하여 5일 이상의 KOSPI종가를 예측한다')

    st.write('NeuralProphet :  KOSPI 주가지수의 종가를 수집하고 딥러닝 기법인 NeuralProphet모델을 5일 이상의 KOSPI 주가지수의 종가를 예측한다')

    st.write('본 연구는 과학기술정보통신부 및 정보통신기획평가원의 SW중심대학지원사업의 연구결과로 수행되었음(2018001874004).')