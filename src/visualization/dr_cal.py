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
start_date = datetime(2019,1,1)

# change integer to date string
def inttodata(i):
    date = start_date + relativedelta(months=i)
    return ("%04d-%02d" % (date.year, date.month))

# This is used to change integer to date list
def datelist(list):
    result = []
    for i in list:
        '''
        result_date = start_date +relativedelta(months=i)
        result.append("%04d-%02d" % (result_date.year, result_date.month))
        '''
        result.append(inttodata(i))
    return result




def dr_cal_visualization():

    current_month = relativedelta(datetime.now(),start_date).months + relativedelta(datetime.now(),start_date).years * 12
    
    data = pd.read_csv('simDTS.csv')
    #data = pd.read_csv('src/visualization/simDTS.csv')

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
    x_range = [pct_cal.index.min(),pct_cal.index.max()]
    y_range = [pct_cal["dr"].append(pct_cal["edr"]).min(),pct_cal["dr"].append(pct_cal["edr"]).max()]
    cal_layout = go.Layout(
    title=
        {
            'y':0.9,
            'x':0.45,
            'xanchor': 'center', 
            'yanchor': 'top'
        },
        xaxis=dict(
            title="calendar time",
            range = x_range,
            tickmode = "array",
            tickvals =  pct_cal.index,
            ticktext = pct_cal['date']

        ),
        yaxis=dict(
            title="default rate(%)",
            range = y_range
        ) 
    )

    cal_trace0 = go.Scatter(
        x = pct_cal.index[0:current_month],
        #x = pct_cal['date'],
        y = pct_cal["dr"][0:current_month],
        mode = 'lines',
        name = 'default rate'   
    )

    cal_trace1 = go.Scatter(
        #x = pct_cal['date'][0:current_month],
        x = pct_cal.index[0:current_month],
        y = pct_cal["edr"][0:current_month],
        mode = 'lines',
        name = 'predicted default rate'
    )



    cal_fig = go.Figure({'data': [cal_trace0,cal_trace1],'layout': cal_layout})
    cal_fig.show()
    #py.plot(cal_fig, filename='res/dr_cal.html',auto_open = False)
    py.plot(cal_fig, filename='dr_cal.html',auto_open = False)

    #plot with predicted value
    cal_trace0 = go.Scatter(
        x = pct_cal.index,
        y = pct_cal["dr"],
        mode = 'lines',
        name = 'default rate'
    )

    cal_trace1 = go.Scatter(
        x = pct_cal.index,
        y = pct_cal["edr"],
        mode = 'lines',
        name = 'predicted default rate'
    )

    cal_fig = go.Figure({'data': [cal_trace0,cal_trace1],'layout': cal_layout})
    cal_fig.show()

    #py.plot(cal_fig, filename='res/dr_cal_predicted.html',auto_open = False)
    py.plot(cal_fig, filename='dr_cal_predicted.html',auto_open = False)

dr_cal_visualization()
