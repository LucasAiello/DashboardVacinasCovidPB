from Dados import *
import dash
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from dash import Dash, html, Input, Output, ctx, dcc

#----------------------------------------------------------------------------------------------------------------------------
#                                                   DASHBOARD
#----------------------------------------------------------------------------------------------------------------------------

div1 = {
    'width': '100%',
    'margin-top': '10px', 
    'display': 'flex', 
    'flex-direction': 'row'
}

div2 = {
    'height': '600px',
    'background-color': '#03181e',
    'margin': '10px',
    'border-radius': '15px'
}

stl_btn_ano = {
    'width': '80px',
    'height': '30px',
    'background-color': '#2f6573',
    'border': '2px solid #03181e',
    'border-radius': '10px',
    'margin': '15px'
}

stl_btn = {
    'width': '90px',
    'height': '50px',
    'background-color': '#2f6573',
    'border': '3px solid #03181e',
    'border-radius': '10px',
    'margin': '15px'
}

#---------------------------------------------------------------------------------------------

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SOLAR])

app.layout = html.Div(style={'width': '100%','height': '700px'}, children=[

    html.Div(style={'width': '100%', 'height': '50', 'margin': '20px 0px'}, children=[

        html.H1(children='VACINAÇÃO CONTRA COVID-19 NA PARAÍBA', style={'text-align': 'center', 'color': '#7fc1d2', 'font-size': '40px', 'padding': '15px', 'margin': '20px'})
        
    ]),
    html.Div(style=div1, children=[
        html.Div(style={'width': '45%', 'height': '600px', 'margin': '10px', 'border-radius': '15px'}, children=[                                                                                           
            html.Div(style={'display': 'flex', 'flex-direction': 'row'}, children=[
                html.Div(style={"width": '50%', 'height': '100px', 'background-color': '#2f6573', 'margin': '10px 10px', 'border': '4px #03181e solid', 'padding': '5px', 'border-radius': '10px'}, children=[

                    html.H2(children='Vacinas Apicadas', style={'font-size': '20px', 'text-align': 'center', 'color': '#eeeeee'}),
                    html.P(len(vacina_covid_pb), style={'font-size': '28px', 'text-align': 'center', 'color': '#eeeeee'})

                ]),
                html.Div([
                    html.Button('Sexo', id='btn-sexo', style=stl_btn, n_clicks=0),
                    html.Button('Fabricante', id='btn-fabricante', style=stl_btn, n_clicks=0)
                ])

            ]),
            html.Div(style={'width': '90%', 'height': '500px', 'background-color': '#03181e', 'margin': '15px', 'border-radius': '10px'}, children=[
                dcc.Dropdown(
                        vacina_covid_pb['paciente_enumSexoBiologico'].unique(),
                        'F',
                        id='filtro-sexo', style={'width': '70px', 'background-color': '#2f6573', 'margin': '5px', 'color': '#03181e', 'padding': '0px'}
                    ),
                html.Div([
                    dcc.Graph(id='grafico-sexo')
                ]
                )
            ])
        ]),
        html.Div(style={'width': '25%', 'height': '635px', 'margin': '10px', 'border-radius': '15px', 'background-color': '#03181e'}, children=[
            html.Div(style={'width': ' 95%', 'height': '50px', 'margin': '10px', 'display': 'flex', 'flex-direction': 'row', }, children=[

                html.Button('2020', id='btn-2020', style=stl_btn_ano, n_clicks=0),
                html.Button('2021', id='btn-2021', style=stl_btn_ano, n_clicks=0),
                html.Button('2022', id='btn-2022', style=stl_btn_ano, n_clicks=0),
                html.Button('2023', id='btn-2023', style=stl_btn_ano, n_clicks=0)
                
            ]),
            html.Div(children=[
                dcc.Graph(id='grafico-ano')
            ])
        ]),
        html.Div(style={'width': '35%', 'height': '635px', 'background-color': '#03181e', 'margin': '10px', 'border-radius': '15px'}, children=[
            html.Div([
                html.Div(children=[
                    dcc.Dropdown(
                        vacina_covid_pb['vacina_descricao_dose'].unique(),
                        '1º Dose',
                        id='filtro-tipo-dose', style={'width': '300px', 'text-align': 'center', 'background-color': '#2f6573', 'margin': '20px 2px', 'color': '#03181e', 'padding': '0px'}
                    ),
                    html.Div(
                        dcc.Graph(id='grafico-faixa-dose')
                    )
                ])

            ])
        ])
    ])
])

