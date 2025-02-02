import streamlit as st
from switchpage import switch_page
st.set_page_config(initial_sidebar_state="collapsed")

with st.form('my_form'):
    st.session_state.working_style = st.radio('What\'s your working style?', ['Artistic','Enterprising','Investigative','Organized','Practical','Service-Oriented'])
    submitted = st.form_submit_button("Continue")
    if submitted:
        switch_page('generate')