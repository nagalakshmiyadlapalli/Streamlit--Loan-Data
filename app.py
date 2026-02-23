import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("loan_NB.pkl")

st.set_page_config(page_title="Loan Approval Prediction", page_icon="🏦", layout="centered")

st.title("🏦 Loan Approval Prediction App")
st.write("Enter applicant details to predict loan approval status")

# ---------------------- INPUT FIELDS ----------------------

Gender = st.selectbox("Gender", ["Male", "Female"])

Married = st.selectbox("Married", ["Yes", "No"])

Dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])

Education = st.selectbox("Education", ["Graduate", "Not Graduate"])

Self_Employed = st.selectbox("Self Employed", ["Yes", "No"])

ApplicantIncome = st.number_input("Applicant Income", min_value=0, value=5000)

CoapplicantIncome = st.number_input("Coapplicant Income", min_value=0, value=0)

LoanAmount = st.number_input("Loan Amount (in thousands)", min_value=0.0, value=100.0)

Loan_Amount_Term = st.number_input("Loan Amount Term (in months)", min_value=12.0, value=360.0)

Credit_History = st.selectbox("Credit History", [1.0, 0.0])

Property_Area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

# ---------------------- INPUT DATAFRAME ----------------------

input_data = pd.DataFrame({
    "Gender": [Gender],
    "Married": [Married],
    "Dependents": [Dependents],
    "Education": [Education],
    "Self_Employed": [Self_Employed],
    "ApplicantIncome": [ApplicantIncome],
    "CoapplicantIncome": [CoapplicantIncome],
    "LoanAmount": [LoanAmount],
    "Loan_Amount_Term": [Loan_Amount_Term],
    "Credit_History": [Credit_History],
    "Property_Area": [Property_Area]
})

# ---------------------- PREDICTION ----------------------

if st.button("Predict Loan Status"):
    prediction = model.predict(input_data)[0]

    if prediction == "Y":
        st.success("✅ Loan Approved")
    else:
        st.error("❌ Loan Rejected")