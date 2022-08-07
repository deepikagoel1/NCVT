from dash import Dash, dash_table,html
import pandas as pd
from collections import OrderedDict
from dash.dependencies import Input, Output
import dash.dash_table as dt
import dash_bootstrap_components as dbc

df = pd.read_csv('iti_trades.csv')

app = Dash(__name__)

app.layout = html.Div([
    dash_table.DataTable(
        
        data=df.to_dict('records'),
        columns=[
            {'id': c, 'name': c}
            for c in df.columns
        ],
        style_cell_conditional=[
            {
                'if': {'column_id': c},
                'textAlign': 'center'
            } for c in ['Date', 'Region']
        ],
        style_data={
            'color': 'black',
            'backgroundColor': 'white',
            'textAlign': 'center'
        },
        style_data_conditional=[
            {
                'if': {'row_index': 'odd'},
                'backgroundColor': 'rgb(220, 220, 220)',
            }
        ],
        style_header={
            'backgroundColor': 'rgb(210, 210, 210)',
            'color': 'black',
            'fontWeight': 'bold',
            'textAlign': 'center'
        },
        editable=True,
        filter_action="native",
        sort_action="native",
        sort_mode='multi',
        row_selectable='multi',
        row_deletable=True,
        selected_rows=[],
        page_action='native',
        page_current= 0,
        page_size= 10
    ),
    html.Div(id='table-dropdown-container')
])

@app.callback(
    Output('table-dropdown-container', 'data'),
    [Input('Filter1_dropwdown', 'value'),
     Input('Filter2_dropwdown', 'value'),
     Input('Filter3_dropwdown', 'value'),
     Input('Filter4_dropwdown', 'value'),
     Input('Filter5_dropwdown', 'value'),
     Input('Filter6_dropwdown', 'value'),
     Input('Filter7_dropwdown', 'value')
    ]
    )

def filter_df(filter_01, filter_02, filter_03, filter_04, filter_05, filter_06, filter_07):
    if (not filter_01 and not filter_02 and not filter_03 and not filter_04 and not filter_05 and not filter_06 and not filter_07):
        # Return all the rows on initial load
        return df.to_dict('records')


    filtered = df.query('filter_1_field in @filter_01 or filter_2_field in @filter_02 or filter_3_field in @filter_03 or filter_4_field in @filter_04 or filter_5_field in @filter_05 or filter_6_field in @filter_06 or filter_7_field in @filter_07')
    return filtered.to_dict('records')

if __name__ == '__main__':
    app.run_server(debug=True)
