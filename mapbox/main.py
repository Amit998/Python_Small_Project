mapboxgl_access_token = 'pk.eyJ1IjoiZGFtaXRsdWNreTk5OCIsImEiOiJja3B4a2k1emEwNnYyMm9xY2ZxdGw5MHl6In0.WkSpCetT2vGgFnKDIx7NYQ'

import pandas as pd
import numpy as np
import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input,Output

import plotly.offline as py
import plotly.graph_objs as go


df=pd.read_csv('finalrecycling.csv')

app=dash.Dash(__name__)

blackkbold={
    'color':'black',
    'font-weight':'bold'
}

app.layout=html.Div([
    html.Div([
        html.UI([
            html.Li("Compost", className='circle', style={'background': '#ff00ff','color':'black',
                    'list-style':'none','text-indent': '17px'}),
                html.Li("Electronics", className='circle', style={'background': '#0000ff','color':'black',
                    'list-style':'none','text-indent': '17px','white-space':'nowrap'}),
                html.Li("Hazardous_waste", className='circle', style={'background': '#FF0000','color':'black',
                    'list-style':'none','text-indent': '17px'}),
                html.Li("Plastic_bags", className='circle', style={'background': '#00ff00','color':'black',
                    'list-style':'none','text-indent': '17px'}),
                html.Li("Recycling_bins", className='circle',  style={'background': '#824100','color':'black',
                    'list-style':'none','text-indent': '17px'}),
        ],
        )
    ])
])