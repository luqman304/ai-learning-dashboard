import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

st.set_page_config(page_title="AI Learning Dashboard", layout="wide")

st.title("🧠 AI Learning Dashboard")

# Load or initialize study log
if "log" not in st.session_state:
    st.session_state.log = []

# Add new study entry
with st.form("study_form"):
    col1, col2 = st.columns(2)
    topic = col1.text_input("Topic")
    resource = col2.text_input("Resource Link")
    notes = st.text_area("Notes", height=100)
    time_spent = st.number_input("Time Spent (hours)", min_value=0.0, step=0.5)
    status = st.selectbox("Status", ["In Progress", "Completed"])
    submitted = st.form_submit_button("Add Entry")

    if submitted and topic:
        st.session_state.log.append({
            "date": datetime.now().strftime("%Y-%m-%d"),
            "topic": topic,
            "resource": resource,
            "notes": notes,
            "time_spent": time_spent,
            "status": status
        })
        st.success("Entry added!")

# Show study log
if st.session_state.log:
    df = pd.DataFrame(st.session_state.log)
    st.subheader("📚 Study Log")
    st.dataframe(df)

    st.subheader("📊 Time Spent per Topic")
    topic_time = df.groupby("topic")["time_spent"].sum().sort_values(ascending=False)
    fig, ax = plt.subplots()
    topic_time.plot(kind="barh", ax=ax)
    st.pyplot(fig)