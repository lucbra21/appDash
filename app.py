from dash import Dash, html, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px

# Inicializamos la aplicación
app = Dash(__name__)
server = app.server  # Necesario para deployment en Render

# Creamos algunos datos de ejemplo
df = pd.DataFrame({
    'Mes': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo'],
    'Ventas': [100, 150, 200, 180, 210]
})

# Definimos el layout de la aplicación
app.layout = html.Div([
    html.H1('Mi Primera Aplicación en Dash',
            style={'textAlign': 'center', 'color': '#2c3e50'}),
    
    html.Div([
        # Dropdown para seleccionar tipo de gráfico
        dcc.Dropdown(
            id='tipo-grafico',
            options=[
                {'label': 'Gráfico de Barras', 'value': 'bar'},
                {'label': 'Gráfico de Línea', 'value': 'line'}
            ],
            value='bar',  # Valor inicial
            style={'width': '50%', 'margin': '10px auto'}
        ),
        
        # Aquí se mostrará el gráfico
        dcc.Graph(id='grafico-principal')
    ])
])

# Callback para actualizar el gráfico
@callback(
    Output('grafico-principal', 'figure'),
    Input('tipo-grafico', 'value')
)
def actualizar_grafico(tipo_grafico):
    if tipo_grafico == 'bar':
        fig = px.bar(df, x='Mes', y='Ventas', title='Ventas Mensuales')
    else:
        fig = px.line(df, x='Mes', y='Ventas', title='Ventas Mensuales')
    
    fig.update_layout(
        title_x=0.5,  # Centra el título
        plot_bgcolor='white',
        paper_bgcolor='white',
    )
    return fig

# Ejecutar el servidor
if __name__ == '__main__':
    app.run_server(debug=True)