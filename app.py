""" BMI Calculator """
# Step 1: Importing streamlit
import streamlit as st

st.title('BMI Calculator')

# Step 2: Taking user inputs
weight = st.number_input(
    label='Enter your weight (kg):',
    min_value=1.0,
    max_value=250.0,
    value=50.0,
    step=0.5
)

height = st.number_input(
    label='Enter your height (m):',
    min_value=0.5,
    max_value=2.2,
    value=1.5,
    step=0.01
)

if st.button('Calculate'):
    bmi = weight / height ** 2
    st.write(f'Your BMI is: {bmi:.2f}')