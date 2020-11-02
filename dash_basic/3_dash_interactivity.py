import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash()

app.layout = html.Div(
    [
        dcc.Input(id='input-id', value='Initial Text', type='text'), # core component input
        html.Div(
            id='output-id'
        ) # html component, default component property -> children
    ]
)

@app.callback(
    Output(component_id='output-id',component_property='children'),
    [Input(component_id='input-id',component_property='value')]
)
def update_front(input_text):
    return 'You have typed {}'.format(input_text)

if __name__ == '__main__':
    app.run_server(debug=True)