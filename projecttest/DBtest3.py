import streamlit as st
import pandas as pd
import plotly.express as px


def main():
    st.title("Dashboard")
    df1 = pd.read_excel('DATA.XLSX', '8 Days - 3 times', skiprows=2, nrows=4)
    st.dataframe(df1)
    fig = px.bar(data_frame = df1, x='Day', y=['Temperature','Humidity','Moisture','pH','Gas','Pressure'], barmode='group')
    st.plotly_chart(fig)


if __name__ == '__main__':
    main()
