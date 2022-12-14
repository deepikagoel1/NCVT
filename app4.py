import streamlit as st
import pandas as pd
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode, JsCode
# from streamlit_card import card


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
gb.configure_side_bar() #Add a sidebar
gb.configure_selection('multiple', use_checkbox=True, groupSelectsChildren="Group checkbox select children") #Enable multi-row selection
gridOptions = gb.build()

cols = st.columns([.333, .333, .333])

option2 = st.selectbox(
     'How many rows you would like to display',
     ('10', '50', '100'))


placeholder = st.empty()    

trades_names = list(df['Trade_Name'].unique())
trade_name = st.sidebar.multiselect("Trade Name",options = trades_names, key =1)
st.write('Trade Name selected as', trade_name)

with placeholder:
    if trade_name:
        df = df[df['Trade_Name'].isin(trade_name)]
        if option2 == '10': 
            AgGrid(df.head(10),
            gridOptions=gridOptions,
            data_return_mode='AS_INPUT', 
            update_mode='SELECTION_CHANGED', 
            fit_columns_on_grid_load=False,
            theme='blue', #Add theme color to the table
            enable_enterprise_modules=True,
            height=350, 
            width='100%',
            reload_data=True,
            key = 1
            )
        elif option2 == '50':
            AgGrid(df.head(50),
            gridOptions=gridOptions,
            data_return_mode='AS_INPUT', 
            update_mode='SELECTION_CHANGED', 
            fit_columns_on_grid_load=False,
            theme='blue', #Add theme color to the table
            enable_enterprise_modules=True,
            height=350, 
            width='100%',
            reload_data=True,
            key = 1
            )
        elif option2 == '100':
            AgGrid(df.head(100),
            gridOptions=gridOptions,
            data_return_mode='AS_INPUT', 
            update_mode='SELECTION_CHANGED', 
            fit_columns_on_grid_load=False,
            theme='blue', #Add theme color to the table
            enable_enterprise_modules=True,
            height=350, 
            width='100%',
            reload_data=True,
            key = 1
            )
             
        
sector_names = list(df['Sector_Name'].unique())
sector_name = st.sidebar.multiselect("Sector Name",options = sector_names, key = 2)
st.write('Sector Name selected as', sector_name)

with placeholder:
    if sector_name:
        df = df[df['Sector_Name'].isin(sector_name)] 
        # placeholder.dataframe(df.reset_index())
        if option2 == '10': 
            AgGrid(df.head(10),
            gridOptions=gridOptions,
            data_return_mode='AS_INPUT', 
            update_mode='SELECTION_CHANGED', 
            fit_columns_on_grid_load=False,
            theme='blue', #Add theme color to the table
            enable_enterprise_modules=True,
            height=350, 
            width='100%',
            reload_data=True,
            key = 2
            )
        elif option2 == '50':
            AgGrid(df.head(50),
            gridOptions=gridOptions,
            data_return_mode='AS_INPUT', 
            update_mode='SELECTION_CHANGED', 
            fit_columns_on_grid_load=False,
            theme='blue', #Add theme color to the table
            enable_enterprise_modules=True,
            height=350, 
            width='100%',
            reload_data=True,
            key = 2
            )
        elif option2 == '100':
            AgGrid(df.head(100),
            gridOptions=gridOptions,
            data_return_mode='AS_INPUT', 
            update_mode='SELECTION_CHANGED', 
            fit_columns_on_grid_load=False,
            theme='blue', #Add theme color to the table
            enable_enterprise_modules=True,
            height=350, 
            width='100%',
            reload_data=True,
            key = 2
            )
        
trade_types = list(df['Trade_Type'].unique())
trade_type = st.sidebar.multiselect("Trade Type",options = trade_types, key = 3)
st.write('Trade Type selected as', trade_type)

