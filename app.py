import streamlit as st
from model import predict_risk

st.set_page_config(
    page_title="Smart Waterbody Safety",
    page_icon="🌊",
    layout="wide"
)

st.title("🌊 AI-Based Smart Waterbody Safety")
st.subheader("Multi-Hazard Early Warning System")

st.write(
    "A smart system for monitoring waterbody conditions "
    "and identifying possible hazards."
)

st.divider()

st.sidebar.header("📡 Waterbody Sensor Data")

water_level = st.sidebar.slider(
    "Water Level (%)", 0, 100, 50
)

water_flow = st.sidebar.slider(
    "Water Flow (%)", 0, 100, 40
)

rainfall = st.sidebar.slider(
    "Rainfall Intensity (%)", 0, 100, 30
)

mud_risk = st.sidebar.slider(
    "Slippery Mud Risk (%)", 0, 100, 20
)

animal_risk = st.sidebar.slider(
    "Animal/Crocodile Risk (%)", 0, 100, 10
)

# Risk prediction
prediction, probability = predict_risk(
    water_level,
    water_flow,
    rainfall,
    mud_risk,
    animal_risk
)

st.divider()

st.header("🤖 AI Risk Prediction")

col1, col2 = st.columns(2)

with col1:
    st.metric("Risk Prediction", prediction)

with col2:
    st.metric("Confidence", f"{probability:.1f}%")

if prediction == "CRITICAL":
    st.error("🚨 CRITICAL DANGER! Avoid the waterbody area.")

elif prediction == "DANGER":
    st.error("⚠️ DANGER! Keep people away from the area.")

elif prediction == "WARNING":
    st.warning("⚠️ WARNING! Continuous monitoring required.")

else:
    st.success("✅ SAFE! Current conditions are relatively safe.")

st.divider()

st.header("🔍 Hazard Monitoring")

if water_level >= 80:
    st.error("🌊 High water level detected!")
else:
    st.success("🌊 Water level is normal.")

if water_flow >= 80:
    st.error("💧 Heavy water flow detected!")
else:
    st.success("💧 Water flow is normal.")

if rainfall >= 80:
    st.warning("🌧️ Heavy rainfall detected!")

if mud_risk >= 70:
    st.warning("🪨 Slippery mud hazard detected!")

if animal_risk >= 70:
    st.error("🐊 Possible animal/crocodile danger detected!")

st.divider()

st.info(
    "The system uses a risk scoring model to classify "
    "waterbody safety conditions."
)

# Monitoring chart
st.divider()

st.header("📊 Waterbody Monitoring Data")

chart_data = {
    "Parameter": [
        "Water Level",
        "Water Flow",
        "Rainfall",
        "Mud Risk",
        "Animal Risk"
    ],
    "Value": [
        water_level,
        water_flow,
        rainfall,
        mud_risk,
        animal_risk
    ]
}

st.bar_chart(
    chart_data,
    x="Parameter",
    y="Value"
)
st.divider()

st.header("🗺️ Waterbody Location")

st.success("📍 Location: Hyderabad, Telangana")

st.write("Monitored Waterbody: Hyderabad Region")

location_data = {
    "lat": [17.3850],
    "lon": [78.4867]
}

st.map(location_data)
st.divider()

st.header("🗺️ Waterbody Location")

st.write("📍 Monitored Location: Hyderabad, Telangana")

location_data = {
    "lat": [17.3850],
    "lon": [78.4867]
}

st.map(location_data)
st.divider()

st.header("📈 Water Level Trend")

trend_data = {
    "Time": ["10:00", "10:30", "11:00", "11:30", "12:00"],
    "Water Level": [45, 50, 55, 65, water_level]
}

st.line_chart(
    trend_data,
    x="Time",
    y="Water Level"
)
st.divider()

st.header("📷 Camera-Based Hazard Monitoring")

st.write(
    "Capture an image of the waterbody area for hazard monitoring."
)

camera_image = st.camera_input("Take a picture")

if camera_image is not None:
    st.image(
        camera_image,
        caption="Captured Waterbody Image",
        use_container_width=True
    )

    st.info(
        "🔍 Image captured successfully. "
        "AI hazard detection can be connected here."
    )
    st.divider()

st.header("⚠️ Hazard Type")

hazard_type = st.selectbox(
    "Select the hazard to monitor:",
    [
        "Rising Water Level",
        "Heavy Water Flow",
        "Heavy Rainfall",
        "Slippery Mud",
        "Animal / Crocodile",
        "Multiple Hazards"
    ]
)

st.write("Selected Hazard:", hazard_type)

if hazard_type == "Rising Water Level":
    st.info("🌊 Monitoring water level changes.")

elif hazard_type == "Heavy Water Flow":
    st.info("💧 Monitoring water flow intensity.")

elif hazard_type == "Heavy Rainfall":
    st.info("🌧️ Monitoring rainfall intensity.")

elif hazard_type == "Slippery Mud":
    st.info("🪨 Monitoring slippery mud risk.")

elif hazard_type == "Animal / Crocodile":
    st.warning("🐊 Monitoring possible animal hazards.")

else:
    st.warning("⚠️ Monitoring multiple hazards simultaneously.")
    st.divider()

st.header("📋 System Status")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("🌊 Water Level", f"{water_level}%")

with col2:
    st.metric("💧 Water Flow", f"{water_flow}%")

with col3:
    st.metric("🌧️ Rainfall", f"{rainfall}%")

with col4:
    st.metric("⚠️ Risk Level", prediction)
    st.divider()

st.caption(
    "🌊 AI-Based Smart Waterbody Safety and Multi-Hazard Early Warning System"
)

st.caption(
    "Developed as an academic project for waterbody hazard monitoring and early warning."
)
