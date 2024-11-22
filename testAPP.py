import streamlit as st
import pandas as pd
import os
import plotly.express as px
import plotly
import plotly.graph_objects as go

st.set_page_config(page_title="Hello World", page_icon=":bar_chart:", layout="wide")
st.title(" :bar_chart: HELLO WORLD")

st.markdown('<style>div.block-container{padding-top:1rem;}</style>',unsafe_allow_html=True)

fl = st.file_uploader(":file_folder: Upload a file",type=(["csv","xlsx","xls"]))
if fl is not None:
    filename = fl.name
    st.write(filename)
    df = pd.read_excel(filename)
else:
    os.chdir(r"C:\Users\BullmaM\OneDrive - Jacobs\Desktop\PythonScripts")
    df=pd.read_excel("output.xlsx")
    
col1,col2, col3 = st.columns((3))
table_data1 = df.groupby('Project Name')['EAC'].sum().reset_index()
with col1:
    st.subheader("test")

    fig = px.bar(table_data1, x='Project Name',y='EAC',title='EAC by Project')
    st.plotly_chart(fig)
    
with col2:
    st.subheader("Test 2")
    
    df=table_data1[table_data1['EAC']>1500000]
    fig = px.bar(df, x='Project Name',y='EAC',title='EAC by Project')
    st.plotly_chart(fig)
    
with col3:
    st.bar_chart(data=df, x='Project Name',y='EAC')