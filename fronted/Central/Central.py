import dash #Se importa la libreria de Dash
from dash import html,dcc # Importa el módulo html de Dash para poder utilizar etiquetas HTML.
import dash_bootstrap_components as dbc # Importa Dash Bootstrap Components que proporciona componentes basados en Bootstrap para Dash.

# Se Define un contenedor central que encapsula todo el contenido de esta sección.
Central = dbc.Container([# Se define un contenedor.
    dbc.Row([ # Se Crea una fila usando.Las filas son usadas para agrupar horizontalmente columnas.
        dbc.Col( 

            html.Div([ # Se crea un contenedor genérico que en este caso contiene un título.
    html.H2("Seleccione tipo de Cimentación a diseñar:", style={'text-align': 'center'}),
    html.Br(), html.Br(), #Espacio de renglon
    
    # Componente RadioItems para seleccionar el tipo de cimentación.
    dcc.RadioItems(   id='cimentacion-radio', # Identificador único para el componente.
            options=[
            {'label': 'Cimentación Corrida', 'value': 'corrida'},
       
            {'label': 'Cimentación Cuadrada', 'value': 'cuadrada'},
           
            {'label': 'Cimentación Circular', 'value': 'circular'},
            
        ],
        value='corrida'  # Valor predeterminado seleccionado
              
        ),
        html.Div(id='output') # División para mostrar resultados o mensajes
])
                                          
                ,md=4,style={'background-color':'#FFF0F5'}),
        
    # Define otra columna para mostrar las fórmulas según el método Terzagui.
        dbc.Col(
            html.Div([
    #texto formulas
    html.H2("Formula metodo Terzagui", style={'text-align': 'center'}),
    html.H3("Cimentación Corrida", style={'text-align': 'center'}),
    html.P("qu= C*Nc+q*Nq+1/2*B*γ*Nγ", style={'text-align': 'center'}),

    html.H3("Cimentación Cuadrada", style={'text-align': 'center'}),
    html.P("qu= 1.3*C*Nc+q*Nq+0.3*B*γ*Nγ", style={'text-align': 'center'}),

    html.H3("Cimentación Circular", style={'text-align': 'center'}),
    html.P("qu= 1.3*C*Nc+q*Nq+0.4*B*γ*Nγ", style={'text-align': 'center'}),
 ])
            
            ,md=4,style={'background-color':'#FFF0F5'}),

        dbc.Col('Imagenes referencia de tipo de cimentación'
                
                , md= 4, style={'background-color':'#FFF0F5'}),
        
    ])
])