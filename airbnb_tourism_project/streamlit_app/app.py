import streamlit as st
import pandas as pd
from pathlib import Path

# ----------------------
# Page config
# ----------------------
st.set_page_config(page_title="Airbnb Tourism Dashboard", layout="wide")

st.title("🏙️ Airbnb Tourism Pressure Dashboard")
st.markdown("**Barcelona • Melbourne • Sydney**")

# ----------------------
# Paths
# ----------------------
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

# ----------------------
# Load data
# ----------------------
@st.cache_data
def load_city(city):
    return pd.read_csv(DATA_DIR / city / f"{city}_final.csv")

# ----------------------
# Sidebar
# ----------------------
st.sidebar.header("Controls")

city = st.sidebar.selectbox(
    "Select City",
    ["barcelona", "melbourne", "sydney"]
)

df = load_city(city)

# ----------------------
# KPIs
# ----------------------
c1, c2, c3 = st.columns(3)

c1.metric("Average Price", round(df["price"].mean(), 2))
c2.metric("Total Listings", len(df))
c3.metric("Avg Reviews", round(df["number_of_reviews"].mean(), 1))

# ----------------------
# Charts
# ----------------------
st.subheader("Price Distribution")
st.bar_chart(df["price"].value_counts().head(30))

st.subheader("Room Type Counts")
st.bar_chart(df["room_type"].value_counts())

st.subheader("Reviews per Month")
st.line_chart(df["reviews_per_month"])

st.subheader("Correlation")
st.dataframe(df.corr(numeric_only=True))
