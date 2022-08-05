from dash import Dash, dash_table,html
import pandas as pd
from collections import OrderedDict



df = pd.read_csv('iti_trades.csv')

app = Dash(__name__)

app.layout = html.Div([
    dash_table.DataTable(
        id='table-dropdown',
        dropdown= {
            'State': {
                'options': [
                    {'label': i, 'value': i}
                    for i in df['State_Name'].unique()
                ]
            },
            'Trades': {
                 'options': [
                    {'label': i, 'value': i}
                    for i in df['Trade_Name'].unique()
                ]
            }
        },
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

if __name__ == '__main__':
    app.run_server(debug=True)
