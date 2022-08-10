import streamlit as st
import pandas as pd
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode, JsCode
from streamlit_card import card


@st.cache
def data_upload():
    df = pd.read_csv(r'iti_trades.csv')
    return df

st.set_page_config(
    page_title="Dashboard",
    page_icon="✅",
    layout="wide",
)

st.title("NCVT MIS Dashboard")
df = data_upload()

gb = GridOptionsBuilder.from_dataframe(df)
gb.configure_pagination(paginationAutoPageSize=True) #Add pagination
gb.configure_default_column(editable = True, groupable = True)
# gb.configure_side_bar() #Add a sidebar
# gb.configure_selection('multiple', use_checkbox=True, groupSelectsChildren="Group checkbox select children") #Enable multi-row selection
gridOptions = gb.build()

cols = st.columns([.333, .333, .333])


placeholder = st.empty()    


states = list(df['State_Name'].unique())
state = st.sidebar.multiselect("State",options = states)

with placeholder:
    if state:
        df = df[df['State_Name'].isin(state)] 
        # placeholder.dataframe(df.reset_index())
        AgGrid(df,
    # gridOptions=gridOptions,
    data_return_mode='AS_INPUT', 
    update_mode='NO_UPDATE', 
    fit_columns_on_grid_load=False,
    theme='blue', #Add theme color to the table
    enable_enterprise_modules=True,
    height=350, 
    width='100%',
    # reload_data=False
    ) 
        
trades_names = list(df['Trade_Name'].unique())
trade_name = st.sidebar.multiselect("Trade Name",options = trades_names)

with placeholder:
    if trade_name:
        df = df[df['Trade_Name'].isin(trade_name)] 
        # placeholder.dataframe(df.reset_index())
        AgGrid(df,
    # gridOptions=gridOptions,
    data_return_mode='AS_INPUT', 
    update_mode='NO_UPDATE', 
    fit_columns_on_grid_load=False,
    theme='blue', #Add theme color to the table
    enable_enterprise_modules=True,
    height=350, 
    width='100%',
    # reload_data=False
    ) 

districts = list(df['District_Name'].unique())
district = st.sidebar.multiselect("District",options = districts)

with placeholder:
    if district:
        df = df[df['District_Name'].isin(district)]
        # placeholder.dataframe(df.reset_index())
        AgGrid(df,
    # gridOptions=gridOptions,
    data_return_mode='AS_INPUT', 
    update_mode='NO_UPDATE', 
    fit_columns_on_grid_load=False,
    theme='blue', #Add theme color to the table
    enable_enterprise_modules=True,
    height=350, 
    width='100%',
    # reload_data=False
    )    
        # placeholder.dataframe(grid_table)
    
durations = list(df['Course_Duration'].unique())
duration = st.sidebar.multiselect("Course Duration",options = durations)


with placeholder:
    if duration:
        
        df = df[df['Course_Duration'].isin(duration)]
        # placeholder.dataframe(df.reset_index())
        AgGrid(df,
    # gridOptions=gridOptions,
    data_return_mode='AS_INPUT', 
    update_mode='NO_UPDATE', 
    fit_columns_on_grid_load=False,
    theme='blue', #Add theme color to the table
    enable_enterprise_modules=True,
    height=350, 
    width='100%',
    # reload_data=False
    ) 
        # placeholder.dataframe(grid_table)
    
years = list(df['Year'].unique())
year = st.sidebar.multiselect('Year',options = years)


with placeholder:
    if year:
        df = df[df['Year'].isin(year)]
        # placeholder.dataframe(df.reset_index())
        AgGrid(df,
    # gridOptions=gridOptions,
    data_return_mode='AS_INPUT', 
    update_mode='NO_UPDATE', 
    fit_columns_on_grid_load=False,
    theme='blue', #Add theme color to the table
    enable_enterprise_modules=True,
    height=350, 
    width='100%',
    # reload_data=False
    )   
        # placeholder.dataframe(grid_table)
    
iti_names = list(df['ITI_Name'].unique())
iti_name = st.sidebar.multiselect('ITI Name',options = iti_names)

with placeholder:
    if iti_name:
        df = df[df['ITI_Name'].isin(iti_name)]
        # placeholder.dataframe(df.reset_index())
        AgGrid(df,
    # gridOptions=gridOptions,
    data_return_mode='AS_INPUT', 
    update_mode='NO_UPDATE', 
    fit_columns_on_grid_load=False,
    theme='blue', #Add theme color to the table
    enable_enterprise_modules=True,
    height=350, 
    width='100%',
    # reload_data=False
    )   
        # placeholder.dataframe(grid_table)
    
iti_categories = list(df['ITI_Category'].unique())
iti_category = st.sidebar.multiselect('ITI Category',options = iti_categories)

with placeholder:
    if iti_category:
        df = df[df['ITI_Category'].isin(iti_category)]
        # placeholder.dataframe(df.reset_index())
        AgGrid(df,
    # gridOptions=gridOptions,
    data_return_mode='AS_INPUT', 
    update_mode='NO_UPDATE', 
    fit_columns_on_grid_load=False,
    theme='blue', #Add theme color to the table
    enable_enterprise_modules=True,
    height=350, 
    width='100%',
    # reload_data=False
    ) 
        # placeholder.dataframe(grid_table)
    
