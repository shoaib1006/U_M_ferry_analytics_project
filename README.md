# 🛥️ Toronto Island Ferry Analytics Dashboard

An end-to-end data analytics project and Streamlit dashboard investigating historical ferry ticket sales and redemptions (2015–2025) for Toronto Island Park.

## 📊 Project Overview
This project analyzes 10 years of ferry operation data to identify demand patterns, seasonality, and operational efficiency. It culminates in an interactive dashboard designed for resource allocation and maintenance scheduling.

## 🔍 Key Findings
- **Peak Demand:** Operational volume peaks at **12:00 PM**, with the busiest window between 11:00 AM and 3:00 PM.
- **Extreme Seasonality:** August is the peak month. The **Off-Season Utilization Index (0.07)** shows winter traffic is only 7% of summer peaks.
- **Efficiency:** Maintained an overall **84.43% ticket redemption rate** across 12.97 million sales.
- **High Correlation:** A **0.94 correlation** between sales and redemptions indicates most passengers use tickets almost immediately.

## 🛠️ Data Cleaning & Engineering
- **Consistency Checks:** Resolved 125,257 logical inconsistencies where redemptions exceeded sales by capping redemptions at the sales count.
- **Feature Engineering:** Extracted `Hour`, `Month`, `Day of Week`, and `Weekend` flags for granular time-series analysis.

## 🚀 Deployment

### Local Setup
1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/ferry-analytics-dashboard.git
   cd ferry-analytics-dashboard
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: .\\venv\\Scripts\\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Dashboard:**
   ```bash
   streamlit run ticsales.py
   ```

## 📦 Technologies Used
- **Python** (Pandas, NumPy)
- **Visualization:** Matplotlib, Seaborn
- **Web Framework:** Streamlit
- **Notebook Environment:** Google Colab
