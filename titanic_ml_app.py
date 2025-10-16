import streamlit as st
import joblib
import numpy as np

# Load your saved model
rfmodel = joblib.load("RFclassifier_titanic_ml.joblib")
st.title("🚢 Titanic Survival Prediction App")

st.write("Enter passenger details below to predict survival:")

# Input fields
pclass = st.selectbox("Passenger Class (1 = 1st, 2 = 2nd, 3 = 3rd)", [1, 2, 3])
sex = st.selectbox("Sex", ["male", "female"])
age = st.slider("Age", 1, 80, 25)
sibsp = st.number_input("Number of Siblings/Spouses Aboard (sibsp)", 0, 8, 0)
parch = st.number_input("Number of Parents/Children Aboard (parch)", 0, 6, 0)
fare = st.number_input("Ticket Fare", 0.0, 500.0, 32.0)

# Preprocessing
sex = 1 if sex == "male" else 0
input_data = np.array([[pclass, sex, age, sibsp, parch, fare]])

# Predict
if st.button("Predict Survival"):
    prediction = rfmodel.predict(input_data)
    result = "🟢 Survived" if prediction[0] == 1 else "🔴 Did Not Survive"
    st.success(f"Prediction: {result}")

st.markdown("---")
st.caption(" RandomForestClassifier Scikit-learn")
