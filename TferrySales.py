import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Page configuration
st.set_page_config(page_title='Ferry Operations Dashboard', layout='wide')
st.title('☖‍♂️ Toronto Island Ferry Analytics Dashboard')

# --- Sidebar: Dashboard Modules & User Roles ---
st.sidebar.header("Dashboard Modules")
st.sidebar.markdown("""
- • **Real-time KPI cards**
- • **Interactive time-series plots**
- • **Date & time filters**
- • **Peak vs off-peak comparison**
""")

st.sidebar.header("User Roles")
st.sidebar.markdown("""
- • **Operations team**
- • **Policy planners**
- • **Management stakeholders**
""")

# --- KPI Row ---
st.header("Real-time KPI Cards")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Sales", "12.97M")
col2.metric("Redemption Rate", "84.43%")
col3.metric("Peak Hour", "12:00 PM")
col4.metric("Off-Season Index", "0.07")

# --- Charts ---
st.markdown("---")
st.subheader("Interactive Demand Analysis")
col_a, col_b = st.columns(2)

with col_a:
    st.write("**Monthly Trends (Peak vs Off-Peak)**")
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    sales = [130455, 146179, 201753, 401395, 1090751, 1814395, 3083858, 3442762, 1605867, 638215, 254575, 161846]
    fig1, ax1 = plt.subplots()
    sns.barplot(x=months, y=sales, palette='magma', ax=ax1)
    st.pyplot(fig1)

with col_b:
    st.write("**Hourly Sales Profile**")
    hours = list(range(24))
    demand = [55357, 24314, 11131, 6734, 15000, 45000, 120000, 350000, 750000, 1100000, 1300000, 1382050, 1423362, 1398298, 1346528, 1208209, 950000, 700000, 500000, 400000, 299957, 238737, 201737, 133926]
    fig2, ax2 = plt.subplots()
    sns.lineplot(x=hours, y=demand, color='darkblue', ax=ax2)
    st.pyplot(fig2)

st.info("Module: Date & Time Filters active via Sidebar (Simulated)")
