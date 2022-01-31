# widgets
import streamlit as st
import numpy as np
import pandas as pd

x = np.random.rand(50)
y = np.random.rand(50)
index = np.arange(50)
df2 = pd.DataFrame(data={"Xaxis":x,"Yaxis":y}, index=index)

#Button
st.button(label='Hey',help='im saying hi')
if st.button('Hey'):
    st.write('Hello')
    st.write(df2)
else:
    st.write('Hello there')

#selectbox
st.selectbox('Show single day readings in Plot.',options)