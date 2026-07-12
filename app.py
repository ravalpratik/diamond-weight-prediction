import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Diamond Weight Prediction",
    page_icon="💎",
    layout="wide"
)

@st.cache_resource
def load_model():
    return joblib.load("diamond_weight_model.joblib")

model = load_model()

st.title("💎 Diamond Final Weight Prediction")
st.write("Predict the final polished diamond weight from rough diamond characteristics.")

st.divider()

col1, col2 = st.columns(2)

with col1:

    rough_weight = st.number_input(
        "Rough Weight (ct)",
        min_value=0.01,
        value=3.50,
        step=0.01
    )

    shape = st.selectbox(
        "Shape",
        ["Round","Oval","Pear","Princess","Emerald","Cushion"]
    )

    length = st.number_input(
        "Length (mm)",
        min_value=0.0,
        value=8.90
    )

    width = st.number_input(
        "Width (mm)",
        min_value=0.0,
        value=8.55
    )

with col2:
    height = st.number_input(
        "Height (mm)",
        min_value=0.0,
        value=5.95
    )

    color = st.selectbox(
        "Color",
        ["D","E","F","G","H","I","J"]
    )

    clarity = st.selectbox(
        "Clarity",
        ["IF","VVS1","VVS2","VS1","VS2","SI1","SI2"]
    )

    crack = st.selectbox(
        "Crack Level",
        ["Low","Medium","High"]
    )

    cut = st.selectbox(
        "Cut Type",
        ["Brilliant","Step","Mixed"]
    )

st.divider()

if st.button("🔮 Predict Final Weight", use_container_width=True):

    input_df = pd.DataFrame({
        "Rough_Weight_ct":[rough_weight],
        "Shape":[shape],
        "Length_mm":[length],
        "Width_mm":[width],
        "Height_mm":[height],
        "Color":[color],
        "Clarity":[clarity],
        "Crack_Level":[crack],
        "Cut_Type":[cut]
    })

    prediction = model.predict(input_df)[0]

    st.success("Prediction Completed Successfully!")

    st.metric(
        label="💎 Predicted Final Weight",
        value=f"{prediction:.2f} ct"
    )

    recovery = (prediction / rough_weight) * 100

    st.metric(
        label="Recovery Percentage",
        value=f"{recovery:.2f}%"
    )

    st.info(
        f"Estimated polished weight is **{prediction:.2f} carats**, "
        f"which is approximately **{recovery:.2f}%** of the rough diamond weight."
    )

st.divider()

st.caption("Developed by **Raval Pratik** | Diamond Weight Prediction using Random Forest Regression")