# iti_nstis = list(df['Details'].unique())
# iti_nsti = st.sidebar.multiselect('ITI/NSTI',options = iti_nstis)

# with placeholder:
#     if iti_nsti:
#         df = df[df['Details'].isin(iti_nsti)]
#         # placeholder.dataframe(df.reset_index())
#         AgGrid(df,
#     gridOptions=gridOptions,
#     data_return_mode='AS_INPUT', 
#     update_mode='NO_UPDATE', 
#     fit_columns_on_grid_load=False,
#     theme='blue', #Add theme color to the table
#     enable_enterprise_modules=True,
#     height=350, 
#     width='100%',
#     reload_data=False
#     )  
        # placeholder.dataframe(grid_table)
    
total_seats = int(df["Totalseats"].sum())
seats_available = int(df["SeatsAvailable"].sum())
total_units = int(df["TotalUnits"].sum())
units_available = int(df["UnitsAvailable"].sum())
admissions = int(df["Admissions"].sum())
num_itis = int(df['ITI_Name'].nunique())
num_trades = int(df['Trade_Name'].nunique())



with cols[0]:
    # st.subheader("Total Seats")
    # st.subheader(f"{total_seats}")
    # st.subheader("Seats Available")
    # st.subheader(f"{seats_available}")  
    wch_colour_box = (0,204,102)
    wch_colour_font = (0,0,0)
    fontsize = 18
    valign = "left"
    iconname = "fas fa-asterisk"
    sline = "Total Seats"
    # lnk = '<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.12.1/css/all.css" crossorigin="anonymous">'
    i = f"{total_seats}"

    htmlstr = f"""<p style='background-color: rgb({wch_colour_box[0]}, 
                                              {wch_colour_box[1]}, 
                                              {wch_colour_box[2]}, 0.75); 
                        color: rgb({wch_colour_font[0]}, 
                                   {wch_colour_font[1]}, 
                                   {wch_colour_font[2]}, 0.75); 
                        font-size: {fontsize}px; 
                        border-radius: 7px; 
                        padding-left: 12px; 
                        padding-top: 18px; 
                        padding-bottom: 18px; 
                        line-height:25px;'>
                        <i class='{iconname} fa-xs'></i> {i}
                        </style><BR><span style='font-size: 14px; 
                        margin-top: 0;'>{sline}</style></span></p>"""

    st.markdown(htmlstr, unsafe_allow_html=True)
    
    wch_colour_box = (0,204,102)
    wch_colour_font = (0,0,0)
    fontsize = 18
    valign = "left"
    iconname = "fas fa-asterisk"
    sline = "Seats Available"
    # lnk = '<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.12.1/css/all.css" crossorigin="anonymous">'
    i = f"{seats_available}"

    htmlstr = f"""<p style='background-color: rgb({wch_colour_box[0]}, 
                                              {wch_colour_box[1]}, 
                                              {wch_colour_box[2]}, 0.75); 
                        color: rgb({wch_colour_font[0]}, 
                                   {wch_colour_font[1]}, 
                                   {wch_colour_font[2]}, 0.75); 
                        font-size: {fontsize}px; 
                        border-radius: 7px; 
                        padding-left: 12px; 
                        padding-top: 18px; 
                        padding-bottom: 18px; 
                        line-height:25px;'>
                        <i class='{iconname} fa-xs'></i> {i}
                        </style><BR><span style='font-size: 14px; 
                        margin-top: 0;'>{sline}</style></span></p>"""

    st.markdown(htmlstr, unsafe_allow_html=True)
    # card("Total Seats", f"{total_seats}")
    # card("Seats Available", f"{seats_available}")
    wch_colour_box = (0,204,102)
    wch_colour_font = (0,0,0)
    fontsize = 18
    valign = "left"
    iconname = "fas fa-asterisk"
    sline = "Number of Trades"
    # lnk = '<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.12.1/css/all.css" crossorigin="anonymous">'
    i = f"{num_trades}"

    htmlstr = f"""<p style='background-color: rgb({wch_colour_box[0]}, 
                                              {wch_colour_box[1]}, 
                                              {wch_colour_box[2]}, 0.75); 
                        color: rgb({wch_colour_font[0]}, 
                                   {wch_colour_font[1]}, 
                                   {wch_colour_font[2]}, 0.75); 
                        font-size: {fontsize}px; 
                        border-radius: 7px; 
                        padding-left: 12px; 
                        padding-top: 18px; 
                        padding-bottom: 18px; 
                        line-height:25px;'>
                        <i class='{iconname} fa-xs'></i> {i}
                        </style><BR><span style='font-size: 14px; 
                        margin-top: 0;'>{sline}</style></span></p>"""

    st.markdown(htmlstr, unsafe_allow_html=True)
    
