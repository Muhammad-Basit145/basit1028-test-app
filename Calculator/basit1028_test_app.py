import streamlit as st
from PIL import Image

st.markdown("""
# Simple Calculator
""")
st.subheader("""This is basic calculator application
   """)
image = Image.open('calc.png')
st.image(image)

st.header("Calculator")

m = st.number_input("Please enter the  your number")
b = st.number_input("Please enter another number")
c = m + b
d = m - b
e = m * b

# m = st.text_input("Please enter the number between 0 and 9")
# b = st.text_input("Please enter another number between 0 and 9")

st.text("The result after addition is")
st.write(c)
st.text("The result after subtraction is")
st.write(d)
st.text("The result after multiplication is")
st.write(e)


st.header("Advanced Calculator")
options = ["Factorial", "Square Root", "Square", "Power"]
choice = st.radio("Option", options)

if choice == "Factorial":
    a = st.number_input("Enter a Number", min_value=0, max_value=100, value=1, step=1)
    factorial = 1
    if a < 0:
        st.write("Sorry!!, factorial does not exist for negative numbers")
    elif a == 0:
        st.write("The factorial of 0 is 1")
    else:
        for i in range(1, a + 1):
            factorial = factorial * i
        st.write("The factorial of", a, "is", factorial)

elif choice == "Power":
    a = st.number_input("Enter a Number", min_value=0, max_value=100, value=1, step=1)
    b = st.number_input("Enter a Power value: ", min_value=0, max_value=100, value=1, step=1)
    result = a ** b
    st.write("Result is : ", result)

elif choice == "Square Root":
    a = st.number_input("Enter a Number", min_value=0, max_value=100, value=1, step=1)

    result = a ** 0.5
    st.write("Result is : ", result)



elif choice == "Square":
    a = st.number_input("Enter a Number", min_value=0, max_value=100, value=1, step=1)
    square_root = a * a
    st.write("Square of", a, "is", square_root)
