# writing on browser
import streamlit as st
import pandas as pd

df=pd.read_excel('DATA - Collection and Analysis - (Rough data).XLSX',sheet_name='8 Days - 3 times',
                        skiprows=2,nrows=24,engine='openpyxl')

st.write("Hello world")
st.write(df)