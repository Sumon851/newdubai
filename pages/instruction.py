import pandas as pd
import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title='NAWE DUBAI INTELLIGENCE PLATFORM',initial_sidebar_state='collapsed',layout='wide')
no_sidebar_style = """
    <style>
        div[data-testid="stSidebarNav"] {display: none;}
    </style>
"""

st.markdown(no_sidebar_style, unsafe_allow_html=True)

st.header('NAWE DUBAI INTELLIGENCE PLATFORM')
st.markdown("---")

st.write(":red[Please Read the Instructions CAREFULLY for further process ]")
st.markdown("---")
st.subheader("Groundwater Level (lowest): ")
st.write("pact the design and execution process of a project. So, for primary evaluation of a project the NAWE digital platform needs the input of lowest groundwater level from ground, in meter unit, recorded in the project area.")


if st.button('Next :arrow_forward:'):
            switch_page('main_new')
