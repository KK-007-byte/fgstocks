


# In[34]:




# In[35]:





# In[36]:
import seaborn as sns
import ta
import pandas as pd
import plotly.graph_objects as go
import plotly.figure_factory as ff
import plotly.express as px
import streamlit as st

from pypfopt.efficient_frontier import EfficientFrontier
from pypfopt.expected_returns import mean_historical_return
from pypfopt.risk_models import CovarianceShrinkage


# In[37]:




st.title("📊 Stock Return Analysis")

# Sidebar
st.sidebar.header("Select Parameters")
tickers = st.sidebar.multiselect("Choose Stocks", ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA'], default=['AAPL', 'MSFT'])
start_date = st.sidebar.date_input("Start Date", pd.to_datetime('2020-01-01'))
end_date = st.sidebar.date_input("End Date", pd.to_datetime('2024-12-31'))

# Load data
@st.cache_data
def load_data(tickers, start, end):
    data = yf.download(tickers, start=start, end=end)
    return data

data = load_data(tickers, start_date, end_date)
returns = data.pct_change().dropna()

# 📌 Correlation Heatmap
if len(tickers) > 1:
    st.subheader("Correlation Heatmap of Daily Returns")
    corr = returns.corr().round(2)
    heatmap = ff.create_annotated_heatmap(
        z=corr.values,
        x=corr.columns.tolist(),
        y=corr.index.tolist(),
        annotation_text=corr.values,
        colorscale='Viridis',
        showscale=True
    )
    st.plotly_chart(heatmap)

# 📌 Histogram of Daily Returns
st.subheader("Histogram of Daily Return Distributions")


hist_fig = px.histogram(
    returns,
    x=('Close','AAPL'),
    facet_col=('Volume', 'AAPL'),
    color=('Volume', 'AAPL'),
    nbins=100,
    title='Daily Return Distributions',
    histnorm='probability'
)

st.plotly_chart(hist_fig)

st.caption("Built with Streamlit & Plotly")


# In[ ]:




