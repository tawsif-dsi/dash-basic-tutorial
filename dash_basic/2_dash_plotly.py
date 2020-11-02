import dash
import dash_html_components as html 
import dash_core_components as dcc 
import plotly.graph_objs as go 
import numpy as np 

app = dash.Dash()

np.random.seed(42)
x_values = np.random.randint(1,101,100)
y_values = np.random.randint(1,101,100)

x_bar = ['A','B','C','D']
y_bar = [15,8,20,10]

app.layout = html.Div(
    [
        html.Div(
            [
                dcc.Graph(
                    id='scatter_plot1',
                    figure={
                        'data':[
                            go.Scatter(
                                x=x_values,
                                y=y_values,
                                mode='markers',
                                marker={
                                    'size':12,
                                    'color': 'rgb(51,204,153)',
                                }
                            )
                        ],
                        'layout': go.Layout(
                            title='My Plot',
                            xaxis={
                                'title':'Some X title'
                            },
                            yaxis={
                                'title':'Some Y title'
                            }
                        )
                    }
                ),
            ]
        ),
        html.Div(
            [
                dcc.Graph(
                    id = 'bar_plot',
                    figure = {
                        'data':[
                            go.Bar(
                                x=x_bar,
                                y=y_bar,
                                marker={
                                    'color': 'rgb(51,204,153)'
                                }
                            )
                        ],
                        'layout': go.Layout(
                            title='Bar PLot',
                            xaxis={
                                'title': 'X_axis',
                            },
                            yaxis={
                                'title': 'Y_axis'
                            }
                        )
                    }
                )
            ]
        )
    ]
)

if __name__ == '__main__':
    app.run_server()