with cols[1]:
    # st.subheader("Total Units")
    # st.subheader(f"{total_units}")
    # st.subheader("Units Available")
    # st.subheader(f"{units_available}")
    # card("Total Units", f"{total_units}")
    # card("Units Available", f"{units_available}")
    wch_colour_box = (0,204,102)
    wch_colour_font = (0,0,0)
    fontsize = 18
    valign = "left"
    iconname = "fas fa-asterisk"
    sline = "Total Units"
    # lnk = '<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.12.1/css/all.css" crossorigin="anonymous">'
    i = f"{total_units}"

    htmlstr = f"""<p style='background-color: rgb({wch_colour_box[0]}, 
                                              {wch_colour_box[1]}, 
                                              {wch_colour_box[2]}, 0.75); 
                        color: rgb({wch_colour_font[0]}, 
                                   {wch_colour_font[1]}, 
                                   {wch_colour_font[2]}, 0.75); 
                        font-size: {fontsize}px; 
                        border-radius: 7px; 
                        padding-left: 12px; 
                        padding-top: 18px; 
                        padding-bottom: 18px; 
                        line-height:25px;'>
                        <i class='{iconname} fa-xs'></i> {i}
                        </style><BR><span style='font-size: 14px; 
                        margin-top: 0;'>{sline}</style></span></p>"""

    st.markdown(htmlstr, unsafe_allow_html=True)
    
    wch_colour_box = (0,204,102)
    wch_colour_font = (0,0,0)
    fontsize = 18
    valign = "left"
    iconname = "fas fa-asterisk"
    sline = "Units Available"
    # lnk = '<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.12.1/css/all.css" crossorigin="anonymous">'
    i = f"{units_available}"

    htmlstr = f"""<p style='background-color: rgb({wch_colour_box[0]}, 
                                              {wch_colour_box[1]}, 
                                              {wch_colour_box[2]}, 0.75); 
                        color: rgb({wch_colour_font[0]}, 
                                   {wch_colour_font[1]}, 
                                   {wch_colour_font[2]}, 0.75); 
                        font-size: {fontsize}px; 
                        border-radius: 7px; 
                        padding-left: 12px; 
                        padding-top: 18px; 
                        padding-bottom: 18px; 
                        line-height:25px;'>
                        <i class='{iconname} fa-xs'></i> {i}
                        </style><BR><span style='font-size: 14px; 
                        margin-top: 0;'>{sline}</style></span></p>"""

    st.markdown(htmlstr, unsafe_allow_html=True)
    
    
with cols[2]:
    # st.subheader("Admissions")
    # st.subheader(f"{admissions}")
    # card("Admissions", f"{admissions}")
    wch_colour_box = (0,204,102)
    wch_colour_font = (0,0,0)
    fontsize = 18
    valign = "left"
    iconname = "fas fa-asterisk"
    sline = "Admissions"
    # lnk = '<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.12.1/css/all.css" crossorigin="anonymous">'
    i = f"{admissions}"

    htmlstr = f"""<p style='background-color: rgb({wch_colour_box[0]}, 
                                              {wch_colour_box[1]}, 
                                              {wch_colour_box[2]}, 0.75); 
                        color: rgb({wch_colour_font[0]}, 
                                   {wch_colour_font[1]}, 
                                   {wch_colour_font[2]}, 0.75); 
                        font-size: {fontsize}px; 
                        border-radius: 7px; 
                        padding-left: 12px; 
                        padding-top: 18px; 
                        padding-bottom: 18px; 
                        line-height:25px;'>
                        <i class='{iconname} fa-xs'></i> {i}
                        </style><BR><span style='font-size: 14px; 
                        margin-top: 0;'>{sline}</style></span></p>"""

    st.markdown(htmlstr, unsafe_allow_html=True)
    
    wch_colour_box = (0,204,102)
    wch_colour_font = (0,0,0)
    fontsize = 18
    valign = "left"
    iconname = "fas fa-asterisk"
    sline = "Number of ITI"
    # lnk = '<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.12.1/css/all.css" crossorigin="anonymous">'
    i = f"{num_itis}"

    htmlstr = f"""<p style='background-color: rgb({wch_colour_box[0]}, 
                                              {wch_colour_box[1]}, 
                                              {wch_colour_box[2]}, 0.75); 
                        color: rgb({wch_colour_font[0]}, 
                                   {wch_colour_font[1]}, 
                                   {wch_colour_font[2]}, 0.75); 
                        font-size: {fontsize}px; 
                        border-radius: 7px; 
                        padding-left: 12px; 
                        padding-top: 18px; 
                        padding-bottom: 18px; 
                        line-height:25px;'>
                        <i class='{iconname} fa-xs'></i> {i}
                        </style><BR><span style='font-size: 14px; 
                        margin-top: 0;'>{sline}</style></span></p>"""

    st.markdown(htmlstr, unsafe_allow_html=True)


def convert_df(df):
       return df.to_csv().encode('utf-8')


csv = convert_df(df)

st.download_button(
   "Press to Download",
   csv,
   "file.csv",
   "text/csv",
   key='download-csv'
)


