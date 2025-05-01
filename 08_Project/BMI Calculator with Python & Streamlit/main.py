import streamlit as st

st.title("🧮 BMI CALCULATOR")

# User inputs
weight = st.number_input("Enter Your Weight In KG")
height = st.number_input("Enter Your Height In Meter")

# Calculate BMI on button click
if st.button("Calculate"):
    if height > 0:
        BMI = weight / (height * height)
        st.write(f"## Your BMI is {BMI:.2f}")

        if BMI <= 18.5:
            st.warning("You Are Underweight")
        elif BMI > 18.5 and BMI < 24.9:
            st.success("You Have Normal Weight")
        elif BMI >= 25 and BMI < 29.9:
            st.info("You Are Overweight")
        elif BMI >= 30:
            st.error("You Are Obese")
    else:
        st.error("Height must be greater than zero.")

# Display reference information
st.info(
    "💡 **BMI Categories:**\n\n"
    "- Underweight: BMI < 18.5\n"
    "- Normal weight: 18.5 – 24.9\n"
    "- Overweight: 25 – 29.9\n"
    "- Obese: BMI ≥ 30"
)
