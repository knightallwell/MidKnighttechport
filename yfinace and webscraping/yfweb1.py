import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import requests


tsla= yf.Tickers('TSLA')
tsla_data=tsla.tickers['TSLA'].history(period='max')
tsla_data.reset_index(inplace=True)
tsla_data.head()
tsla_data.info()
tsla_data.tail()
gme= yf.Ticker('GME')
gme_data=gme.history(period='max')
gme_data.reset_index(inplace=True)
gme_data.head()

webtsla='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm'
data_tsla=requests.get(webtsla).text
soup=BeautifulSoup(data_tsla, 'html5lib')
tsla_revenue=pd.read_html(data_tsla, match="Tesla Quarterly Revenue")[0]
tsla_revenue.rename(inplace=True,columns={"Tesla Quarterly Revenue (Millions of US $)": "Date", "Tesla Quarterly Revenue (Millions of US $).1": "Revenue"})
tsla_revenue
tsla_revenue['Revenue']=tsla_revenue['Revenue'].str.replace(',|\$',"", regex=True)
tsla_revenue.dropna(inplace=True)
tsla_revenue=tsla_revenue[tsla_revenue['Revenue']!=""]
tsla_revenue
gmeweb='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html'
gme22=requests.get(gmeweb).text
gmedata=BeautifulSoup(gme22, 'html5lib')
gme_revenue=pd.read_html(gme22,match="GameStop Quarterly Revenue")[0]
gme_revenue.rename(inplace=True, columns={"GameStop Quarterly Revenue (Millions of US $)": "Date", "GameStop Quarterly Revenue (Millions of US $).1": "Revenue"})
gme_revenue
gme_revenue['Revenue']=gme_revenue['Revenue'].str.replace(',|\$',"", regex=True)
gme_revenue.dropna(inplace=True)
gme_revenue=gme_revenue[gme_revenue['Revenue']!=""]
gme_revenue

def make_graph(stock_data, revenue_data, stock):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Historical Share Price", "Historical Revenue"), vertical_spacing = .3)
    stock_data_specific = stock_data[stock_data.Date <= '2021--06-14']
    revenue_data_specific = revenue_data[revenue_data.Date <= '2021-04-30']
    fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data_specific.Date), y=stock_data_specific.Close.astype("float"), name="Share Price"), row=1, col=1)
    fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data_specific.Date), y=revenue_data_specific.Revenue.astype("float"), name="Revenue"), row=2, col=1)
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    fig.update_layout(showlegend=False,
    height=900,
    title=stock,
    xaxis_rangeslider_visible=True)
    fig.show()

make_graph(tsla_data,tsla_revenue,'Tesla')
make_graph(gme_data,gme_revenue,'Tesla')
