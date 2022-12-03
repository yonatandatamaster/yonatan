import streamlit as st


st.set_page_config(page_title="Multipage App",
    page_icon=":bar_chart:", layout='wide')

st.title('Live Dashboard Program Kampus A🤖')
st.sidebar.title('Live Dashboard Pencapaian Program')


import pandas as pd
import numpy as np


import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_excel('Data Konsumen A_46_KONSUMEN.xlsx',skiprows = 2)
df.drop(['Unnamed: 0','HP','Harga','Unnamed: 8','Unnamed: 9'],axis = 1,inplace = True)


bumo_count = df['Bumo'].value_counts()
bumo_count = pd.DataFrame({'BUMO':bumo_count.index,'Jumlah Konsumen':bumo_count.values})

st.sidebar.markdown('### BUMO Konsumen')
select = st.sidebar.selectbox('Pilih Jenis Visualisasi',['Bar Chart','Pie Chart'],key='1')

if not st.sidebar.checkbox('Hide',True):
    if select == 'Bar Chart':
        st.markdown('#### Jumlah Konsumen by BUMO (All Brands)')
        fig = px.bar(bumo_count, x= 'BUMO',y = 'Jumlah Konsumen',color = 'BUMO',height = 500,width = 900)
        st.plotly_chart(fig)
       
    else:
        st.markdown('Jumlah Konsumen by BUMO (Top 10 Only)')
        fig = px.pie(bumo_count.sample(n=10),names = 'BUMO',values = 'Jumlah Konsumen',height = 400,width=1000)
        st.plotly_chart(fig)
     
        


df_2 = pd.read_excel('Data Konsumen A_46_KONSUMEN.xlsx',sheet_name = 'DATA_2')
df_2['Change']= (df_2['TOT_SCAN']/df_2['SE_LAB20']).round(2)

st.sidebar.markdown('### Progress Program')
select_2 = st.sidebar.selectbox('Pilih Data',['Outlet Terdata vs Outlet Beli','Sell-In vs Scan'])

if not st.sidebar.checkbox('Hide',True, key = '10'):
    
    if select_2 == 'Outlet Terdata vs Outlet Beli':
        st.markdown('#### Pencapaian Target Outlet')
        fig = px.bar(df_2,x='Minggu', y=['O_BELI','O_TERDATA'],barmode = 'group',height=400,width = 1000)
        st.plotly_chart(fig)
    else:
        st.markdown('#### Pencapaian Target Scan (%)')
        fig = px.bar(df_2,x = 'Minggu',y =['TOT_SCAN','SE_LAB20'],barmode = 'group',height=400,width = 1000)
        fig_2 = px.line(df_2, x ='Minggu',y='Change')
        fig_2.update_layout(template='gridon')
        st.plotly_chart(fig)
        st.plotly_chart(fig_2)

df_3 = pd.read_excel('Data Konsumen A_46_KONSUMEN.xlsx',sheet_name = 'DATA_3')

df_3.columns = ['DSO', 'ID_Outlet', 'Nama_Outlet', 'Alamat', 'Area_Kampus', 'Promotor', 'Program', 'Minggu', 'Brand', 'Pembelian_(bks)', 'latitude', 'longitude']

df_3['Brand'].replace('D SUPER 12','D Super 12',inplace = True)
df_3['Brand'].replace('LA ICE 16','LA Ice 16',inplace = True)
df_3['Brand'].replace('La Ice 16','LA Ice 16',inplace = True)
df_3['Brand'].replace('LA ICE PB 16','LA Ice PB 16',inplace = True)
df_3['Brand'].replace('LA BOLD 16','LA Bold 16',inplace = True)
df_3['Brand'].replace('LA BOLD 20','LA Bold 20',inplace = True)
df_3['Brand'].replace('D. COKLAT 12','D Coklat 12',inplace = True)
df_3['Brand'].replace('D. SUPER 50','D Super 50',inplace = True)

del_val = ['D Coklat 12','D Super 50']
df_3 = df_3[df_3.Brand.isin(del_val)==False]


# In case need groupby and pivot:
#grpd_3 = df_3[['DSO','Program','Brand','Pembelian_(bks)']]
#gby_3 = grpd_3.groupby(['DSO','Brand'],as_index = False).sum()
#pvt_3 = gby_3.pivot(index='DSO',columns = 'Brand')
#pvt_3.columns = pvt_3.columns.droplevel(0)
# -------------------------------


st.sidebar.subheader('Omset by DSO')
choice = st.sidebar.multiselect('Pilih DSO nya:',('Depok','Jakarta Barat','Jakarta Selatan','Jakarta Timur'))

