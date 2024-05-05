import dash #Se importa la libreria de Dash
from dash import html
import dash_bootstrap_components as dbc
import math
from dash.dependencies import Input, Output


#se importa el front 
from fronted.fronted import layout
app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])
app=app.server
app.layout = layout


@app.callback(
    Output('ResultadoOperacion', 'children'),
    [Input('EntradaCohesion', 'value'),
     Input('EntradaSobreCarga', 'value'),
     Input('EntradaBase', 'value'),
     Input('EntradaPesoEspecifico', 'value'),
     Input('EntradaAnguloFriccion', 'value'),
     Input('cimentacion-radio', 'value')]
)


def update_output(EntradaCohesion, EntradaSobreCarga, EntradaBase, EntradaPesoEspecifico, EntradaAnguloFriccion, selected_value):
   
    if None in (EntradaCohesion, EntradaSobreCarga, EntradaBase, EntradaPesoEspecifico, EntradaAnguloFriccion, selected_value):
        return "Por favor, complete todos los campos para calcular la carga última del suelo."

    try:
        EntradaCohesion = float(EntradaCohesion)
        EntradaSobreCarga = float(EntradaSobreCarga)
        EntradaBase = float(EntradaBase)
        EntradaPesoEspecifico = float(EntradaPesoEspecifico)
        EntradaAnguloFriccion = float(EntradaAnguloFriccion)

    except ValueError:
        return "Por favor, asegúrese de que todos los campos numéricos contienen valores válidos."
    

    nq = math.tan(math.radians(45 + (EntradaAnguloFriccion / 2))) ** 2 * math.e ** (math.pi * math.tan(math.radians(EntradaAnguloFriccion)))
    cot_angulo_friccion = 1 / math.tan(math.radians(EntradaAnguloFriccion))
    nc = (nq - 1) * cot_angulo_friccion
    nγ = 2 * (nq + 1) * math.tan(math.radians(EntradaAnguloFriccion))


    if selected_value == 'corrida':
        resultado1 = (float(EntradaCohesion)*nc)+(float(EntradaSobreCarga)*nq)+(0.5*float(EntradaBase)*float(EntradaPesoEspecifico)*nγ)
        
    elif selected_value == 'cuadrada':
        resultado1 = 1.3*float(EntradaCohesion)*nc+float(EntradaSobreCarga)*nq+0.3*float(EntradaBase)*float(EntradaPesoEspecifico)*nγ # operación
    elif selected_value == 'circular':
        resultado1 = 1.3*float(EntradaCohesion)*nc+float(EntradaSobreCarga)*nq+0.4*float(EntradaBase)*float(EntradaPesoEspecifico)*nγ   #operación
    else:
        resultado1 = None

    return 'La Carga ultima del suelo cimentación diseñada es [KN/m2] : ' + str(resultado1)
    




if __name__ =='__main__':
    app.run_server(debug=True)
    