with placeholder:
    if trade_type:
        df = df[df['Trade_Type'].isin(trade_type)] 
        # placeholder.dataframe(df.reset_index())
        if option2 == '10': 
            AgGrid(df.head(10),
            gridOptions=gridOptions,
            data_return_mode='AS_INPUT', 
            update_mode='SELECTION_CHANGED', 
            fit_columns_on_grid_load=False,
            theme='blue', #Add theme color to the table
            enable_enterprise_modules=True,
            height=350, 
            width='100%',
            reload_data=True,
            key = 3
            )
        elif option2 == '50':
            AgGrid(df.head(50),
            gridOptions=gridOptions,
            data_return_mode='AS_INPUT', 
            update_mode='SELECTION_CHANGED', 
            fit_columns_on_grid_load=False,
            theme='blue', #Add theme color to the table
            enable_enterprise_modules=True,
            height=350, 
            width='100%',
            reload_data=True,
            key = 3
            )
        elif option2 == '100':
            AgGrid(df.head(100),
            gridOptions=gridOptions,
            data_return_mode='AS_INPUT', 
            update_mode='SELECTION_CHANGED', 
            fit_columns_on_grid_load=False,
            theme='blue', #Add theme color to the table
            enable_enterprise_modules=True,
            height=350, 
            width='100%',
            reload_data=True,
            key = 3
            )



states = list(df['State_Name'].unique())
state = st.sidebar.multiselect("State",options = states, key = 4)
st.write('State Name selected as', state)
with placeholder:
    if state:
        df = df[df['State_Name'].isin(state)] 
        # placeholder.dataframe(df.reset_index())
        if option2 == '10': 
            AgGrid(df.head(10),
            gridOptions=gridOptions,
            data_return_mode='AS_INPUT', 
            update_mode='SELECTION_CHANGED', 
            fit_columns_on_grid_load=False,
            theme='blue', #Add theme color to the table
            enable_enterprise_modules=True,
            height=350, 
            width='100%',
            reload_data=True,
            key = 4
            )
        elif option2 == '50':
            AgGrid(df.head(50),
            gridOptions=gridOptions,
            data_return_mode='AS_INPUT', 
            update_mode='SELECTION_CHANGED', 
            fit_columns_on_grid_load=False,
            theme='blue', #Add theme color to the table
            enable_enterprise_modules=True,
            height=350, 
            width='100%',
            reload_data=True,
            key = 4
            )
        elif option2 == '100':
            AgGrid(df.head(100),
            gridOptions=gridOptions,
            data_return_mode='AS_INPUT', 
            update_mode='SELECTION_CHANGED', 
            fit_columns_on_grid_load=False,
            theme='blue', #Add theme color to the table
            enable_enterprise_modules=True,
            height=350, 
            width='100%',
            reload_data=True,
            key = 4
            )
    
        

districts = list(df['District_Name'].unique())
district = st.sidebar.multiselect("District",options = districts, key = 5)
st.write('District Name selected as', district)
with placeholder:
    if district:
        df = df[df['District_Name'].isin(district)]
        # placeholder.dataframe(df.reset_index())
        if option2 == '10': 
            AgGrid(df.head(10),
            gridOptions=gridOptions,
            data_return_mode='AS_INPUT', 
            update_mode='SELECTION_CHANGED', 
            fit_columns_on_grid_load=False,
            theme='blue', #Add theme color to the table
            enable_enterprise_modules=True,
            height=350, 
            width='100%',
            reload_data=True,
            key = 5
            )
        elif option2 == '50':
            AgGrid(df.head(50),
            gridOptions=gridOptions,
            data_return_mode='AS_INPUT', 
            update_mode='SELECTION_CHANGED', 
            fit_columns_on_grid_load=False,
            theme='blue', #Add theme color to the table
            enable_enterprise_modules=True,
            height=350, 
            width='100%',
            reload_data=True,
            key = 5
            )
        elif option2 == '100':
            AgGrid(df.head(100),
            gridOptions=gridOptions,
            data_return_mode='AS_INPUT', 
            update_mode='SELECTION_CHANGED', 
            fit_columns_on_grid_load=False,
            theme='blue', #Add theme color to the table
            enable_enterprise_modules=True,
            height=350, 
            width='100%',
            reload_data=True,
            key = 5
            )  
        # placeholder.dataframe(grid_table)
    
