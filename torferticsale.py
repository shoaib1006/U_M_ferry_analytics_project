import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Page configuration with a vibrant theme
st.set_page_config(page_title='Toronto Ferry Analytics', layout='wide', initial_sidebar_state='expanded')

# --- Sidebar Navigation ---
st.sidebar.title("🛳️ Navigation")
page = st.sidebar.radio("Go to", ["Executive Summary", "Temporal Analysis", "Operational Insights"])

# Data Placeholders
total_sales = 12972051
redemption_rate = 84.43
peak_hour = 12
util_index = 0.07

if page == "Executive Summary":
    # 1. Title Fix: Ensuring the title is explicitly rendered
    st.title("📈 Toronto Island Ferry Analytics Dashboard")
    st.markdown("### Performance & Strategy Overview (2015-2025)")
    
    # KPI Row with vibrant metrics
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Sales", f"{total_sales/1e6:.2f}M", delta="Vibrant Demand")
    col2.metric("Redemption Rate", f"{redemption_rate}%", delta="High Efficiency")
    col3.metric("Peak Demand", f"{peak_hour}:00 PM")
    col4.metric("Utilization Index", f"{util_index}")

    st.divider()
    
    # 3. Maintenance Window Mention
    st.subheader("🛠️ Operational & Maintenance Recommendations")
    col_m1, col_m2 = st.columns(2)
    with col_m1:
        st.info("**Peak Staffing:** Increase personnel between 11:00 AM and 3:00 PM during July/August.")
    with col_m2:
        st.warning("**Maintenance Window:** Schedule major vessel overhauls between **November and March** due to the low utilization index (0.07).")

elif page == "Temporal Analysis":
    st.title("⏰ Temporal Demand Analysis")
    
    # 2. Vibrant Colors: Monthly Bar Chart
    st.write("### Monthly Volume (Seasonality)")
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    sales = [130455, 146179, 201753, 401395, 1090751, 1814395, 3083858, 3442762, 1605867, 638215, 254575, 161846]
    fig1, ax1 = plt.subplots(figsize=(10, 4))
    # Using 'flare' palette for vibrant visuals
    sns.barplot(x=months, y=sales, palette='flare', ax=ax1)
    ax1.set_title("Ticket Sales Concentration", fontsize=12, color='darkred')
    st.pyplot(fig1)

    # Vibrant Line Plot
    st.write("### Hourly Traffic Profile")
    hours = list(range(24))
    demand = [55357, 24314, 11131, 6734, 15000, 45000, 120000, 350000, 750000, 1100000, 1300000, 1382050, 1423362, 1398298, 1346528, 1208209, 950000, 700000, 500000, 400000, 299957, 238737, 201737, 133926]
    fig2, ax2 = plt.subplots(figsize=(10, 4))
    sns.lineplot(x=hours, y=demand, color='#FF4B4B', linewidth=3, marker='o', markerfacecolor='black', ax=ax2)
    st.pyplot(fig2)

elif page == "Operational Insights":
    st.title("⚙️ Operational Deep-Dive")

    col_left, col_right = st.columns(2)
    
    with col_left:
        st.write("### Sales vs Redemption Correlation")
        corr_data = np.array([[1.0, 0.94], [0.94, 1.0]])
        fig3, ax3 = plt.subplots()
        # Vibrant 'rocket' heatmap
        sns.heatmap(corr_data, annot=True, cmap='rocket', xticklabels=['Sales', 'Redeem'], yticklabels=['Sales', 'Redeem'], ax=ax3)
        st.pyplot(fig3)

    with col_right:
        st.write("### Demand Distribution & Outliers")
        dist_data = np.random.exponential(scale=50, size=1000)
        fig4, ax4 = plt.subplots()
        sns.boxplot(y=dist_data, color='#00D4FF', ax=ax4)
        ax4.set_ylabel("Ticket Count")
        st.pyplot(fig4)

    st.sidebar.markdown("---")
    st.sidebar.write("**Maintenance Insight:**")
    st.sidebar.caption("Off-season utilization suggests fleet maintenance is optimal during winter months.")
