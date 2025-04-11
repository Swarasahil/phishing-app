
import streamlit as st
import pickle
from feature_extractor import extract_features
import pandas as pd

# Load model
model = pickle.load(open("phishing_model.pkl", "rb"))

st.title("🔍 Phishing URL Detector")
url_input = st.text_input("Enter a URL to check if it's phishing:")

if st.button("Check URL"):
    if url_input:
        features = extract_features(url_input)
        df = pd.DataFrame([features])
        prediction = model.predict(df)[0]
        st.markdown("### 🛡️ Result:")
        if prediction == 1:
            st.error("⚠️ This is a Phishing Website!")
        else:
            st.success("✅ This is a Legitimate Website.")
