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


df_2 = pd.read_excel('Data Konsumen A_46_KONSUMEN.xlsx',sheet_name = 'DATA_2')
df_2['Change']= (df_2['TOT_SCAN']/df_2['SE_LAB20']).round(2)

st.sidebar.markdown('### Progress Program')
select_2 = st.sidebar.selectbox('Pilih Data',['Outlet Terdata vs Outlet Beli','Sell-In vs Scan'])

if not st.sidebar.checkbox('Hide',True, key = '10'):
    
    if select_2 == 'Outlet Terdata vs Outlet Beli':
        st.markdown('#### Pencapaian Target Outlet')
        fig = px.bar(df_2,x='Minggu', y=['O_BELI','O_TERDATA'],barmode = 'group')
        st.plotly_chart(fig)
    else:
        st.markdown('#### Pencapaian Target Scan')
        fig = px.bar(df_2,x = 'Minggu',y =['TOT_SCAN','SE_LAB20'],barmode = 'group')
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
grpd_3 = df_3[['DSO','Program','Brand','Pembelian_(bks)']]
gby_3 = grpd_3.groupby(['DSO','Brand'],as_index = False).sum()
pvt_3 = gby_3.pivot(index='DSO',columns = 'Brand')
pvt_3.columns = pvt_3.columns.droplevel(0)
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
    choice_2 = st.slider('Pilih Minggu',0,5)

st.sidebar.markdown('---')
st.sidebar.markdown('---')

min_ = df_3['Minggu'].min()

print(type(min_))
listt = [1,2,3,4,5,5,5,5]

huhu = df_3['Minggu'].values

## print(np.unique(df_3['Minggu'].values.tolist()))

sheet_id = '1UgUrsuKOpxROHkvraJVdHvcWMRZplLShbiTP_izNTnM'

xls = pd.ExcelFile(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=xlsx")
dfdf = pd.read_excel(xls)
dfdf.columns = ['Timestamp', 'Email', 'Kode',
       'Nama', 'Usia',
       'Profesi_notfix',
       'No_HP',
       'BUMO',
       'Profesi',
       'SOA']



datadata = dfdf[['BUMO','Profesi']]

fig = px.histogram(dfdf[dfdf['Profesi']=="Mahasiswa"],x='BUMO',y = 'Usia',histfunc='avg',color='BUMO')
st.plotly_chart(fig)












