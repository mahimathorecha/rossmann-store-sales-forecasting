from pathlib import Path
from io import BytesIO

import pandas as pd
import plotly.express as px
import streamlit as st
st.set_page_config(page_title="Rossmann Dashboard", layout="wide")

st.title("Rossmann Sales & Customer Forecasts")
st.caption("Saved forecasts for August–September 2015")

file = Path(__file__).resolve().parent / "predictions" / "dashboard_forecasts.csv"

if not file.is_file():
    st.error(f"Cannot find: {file}")
    st.stop()

df = pd.read_csv(file, parse_dates=["Date"])

store = st.sidebar.selectbox(
    "Select store",
    ["All stores"] + sorted(df["Store"].unique().tolist()),
)

# Date range filter
st.sidebar.subheader("Select Date Range")

start_date = st.sidebar.date_input(
    "Start date",
    value=df["Date"].min().date(),
    min_value=df["Date"].min().date(),
    max_value=df["Date"].max().date(),
)

end_date = st.sidebar.date_input(
    "End date",
    value=df["Date"].max().date(),
    min_value=df["Date"].min().date(),
    max_value=df["Date"].max().date(),
)

# Apply filters
df = df[
    (df["Date"].dt.date >= start_date) &
    (df["Date"].dt.date <= end_date)
]

if store != "All stores":
    df = df[df["Store"] == store]

if df.empty:
    st.warning("No forecast records found for these filters.")
    st.stop()

col1, col2, col3 = st.columns(3)
col1.metric("Forecast sales", f"{df['Sales'].sum():,.0f}")
col2.metric(
    "Forecast customer visits",
    f"{df['Customers_prediction'].sum():,.0f}",
)
col3.metric("Stores", df["Store"].nunique())

st.caption("Predictions are estimates. Customer visits are not unique people.")

daily = df.groupby("Date", as_index=False)[
    ["Sales", "Customers_prediction"]
].sum()

st.plotly_chart(
    px.line(daily, x="Date", y="Sales", title="Daily sales forecast"),
    use_container_width=True,
)

st.plotly_chart(
    px.line(
        daily,
        x="Date",
        y="Customers_prediction",
        title="Daily customer visits forecast",
    ),
    use_container_width=True,
)

# Sales vs Customers comparison chart

comparison = daily.melt(
    id_vars="Date",
    value_vars=["Sales", "Customers_prediction"],
    var_name="Metric",
    value_name="Forecast"
)

st.subheader("Sales vs Customer Visits Comparison")

fig = px.line(
    comparison,
    x="Date",
    y="Forecast",
    color="Metric",
    title="Sales and Customer Visits Trend",
    markers=True,
)

st.plotly_chart(fig, use_container_width=True)


# Top 10 Stores by Forecast Sales

store_performance = (
    df.groupby("Store", as_index=False)["Sales"]
    .sum()
    .sort_values("Sales", ascending=False)
    .head(10)
)

st.subheader("Top 10 Stores by Forecast Sales")

fig = px.bar(
    store_performance,
    x="Store",
    y="Sales",
    title="Top 10 Stores - Forecast Sales",
    labels={
        "Store": "Store ID",
        "Sales": "Forecast Sales"
    },
    text_auto=".2s"
)

st.plotly_chart(fig, use_container_width=True)


# Store Performance Analysis Table

store_summary = (
    df.groupby("Store")
    .agg(
        Total_Forecast_Sales=("Sales", "sum"),
        Total_Forecast_Customers=("Customers_prediction", "sum"),
        Average_Daily_Sales=("Sales", "mean"),
        Average_Daily_Customers=("Customers_prediction", "mean"),
    )
    .reset_index()
)

store_summary = store_summary.sort_values(
    "Total_Forecast_Sales",
    ascending=False
)

st.subheader("Store Performance Analysis")

st.dataframe(
    store_summary,
    use_container_width=True,
    hide_index=True,
    column_config={
        "Store": "Store ID",
        "Total_Forecast_Sales": st.column_config.NumberColumn(
            "Total Forecast Sales", format="%.2f"
        ),
        "Total_Forecast_Customers": st.column_config.NumberColumn(
            "Total Forecast Customers", format="%.2f"
        ),
        "Average_Daily_Sales": st.column_config.NumberColumn(
            "Average Daily Sales", format="%.2f"
        ),
        "Average_Daily_Customers": st.column_config.NumberColumn(
            "Average Daily Customers", format="%.2f"
        ),
    }
)


# Excel Forecast Summary Report

excel_buffer = BytesIO()

overall_summary = pd.DataFrame({
    "Metric": [
        "Total Forecast Sales",
        "Total Forecast Customer Visits",
        "Number of Stores",
        "Forecast Start Date",
        "Forecast End Date"
    ],
    "Value": [
        df["Sales"].sum(),
        df["Customers_prediction"].sum(),
        df["Store"].nunique(),
        df["Date"].min().strftime("%Y-%m-%d"),
        df["Date"].max().strftime("%Y-%m-%d")
    ]
})

with pd.ExcelWriter(excel_buffer, engine="openpyxl") as writer:
    overall_summary.to_excel(
        writer, sheet_name="Overall Summary", index=False
    )

    store_summary.to_excel(
        writer, sheet_name="Store Performance", index=False
    )

    daily.to_excel(
        writer, sheet_name="Daily Forecasts", index=False
    )

excel_buffer.seek(0)

st.subheader("Download Excel Forecast Report")

st.download_button(
    label="Download Excel Report",
    data=excel_buffer.getvalue(),
    file_name="Rossmann_Forecast_Summary.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)


st.subheader("Forecast records")
st.dataframe(df, use_container_width=True, hide_index=True)

st.download_button(
    "Download selected forecasts",
    df.to_csv(index=False).encode("utf-8"),
    file_name="selected_forecasts.csv",
    mime="text/csv",
)