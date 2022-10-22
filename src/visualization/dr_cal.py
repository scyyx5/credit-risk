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


# This is used to change integer to date list
def datelist(list):
    start_date = datetime(2016,1,1)
    result = []
    for i in list:
        result_date = start_date +relativedelta(months=i)
        result.append("%04d-%02d" % (result_date.year, result_date.month))
        
    return result




def dr_cal():
    
    # data = pd.read_csv('../../visualization/simDTS.csv')
    data = pd.read_csv('src/visualization/simDTS.csv')

    #pre processing
    data['cal'] = data['t'] + data['v']
    grouped_cal = data.groupby('cal')[['cal','y','pd']]
    pct_cal = grouped_cal.agg({'cal' : 'count','y':'sum','pd':'sum'})

    #pct_cal

    data['cal'] = data['t'] + data['v']
    pct_cal = data.groupby(['cal']).agg(number = ('cal','count'),dr=('y','sum'),edr=('pd','sum'))
    #pct_cal

    pct_cal["dr"] = pct_cal["dr"]/pct_cal["number"]
    pct_cal["edr"] = pct_cal["edr"]/pct_cal['number']

    pct_cal['date'] = datelist(pct_cal.index)

    # visualization
    cal_layout = go.Layout(
    title=
        {   'text': "default rate and calendar time",
            'y':0.9,
            'x':0.45,
            'xanchor': 'center', 
            'yanchor': 'top'
        },
        xaxis=dict(
            title="calendar time"
        ),
        yaxis=dict(
            title="default rate(%)"
        ) 
    )

    cal_trace0 = go.Scatter(
        x = pct_cal['date'],
        y = pct_cal["dr"],
        mode = 'lines',
        name = 'default rate'   
    )

    cal_trace1 = go.Scatter(
        x = pct_cal['date'],
        y = pct_cal["edr"],
        mode = 'lines',
        name = 'predicted default rate'   
    )

    cal_fig = go.Figure({'data': [cal_trace0,cal_trace1],'layout': cal_layout})
    #cal_fig.show()

    py.plot(cal_fig, filename='res/dr_cal.html',auto_open = False)


dr_cal()
