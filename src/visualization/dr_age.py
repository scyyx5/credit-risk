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

def dr_age(): 
    # data = pd.read_csv('../../visualization/simDTS.csv')
    data = pd.read_csv('src/visualization/simDTS.csv')

    #pre processing
    pct_age = data.groupby(['t']).agg(number = ('t','count'),dr=('y','sum'),edr=('pd','sum'),std = ('pd','std'))
    pct_age["dr"] = pct_age["dr"]/pct_age["number"]
    pct_age["edr"] = pct_age["edr"]/pct_age["number"]

    #visualization
    age_layout = go.Layout(
        title=
        {   'text': "default rate and age",
            'y':0.9,
            'x':0.45,
            'xanchor': 'center', 
            'yanchor': 'top'
        },
        xaxis=dict(
            title="age(month)"
        ),
        yaxis=dict(
            title="default rate(%)"
        ) 
    )

    age_trace0 = go.Scatter(
        x = pct_age.index,
        y = pct_age["dr"],
        mode = 'lines',
        name = 'default rate'   
    )

    age_trace1 = go.Scatter(
        x = pct_age.index,
        y = pct_age["edr"],
        mode = 'lines',
        name = 'predicted default rate'   
    )

    age_fig = go.Figure({'data': [age_trace0, age_trace1],'layout': age_layout})
    #age_fig.show()
    # save image
    py.plot(age_fig,filename = 'res/dr_age.html',auto_open = False)


dr_age()
