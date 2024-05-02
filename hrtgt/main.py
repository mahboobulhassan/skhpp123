import streamlit as st
import pandas as pd

file='../HRT-ULA-2M.xlsx'
df=pd.read_excel(file)

st.title("Hrt Geotech Instruments")
st.dataframe(df)