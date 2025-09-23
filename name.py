import streamlit as st

st.title("123456789_10")
name = st.text_input('please type your name :')
menu = st.selectbox('whats your most used app? : ', ['youtube', 'instagram', 'X'])
time = st.slider('using time per day', 0, 12, 3)
if st.button('my digital habit'):
    st.write(f'user {name}! you used {menu} for {time} day')
    st.balloons()
