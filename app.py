import streamlit as st
import time
import random
import datetime

# ---------- SIDEBAR: CONTROLS ----------
st.sidebar.title("🎮 Control Panel")

mode = st.sidebar.radio("Select Mode", ["Auto", "Manual", "Sleep"])
speed = st.sidebar.slider("Speed (%)", 0, 100, 50)
led = st.sidebar.checkbox("💡 LED On")
target_date = st.sidebar.date_input("Set Target Date")
user_note = st.sidebar.text_area("Notes")

if st.sidebar.button("🚀 Execute Task"):
    st.sidebar.success("Command sent!")

# ---------- MAIN DASHBOARD ----------
st.title("📊 System Dashboard")
st.markdown("Monitor and control your system in real-time.")

# --- System Overview ---
st.header("🧠 System Overview")
col1, col2, col3 = st.columns(3)
col1.metric("Status", "✅ Online")
col2.metric("Speed", f"{speed} %")
col3.metric("Mode", mode)

# --- Device Info ---
with st.expander("📦 Device Details"):
    st.write(f"🔌 LED: {'ON' if led else 'OFF'}")
    st.write(f"📅 Target Date: {target_date}")
    st.write(f"📝 Notes: {user_note or 'None'}")

# --- Live Chart (Simulated Data) ---
st.header("📈 Sensor Data")

sensor_data = [random.randint(40, 90) for _ in range(20)]
st.line_chart(sensor_data)

# --- Real-Time Logs ---
st.header("📋 System Log")
log_placeholder = st.empty()

for i in range(5):
    log_placeholder.write(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] Step {i+1}: Task in progress...")
    time.sleep(0.3)

log_placeholder.success("✅ All tasks completed.")


