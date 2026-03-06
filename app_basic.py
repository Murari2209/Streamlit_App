import streamlit as st

st.title("Welcome to Streamlit!")
st.text_input("Enter your name", key="name")
if st.button("Greet Me"):
    st.write(f"Hello, {st.session_state.name}!")