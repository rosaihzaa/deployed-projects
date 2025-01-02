import streamlit as st
from datetime import datetime
import joblib
import pandas as pd
from xgboost import XGBClassifier
from sklearn.preprocessing import StandardScaler
import streamlit.components.v1 as components
import plotly.express as px

def class_project():
    st.markdown(
        '''
            <h1 style='text-align: center; font-size:25px;'>
               Customer Response Analysis to Deposit Offers 
            </h1>
        ''',
        unsafe_allow_html=True
    )
    st.markdown(
        '''
            <figure style='text-align:center;'>
                <img src='https://images.pexels.com/photos/4386370/pexels-photo-4386370.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2'>
                <figcaption style="font-style:normal; font-size:10px; color:black; text-decoration:none;">
                Pexels.com/Photo By: Kaboompics.com</figcaption>
            </figure>
        ''',
        unsafe_allow_html=True
    )
    st.markdown(
        '''
            <h1 style='text-align: left; font-size:20px;'>
               Introduction
            </h1>
        ''',
        unsafe_allow_html=True
    )
    st.markdown(
        '''<h1 style='text-align:left;font-size:15px;font-weight:normal;text-indent:30px; line-height:2;'>
        Increasing customer interest in deposits can be achived 
        through a good marketing strategy. Predicting potential customers
        who are likely to make deposits is important to optimize the marketing
        target suitable for using the product. Predictions are made with an accurate 
        model to determine whether customers will be interested in the deposit product
        or not.
        </h1>
        ''', unsafe_allow_html=True
    )
    st.markdown(
        '''
            <h1 style='text-align: left; font-size:20px;'>
               Goal
            </h1>
        ''',
        unsafe_allow_html=True
    )
    st.markdown(
        'Understanding customer responses to opening/declining deposit.'
    )

    st.markdown(
        '''
            <h1 style='text-align: left; font-size:20px;'>
               Try to Prediction!
            </h1>
        ''',
        unsafe_allow_html=True
    )

#__________________________________Predict__________________
    # CSS box


    col1, col2, col3 = st.columns(3)

    with col1:
    # Get Month
        date = st.date_input(
        'Choose Campaign Date:',
        min_value=datetime(2020,1,1),
        max_value=datetime(2026,12,31),
        value=datetime.today()
    )
        month = date.month
    # Get Balance
        balance = st.number_input('Enter Balance:',
        min_value= -100000,
        max_value=100000,
        value=0,
        placeholder='Please Insert Number'
        )
    # Get Job
        job = st.selectbox(
        'Choose Job:',
        ['Please Select', 'Office', 'Bussines', 'Technician', 'Household', 'Manual', 'Others'],
    )
        if job == 'Others':
            job = 0
        elif job == 'Office':
            job = 1
        elif job == 'Bussines':
            job = 2
        elif job == 'Technician':
            job = 3
        elif job == 'Household':
            job = 4
        elif job == 'Manual':
            job = 5
        elif job == 'Please Select':
            job = None
    #Get Previous
        cust_new = st.selectbox(
        'Choose Previous Campaign:',
        ['Please Select', 'No Participate', 'Participate'],
    )
        if cust_new == 'No Participate':
            cust_new = 0
        elif cust_new == 'Participate':
            cust_new = 1
        elif cust_new == 'Please Select':
            cust_new = None

    with col2:
    # Get Contact
        contact = st.selectbox(
        'Choose Contact Type:',
        ['Please Select', 'Cellular', 'Telephone', 'Others'],
    )
        if contact == 'Cellular':
            contact = 1
        elif contact == 'Telephone':
            contact =2
        elif contact == 'Others':
            contact =0
        elif contact == 'Please Select':
            contact = None

    # Get F. Stress
        f_stress = st.selectbox(
        'Choose Financial Stress:',
        ['Please Select', 'Low stress', 'Medium stress', 'High stress', 'Critical stress'],
    )
        if f_stress == 'Low stress':
            f_stress = 0
        elif f_stress == 'Medium stress':
            f_stress = 1
        elif f_stress == 'High stress':
            f_stress = 2
        elif f_stress == 'Critical stress':
            f_stress = 3
        elif f_stress == 'Please Select':
            f_stress = None
    #Get Marital
        marital = st.selectbox(
        'Choose Marital Status:',
        ['Please Select', 'Married', 'No Married'],
    )
        if marital == 'Married':
            marital = 0
        elif marital == 'No Married':
            marital = 1
        elif marital == 'Please Select':
            marital = None
    # Get Poutcome
        p_success = st.selectbox(
        'Choose Result Previous Campaign:',
        ['Please Select', 'Success', 'Others'],
    )
        if p_success == 'Success':
            p_success = 0
        elif p_success == 'Others':
            p_success = 1
        elif p_success == 'Please Select':
            p_success = None
    
    with col3:
    #Get Duration
        duration = st.selectbox(
        'Choose Duration Contact:',
        ['Please Select','<100 seconds', '100-300 seconds', '300-600 seconds', '>600 seconds'],
    )
        if duration == '<100 seconds':
            duration = 0
        elif duration == '100-300 seconds':
            duration = 1
        elif duration == '300-600 seconds':
            duration = 2
        elif duration == '>600 seconds':
            duration = 3
        elif duration == 'Please Select':
            duration = None

    data = [balance, contact, month, duration, f_stress, cust_new, job, marital, p_success]
    scaler = joblib.load('scaler.joblib')
    model = joblib.load('modelXGB.joblib')

    columns=['balance', 'contact', 'month', 'duration_cat', 'financial_stress', 
             'previous_campaign', 'job_grouped', 'marital_yes', 'poutcome_success']

    input_data_df = pd.DataFrame([data], columns=columns)

    std_data = scaler.transform(input_data_df)

    prediction = model.predict(std_data)

    with col3:
        if st.button('Predict'):
            if None in data:
                st.markdown(':red[Please select/input correct data.]')
            else:
                if prediction == 0:
                    st.markdown(':red-background[The customer is likely to **reject** opening a deposit account.]')
                elif prediction == 1:
                    st.markdown(':green-background[The customer is likely to **open** a deposit account.]')


    

    
    
    st.markdown('**OR**')
    
    
    upload = st.file_uploader(
        label='Upload File:',
        type=['csv'],
        accept_multiple_files=False
    )
    if upload != None:
        data_csv = pd.read_csv(upload)

        std_data = scaler.transform(data_csv[columns])

        prediction = model.predict(std_data)

        data_csv['prediction'] = prediction

        data_csv['prediction'] = data_csv['prediction'].map({0:'No', 1:'Yes'})

    if st.button('Predict File'):
        column1, column2 = st.columns(2)
        with column1:
            file_csv = data_csv.to_csv(index=False)
            st.download_button(
                    label= 'Download Prediction Results',
                    data=file_csv,
                    file_name='Prediction.csv',
                    mime='text/csv'
            )
        count_data = data_csv['prediction'].value_counts()
        fig = px.pie(values=count_data,
                         names=count_data.index,
                         color=count_data.index,
                         color_discrete_map={'Yes':'orange', 'No':'red'},
                         title='Prediction Results Response Deposito')
        fig.update_layout(title_x=0.25)

        st.plotly_chart(fig)
        st.markdown('''<p style='color:orange;'>Yes : The customer is likely to open a deposit account.</p>
                            <p style='color:red;'>No : The customer is likely to reject opening a deposit account.</p>''', unsafe_allow_html=True)


  
