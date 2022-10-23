import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv

import plotly.express as p
import plotly.offline as py
# py.init_notebook_mode(connected=True)
import plotly.graph_objs as go
import plotly.figure_factory as ff    

from datetime import datetime
from dateutil.relativedelta import relativedelta





#visualization
def dr_age_visualization():
    current_age = 10
    #data = pd.read_csv('simDTS.csv')
    data = pd.read_csv('src/visualization/simDTS.csv')

    #pre processing
    pct_age = data.groupby(['t']).agg(number = ('t','count'),dr=('y','sum'),edr=('pd','sum'),std = ('pd','std'))
    pct_age["dr"] = pct_age["dr"]/pct_age["number"]
    pct_age["edr"] = pct_age["edr"]/pct_age["number"]

    x_range = [pct_age.index.min(),pct_age.index.max()]
    y_range = [pct_age["dr"].append(pct_age["edr"]).min(),pct_age["dr"].append(pct_age["edr"]).max()]

    age_layout = go.Layout(
        title=
        {
            'y':0.9,
            'x':0.45,
            'xanchor': 'center',
            'yanchor': 'top'
        },
        xaxis=dict(
            title="age(month)",
            range=x_range
        ),
        yaxis=dict(
            title="default rate(%)",
            range=y_range
        )
    )


    age_trace0 = go.Scatter(
        x = pct_age.index[0:current_age],
        y = pct_age["dr"][0:current_age],
        mode = 'lines',
        name = 'default rate'   
    )

    age_trace1 = go.Scatter(
        x = pct_age.index[0:current_age],
        y = pct_age["edr"][0:current_age],
        mode = 'lines',
        name = 'expected default rate'
    )

    age_fig = go.Figure({'data': [age_trace0, age_trace1],'layout': age_layout})
    #age_fig.show()
    # save image
    py.plot(age_fig,filename = 'res/dr_age.html',auto_open = False)



    #visualization with predicted value
    age_predicted_trace0 = go.Scatter(
        x = pct_age.index,
        y = pct_age["dr"],
        mode = 'lines',
        name = 'default rate'
    )

    age_predicted_trace1 = go.Scatter(
        x = pct_age.index,
        y = pct_age["edr"],
        mode = 'lines',
        name = 'expected default rate'
    )

    age_predicted_fig = go.Figure({'data': [age_predicted_trace0, age_predicted_trace1],'layout': age_layout})
    #age_fig.show()
    # save image
    py.plot(age_predicted_fig,filename = 'res/dr_age_predicted.html',auto_open = False)

dr_age_visualization()
