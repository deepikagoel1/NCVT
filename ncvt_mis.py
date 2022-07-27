import pandas as pd
import plotly.express as px
import streamlit as st
import numpy as np
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode



def run():
# file1 = r
    data = pd.read_csv(r'C:\Users\goeld\Downloads\iti_trades.csv')

    # print(data)
    st.set_page_config(page_title = "NCVT MIS DASHBOARD", layout = "wide")

    # states = list(data['State_Name'].drop_duplicates())
    

    # st.sidebar.header("Please Filter Here:")
    # state = st.sidebar.multiselect("State",
    #                                    options = states
    #                                    )
    
    # districts = data['District_Name'].drop_duplicates()
    # districts = list(districts.loc[data['State_Name']==state])
    
    
    # durations = list(data['Course_Duration'].drop_duplicates())
    
    
    # district = st.sidebar.multiselect("District",
    #                                    options = districts
    #                                    )
    # duration =  st.sidebar.multiselect("Course_Duration",
    #                                    options = durations
    #                                    )
    
    sidebars = {}
    
    col = data.columns
    
    column =['Trade_Name', 'Course_Duration', 'ITI_Name', 'Year', 'State_Name',
              'District_Name', 'ITI_Category',
              ]
    
  
    
    st.title("NCVT MIS DASHBOARD")
    
    st.dataframe(data)
    
    # data = data[data['State_Name'].isin(state)]
    # data = data[data['District_Name'].isin(district)]
    # data = data[data['Course_Duration'].isin(duration)]
    
    # data_selection = data.query(
    #         "state == @state & district == @district"
    #     )
    
    # data['']
    st.title("Filtered Data")
    
    
    
    
    # state = st.sidebar.multiselect(
    # "Select the State",
    # options=data["State_Name"].unique())

    # district = st.sidebar.multiselect(
    #     "Select the Districts",
    #     options=data["District_Name"].unique())

    # trades = st.sidebar.multiselect(
    #     "Select the Trades",
    #     options=data["Trade_Name"].unique())
    
    # crd = st.sidebar.multiselect(
    #     "Select the Duration",
    #     options=data["Course_Duration"].unique())
    
    # iti_name =  st.sidebar.multiselect(
    #     "Select ITI",
    #     options=data["ITI_Name"].unique())
    
    # year =  st.sidebar.multiselect(
    #     "Select Year",
    #     options=data["Year"].unique())
    
    # iti_category = st.sidebar.multiselect(
    #     "Select Category of ITI",
    #     options=data["ITI_Category"].unique())

    # data_selection = data.query(
    #     "State_Name == @state and District_Name == @district and Trade_Name == @trades and Course_Duration == @crd and ITI_Name == @iti_name and Year == @year and ITI_Category of ITI == @iti_category"
    #         )
    # st.dataframe(data_selection)
    
   
    
    for y in column:
        if (data[y].dtype == np.object):
            ucolumns=list(data[y].unique())
            sidebars[y+"filter"]=st.sidebar.multiselect('Filter '+y, ucolumns)
    
    st.write(sidebars)
    
    

    # with open(r'C:\Users\goeld\Downloads\trades_iti.xlsx', encoding="utf-8",  errors="ignore") as f:
    #     st.download_button("Download Excel File", f)

run()
