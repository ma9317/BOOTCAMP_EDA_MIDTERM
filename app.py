import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Brent vs WTI Dashboard")

# load data
data = pd.read_csv("oil_data_clean.csv")
data['date'] = pd.to_datetime(data['date'])

# 🔽 INTERACTIVITY (this is what you were missing)

# date range selector
start_date = st.date_input("Start date", data['date'].min())
end_date = st.date_input("End date", data['date'].max())

# filter data
filtered = data[(data['date'] >= str(start_date)) & (data['date'] <= str(end_date))]

# toggle which lines to show
show_wti = st.checkbox("Show WTI", True)
show_brent = st.checkbox("Show Brent", True)

# plot
fig, ax = plt.subplots()

if show_wti:
    ax.plot(filtered['date'], filtered['WTI_price'], label='WTI')

if show_brent:
    ax.plot(filtered['date'], filtered['BRENT_price'], label='Brent')

ax.legend()
ax.set_title("Crude Oil Prices Over Time")

st.pyplot(fig)