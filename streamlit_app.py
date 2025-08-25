import streamlit as st
import pandas as pd


st.title('🎈 Machine Learning App')

st.write('This app builds a machine learning model')

with st.expander("Data"):
  st.write("**Raw data**")
  df = pd.read_csv("https://raw.githubusercontent.com/dataprofessor/data/refs/heads/master/penguins_cleaned.csv")
  df
  
  st.write('**x**')
  x = df.drop('species', axis=1)
  x

  st.write('**Y**')
  y = df.species
  y

with st.expander('Data visualization'):
  #"bill_length_mm","bill_depth_mm","flipper_length_mm","body_mass_g"
  st.scatter_chart(data=df, x='bill_length_mm', y='body_mass_g', color='species')

