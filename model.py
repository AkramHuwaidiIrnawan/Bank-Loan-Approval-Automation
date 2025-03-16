import streamlit as st
import pandas as pd
import joblib
from PIL import Image

df = pd.read_csv('loan_approval_dataset.csv')    
st.write(df) 

def user_input():
    loan_term = st.selectbox('loan_term',df[' loan_term'].unique())
    cibil_score = st.number_input('cibil_score ')
    

    data = {
        'loan_term': loan_term,
        'cibil_score': cibil_score 
        }
    features = pd.DataFrame(data, index=[0])
    return features


input = user_input()

st.subheader('User Input')
st.write(input)

load_model = joblib.load("model.pkl")

if st.button("Predict"):
    prediction = load_model.predict(input)
    st.header(f'Harga prediksi  : {prediction}')
        
    if prediction ==1 :
        prediction = 'Loan anda aprrove  '
    else:
        prediction = 'Loan anda tidak aprove '

    st.subheader('Kesimpulan Model  : ')
    st.header(prediction)