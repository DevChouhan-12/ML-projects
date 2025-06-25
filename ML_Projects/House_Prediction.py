import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

# Dataset
data = {
    'Area': [1400, 1600, 1700, 1875, 1100, 1550, 2350, 2450, 1425, 1700],
    'Bedrooms': [3, 3, 3, 4, 2, 3, 4, 4, 2, 3],
    'Age': [10, 5, 8, 2, 12, 7, 4, 5, 6, 3],
    'Price': [75, 85, 89, 95, 60, 82, 115, 118, 76, 90]
}
df = pd.DataFrame(data)

# Model Training
X = df[['Area', 'Bedrooms', 'Age']]
y = df['Price']
model = LinearRegression()
model.fit(X, y)

# Streamlit App
st.title("🏡 House Price Predictor")

# User Inputs
area = st.number_input("Enter Area (sq ft)", min_value=500, max_value=5000, value=1500)
bedrooms = st.number_input("Enter Number of Bedrooms", min_value=1, max_value=10, value=3)
age = st.number_input("Enter Age of the House", min_value=0, max_value=50, value=5)

# Prediction Button
if st.button("Predict Price"):
    new_data = pd.DataFrame([[area, bedrooms, age]], columns=['Area', 'Bedrooms', 'Age'])
    predicted_price = model.predict(new_data)stre
    st.success(f"🏷️ Estimated House Price: ₹{round(predicted_price[0], 2)} Lakh")
