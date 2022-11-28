import streamlit as st


st.set_page_config(page_title="Multipage App",
    page_icon=":bar_chart:",
    layout="wide")

st.title('Live Dashboard Program Kampus A🤖')
st.sidebar.title('Live Dashboard Pencapaian Program')


import pandas as pd
import numpy as np


import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go




df = pd.read_excel('Data Konsumen A_46_KONSUMEN.xlsx',skiprows = 2)
df.drop(['Unnamed: 0','HP','Harga','Unnamed: 8','Unnamed: 9'],axis = 1,inplace = True)

grouped_1 = df[['Bumo','Profesi','Usia']].groupby(['Bumo'],as_index = False).mean()

bumo_count = df['Bumo'].value_counts()
bumo_count = pd.DataFrame({'BUMO':bumo_count.index,'Jumlah Konsumen':bumo_count.values})

st.sidebar.markdown('### BUMO Konsumen')
select = st.sidebar.selectbox('Pilih Jenis Visualisasi',['Bar Chart','Pie Chart'],key='1')

if not st.sidebar.checkbox('Hide',True):
    
    if select == 'Bar Chart':
        st.markdown('Jumlah Konsumen by BUMO (All Brands)')
        fig = px.bar(bumo_count, x= 'BUMO',y = 'Jumlah Konsumen',color = 'BUMO',height = 500)
        st.plotly_chart(fig)
    else:
        st.markdown('Jumlah Konsumen by BUMO (Top 8 Only)')
        fig = px.pie(bumo_count.head(8),names = 'BUMO',values = 'Jumlah Konsumen',)
        st.plotly_chart(fig)

    
st.sidebar.markdown('### Does Cing love me?')
select = st.sidebar.selectbox('Pilih Yak!',['I love my BF yonatan so much','Nahh i hate him!'],key='2')

if not st.sidebar.checkbox('Hide',True, key='3'):
    if select == 'I love my BF yonatan so much':
        st.markdown('### I LOVE YOU TOO!!')
    else:
        st.markdown('oh wow, how much u hate him?')
        st.selectbox('Pilih huh',['Benci bet','mayan benci'])















