import streamlit as st

def grocery(order):
    discount = 25 if order > 200 else 0
    disc_amt = discount * order / 100
    tax = 0.07 * (order - disc_amt)
    return tax, disc_amt

st.title('Grocery Order Calculator')

order = st.selectbox('Select the amount of your order', range(1, 10001))
tax, discount_amount = grocery(order)

st.write(f'The discount is ${discount_amount:.2f}')
st.write(f'The tax is ${tax:.2f}')

