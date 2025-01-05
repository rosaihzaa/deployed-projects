import streamlit as st
import pandas as pd

def aboutme():
    st.markdown('''<h1 style='text-align:left;font-size:30px;font-weight:bolder;'>
            Hello!
         </h1>''', unsafe_allow_html=True)
    st.markdown('''
            <h1 style='text-align:left;font-size:15px;font-weight:normal;text-indent:30px; line-height:2;'>
            My name is Rosa Ihza Arlinda, a health graduate with a deep interest in data. 
            Currently, I am deepening my knowledge in the field of data science, 
            focusing on mastering SQL, Python, and data visualization. 
            In addition, I have also learned the basics of cloud computing 
            which helps in understanding the current technology infrastructure. 
            I have good communication skills and analytical skills, which allow me to identify patterns, find solutions, 
            and convey ideas effectively in a team environment.
            </h1>
            ''',
            unsafe_allow_html=True)
    st.markdown('         ')
    
    edu = {'Name':['STIKes Mitra Keluarga','dibimbing.id'],
           'Major': ['Medical Laboratory Technology', 'Data Science'],
           'Year':['2018-2021', '2024']}
    education = pd.DataFrame(edu)
    st.markdown(
        '''
            <h1 style='text-align: left; font-size:20px;'>
               Education
            </h1>
        ''',
        unsafe_allow_html=True
    )
    st.table(education.reset_index(drop=True))
    st.markdown('         ')
    st.markdown(
        '''
            <h1 style='text-align: left; font-size:20px;'>
               Skills
            </h1>
        ''',
        unsafe_allow_html=True
    )
    col1, col2 = st.columns(2)
    with col1:
        st.selectbox('**Hard Skills**', ['Details', 'Python', 'SQL', 'Scripting', 'Machine Learning', 'Data Visualization', 'Web Scraping'])
    with col2:
        st.selectbox('**Tools**', ['Details', 'Jupiter Notebook', 'VScode', 'Tableau', 'Looker', 'Power BI', 'Streamlit', 'PostgreSQL', 'Dbeaver', 'AWS', 'BigQuery'])
    st.markdown('         ')
    st.markdown(
        '''
            <h1 style='text-align: left; font-size:20px;'>
               Certification
            </h1>
        ''',
        unsafe_allow_html=True
    )
    
    st.selectbox('** **',['Details','AWS Certified Cloud Practitioner']) 


