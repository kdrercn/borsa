import numpy as np
import pandas as pd

#Data Source
import yfinance as yf

#Data viz
import plotly.graph_objs as go
import matplotlib.pyplot as plt


tupras = yf.Ticker('EREGL.IS')
hist = tupras.history(period='3mo', interval='1h')

from plotly.subplots import make_subplots

fig3 = make_subplots(specs=[[{"secondary_y": True}]])
fig3.add_trace(go.Candlestick(x=hist.index,
                              open=hist['Open'],
                              high=hist['High'],
                              low=hist['Low'],
                              close=hist['Close'],
                             ))
fig3.add_trace(go.Bar(x=hist.index, y=hist['Volume'], name='Volume'),secondary_y=True)
fig3.update_layout(xaxis_rangeslider_visible=False)
fig3.add_trace(go.Scatter(x=hist.index,y=hist['Close'].ewm(span=5).mean(),marker_color='red',name='5'))
fig3.add_trace(go.Scatter(x=hist.index,y=hist['Close'].ewm(span=22).mean(),marker_color='green',name='22'))
fig3.add_trace(go.Bar(x=hist.index, y=hist['Volume'], name='Volume'),secondary_y=True)
fig3.update_layout(title={'text':'EREGL', 'x':0.5})
fig3.update_yaxes(range=[0,1000000000],secondary_y=True)
fig3.update_yaxes(visible=False, secondary_y=True)
fig3.update_layout(xaxis_rangeslider_visible=False)  #hide range slider
fig3.update_xaxes(rangebreaks = [
                       dict(bounds=['sat','mon']), # hide weekends
                       #dict(bounds=[16, 9.5], pattern='hour'), # for hourly chart, hide non-trading hours (24hr format)
                       dict(values=["2023-06-28","2023-06-29","2023-06-30"]) #hide Xmas and New Year
                                ])
fig3.show()

ema5 = hist['Close'].ewm(span=5).mean()
ema22 = hist['Close'].ewm(span=22).mean()

c = []

for x, y in zip(ema5,ema22):
    if x > y:
        c.append("5")    
    elif y > x:
        c.append("22")
    else:
        c.append("EŞİT")

a = c

b=a[0:1]
for i in range(len(a)-1):
    #print (a[i],a[i+1])
    if a[i]!=a[i+1]:
        b.append(a[i+1])
a=b

c = []

for x, y in zip(ema5,ema22):
    if x > y:
        c.append("5")    
    elif y > x:
        c.append("22")
    else:
        c.append("EŞİT")
a=c

c[0] = 5

b=[]
for i in range(len(a)-1):
        b.append(a[i+1])

b.insert(-1,b[-2])

sonuc = []

for m in range(len(c)):
    sonuc.append(0)

for x in range(len(c)):
    
    if b[x] == c[x]:
        sonuc[x] = "İŞLEM YOK"
    
    if b[x] == "5" and c[x] == "22":
        sonuc[x] = "SAT"
    
    if b[x] == "22" and c[x] == "5":
        sonuc[x] = "AL"

print(sonuc)

