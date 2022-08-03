import streamlit as st
import pandas as pd
import time
# from pyspark.sql.functions import col

st.title("Dashboard")

if 'number_of_rows' not in st.session_state:
    st.session_state['number_of_rows'] = 5
    #st.session_state['type'] = 'Categorical'
    
df = pd.read_csv(r'C:\Users\goeld\Downloads\iti_trades.csv')

df1 = df[['Trade_Name', 'Course_Duration', 'ITI_Name', 'Year', 'ITI_Address', 'State_Name', 'District_Name', 'ITI_Category', 'Principal_Name', 'Principal_Email_id', 'Details']]

# st.set_page_config(
#     page_title="Data Science Dashboard",
#     page_icon="✅",
#     layout="wide",
# )

left_column, middle_column, right_column = st.columns(3, gap = 'medium')
                 
increment = st.button('Show more columns ')

if increment:
    st.session_state.number_of_rows += 1


decrement = st.button('Show few columns ')

if decrement:
    st.session_state.number_of_rows -= 1
    
states = list(df1['State_Name'].unique())
state = st.sidebar.multiselect("State",options = states)
# if state:
#     df1 = df1[df1['State_Name'].isin(state)]
    # st.dataframe(df1, width=1000, height=500)
    # st.table(df.head(st.session_state['number_of_rows']))
    # st.dataframe()


districts = list(df1['District_Name'].unique())
district = st.sidebar.multiselect("District",options = districts)
# if district:
#     df1 = df1[df1['District_Name'].isin(district)]
    
#     st.dataframe(df1, width=1000, height=500)

durations = list(df1['Course_Duration'].drop_duplicates())
duration = st.sidebar.multiselect("Course Duration",options = durations)
# df1 = df1[df1['Course_Duration'].isin(duration)]

years = list(df1['Year'].drop_duplicates())
year = st.sidebar.multiselect('Year',options = years)
# df1 = df1[df1['Year'].isin(year)]

iti_names = list(df1['ITI_Name'].drop_duplicates())
iti_name = st.sidebar.multiselect('ITI Name',options = iti_names)
# df1 = df1[df1['ITI_Name'].isin(iti_name)]

iti_categories = list(df1['ITI_Category'].drop_duplicates())
iti_category = st.sidebar.multiselect('ITI Category',options = iti_categories)
# df1 = df1[df1['ITI_Category'].isin(iti_category)]

iti_nstis = list(df1['Details'].drop_duplicates())
iti_nsti = st.sidebar.multiselect('ITI/NSTI',options = iti_nstis)
# df1 = df1[df1['Details'].isin(iti_nsti)]

placeholder = st.empty()

# Replace the placeholder with some text:
st.dataframe(df1.head().reset_index())

hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
            """
st.markdown(hide_table_row_index, unsafe_allow_html=True)


# Replace the chart with several elements:
with st.empty():
   

# # Clear all those elements:
# placeholder.empty()

# Inject CSS with Markdown

    if state:
        # placeholder = st.empty()
        df1 = df1[df1['State_Name'].isin(state)]
        # df1.query(df1)
        # for i in range(df1.shape[0]):
        # df1.filter(df1[df1['State_Name'].isin(state)])
        # df1.filter(col("State_Name") == state)
        st.dataframe(df1.head().reset_index(), width=1000, height=500)
    # placeholder.empty()
    if district:
        # placeholder.empty()
        df1 = df1[df1['District_Name'].isin(district)] 
        # df1.query(df1)
        # df1.filter(df1.District_Name == district)
        
        st.dataframe(df1.head().reset_index(), width=1000, height=500)
    # placeholder.empty()
    if duration:
        # placeholder.empty()
        df1 = df1[df1['Course_Duration'].isin(duration)]
        st.dataframe(df1.head().reset_index(), width=1000, height=500)
    # placeholder.empty()


# TOP KPI's
total_seats = int(df["Totalseats"].sum())
seats_available = int(df["SeatsAvailable"].sum())
total_units = int(df["TotalUnits"].sum())
units_available = int(df["UnitsAvailable"].sum())
admissions = int(df["Admissions"].sum())



# left_column, middle_column, right_column = st.columns(3, gap = 'medium')

# st.table(df.head(st.session_state['number_of_rows']))


# types = {'State': [state],'District': [district], duration, year, iti_name, iti_category, iti_nsti], 'Numerical': [total_seats, seats_available, total_units, units_available, admissions]}

# column = st.selectbox('Select a column', types[st.session_state['type']])

# # type_of_column = st.radio("What kind of analysis", ['Categorical', 'Numerical'], on_change=handle_click_wo_button, key = 'kind_of_column')

# # type_of_column = st.radio("What kind of analysis", ['Categorical', 'Numerical'])

# # change = st.button('change', on_click = handle_click, args = [type_of_column])

# st.session_state['type'] = st.radio("What kind of analysis", ['Categorical', 'Numerical'])

# if st.session_state['type'] == 'Categorical':
#     st.dataframe(df[column])
    
# # else:
# #     with placeholder.container():
# #     # with left_column:
# #         left_column.metric(label = "Total Seats", value = f"{total_seats}")
# #         left_column.metric(label = "Seats Available", value = f"{seats_available}")
# #         # st.subheader("Total Seats")
# #         # st.subheader(f"{total_seats}")
# #         # st.subheader("Seats Available")
# #         # st.subheader(f"{seats_available}")
        
# #     # with middle_column:
# #         middle_column.metric(label = "Total Units", value = f"{total_units}")
# #         middle_column.metric(label = "Units Available", value = f"{units_available}")
# #         # st.subheader("Total Units")
# #         # st.subheader(f"{total_units}")
# #         # st.subheader("Units Available")
# #         # st.subheader(f"{units_available}")
# #     # with right_column:
# #     #     st.subheader("Admissions")
# #     #     st.subheader(f"{admissions}")
# #         right_column.metric(label = "Admissions", value = f"{admissions}")

# # st.markdown("""---""")

# st.markdown("### Detailed Data View")
        
# st.dataframe(df1.reset_index(), width=1000, height=500)

time.sleep(1)
# @st.cache(ttl=24*60*60) 

    
# st.table(df.head(st.session_state['number_of_rows']))