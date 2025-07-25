import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page config
st.set_page_config(page_title="Retail Superstore Dashboard", layout="wide")

# Title and description
st.markdown("<h1 style='text-align: center; color: #1f77b4;'>📊 Retail Superstore Sales Dashboard</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px;'>An interactive dashboard to explore and analyze sales trends, customer segments, and regional performance</p>", unsafe_allow_html=True)
st.markdown("---")

# Load dataset
df = pd.read_csv("C:/Users/NITI/OneDrive/Desktop/Data Analyst project/sales_data.csv", encoding='latin1')
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Month'] = df['Order Date'].dt.to_period('M').astype(str)

# Sidebar filters
st.sidebar.header("🧰 Filter Options")
selected_category = st.sidebar.multiselect("Select Category", options=df['Category'].unique(), default=df['Category'].unique())
selected_segment = st.sidebar.multiselect("Select Segment", options=df['Segment'].unique(), default=df['Segment'].unique())

# Filtered Data
df_filtered = df[(df['Category'].isin(selected_category)) & (df['Segment'].isin(selected_segment))]

# 📈 Monthly Trends
st.subheader("📅 Monthly Sales Trend vs Monthly Order Count")
col1, col2 = st.columns(2)

with col1:
    sales_trend = df_filtered.groupby('Month')['Sales'].sum().reset_index()
    fig1, ax1 = plt.subplots(figsize=(8, 4))
    sns.lineplot(data=sales_trend, x='Month', y='Sales', marker='o', ax=ax1)
    ax1.set_title("Monthly Sales Trend", fontsize=12)
    ax1.tick_params(axis='x', rotation=45)
    st.pyplot(fig1)

with col2:
    order_count = df_filtered.groupby('Month')['Order ID'].nunique().reset_index(name='Order Count')
    fig2, ax2 = plt.subplots(figsize=(8, 4))
    sns.lineplot(data=order_count, x='Month', y='Order Count', marker='o', color='green', ax=ax2)
    ax2.set_title("Monthly Order Count", fontsize=12)
    ax2.tick_params(axis='x', rotation=45)
    st.pyplot(fig2)

st.markdown("---")

# 📦 Category & Segment Wise
st.subheader("📦 Category-wise & Segment-wise Sales Analysis")
col3, col4 = st.columns(2)

with col3:
    category_sales = df_filtered.groupby('Category')['Sales'].sum().reset_index().sort_values(by='Sales', ascending=False)
    fig3, ax3 = plt.subplots(figsize=(6, 4))
    sns.barplot(data=category_sales, x='Sales', y='Category', palette='Set2', ax=ax3)
    ax3.set_title("Category-wise Sales", fontsize=12)
    st.pyplot(fig3)

with col4:
    segment_sales = df_filtered.groupby('Segment')['Sales'].sum().reset_index().sort_values(by='Sales', ascending=False)
    fig4, ax4 = plt.subplots(figsize=(6, 4))
    sns.barplot(data=segment_sales, x='Sales', y='Segment', palette='Set3', ax=ax4)
    ax4.set_title("Segment-wise Sales", fontsize=12)
    st.pyplot(fig4)

st.markdown("---")

# 🌍 Region Analysis
st.subheader("🌍 Region-wise Sales and Profit Analysis")
col5, col6 = st.columns(2)

with col5:
    region_sales = df_filtered.groupby('Region')['Sales'].sum().reset_index().sort_values(by='Sales', ascending=False)
    fig5, ax5 = plt.subplots(figsize=(6, 4))
    sns.barplot(data=region_sales, x='Sales', y='Region', palette='coolwarm', ax=ax5)
    ax5.set_title("Region-wise Sales", fontsize=12)
    st.pyplot(fig5)

with col6:
    region_profit = df_filtered.groupby('Region')['Profit'].sum().reset_index().sort_values(by='Profit', ascending=False)
    fig6, ax6 = plt.subplots(figsize=(6, 4))
    sns.barplot(data=region_profit, x='Profit', y='Region', palette='Spectral', ax=ax6)
    ax6.set_title("Region-wise Profit", fontsize=12)
    st.pyplot(fig6)

st.markdown("---")

# Footer
st.markdown("<p style='text-align: center; color: grey;'>Built with ❤️ using Streamlit | By Niti</p>", unsafe_allow_html=True)
