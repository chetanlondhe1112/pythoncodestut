import numpy as np
import streamlit as st
import pandas as pd

# writing anything
st.write("Hello world")

# Writing Dataframe
df = pd.read_excel('DATA.XLSX', sheet_name='8 Days - 3 times', skiprows=2, nrows=4)
st.write(df)

x = np.random.rand(50)
y = np.random.rand(50)
index = np.arange(50)
df2 = pd.DataFrame(data={"Xaxis":x,"Yaxis":y}, index=index)
st.write(df2)
# writing Title
st.title("This is a Test")

# display string formatted as markdown.
st.markdown("Hello **world**!")

# Display text in header formatting
st.header("This is a header")
st.subheader("This is a subheader")

#display text in small font
st.caption("This is written small caption text")

#display code block with optional syntax
st.code("a = 1234")

# DATA DISPLAY ELEMENTS

# Static Tabels
st.table(df)

# CHART ELEMENTS

# Line CHarts
st.line_chart(data=df2)