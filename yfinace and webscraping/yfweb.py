import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import requests
import datetime



tsla= yf.Tickers('TSLA')
tsla_data=tsla.tickers['TSLA'].history(period='max')
tsla_data.head()
tsla_data.info()
tsla_data.tail()
gme= yf.Ticker('GME')
gme_data=gme.history(period='max')
gme_data.head()

webtsla='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm'

data_tsla=requests.get(webtsla)
soup=BeautifulSoup(data_tsla.text, 'html')
spup=soup.find('table')
tslarevenew1=pd.read_html(str(spup))[0]
tslarevenew1

gmeweb='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html'
gme22=requests.get(gmeweb)
gmedata=BeautifulSoup(gme22.text, 'html')
gme_soup=gmedata.find('table')
gme_soup
gme_soup1=pd.read_html(str(gme_soup))[0]
gme_soup1

tsla_data
tslarevenew1.tail()
gme_data.head()
gme_soup1.tail()

tslarevenew1['Tesla Annual Revenue (Millions of US $).1']=tslarevenew1['Tesla Annual Revenue (Millions of US $).1'].str.replace(',|\$',"", regex=True)
gme_soup1['GameStop Annual Revenue (Millions of US $).1']=gme_soup1['GameStop Annual Revenue (Millions of US $).1'].str.replace(',|\$',"", regex=True)

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

make_graph(gme_data,gme_soup1,'gme')

sns.relplot(data=tsla_data, x='Stock Splits', y='Date', kind='line')
plt.ylabel('Date')
plt.xlabel('Stock Splits')
plt.title('Tesla stock')
plt.grid()
plt.ylim()
plt.tight_layout()

sns.relplot(data=tslarevenew1, y='Tesla Annual Revenue (Millions of US $).1', x='Tesla Annual Revenue (Millions of US $)', kind='line')
plt.ylabel('Revenue')
plt.xlabel('Date')
plt.title('Tesla stock')
plt.grid()
plt.ylim()
plt.tight_layout()

sns.relplot(data=gme_data, x='Stock Splits', y='Date', kind='line')
plt.ylabel('Date')
plt.xlabel('Stock Splits')
plt.title('GameStop')
plt.grid()
plt.ylim()
plt.tight_layout()

sns.relplot(data=gme_soup1, y='GameStop Annual Revenue (Millions of US $).1', x='GameStop Annual Revenue (Millions of US $)', kind='line')
plt.ylabel('Revenue')
plt.xlabel('Date')
plt.title('GameStop')
plt.grid()
plt.ylim()
plt.tight_layout()

