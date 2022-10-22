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
    py.plot(age_fig,filename = 'dr_age.html')

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

    py.plot(cal_fig, filename='dr_cal.html') 

dr_age()
dr_cal()
