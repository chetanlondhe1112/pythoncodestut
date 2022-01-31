import streamlit as st
import pandas as pd
import plotly.express as px


def main():
    st.title("Dashboard")
    df1 = pd.read_excel('DATA - Collection and Analysis - (Rough data).XLSX', sheet_name='8 Days - 3 times',
                        skiprows=2)
    st.dataframe(df1)

    fig = px.bar(data_frame=df1, x='Day', y=['Temperature', 'Humidity', 'Moisture', 'pH', 'Gas', 'Pressure'], barmode='group', base='Time (in 24 hr format)')
    fig2 = px.bar(data_frame=df1, x='Day', y=['Temperature', 'Humidity', 'Moisture', 'pH', 'Gas', 'Pressure'], facet_col='Time (in 24 hr format)',barmode='group')
    fig3 = px.bar(data_frame=df1, x='Day', y=['Temperature', 'Humidity', 'Moisture', 'pH', 'Gas', 'Pressure'], facet_row='Time (in 24 hr format)',barmode='group')
    fig4 = px.bar(data_frame=df1, x='Time (in 24 hr format)', y=['Temperature', 'Humidity', 'Moisture', 'pH', 'Gas', 'Pressure'],barmode='group')
    fig5 = px.line(data_frame=df1, x='Day', y=['Temperature', 'Humidity', 'Moisture', 'pH', 'Gas', 'Pressure'],)
    st.plotly_chart(fig)
    st.plotly_chart(fig2)
    st.plotly_chart(fig3)
    st.plotly_chart(fig4)
    st.plotly_chart(fig5)
    fig_1 = px.line(data_frame=df1, x='Day', y='Temperature', markers=True, facet_row='Time (in 24 hr format)')
    st.plotly_chart(fig_1)


    st.sidebar.header("Please Filter Here:")
    Temperature = st.sidebar.multiselect("select The Tab:", options=df1["Temperature"].unique(), default=df1["Temperature"].unique())
    df1_selection = df1.querry("Temperature==@Temperature")
if __name__ == '__main__':
    main()
