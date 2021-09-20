import dash
from dash.development.base_component import Component
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    html.H1(id= 'text', children='Exemplo'),

    # ------------------- MENU DROPDOWN
    dcc.Dropdown(
        id='dropdown',
        options=[
            {'label': 'All', 'value': 'ALL'},
            {'label': 'Montreal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value='ALL'
    ),

    # ------------------- GRAFICO I
    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

@app.callback(
    Output(component_id='example-graph', component_property='figure'),
    Input(component_id='dropdown', component_property='value')
)
def changeText(value):
    if value == 'ALL':
        return px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")
    elif
        return px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")
    return value

if __name__ == '__main__':
    app.run_server(debug=True)