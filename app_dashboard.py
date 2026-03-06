## Mini Dashboard 
import streamlit as st

## streamlit/app_dashboard.py
st.title("Simple Sales Dashboard")
st.write("A simple dashboard to display sales data")

## Dropdown to select month
months = st.selectbox("Select Month", ["January", "February", "March", "April"])

## Sample sales data for each month
sales = {
    "January": 1200,
    "February": 1500,
    "March": 900,
    "April": 2000
}

## Displaying the total sales for the selected month
st.metric("Total Sales", f"Rs- {sales[months]}")
st.write(f"Total Sales for {months}: Rs- {sales[months]}")

### Displaying a bar chart for sales data
st.bar_chart(list(sales.values()))
