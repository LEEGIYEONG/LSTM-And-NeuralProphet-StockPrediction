import streamlit as st

def app():
    st.title('페이지마다 적용된 예측 알고리즘의 설명')

    st.write('LSTM : KOSPI 주가지수의 종가를 수집하고 딥러닝 기법인 LSTM모델을 사용하여 KOSPI종가를 예측한다')

    st.write('NeuralProphet모델을 사용하여 KOSPI 주가지수의 종가를 예측한다')

    st.write('BERT 자연어 모델을 통한 경제뉴스 감성분류하여 주가지수를 예측한다')

    st.write('본 연구는 과학기술정보통신부 및 정보통신기획평가원의 SW중심대학지원사업의 연구결과로 수행되었음(2018001874004).')