if len(choice)>0:
    st.markdown('#### Breakdown Omset Total')
    choice_data = df_3[df_3.DSO.isin(choice)]
    min_ = choice_data['Minggu'].min().astype('int')
    max_ = choice_data['Minggu'].max().astype('int')
    fig_choice = px.histogram(choice_data, x = 'Brand',y='Pembelian_(bks)', histfunc='sum',facet_col='DSO',color='Brand',labels={'DSO':'Omset'},height=600,width=800)
    st.plotly_chart(fig_choice)
    fig_choice_2 = px.line(choice_data,x='Minggu',y='Pembelian_(bks)')


st.sidebar.markdown('---')
st.sidebar.markdown('---')


# Data Depok A
sheet_id_depok_a = '1LGliLdr2teOiY4QlRhOx73dkJ5JunhvVfiPHrDvx4Uk'

xls_depok_a = pd.ExcelFile(f"https://docs.google.com/spreadsheets/d/{sheet_id_depok_a}/export?format=xlsx")
df_depok_a = pd.read_excel(xls_depok_a,skiprows=1982)
df_depok_a.columns = ['Timestamp', 'Nama', 'Usia',
       'No HP', 'Profesi_notfix',
       'Kode',
       'SOA',
       'email',
       'Profesi',
       'BUMO']

df_depok_a = df_depok_a.loc[:,['Timestamp', 'email', 'Kode',
       'Nama', 'Usia',
       'Profesi',
       'No HP',
       'BUMO',
       'Profesi_notfix',
       'SOA']]


# --------------------------------------------------------------

# Data Jakarta Barat A
sheet_id_jakbar_a = '1dvkWPfxFF_jB3YlCN5tsQCmuiXkLuZOGeb2W6ffLS5k'

xls_jakbar_a = pd.ExcelFile(f"https://docs.google.com/spreadsheets/d/{sheet_id_jakbar_a}/export?format=xlsx")
df_jakbar_a = pd.read_excel(xls_jakbar_a,skiprows = 1304 )
df_jakbar_a.columns = ['Timestamp', 'email', 'Kode',
       'Nama', 'Usia',
       'Profesi',
       'No HP',
       'BUMO',
       'Profesi_notfix',
       'SOA']
# --------------------------------------------------------------

# Data Jakarta Selatan A
sheet_id_jaksel_a = '1C3OlhfRdH2KdqUwME2jqedHx33oKFFR8nE0g-aMNsn4'

xls_jaksel_a = pd.ExcelFile(f"https://docs.google.com/spreadsheets/d/{sheet_id_jaksel_a}/export?format=xlsx")
df_jaksel_a = pd.read_excel(xls_jaksel_a,skiprows = 697 )
df_jaksel_a.columns = ['Timestamp', 'email', 'Kode',
       'Nama', 'Usia',
       'Profesi',
       'No HP',
       'BUMO',
       'Profesi_notfix',
       'SOA']

# --------------------------------------------------------------

### Data Append A

data_append_a = pd.concat([df_depok_a,df_jakbar_a, df_jaksel_a],ignore_index = True)

bumo_a_terbanyak = data_append_a['BUMO'].value_counts().to_frame().reset_index(names=['Brand'])

col1, col2, col3 = st.columns(3)
with col1:
    st.header('Profil Konsumen Kampus')
    select_kampus = st.selectbox('Pilih ya',['Kampus A','Kampus B'])
    if select_kampus == 'Kampus A':
        st.markdown('Jumlah konsumen tercatat dari awal program hingga saat ini terlihat paling dominan trial yaitu dari BUMO : '+ str(bumo_a_terbanyak.iloc[0,0]).upper()+" " + 'sebanyak '+str(bumo_a_terbanyak.iloc[0,1])+" " + 'orang.')
        with col2:
            fig = px.histogram(data_append_a,x = 'BUMO',y = 'Usia',
                                histfunc='count', 
                                labels={'BUMO':'Data BUMO Masuk'}).update_layout(yaxis_title='Jumlah Scan by BUMO')
            st.plotly_chart(fig)
    else:
        with col2:
            datadata = data_append_a[data_append_a['SOA']=='dari spg']
            fig = px.histogram(datadata,x = 'BUMO',y = 'Usia',
                               histfunc='count', 
                               labels={'BUMO':'Data BUMO Masuk'}).update_layout(yaxis_title='Jumlah Konsumen by BUMO')
            st.plotly_chart(fig)
            
