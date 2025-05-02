import streamlit as st
import numpy as np
import joblib

# Custom styles
st.set_page_config(page_title="FDIA Detection", layout="centered")

st.markdown(
    """
    <style>
    .main {
        background-color: #f4f4f4;
    }
    .title {
        font-size: 32px;
        font-weight: bold;
        color: #3366cc;
    }
    .subtitle {
        font-size: 18px;
        color: #444;
    }
    .stButton>button {
        background-color: #3366cc;
        color: white;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True
)

# Load model
model = joblib.load('fdia_rf_model.pkl')

# Title Section
st.markdown("<div class='title'>🛡️ FDIA Detection System</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Real-time Detection of False Data Injection in IoT Telemetry</div>", unsafe_allow_html=True)
st.markdown("---")

# Input Fields in Columns
st.subheader("📥 Input Telemetry Data")

col1, col2 = st.columns(2)

with col1:
    cpu = st.slider("🔧 CPU Usage (%)", 0.0, 100.0, 50.0)
    memory = st.slider("💾 Memory Usage (%)", 0.0, 100.0, 50.0)
    net_in = st.number_input("⬇️ Network In (kbps)", min_value=0.0, value=500.0)

with col2:
    disk = st.slider("🗄️ Disk Usage (%)", 0.0, 100.0, 50.0)
    net_out = st.number_input("⬆️ Network Out (kbps)", min_value=0.0, value=500.0)

# Predict
st.markdown("### 🔍 Click Below to Analyze")

if st.button("🚀 Run Prediction"):
    input_data = np.array([[cpu, disk, memory, net_in, net_out]])
    prediction = model.predict(input_data)[0]
    label = "False Data Injection" if prediction == 1 else "Normal"

    st.markdown("---")
    if prediction == 1:
        st.error("⚠️ **Anomaly Detected: False Data Injection Attack**")
    else:
        st.success("✅ **System Operating Normally: No Anomaly Detected**")

    st.metric(label="Prediction Result", value=label)
