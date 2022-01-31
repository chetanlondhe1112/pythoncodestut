# dashboard practice
import pandas as pd
import streamlit as st
import plotly.express as px



#chart_title = input("Enter the title for chart")
st.set_page_config(page_title="Environmental Parameters",page_icon=":bar_chart:",layout="wide")
df=pd.read_excel('DATA - Collection and Analysis - (Rough data).XLSX',sheet_name='8 Days - 3 times',
                        skiprows=2,nrows=24)

# Plots functions
def Bar_Plot(Data):
    fig = px.bar(data_frame=Data, x='Day', y=['Temperature', 'Humidity', 'Moisture',
                                            'pH', 'Gas', 'Pressure'],
                 facet_col='Time (in 24 hr format)', barmode='group', base='Time (in 24 hr format)', width=1100,
                 height=400)
    st.plotly_chart(fig)

def Bar_Plot2(Data,Parameter):
    fig=px.bar(data_frame=Data,x='Day',y=Parameter,barmode='group',color='Time (in 24 hr format)',
               text=Parameter,width=1100, height=400)

    st.plotly_chart(fig)

def Line_plot(Data):
    fig = px.line(data_frame=Data, x='Day',y=['Temperature', 'Humidity', 'Moisture',
                                            'pH', 'Gas', 'Pressure'],facet_col='Time (in 24 hr format)',
                  width=1100, height=400)
    st.plotly_chart(fig)

def Line_plot2(Data,Parameter):
    fig = px.line(data_frame=df, x='Day', y=Parameter, line_group='Time (in 24 hr format)',
                    color='Time (in 24 hr format)', width=1100, height=400, text=Parameter)
    st.plotly_chart(fig)


#st.markdown("---")
st.title("Chart")
Plot_change= st.button(label="Bar Plot",help="To see in Bar Plot")
Plot_change= st.button(label="Line Plot",help="To see in Line Plot")
if Plot_change:
    Line_plot(df)
else:
    Bar_Plot(df)

st.markdown("---")
# per day readings plot

Day_1=df[0:3]
Day_2=df[3:6]
Day_3=df[6:9]
Day_4=df[9:12]
Day_5=df[12:15]
Day_6=df[15:18]
Day_7=df[18:21]
Day_8=df[21:24]

# Parameters
Temperature=df.Temperature
Humidity=df.Humidity
Moisture=df.Moisture
pH=df.pH
Gas=df.Gas
Pressure=df.Pressure

# Option for Single Day plot
st.subheader("Single Day Readings Plot:")
option = st.selectbox('Choose Days for Readings:',
                     options=('Day_1','Day_2','Day_3','Day_4','Day_5','Day_6','Day_7','Day_8'))
if option=='Day_1':
    Bar_Plot(Day_1)
elif option=='Day_2':
    Bar_Plot(Day_2)
elif option=='Day_3':
    Bar_Plot(Day_3)
elif option == 'Day_4':
    Bar_Plot(Day_4)
elif option =='Day_5':
    Bar_Plot(Day_5)
elif option == 'Day_6':
    Bar_Plot(Day_6)
elif option == 'Day_7':
    Bar_Plot(Day_7)
elif option=='Day_8':
    Bar_Plot(Day_8)

st.markdown("---")

# Parameters Over days
st.subheader("Parameter Over Days:")
option2 = st.selectbox('Choose a Parameter:',
                     options=('Temperature', 'Humidity', 'Moisture',
                                            'pH', 'Gas', 'Pressure'))
Plot_change2= st.button(label="Bar_Plot",help="To see in Bar Plot")
Plot_change2= st.button(label="Line_Plot",help="To see in Line Plot")

if option2=='Temperature':
    if Plot_change2:
        Line_plot2(df,Temperature)
    else:
        Bar_Plot2(df,Temperature)
elif option2=='Humidity':
    if Plot_change2:
        Line_plot2(df, Humidity)
    else:
        Bar_Plot2(df, Humidity)
elif option2=='Moisture':
    if Plot_change2:
        Line_plot2(df, Moisture)
    else:
        Bar_Plot2(df, Moisture)
elif option2 == 'pH':
    if Plot_change2:
        Line_plot2(df, pH)
    else:
        Bar_Plot2(df, pH)
elif option2 =='Gas':
    if Plot_change2:
        Line_plot2(df, Gas)
    else:
        Bar_Plot2(df, Gas)
elif option2 == 'Pressure':
    if Plot_change2:
        Line_plot2(df, Pressure)
    else:
        Bar_Plot2(df, Pressure)
