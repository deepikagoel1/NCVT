import pandas as pd
import plotly.express as px
import streamlit as st
import numpy as np
from collections.abc import Iterable

from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode

data = pd.read_csv(r'C:\Users\goeld\Downloads\iti_trades.csv')


# TOP KPI's
total_seats = int(data["Totalseats"].sum())
seats_available = int(data["SeatsAvailable"].sum())
total_units = int(data["TotalUnits"].sum())
units_available = int(data["UnitsAvailable"].sum())
admissions = int(data["Admissions"].sum())
left_column, middle_column, right_column = st.columns(3, gap = 'medium')
with left_column:
    # st.metric(label = "Total Seats", value = f"{total_seats}")
    st.subheader("Total Seats")
    st.subheader(f"{total_seats}")
    st.subheader("Seats Available")
    st.subheader(f"{seats_available}")
    
with middle_column:
    st.subheader("Total Units")
    st.subheader(f"{total_units}")
    st.subheader("Units Available")
    st.subheader(f"{units_available}")
with right_column:
    st.subheader("Admissions")
    st.subheader(f"{admissions}")

st.markdown("""---""")


# AgGrid(data)

gb = GridOptionsBuilder.from_dataframe(data)
gb.configure_pagination(paginationAutoPageSize=True) #Add pagination
gb.configure_side_bar() #Add a sidebar
gb.configure_selection('multiple', use_checkbox=True, groupSelectsChildren="Group checkbox select children") #Enable multi-row selection
gridOptions = gb.build()

grid_response = AgGrid(
    data,
    gridOptions=gridOptions,
    data_return_mode='AS_INPUT', 
    update_mode='MODEL_CHANGED', 
    fit_columns_on_grid_load=False,
    theme='blue', #Add theme color to the table
    enable_enterprise_modules=True,
    height=350, 
    width='100%',
    reload_data=True
)

data = grid_response['data']
selected = grid_response['selected_rows'] 
df = pd.DataFrame(selected) #Pass the selected rows to a new dataframe df

# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

