import streamlit as st

def app():
    st.title('예측 알고리즘의 설명')

    st.write('LSTM : KOSPI 주가지수의 종가를 수집하고 딥러닝 기법인 LSTM모델을 사용하여 5일 이상의 KOSPI종가를 예측한다. (X 축 : 날짜, Y 축 : 주가 가격)')
    
    st.write('NeuralProphet : KOSPI 주가지수의 종가를 수집하고 딥러닝 기법인 NeuralProphet모델을 사용하여 5일 이상의 KOSPI종가를 예측한다. (X 축 : 날짜, Y 축 : 주가 가격)')

    st.write('예측 방법 : 위 네비게이션 바에서 LSTM, NeuralProphet 페이지로 이동 시 주가지수의 데이터 프레임, 그래프 출력 이후 자동으로 접속 시점을 기준으로 예측을 실행한다. ')

    st.write('본 연구는 과학기술정보통신부 및 정보통신기획평가원의 SW중심대학지원사업의 연구결과로 수행되었음(2018001874004).')
