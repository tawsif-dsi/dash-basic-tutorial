import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

random_x = np.random.randint(1,101,100)
random_y = np.random.randint(1,101,100)

data = [go.Scatter(
    x=random_x,
    y=random_y,
    mode='markers',
    marker=dict(
        size=12,
        color='rgb(12,201,54)',
    )
)]
layout = go.Layout(
    title ='Scatter Plot',
    xaxis = {'title':'X AXIS'},
    yaxis = dict(title='Y AXIS')
)
fig = go.Figure(data=data,layout=layout)
pyo.plot(fig)

