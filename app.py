import streamlit as st
import pandas as pd
import numpy as np
import joblib


# ----------------------------
# Load Model Files
# ----------------------------

model = joblib.load("Gradient_boosting_regressor.pkl")
scaler = joblib.load("scaler.pkl")
columns = joblib.load("columns.pkl")


# ----------------------------
# Page Configuration
# ----------------------------

st.set_page_config(
    page_title="Health Insurance Cost Predictor",
    page_icon="🏥",
    layout="wide"
)


# ----------------------------
# Custom CSS
# ----------------------------

st.markdown(
"""
<style>

.main{
    background-color:#f8f9fa;
}

h1{
    color:#0d6efd;
    text-align:center;
}

.card{
    background:white;
    padding:25px;
    border-radius:15px;
    box-shadow:0px 5px 20px rgba(0,0,0,0.1);
}

.result{
    background:#d1e7dd;
    padding:20px;
    border-radius:12px;
    color:#0f5132;
    font-size:25px;
    text-align:center;
}

.stButton>button{

    width:100%;
    height:50px;
    border-radius:10px;
    background:#0d6efd;
    color:white;
    font-size:18px;

}

</style>
""",
unsafe_allow_html=True
)



# ----------------------------
# Title
# ----------------------------

st.markdown(
"<h1>🏥 Health Insurance Cost Prediction</h1>",
unsafe_allow_html=True
)

st.write(
"""
This application predicts medical insurance charges using
a trained Gradient Boosting Regression model.
"""
)


# ----------------------------
# Input Section
# ----------------------------

st.markdown('<div class="card">', unsafe_allow_html=True)


col1,col2,col3 = st.columns(3)


with col1:

    age = st.number_input(
        "Age",
        min_value=1,
        max_value=100,
        value=30
    )


    bmi = st.number_input(
        "BMI",
        min_value=10.0,
        max_value=60.0,
        value=25.0
    )


with col2:

    children = st.number_input(
        "Number of Children",
        min_value=0,
        max_value=10,
        value=0
    )


    gender = st.selectbox(
        "Gender",
        ["Male","Female"]
    )


with col3:

    smoker = st.selectbox(
        "Smoker",
        ["No","Yes"]
    )


    region = st.selectbox(
        "Region",
        [
            "northeast",
            "northwest",
            "southeast",
            "southwest"
        ]
    )


st.markdown('</div>', unsafe_allow_html=True)



# ----------------------------
# Prediction Button
# ----------------------------

st.write("")


if st.button("Predict Insurance Cost"):


    # Create empty dataframe with trained columns

    input_data = pd.DataFrame(
        np.zeros((1,len(columns))),
        columns=columns
    )


    # Numerical features

    input_data["age"] = age
    input_data["bmi"] = bmi
    input_data["children"] = children



    # Gender encoding

    if gender=="Female":
        input_data["is_female"]=1
    else:
        input_data["is_female"]=0



    # Smoker encoding

    if smoker=="Yes":
        input_data["is_smoker"]=1
    else:
        input_data["is_smoker"]=0



    # Region encoding

    region_col = "region_" + region

    if region_col in input_data.columns:
        input_data[region_col]=1



    # BMI Category

    if bmi < 24.9:

        if "bmi_category_Normal" in input_data:
            input_data["bmi_category_Normal"]=1


    elif bmi < 29.9:

        if "bmi_category_Overweight" in input_data:
            input_data["bmi_category_Overweight"]=1


    else:

        if "bmi_category_Obese" in input_data:
            input_data["bmi_category_Obese"]=1



    # Scale input

    scaled_input = scaler.transform(input_data)



    # Prediction

    prediction = model.predict(
        scaled_input
    )[0]


    st.markdown(
    f"""
    <div class="result">
    💰 Estimated Insurance Cost<br>
    <b>${prediction:,.2f}</b>
    </div>
    """,
    unsafe_allow_html=True
    )



# ----------------------------
# Footer
# ----------------------------

st.write("")
st.info(
"""
Model Used: Gradient Boosting Regressor  
Features: 12 engineered features  
Scaling: StandardScaler
"""
)