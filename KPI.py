import streamlit as st


st.set_page_config(page_title="Depok Promotor KPI",
    page_icon=":bar_chart:", layout='wide')

st.title('Depok Program KPI')
st.sidebar.title('Periode Des - Mar 23')


import pandas as pd
import numpy as np


import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

import matplotlib.pyplot as plt
import seaborn as sns

#---- Loading Data Pemukiman

def load_pemu_table():
    data = pd.read_excel('File KPI.xlsx', sheet_name = 'Pemukiman')
    data_gb = data[['Minggu','Promotor','ID Outlet',
                    'Penukaran']].groupby(['Minggu','Promotor','ID Outlet'],
                                          as_index = False).sum()
    
    data_gb.rename_axis(None,inplace = True)
    #data_gb = data_gb[data_gb.Promotor.isin(promotor)]
    data_pvt = data_gb.pivot_table(index = 'Promotor', 
                                   columns = 'Minggu',values = 'ID Outlet',aggfunc = 'count', fill_value = 0).rename_axis(None)
    data_pvt = data_pvt.astype(float)
    data_pvt['AVG OAP'] = data_pvt.mean(axis=1)
    data_pvt.reset_index(names = 'Promotor', inplace = True)
    
    target = pd.read_excel('File KPI.xlsx', sheet_name = 'Target Program')
    target.replace(np.nan,0, inplace = True)
    target.iloc[:,1:] = target.iloc[:,1:].astype(float)
    
    kpi_pemu = data_pvt[['Promotor','AVG OAP']].merge(target[['Promotor','MAA Pemukiman']])
    kpi_pemu['% AVG KPI'] = ((kpi_pemu['AVG OAP'] / kpi_pemu['MAA Pemukiman'])*100).map(float).round(1).map(str) +'%'
    kpi_pemu.sort_values(by = '% AVG KPI', ascending = False, inplace = True)
    return kpi_pemu                      


def load_pemu_chart():
    data = pd.read_excel('File KPI.xlsx', sheet_name = 'Pemukiman')
    data_gb = data[['Minggu','Promotor','ID Outlet',
                    'Penukaran']].groupby(['Minggu','Promotor','ID Outlet'],
                                          as_index = False).sum()
    
    data_gb.rename_axis(None,inplace = True)
    #data_gb = data_gb[data_gb.Promotor.isin(promotor)]
    data_pvt = data_gb.pivot_table(index = 'Promotor', 
                                   columns = 'Minggu',values = 'ID Outlet',aggfunc = 'count', fill_value = 0).rename_axis(None)
    data_pvt = data_pvt.astype(float)
    data_pvt['AVG OAP'] = data_pvt.mean(axis=1)
    data_pvt.reset_index(names = 'Promotor', inplace = True)
    
    target = pd.read_excel('File KPI.xlsx', sheet_name = 'Target Program')
    target.replace(np.nan,0, inplace = True)
    target.iloc[:,1:] = target.iloc[:,1:].astype(float)
    
    kpi_pemu = data_pvt[['Promotor','AVG OAP']].merge(target[['Promotor','MAA Pemukiman']])
    kpi_pemu['% AVG KPI'] = ((kpi_pemu['AVG OAP'] / kpi_pemu['MAA Pemukiman'])*100).map(float).round(1)
    kpi_pemu.sort_values(by = '% AVG KPI', ascending = False, inplace = True)
    return kpi_pemu 

promotor=['ADE FAHMI']

pemu_tab = load_pemu_table()
pemu_cha = load_pemu_chart()

fig = px.bar(pemu_cha, x = 'Promotor', y ='% AVG KPI').update_layout(yaxis_ticksuffix = '% Aktif vs Target')

st.header('Program Pemukiman')
st.markdown('Perhitungan persentase dihitung dari rata-rata Outlet Aktif per Minggu dibagi dengan Target Outlet')
st.plotly_chart(fig)