durations = list(df['Course_Duration'].unique())
duration = st.sidebar.multiselect("Course Duration",options = durations, key = 6)
st.write('Course Duration selected as', duration)

with placeholder:
    if duration:
        
        df = df[df['Course_Duration'].isin(duration)]
        # placeholder.dataframe(df.reset_index())
        if option2 == '10': 
            AgGrid(df.head(10),
            gridOptions=gridOptions,
            data_return_mode='AS_INPUT', 
            update_mode='SELECTION_CHANGED', 
            fit_columns_on_grid_load=False,
            theme='blue', #Add theme color to the table
            enable_enterprise_modules=True,
            height=350, 
            width='100%',
            reload_data=True,
            key = 6
            )
        elif option2 == '50':
            AgGrid(df.head(50),
            gridOptions=gridOptions,
            data_return_mode='AS_INPUT', 
            update_mode='SELECTION_CHANGED', 
            fit_columns_on_grid_load=False,
            theme='blue', #Add theme color to the table
            enable_enterprise_modules=True,
            height=350, 
            width='100%',
            reload_data=True,
            key = 6
            )
        elif option2 == '100':
            AgGrid(df.head(100),
            gridOptions=gridOptions,
            data_return_mode='AS_INPUT', 
            update_mode='SELECTION_CHANGED', 
            fit_columns_on_grid_load=False,
            theme='blue', #Add theme color to the table
            enable_enterprise_modules=True,
            height=350, 
            width='100%',
            reload_data=True,
            key = 6
            )
        # placeholder.dataframe(grid_table)
    
years = list(df['Year'].unique())
year = st.sidebar.multiselect('Year',options = years, key = 7)

st.write('Admitted Year Selected as', year)

with placeholder:
    if year:
        df = df[df['Year'].isin(year)]
        # placeholder.dataframe(df.reset_index())
        if option2 == '10': 
            AgGrid(df.head(10),
            gridOptions=gridOptions,
            data_return_mode='AS_INPUT', 
            update_mode='SELECTION_CHANGED', 
            fit_columns_on_grid_load=False,
            theme='blue', #Add theme color to the table
            enable_enterprise_modules=True,
            height=350, 
            width='100%',
            reload_data=True,
            key = 7
            )
        elif option2 == '50':
            AgGrid(df.head(50),
            gridOptions=gridOptions,
            data_return_mode='AS_INPUT', 
            update_mode='SELECTION_CHANGED', 
            fit_columns_on_grid_load=False,
            theme='blue', #Add theme color to the table
            enable_enterprise_modules=True,
            height=350, 
            width='100%',
            reload_data=True,
            key = 7
            )
        elif option2 == '100':
            AgGrid(df.head(100),
            gridOptions=gridOptions,
            data_return_mode='AS_INPUT', 
            update_mode='SELECTION_CHANGED', 
            fit_columns_on_grid_load=False,
            theme='blue', #Add theme color to the table
            enable_enterprise_modules=True,
            height=350, 
            width='100%',
            reload_data=True,
            key = 7
            ) 
        # placeholder.dataframe(grid_table)
    
iti_names = list(df['ITI_Name'].unique())
iti_name = st.sidebar.multiselect('ITI Name',options = iti_names, key = 8)

st.write('ITI Name selected as', iti_name)

