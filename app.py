import os
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from plotly.subplots import make_subplots
#from dash.dependencies import Input, Output
import plotly.express as px

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
file_name = 'https://raw.githubusercontent.com/elimywilliams/sc_covid19/master/countryLags.csv'
countryLags = pd.read_csv(file_name)
countryLags['Date'] = countryLags['Date'].astype('datetime64[ns]')

file_name = 'https://raw.githubusercontent.com/elimywilliams/sc_covid19/master/allStateLags.csv'
stateLags = pd.read_csv(file_name)
stateLags['Date'] = stateLags['datetest'].astype('datetime64[ns]')

app = dash.Dash(__name__, external_stylesheets=external_stylesheets,suppress_callback_exceptions=True)

countryOPTS = [{'label': 'Spain', 'value': 'Spain'},
            {'label': 'Italy', 'value': 'Italy'},
            {'label': 'Sweden', 'value': 'Sweden'},
            {'label': 'Switzerland', 'value': 'Switzerland'},
            {'label': 'Australia', 'value': 'Australia'},
            {'label': 'Austria', 'value': 'Austria'},
            {'label': 'France', 'value': 'France'},
            {'label': 'Germany', 'value': 'Germany'},
            {'label': 'Turkey', 'value': 'Turkey'},
            {'label': 'United States of America', 'value': 'US'},
            {'label': 'New Zealand', 'value': 'New Zealand'},
            {'label': 'United Kingdom', 'value': 'UK'},
            {'label': 'Mexico', 'value': 'Mexico'}]


stateOPTS = [
    {'label':'Arkansas','value':"AR"},
    {'label':'Alabama','value':"AL"},
    {'label':'Alaska','value':"AK"},

    {'label':'Arizona','value':"AZ"},
    {'label':'Connecticut','value':'CT'},
    {'label':'California','value':'CA'},
    {'label':'Colorado','value':"CO"},
    {'label':'Delaware','value':"DE"},

    {'label':'Florida','value':"FL"},
    {'label':'Georgia','value':"GA"},
    {'label':'Hawaii','value':'HI'},
    {'label':'Idaho','value':"ID"},

    {'label':'Illinois','value':"IL"},
    {'label':'Indiana','value':'IN'},
    {'label':'Iowa','value':"IA"},
    {'label':'Kansas','value':"KS"},

    {'label':"Kentucky",'value':"KY"},
    {'label':'Louisianna','value':"LA"},
    {'label':"Massachusetts",'value':"MA"},
    {'label':'Maine','value':"ME"},
    {'label':'Maryland','value':"MD"},

    {'label':'Michigan','value':"MI"},

    {'label':'Minnesota','value':"MN"},
    {'label':'Mississippi','value':'MS'},
    {'label':'Missouri','value':'MO'},
    {'label':'Montana','value':"MT"},
    {'label':'North Dakota','value':"ND"},
    {'label':'Nebraska','value':"NE"},

    {'label':'Nevada','value':"NV"},
    {'label':'New Hampshire','value':"NH"},
    

    {'label':'New Jersey','value':'NJ'},
    {'label':'New Mexico','value':"NM"},

    {'label':'New York','value':"NY"},
    {'label':'North Carolina','value':'NC'},
    {'label':'Ohio','value':"OH"},
    {'label':'Oklahoma','value':"OK"},
    {'label':'Oregon','value':'OR'},
    {'label':'Pennsylvania','value':'PA'},
    {'label':'Rhode Island','value':"RI"},
    {'label':'South Carolina','value':'SC'},
    {'label':'South Dakota','value':"SD"},
    {'label':'Tennessee','value':"TN"},
    {'label':'Texas','value':'TX'},
    {'label':'Vermont','value':"VT"},

    {'label':'Virginia','value':"VA"},
    {'label':'Washington','value':'WA'},
    {'label':'West Virginia','value':"WV"},

    {'label':'Wisconsin','value':'WI'},
    {'label':'Wyoming','value':'WY'}  
    ]




projOPTS = [
            {'label': 'Con Edison', 'value': 'ConEd'},
            {'label': 'Duke Ohio', 'value': 'DukeOH'},
            {'label': 'Dom Questar (UT)', 'value': 'DomQuest'},
            {'label': 'WEC Energy (WI)', 'value': 'WEC_WI'},
            {'label': 'WPS MMD (WI)', 'value': 'WPS_WI'},
            {'label': 'Peoples (IL)', 'value': 'PeoplesIL'},
            {'label': 'ACLARA (NY)))', 'value': 'Aclara'},
            {'label': 'Duke IPI', 'value': 'DukeIPI'},
            {'label': 'Norwhich Public Utilities', 'value': 'norwhich'},
            {'label': 'Trussville (AL)', 'value': 'Trussville'},
            {'label': 'CPS (TX)))', 'value': 'CPS_TX'},
            {'label': 'Dominion (SC)', 'value': 'DominionSC'},
            {'label': 'Dominion (NC)', 'value': 'DominionNC'}
        ]




whichAvgOPTS = [
        {'label': '7 Day ', 'value': 'sevenday'},
        {'label': '3 Day', 'value': 'threeday'},
        {'label': 'Daily', 'value': 'daily'},
        {'label': 'Cumulative','value':'total'}
    ]

popOPTS = [
    {'label':'Relative to Population','value':'relpop'},
    {'label':'Raw Cases', 'value':'nonrelpop'}
    
    
    ]
tab1 = html.Div([
    html.H3('Country by Country Information'),
    dcc.Dropdown(id='countryChoice',
                 options= countryOPTS,
                 value = 'US'
    ),
     dcc.RadioItems(
        id = 'whichAvg2',
    options= whichAvgOPTS,
    value='sevenday',  labelStyle={'display': 'inline-block'}

    ),
     dcc.RadioItems(
         id = 'popratio2',
         options = popOPTS,
         value='relpop',
         labelStyle = {'display':'inline-block'}
         ),
    dcc.Graph(id='graph_close')
    
])




tab2 = html.Div([
    html.H3('State by State Information'),
     dcc.Dropdown(id='stateChoice',
                 options= stateOPTS,
                 value = 'CO'
    ),
    dcc.RadioItems(
        id = 'whichAvg',
    options= whichAvgOPTS,
    value='threeday',  labelStyle={'display': 'inline-block'}

    ) , 
    dcc.RadioItems(
        id = 'popratio',
        options = popOPTS,
        value = 'relpop',
        labelStyle = {'display':'inline-block'}
        ),
    dcc.Graph(id='state_graph')
])    


tab3 = html.Div([
    html.H3('SC Project Information'),
    dcc.Dropdown(
        id = 'whichProj',
        options = projOPTS,
        value = 'ConEd'
        ) 
    ])


server = app.server

app.layout = html.Div([
    html.H2('Hello World'),
    dcc.Dropdown(
        id='dropdown',
        options=[{'label': i, 'value': i} for i in ['LA', 'NYC', 'MTL']],
        value='LA'
    ),
    html.Div(id='display-value')
])

@app.callback(dash.dependencies.Output('display-value', 'children'),
              [dash.dependencies.Input('dropdown', 'value')])
def display_value(value):
    return 'You have selected "{}"'.format(value)

if __name__ == '__main__':
    app.run_server(debug=True)