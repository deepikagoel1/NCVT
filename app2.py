import streamlit as st
import pandas as pd
import time
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode


st.title("NCVT MIS Dashboard")

df = pd.read_csv(r'C:\Users\goeld\Downloads\NCVT_MIS_DASH\iti_trades.csv')

gb = GridOptionsBuilder.from_dataframe(df)
gb.configure_pagination(paginationAutoPageSize=True) #Add pagination
gb.configure_default_column(editable = True, groupable = True)
gb.configure_side_bar() #Add a sidebar
gb.configure_selection('multiple', use_checkbox=True, groupSelectsChildren="Group checkbox select children") #Enable multi-row selection
gridOptions = gb.build()
    
placeholder = st.empty()

df1 = df[['Trade_Name', 'Course_Duration', 'ITI_Name', 'Year', 'ITI_Address', 'State_Name', 'District_Name', 'ITI_Category', 'Principal_Name', 'Principal_Email_id', 'Details']]
  
states = list(df['State_Name'].unique())
state = st.sidebar.multiselect("State",options = states)

if state:
    df = df[df['State_Name'].isin(state)] 
    
    # df = grid_response['data']
    # selected = grid_response['selected_rows'] 
    # df1 = pd.DataFrame(selected) #Pass the selected rows to a new dataframe df   
    # placeholder.dataframe(df1.reset_index())


districts = list(df['District_Name'].unique())
district = st.sidebar.multiselect("District",options = districts)

if district:
    df = df[df['District_Name'].isin(district)]
    # grid_response = AgGrid(
    # df,
    # gridOptions=gridOptions,
    # data_return_mode='AS_INPUT', 
    # update_mode='VALUE_CHANGED', 
    # fit_columns_on_grid_load=False,
    # theme='fresh', #Add theme color to the table
    # enable_enterprise_modules=True,
    # allow_unsafe_jscode = True,
    # height=600, 
    # width='100%',
    # reload_data=True
    # )
    # grid_response = AgGrid(
    # df,
    # gridOptions=gridOptions,
    # data_return_mode='AS_INPUT', 
    # update_mode='VALUE_CHANGED', 
    # fit_columns_on_grid_load=False,
    # theme='blue', #Add theme color to the table
    # enable_enterprise_modules=True,
    # height=350, 
    # width='100%',
    # reload_data=True
    # )
    # new_df = grid_response['data']
    # placeholder.write(df.reset_index())
    # selected = grid_response['selected_rows'] 
    # df1 = pd.DataFrame(selected) #Pass the selected rows to a new dataframe df   
    # placeholder.dataframe(df1.reset_index())
    # placeholder.dataframe(df.reset_index())
    
durations = list(df['Course_Duration'].drop_duplicates())
duration = st.sidebar.multiselect("Course Duration",options = durations)

if duration:
    
    df = df[df['Course_Duration'].isin(duration)]
    placeholder.dataframe(df.reset_index())
    
years = list(df['Year'].drop_duplicates())
year = st.sidebar.multiselect('Year',options = years)

if year:
    df = df[df['Year'].isin(year)]
    placeholder.dataframe(df.reset_index())
    
iti_names = list(df['ITI_Name'].drop_duplicates())
iti_name = st.sidebar.multiselect('ITI Name',options = iti_names)

if iti_name:
    df = df[df['ITI_Name'].isin(iti_name)]
    placeholder.dataframe(df.reset_index())
    
iti_categories = list(df['ITI_Category'].drop_duplicates())
iti_category = st.sidebar.multiselect('ITI Category',options = iti_categories)

if iti_category:
    df = df[df['ITI_Category'].isin(iti_category)]
    placeholder.dataframe(df.reset_index())
    
iti_nstis = list(df['Details'].drop_duplicates())
iti_nsti = st.sidebar.multiselect('ITI/NSTI',options = iti_nstis)

if iti_nsti:
    df = df[df['Details'].isin(iti_nsti)]
    # placeholder.dataframe(df.reset_index())
    
grid_response = AgGrid(
    df,
    gridOptions=gridOptions,
    data_return_mode='AS_INPUT', 
    update_mode='VALUE_CHANGED', 
    fit_columns_on_grid_load=True,
    theme='fresh', #Add theme color to the table
    enable_enterprise_modules=True,
    allow_unsafe_jscode = True,
    height=600, 
    width='100%',
    reload_data=True
    )
    # new_df = grid_response['data']
    # placeholder.write(df.reset_index())


def convert_df(df):
       return df.to_csv().encode('utf-8')

left_column, middle_column, right_column = st.columns(3, gap = 'medium')

total_seats = int(df["Totalseats"].sum())
seats_available = int(df["SeatsAvailable"].sum())
total_units = int(df["TotalUnits"].sum())
units_available = int(df["UnitsAvailable"].sum())
admissions = int(df["Admissions"].sum())

with left_column:
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

csv = convert_df(df)

st.download_button(
   "Press to Download",
   csv,
   "file.csv",
   "text/csv",
   key='download-csv'
)