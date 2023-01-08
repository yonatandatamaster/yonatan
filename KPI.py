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

# PROGRAM PEMUKIMAN-------------

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
    kpi_pemu[['AVG OAP', 'MAA Pemukiman']] = kpi_pemu[['AVG OAP', 'MAA Pemukiman']].astype(str).round(1)
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



pemu_tab = load_pemu_table()
pemu_cha = load_pemu_chart()

fig = px.bar(pemu_cha, x = 'Promotor', y ='% AVG KPI',height =300, width = 450).update_layout(yaxis_ticksuffix = '% Aktif vs Target')

st.header('Program Pemukiman')
st.markdown('Perhitungan persentase 👇 dihitung dari rata-rata Outlet Aktif per Minggu dibagi dengan Target Outlet')
st.plotly_chart(fig)

st.markdown('Score terbaik diraih ' + str(pemu_tab.iloc[0,0]) + ' dengan % Outlet Aktif Program Pemukiman sebesar  ' + str(pemu_tab.iloc[0,3]) + '!')

pemu_tab2 =pemu_tab.set_index('Promotor')

colpemu1, colpemu2 =st.columns([4,6])
with colpemu1:
    st.dataframe(pemu_tab2, use_container_width= True)

st.text(' ')
st.text(' ')
st.text(' ')
st.text(' ')

## PROGRAM OJOL ---------------------------
def load_ojol_table():
    data = pd.read_excel('File KPI.xlsx', sheet_name = 'Ojol')
    data = data.replace(np.nan, 0)
    data['Total Cangkang'] = data[['D King 12','D Coklat 12','Jump 16']].sum(axis = 1)
    
    data_gb = data[['Minggu','Promotor','ID Outlet',
                    'Total Cangkang']].groupby(['Minggu','Promotor','ID Outlet'],
                                          as_index = False).sum()
    

    data_gb.rename_axis(None,inplace = True)
    data_pvt = data_gb.pivot_table(index = 'Promotor', 
                                   columns = 'Minggu',values = 'ID Outlet',aggfunc = 'count', fill_value = 0).rename_axis(None)
    data_pvt = data_pvt.astype(float)
    data_pvt['AVG OAP'] = data_pvt.mean(axis=1)
    data_pvt.reset_index(names = 'Promotor', inplace = True)
    
    target = pd.read_excel('File KPI.xlsx', sheet_name = 'Target Program')
    target.replace(np.nan,0, inplace = True)
    target.iloc[:,1:] = target.iloc[:,1:].astype(float)
    
    kpi_pemu = data_pvt[['Promotor','AVG OAP']].merge(target[['Promotor','MAA Ojol']])
    kpi_pemu['% AVG KPI'] = ((kpi_pemu['AVG OAP'] / kpi_pemu['MAA Ojol'])*100).map(float).round(1).map(str) +'%'
    kpi_pemu.sort_values(by = '% AVG KPI', ascending = False, inplace = True)
    kpi_pemu[['AVG OAP', 'MAA Ojol']] = kpi_pemu[['AVG OAP', 'MAA Ojol']].astype(str).round(1)

    return kpi_pemu


def load_ojol_chart():
    data = pd.read_excel('File KPI.xlsx', sheet_name = 'Ojol')
    data = data.replace(np.nan, 0)
    data['Total Cangkang'] = data[['D King 12','D Coklat 12','Jump 16']].sum(axis = 1)
    
    data_gb = data[['Minggu','Promotor','ID Outlet',
                    'Total Cangkang']].groupby(['Minggu','Promotor','ID Outlet'],
                                          as_index = False).sum()
    

    data_gb.rename_axis(None,inplace = True)
    data_pvt = data_gb.pivot_table(index = 'Promotor', 
                                   columns = 'Minggu',values = 'ID Outlet',aggfunc = 'count', fill_value = 0).rename_axis(None)
    data_pvt = data_pvt.astype(float)
    data_pvt['AVG OAP'] = data_pvt.mean(axis=1)
    data_pvt.reset_index(names = 'Promotor', inplace = True)
    
    target = pd.read_excel('File KPI.xlsx', sheet_name = 'Target Program')
    target.replace(np.nan,0, inplace = True)
    target.iloc[:,1:] = target.iloc[:,1:].astype(float)
    
    kpi_pemu = data_pvt[['Promotor','AVG OAP']].merge(target[['Promotor','MAA Ojol']])
    kpi_pemu['% AVG KPI'] = ((kpi_pemu['AVG OAP'] / kpi_pemu['MAA Ojol'])*100).map(float).round(1).map(str) +'%'
    kpi_pemu.sort_values(by = '% AVG KPI', ascending = False, inplace = True)
    kpi_pemu[['AVG OAP', 'MAA Ojol']] = kpi_pemu[['AVG OAP', 'MAA Ojol']].astype(float).round(1)

    return kpi_pemu




ojol_tab = load_ojol_table()
ojol_cha = load_ojol_chart()


fig2 = px.bar(ojol_cha, x = 'Promotor', y ='% AVG KPI',height =300, width = 450).update_layout(yaxis_ticksuffix = '% Aktif vs Target')

st.header('Program Ojol')
st.markdown('Perhitungan persentase 👇 dihitung dari rata-rata Outlet Aktif per Minggu dibagi dengan Target Outlet')
st.plotly_chart(fig2)

st.markdown('Score terbaik diraih ' + str(ojol_tab.iloc[0,0]) + ' dengan % Outlet Aktif Program Ojol sebesar  ' + str(ojol_tab.iloc[0,3]) + '!')

ojol_tab2 = ojol_tab.set_index('Promotor')

colojol1, colojol2 = st.columns([4,6])
with colojol1:
    tab1, tab2 = st.tabs(['TOTAL','Minggu-an'])
    with tab1:
        st.dataframe(ojol_tab2, use_container_width= True)
    with tab2:
        def load_ojol_table_weekly():
            data = pd.read_excel('File KPI.xlsx', sheet_name = 'Ojol')
            data = data.replace(np.nan, 0)
            data['Total Cangkang'] = data[['D King 12','D Coklat 12','Jump 16']].sum(axis = 1)
            
            data_gb = data[['Minggu','Promotor','ID Outlet',
                            'Total Cangkang']].groupby(['Minggu','Promotor','ID Outlet'],
                                                  as_index = False).sum()
            

            data_gb.rename_axis(None,inplace = True)
            data_pvt = data_gb.pivot_table(index = 'Promotor', 
                                           columns = 'Minggu',
                                           values = 'ID Outlet',aggfunc = 'count', fill_value = 0).rename_axis(None)
            data_pvt_t = data_pvt.transpose()
            return data_pvt_t
        ojol_wely = load_ojol_table_weekly()
        fig = px.line(ojol_wely, height = 280, width= 425).update_layout(yaxis_ticksuffix = ' Outlet Aktif').update_xaxes(dtick = 1)
        st.plotly_chart(fig)





