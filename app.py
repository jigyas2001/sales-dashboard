import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Sales Dashboard", layout="wide")

@st.cache_data
def load():
    df = pd.read_csv("data/superstore.csv", encoding="latin-1")
    df["Order Date"] = pd.to_datetime(df["Order Date"])
    return df.drop_duplicates()

df = load()
st.title("Cloud-Based Sales Analytics Dashboard")

# Filters
regions = st.sidebar.multiselect("Region", df["Region"].unique(), df["Region"].unique())
years = st.sidebar.multiselect("Year", sorted(df["Order Date"].dt.year.unique()),
                               sorted(df["Order Date"].dt.year.unique()))
d = df[df["Region"].isin(regions) & df["Order Date"].dt.year.isin(years)]

# KPIs
c1, c2, c3 = st.columns(3)
c1.metric("Total Sales", f"{d['Sales'].sum():,.0f}")
c2.metric("Total Profit", f"{d['Profit'].sum():,.0f}")
c3.metric("Orders", d["Order ID"].nunique())

# Charts
a, b = st.columns(2)
a.plotly_chart(px.bar(d.groupby("Region")["Sales"].sum().reset_index(),
               x="Region", y="Sales", title="Sales by Region"), use_container_width=True)
b.plotly_chart(px.bar(d.groupby("Category")["Profit"].sum().reset_index(),
               x="Category", y="Profit", title="Profit by Category"), use_container_width=True)

m = d.set_index("Order Date").resample("MS")["Sales"].sum().reset_index()
st.plotly_chart(px.line(m, x="Order Date", y="Sales", title="Monthly Sales Trend"), use_container_width=True)

top = d.groupby("Product Name")["Sales"].sum().nlargest(10).reset_index()
st.plotly_chart(px.bar(top, x="Sales", y="Product Name", orientation="h",
                title="Top 10 Products"), use_container_width=True)