@app.callback(
    Output('grafico-ano', 'figure'),
    Input('btn-2020', 'n_clicks'),
    Input('btn-2021', 'n_clicks'),
    Input('btn-2022', 'n_clicks'),
    Input('btn-2023', 'n_clicks')
)
def atualizaGraficoAno(btn1, btn2, btn3, btn4):
    valor = vaci_2020_meses
    ano = 2020
    if "btn-2020" == ctx.triggered_id:
        valor = vaci_2020_meses
        ano = 2020

    elif "btn-2021" == ctx.triggered_id:
        valor = vaci_2021_meses
        ano = 2021

    elif "btn-2022" == ctx.triggered_id:
        valor = vaci_2022_meses
        ano = 2022

    elif "btn-2023" == ctx.triggered_id:
        valor = vaci_2023_meses
        ano = 2023

    grafico_ano = px.line(x=meses, y=valor)
    grafico_ano.update_traces(line_color='#478797')
    grafico_ano.update_layout(
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(0, 0, 0, 0)',
        font_color='#67909b',
        separators=".,",
        xaxis=dict(gridcolor='#002b36', showline=True, linewidth=2, linecolor='#002b36'),
        yaxis=dict(gridcolor='#002b36', showline=True, linewidth=2, linecolor='#002b36'),
        width=400,
        xaxis_title='Meses',
        yaxis_title='Qtd. Vacinas',
        title= f'Contagem de Vacinação do ano {ano}'
)
    return grafico_ano

@app.callback(
    Output('grafico-faixa-dose', 'figure'),
    Input('filtro-tipo-dose', 'value')
)
def atualizaGraficoFaixaDose(dose):
    dados_filtrados = vacina_covid_pb[vacina_covid_pb['vacina_descricao_dose'] == dose]
    contagem_faixa_etaria = dados_filtrados['paciente_faixaEtaria'].value_counts()
    contagem_faixa_etaria = contagem_faixa_etaria.reindex(faixas_etarias)

    grafico_faixa_dose = px.bar(x=contagem_faixa_etaria.index, y=contagem_faixa_etaria)

    grafico_faixa_dose.update_traces(marker_color='#478797')
    grafico_faixa_dose.update_layout(
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(0, 0, 0, 0)',
        font_color='#67909b',
        separators=".,",
        xaxis=dict(gridcolor='#002b36', showline=True, linewidth=2, linecolor='#002b36'),
        yaxis=dict(gridcolor='#002b36', showline=True, linewidth=2, linecolor='#002b36'),
        width=500,
        xaxis_title='Faixa Etaria',
        yaxis_title='Qtd. Vacinas',
        title= f'Vacina de {dose} por faixa Etaria'
    )
    return grafico_faixa_dose

@app.callback(
    Output('grafico-sexo', 'figure'),
    Input('btn-sexo', 'n_clicks'),
    Input('btn-fabricante', 'n_clicks'),
    Input('filtro-sexo', 'value')
)
def atualizaGraficoSexo(btn1, btn2, sexo):
    dados_filtrados = vacina_covid_pb[vacina_covid_pb['paciente_enumSexoBiologico'] == sexo]
    contagem = dados_filtrados['paciente_racaCor_valor'].value_counts()
    grafico_sexo = px.bar(x=contagem.index, y=contagem)

    grafico_sexo.update_traces(marker_color='#478797')
    grafico_sexo.update_layout(
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(0, 0, 0, 0)',
        font_color='#67909b',
        separators=".,",
        xaxis=dict(gridcolor='#002b36', showline=True, linewidth=2, linecolor='#002b36'),
        yaxis=dict(gridcolor='#002b36', showline=True, linewidth=2, linecolor='#002b36'),
        width=500,
        title='Grafico Raça por Sexo biologico',
        xaxis_title='Raça / Cor',
        yaxis_title='Qtd. Vacinas'
    )

    if "btn-sexo" == ctx.triggered_id:
        dados_filtrados = vacina_covid_pb[vacina_covid_pb['paciente_enumSexoBiologico'] == sexo]
        contagem = dados_filtrados['paciente_racaCor_valor'].value_counts()
        grafico_sexo = px.bar(x=contagem.index, y=contagem)

        grafico_sexo.update_traces(marker_color='#478797')
        grafico_sexo.update_layout(
            plot_bgcolor='rgba(0, 0, 0, 0)',
            paper_bgcolor='rgba(0, 0, 0, 0)',
            font_color='#67909b',
            separators=".,",
            xaxis=dict(gridcolor='#002b36', showline=True, linewidth=2, linecolor='#002b36'),
            yaxis=dict(gridcolor='#002b36', showline=True, linewidth=2, linecolor='#002b36'),
            width=500,
            title='Grafico Raça por Sexo biologico',
            xaxis_title='Raça / Cor',
            yaxis_title='Qtd. Vacinas'
        )
        

    if "btn-fabricante" == ctx.triggered_id:
        grafico_sexo = px.bar(x=count.index, y=count)

        grafico_sexo.update_traces(marker_color='#478797')
        grafico_sexo.update_layout(
            plot_bgcolor='rgba(0, 0, 0, 0)',
            paper_bgcolor='rgba(0, 0, 0, 0)',
            font_color='#67909b',
            separators=".,",
            xaxis=dict(gridcolor='#002b36', showline=True, linewidth=2, linecolor='#002b36'),
            yaxis=dict(gridcolor='#002b36', showline=True, linewidth=2, linecolor='#002b36'),
            width=500,
            title="Fabricantes de Vacina",
            xaxis_title='Fabricante',
            yaxis_title='Qtd. Vacinas'
        )

    return grafico_sexo

if __name__ == '__main__':
    app.run_server(debug=False)