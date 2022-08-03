import streamlit as st 
import pandas as pd
import numpy as np
import time
import plotly.express as px
from collections.abc import Iterable
# from streamlit_kpi_metric import metric, metric_row
from streamlit_metrics import metric, metric_row
 
df = pd.read_csv('iti_trades.csv')

df1 = df[['Trade_Name', 'Course_Duration', 'ITI_Name', 'Year', 'ITI_Address', 'State_Name', 'District_Name', 'ITI_Category', 'Principal_Name', 'Principal_Email_id', 'Details']]
# df_result_search = pd.DataFrame() 
# st.title("NCVT MIS DASHBOARD")
# st.dataframe(df1, width=1000, height=500)

st.set_page_config(
    page_title="Data Science Dashboard",
    page_icon="✅",
    layout="wide",
)


# creating a single-element container.
placeholder = st.empty()


states = list(df1['State_Name'].unique())
state = st.sidebar.multiselect("State",options = states)
df1 = df1[df1['State_Name'].isin(state)]


districts = list(df1['District_Name'].unique())
district = st.sidebar.multiselect("District",options = districts)
df1 = df1[df1['District_Name'].isin(district)]
# st.dataframe(df, width=1000, height=500)

durations = list(df1['Course_Duration'].drop_duplicates())
duration = st.sidebar.multiselect("Course Duration",options = durations)
df1 = df1[df1['Course_Duration'].isin(duration)]

years = list(df1['Year'].drop_duplicates())
year = st.sidebar.multiselect('Year',options = years)
df1 = df1[df1['Year'].isin(year)]

iti_names = list(df1['ITI_Name'].drop_duplicates())
iti_name = st.sidebar.multiselect('ITI Name',options = iti_names)
# df1 = df1[df1['ITI_Name'].isin(iti_name)]

iti_categories = list(df1['ITI_Category'].drop_duplicates())
iti_category = st.sidebar.multiselect('ITI Category',options = iti_categories)
df1 = df1[df1['ITI_Category'].isin(iti_category)]

iti_nstis = list(df1['Details'].drop_duplicates())
iti_nsti = st.sidebar.multiselect('ITI/NSTI',options = iti_nstis)
df1 = df1[df1['Details'].isin(iti_nsti)]

# TOP KPI's
total_seats = int(df["Totalseats"].sum())
seats_available = int(df["SeatsAvailable"].sum())
total_units = int(df["TotalUnits"].sum())
units_available = int(df["UnitsAvailable"].sum())
admissions = int(df["Admissions"].sum())
left_column, middle_column, right_column = st.columns(3, gap = 'medium')

metric_row(
    {
        "Total Seats": f"{total_seats}",
        "Seats Available" : f"{seats_available}",
        "Metric 3": 300,
        "Metric 4": 400,
        "Metric 5": 500,
    }
)

# with placeholder.container():
#     # with left_column:
#         left_column.metric(label = "Total Seats", value = f"{total_seats}")
#         left_column.metric(label = "Seats Available", value = f"{seats_available}")
#         # st.subheader("Total Seats")
#         # st.subheader(f"{total_seats}")
#         # st.subheader("Seats Available")
#         # st.subheader(f"{seats_available}")
        
#     # with middle_column:
#         middle_column.metric(label = "Total Units", value = f"{total_units}")
#         middle_column.metric(label = "Units Available", value = f"{units_available}")
#         # st.subheader("Total Units")
#         # st.subheader(f"{total_units}")
#         # st.subheader("Units Available")
#         # st.subheader(f"{units_available}")
#     # with right_column:
#     #     st.subheader("Admissions")
#     #     st.subheader(f"{admissions}")
#         right_column.metric(label = "Admissions", value = f"{admissions}")

st.markdown("""---""")

st.markdown("### Detailed Data View")
        
st.dataframe(df1.reset_index(), width=1000, height=500)

time.sleep(1)
# @st.cache(ttl=24*60*60) 




#------------------------------------------------------------------------------------------------------------------------------------------
# for i in range(df1.shape[0]):
#     if df1.loc[i, 'State_Name'] in state:
#     # df1 = df1[df1['State_Name'].isin(state)]
#         st.dataframe(df1, width=1000, height=500)
#         if df1.loc[i, 'District_Name'] in district:
#             st.dataframe(df1, width=1000, height=500)
#         elif df1.loc[i, 'Course_Duration'] in duration:
#             # df1 = df1[df1['Course_Duration'].isin(duration)]
#             st.dataframe(df1, width=1000, height=500)
#         elif df1.loc[i, 'Year'] in year:
#             st.dataframe(df1, width=1000, height=500)
#         elif df1.loc[i, 'ITI_Name'] in iti_name:
#             st.dataframe(df1, width=1000, height=500)
#         elif df1.loc[i, 'ITI_Category'] in iti_category:
#             st.dataframe(df1, width=1000, height=500)
#         elif df1.loc[i, 'Details'] in iti_nsti:
#             st.dataframe(df1, width=1000, height=500)
#         else:
#             break