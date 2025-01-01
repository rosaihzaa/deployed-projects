
import streamlit as st
import os
from aboutme import aboutme
from class_project import class_project
from closing import closing

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'C:\Users\inioc\streamlit-porto\bank-marketing-project-446413-a16e16990932.json'

st.markdown('''<h1 style='text-align:center;font-size:40px;font-weight:bolder;color:#FF4B4B; line-height:2;'>
            Rosa's Portfolio in Data Science 
         </h1>''', unsafe_allow_html=True)
tab1, tab2 = st.tabs(['About Me', 'Classification Project'])

#About me
with tab1:
    aboutme()
    st.markdown('         ')
    st.markdown('         ')
    st.markdown('         ')
    st.markdown('         ')
    closing()
    
with tab2:
    class_project()
    st.markdown('         ')
    st.markdown('         ')
    st.markdown('         ')
    st.markdown('         ')
    closing()
    
