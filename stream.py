import streamlit as st
import joblib
import pandas as pd 



st.title('Phishing Detection')

path="./dataset.csv"
df=pd.read_csv(path)
df.drop(columns='index',inplace=True)

Cols = df.columns
inputData = []
for col in Cols:
  col = st.number_input(format(col.title()) ,key=col)
  inputData.append(col)

if st.button('Detect'):
  loaded_model = joblib.load('tree.pkl')
  result = loaded_model.predict([inputData])
  
  for r in result:
    if r == 0:
      st.success('Not Phishing')
    else:
      st.success('Phishing')