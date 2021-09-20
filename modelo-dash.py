#!/usr/bin/env python
# -*- coding: utf-8 -*-

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output
import dash_html_components as html
import yfinance as yf
import pandas_datareader.data as web



app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])


yf.pdr_override()

# ----------------- CRIPTMOEDAS
tickers = ["XRP-USD","BTC-USD", "ETH-USD", "SOL1-USD"] #RIPPLE X BITCOIN
carteira = web.get_data_yahoo(tickers)["Close"]
#carteira = web.get_data_yahoo(tickers, start="2020-01-01")["Close"]
carteira.plot(subplots=True, figsize=(22,8))

# ----------------- AÇÕES
tickers2 = ["ABEV3.SA","ITSA4.SA", "VALE3.SA", "WEGE3.SA"] 
carteira2 = web.get_data_yahoo(tickers2, period= "5y")["Close"]
carteira2.plot(subplots=True, figsize=(22,8))

# ----------------- FOREX
tickers3 = ["USDBRL=X","EURBRL=X", "JPYBRL=X"] 
carteira3 = web.get_data_yahoo(tickers3, period= "5y")["Close"]
carteira3.plot(subplots=True, figsize=(22,8))

############################# BANCO DE DADOS
# ----------------- SELECT I 
#conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-GSL6MTU;DATABASE=imp-cgdf;Trusted_Connection=yes;')
#def connectSQLServer(conn):
#    connSQLServer = conn
#    return connSQLServer
#sql_query = (''' SELECT nome, tonner, dt, total_cilindro FROM impressoras ORDER BY tonner ''')

# ----------------- SELECT II
#sql_query2 = (''' select dt, 'off' as conexao, sum(1) as qtd from [imp-cgdf].[dbo].[impressoras] 
#where [total_impressao] like '0' group by dt
#union all
#select dt, 'on' as conexao, sum(1) as qtd from [imp-cgdf].[dbo].[impressoras] 
#where [total_impressao] not like '0' group by dt ''')


############################# TRATAMENTO DE DADOS

#qtd_online = df2['qtd'][3] 
#qtd_offline = df2['qtd'][1]

############################# GRAFICOS
#fig = px.bar(df, x=(df["nome"]), y=(df["tonner"]), barmode="group")
fig = px.line(carteira)
#fig2 = px.line(carteira2)


############################# LAYOUT
app.layout = dbc.Container(children=[
    
    ############################# HEADER
    html.Div([
        #------------------- TITULO
        html.H2(children='Holding Kapital - HK'),
        # ------------------- DESCRIÇÃO I
        html.Div(children='''Sistema de monitoramento de ativos'''),
    ]),
   
    ################### CARDS
    dbc.Row([
        dbc.Col([
            #----- ONLINE
            dbc.Card ([
                html.Span('VALORIZAÇÃO ACUMULADA: '),
                html.H3(style={"color": "#adfc92"}, children= 'qtd_online')
            ]) 
        ]),

        dbc.Col([
            #----- OFFLINE
            dbc.Card ([
                html.Span('DESVALORIZAÇÃO ACUMULADA :'),
                html.H3(style={"color": "#ff0000"}, children= 'qtd_offline')
            ]) 
        ]),
    ]),   

    
    # ------------------- DESCRIÇÃO II
    html.H3(id= 'text', children='Buscar por:'),

   
    ################### FILTROS
    dbc.Row([
        dbc.Col([
            #----- TIPO DE DADO
            dcc.Dropdown(
            id='dropdown',
            options=[
                {'label': 'Criptomoedas', 'value': 'CRIPTOMOEDAS'},
                {'label': 'Ações', 'value': 'ACOES'},
                {'label': 'Forex', 'value': 'FOREX'}
            ],
            value='CRIPTOMOEDAS'
            ),
        ]),
        #----- DATA
        dbc.Col([
            dcc.DatePickerSingle(
                id='date-picker',
            )
        ]),
    ]),   

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
    if value == 'CRIPTOMOEDAS':
        return px.line(carteira)
    elif value == 'ACOES':
        return px.line(carteira2)
    else:
        return px.line(carteira3)
    return
    

if __name__ == '__main__':
    app.run_server(debug=True)