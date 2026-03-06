import streamlit as st

st.title("Product Form")

## Input for product name
product_name = st.sidebar.text_input("Enter the product name")

product_category = st.selectbox("Select the product category", ["Electronics", "Fashion", "Home Appliances", "Books", "Toys"]) 
## Input for product price
product_price = st.number_input("Enter the price of the product", min_value=0, step=1)

if st.button("Add Product"):
    st.write("Product added successfully!")
    st.write(f"Product Name: {product_name}")
    st.write(f"Product Category: {product_category}")
    st.write(f"Product Price: Rs- {product_price}")