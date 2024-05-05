import dash 
from dash import html
import dash_bootstrap_components as dbc

#Se realiza las definiciones de cada una de las variables a utilizar 
Definiciones = dbc.Container([
    dbc.Row([
        dbc.Col(
            html.Div([
    html.H1("CONCEPTOS IMPORTANTES"),
    html.H3("Cohesión"),
    html.P("La cohesión en suelos es una propiedad que describe la capacidad de las partículas de suelo para mantenerse unidas o adherirse entre sí."),
    html.H3("Sobre Carga"),
    html.P("La sobrecarga en suelos se refiere a la presión adicional ejercida sobre el suelo que puede afectar su comportamiento geotécnico"),
    html.H3("Peso Específico γ"),
    html.P("El peso específico del suelo, también conocido como peso unitario o densidad del suelo, es una medida de la masa de un determinado volumen de suelo.  Se expresa en unidades de peso por unidad de volumen, generalmente en kN/m³"),
    html.H3("B"),
    html.P("Ancho Zapata"),
    html.H3("Factores de Capacidad de Carga"),
    html.P("Son coeficientes que se utilizan en la ecuación de capacidad de carga última de suelos para determinar la capacidad de carga de una cimentación en una masa de suelo."),
    html.P("Nc (Factor de capacidad de carga por cohesión): Este factor se relaciona con la cohesión del suelo. "),
    html.P("Nq (Factor de capacidad de carga por presión neta): Este factor se refiere a la presión neta del suelo sobre la cimentación. "),
    html.P("Nγ (Factor de capacidad de carga por peso unitario): Este factor se relaciona con el peso unitario del suelo sobre la cimentación."),
    html.H3("Ángulo de fricción Φ"),
    html.P("Este ángulo se define como el ángulo de inclinación máxima a la cual una superficie de suelo puede soportar una carga sin que se produzca un deslizamiento o falla. Es un indicador de la fricción entre las partículas del suelo, y su valor está influenciado por las propiedades de los materiales del suelo, como el tamaño y la forma de las partículas, la compactación y el contenido de humedad."),
            ])
            
            , md= 12, style={'background-color':'#FFF0F5'}),
             
    ])
])