import streamlit as st

st.title("Price Calculator")

## Input for product price
product_price = st.number_input("Enter the price of the product", min_value=0, step=1)

## Slider for selecting discount percentage
discount_percentage = st.slider("Select discount percentage", min_value=0, max_value=100, value=0, step=1)
## Calculating the final price after applying the discount
if st.button("Calculate Final Price"):
    discount_amount = product_price * (discount_percentage / 100)
    final_price = int(product_price - discount_amount)
    st.write(f"Final Price after {discount_percentage}% discount: Rs- {final_price}")  

## Displaying the original price, discount percentage, and final price in a table
    st.table({
        "Original Price": [product_price],
        "Discount Percentage": [discount_percentage],
        "Final Price": [final_price]
    })  
