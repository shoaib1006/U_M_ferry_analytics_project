import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Page configuration
st.set_page_config(page_title='Ferry Operations Dashboard', layout='wide')
st.title('🛥️ Toronto Island Ferry Analytics Dashboard')

# --- Sidebar findings and info ---
st.sidebar.header("Project Context")
st.sidebar.info("Analysis of historical ferry ticket sales and redemption data (2015-2025).")

# --- KPI Row ---
st.header("Key Performance Indicators")
col1, col2, col3, col4 = st.columns(4)
# Note: In a production app, these values would be calculated from a database/CSV
col1.metric("Total Sales", "12.97M")
col2.metric("Redemption Rate", "84.43%")
col3.metric("Peak Hour", "12:00 PM")
col4.metric("Off-Season Index", "0.07")

# --- Visualizations Row 1 ---
st.markdown("---")
col_a, col_b = st.columns(2)

with col_a:
    st.subheader("📅 Monthly Sales Trends")
    # Example data structure matching our analysis
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    sales_data = [130455, 146179, 201753, 401395, 1090751, 1814395, 3083858, 3442762, 1605867, 638215, 254575, 161846]
    fig1, ax1 = plt.subplots()
    sns.barplot(x=months, y=sales_data, palette='viridis', ax=ax1)
    ax1.set_title("Total Ticket Sales by Month")
    st.pyplot(fig1)

with col_b:
    st.subheader("⏲️ Hourly Demand Profile")
    # Example data representing the peak at 12:00
    hours = list(range(24))
    # Simplified trend line based on our peak findings
    fig2, ax2 = plt.subplots()
    # Dummy demand curve centered around noon
    demand = [55357, 24314, 11131, 6734, 15000, 45000, 120000, 350000, 750000, 1100000, 1300000, 1382050, 1423362, 1398298, 1346528, 1208209, 950000, 700000, 500000, 400000, 299957, 238737, 201737, 133926]
    sns.lineplot(x=hours, y=demand, marker='o', color='teal', ax=ax2)
    ax2.set_title("Passenger Volume by Hour of Day")
    ax2.set_xticks(range(0, 24, 2))
    st.pyplot(fig2)

# --- Performance Section ---
st.markdown("---")
st.header("📊 Toronto Island Ferry Performance & Findings")

left_info, right_info = st.columns(2)

with left_info:
    st.markdown("### Key Findings")
    st.write("- **Extreme Seasonality:** Winter traffic is just 7% of summer peak volume (Index: 0.07).")
    st.write("- **Peak Windows:** Operational demand surges between **11:00 AM and 3:00 PM**, peaking at noon.")
    st.write("- **Immediate Use:** A 0.94 correlation suggests tickets are mostly redeemed in the same time-block as purchase.")

with right_info:
    st.markdown("### Operational Recommendations")
    st.success("**Dynamic Staffing:** Allocate maximum personnel during the 11:00-15:00 summer window.")
    st.warning("**Maintenance Window:** Major vessel maintenance should be prioritized between November and March.")

st.markdown("---")
st.info("Dashboard generated from Toronto Island Ferry Dataset (2015-2025) analysis.")
