# app.py

import streamlit as st
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Page Configuration
st.set_page_config(page_title="🎓 Admission Predictor", layout="centered")
st.title("🎓 Student Admission Predictor using Logistic Regression")

# File Upload
uploaded_file = st.file_uploader("admission_data.csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader("📊 Uploaded Dataset Preview")
    st.write(df.head())

    # Step 1: Split features & labels
    X = df[['Exam1', 'Exam2']]
    y = df['Admitted']

    # Step 2: Train-Test Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Step 3: Train Model
    model = LogisticRegression()
    model.fit(X_train, y_train)

    # Step 4: Evaluate
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    st.success(f"✅ Model trained successfully with accuracy: {round(accuracy*100, 2)}%")

    # Step 5: Take user input
    st.subheader("📥 Enter New Student's Exam Scores")
    exam1 = st.number_input("📌 Exam 1 Score", min_value=0, max_value=100, value=70)
    exam2 = st.number_input("📌 Exam 2 Score", min_value=0, max_value=100, value=75)

    if st.button("🚀 Predict Admission"):
        new_data = pd.DataFrame([[exam1, exam2]], columns=["Exam1", "Exam2"])
        prediction = model.predict(new_data)[0]

        if prediction == 1:
            st.success("🎉 The student is likely to be ADMITTED.")
        else:
            st.error("❌ The student is likely to be REJECTED.")

else:
    st.warning("📎 Please upload the dataset to begin.")