with placeholder:
    if iti_name:
        df = df[df['ITI_Name'].isin(iti_name)]
        # placeholder.dataframe(df.reset_index())
        if option2 == '10': 
            AgGrid(df.head(10),
            gridOptions=gridOptions,
            data_return_mode='AS_INPUT', 
            update_mode='SELECTION_CHANGED', 
            fit_columns_on_grid_load=False,
            theme='blue', #Add theme color to the table
            enable_enterprise_modules=True,
            height=350, 
            width='100%',
            reload_data=True,
            key = 8
            )
        elif option2 == '50':
            AgGrid(df.head(50),
            gridOptions=gridOptions,
            data_return_mode='AS_INPUT', 
            update_mode='SELECTION_CHANGED', 
            fit_columns_on_grid_load=False,
            theme='blue', #Add theme color to the table
            enable_enterprise_modules=True,
            height=350, 
            width='100%',
            reload_data=True,
            key = 8
            )
        elif option2 == '100':
            AgGrid(df.head(100),
            gridOptions=gridOptions,
            data_return_mode='AS_INPUT', 
            update_mode='SELECTION_CHANGED', 
            fit_columns_on_grid_load=False,
            theme='blue', #Add theme color to the table
            enable_enterprise_modules=True,
            height=350, 
            width='100%',
            reload_data=True,
            key = 8
            )   
        # placeholder.dataframe(grid_table)
    
iti_categories = list(df['ITI_Category'].unique())
iti_category = st.sidebar.multiselect('ITI Category',options = iti_categories, key = 9)

st.write('ITI Category selected as', iti_category)

with placeholder:
    if iti_category:
        df = df[df['ITI_Category'].isin(iti_category)]
        # placeholder.dataframe(df.reset_index())
        if option2 == '10': 
            AgGrid(df.head(10),
            gridOptions=gridOptions,
            data_return_mode='AS_INPUT', 
            update_mode='SELECTION_CHANGED', 
            fit_columns_on_grid_load=False,
            theme='blue', #Add theme color to the table
            enable_enterprise_modules=True,
            height=350, 
            width='100%',
            reload_data=True,
            key = 9
            )
        elif option2 == '50':
            AgGrid(df.head(50),
            gridOptions=gridOptions,
            data_return_mode='AS_INPUT', 
            update_mode='SELECTION_CHANGED', 
            fit_columns_on_grid_load=False,
            theme='blue', #Add theme color to the table
            enable_enterprise_modules=True,
            height=350, 
            width='100%',
            reload_data=True,
            key = 9
            )
        elif option2 == '100':
            AgGrid(df.head(100),
            gridOptions=gridOptions,
            data_return_mode='AS_INPUT', 
            update_mode='SELECTION_CHANGED', 
            fit_columns_on_grid_load=False,
            theme='blue', #Add theme color to the table
            enable_enterprise_modules=True,
            height=350, 
            width='100%',
            reload_data=True,
            key = 9
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
#     update_mode='SELECTION_CHANGED', 
#     fit_columns_on_grid_load=False,
#     theme='blue', #Add theme color to the table
#     enable_enterprise_modules=True,
#     height=350, 
#     width='100%',
#     reload_data=True
#     )  
        # placeholder.dataframe(grid_table)
    
total_seats = int(df["Totalseats"].sum())
seats_available = int(df["SeatsAvailable"].sum())
total_units = int(df["TotalUnits"].sum())
units_available = int(df["UnitsAvailable"].sum())
admissions = int(df["Admissions"].sum())
num_itis = int(df['ITI_Name'].nunique())
num_trades = int(df['Trade_Name'].nunique())
women_iti = int(df['ITI_Women'].nunique())
    


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
    
    
    wch_colour_box = (0,204,102)
    wch_colour_font = (0,0,0)
    fontsize = 18
    valign = "left"
    iconname = "fas fa-asterisk"
    sline = "Number of Women ITI"
    # lnk = '<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.12.1/css/all.css" crossorigin="anonymous">'
    i = f"{women_iti}"

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
    
if admissions > 500:
    st.subheader('ITI Names')
    st.write(df['ITI_Name'])

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


