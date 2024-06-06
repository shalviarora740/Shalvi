import streamlit as st

# Add a title
st.title("My First Streamlit App")

# Add an input widget
name = st.text_input("Enter your name", "Type here...")

if name:

     st.write(f"Hello, {name}!")
