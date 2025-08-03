import streamlit as st
import pandas as pd

# Page setup
st.set_page_config(page_title="Weekly Timetable - View Only", layout="wide")
st.title("📘 MSc Weekly Study Timetable")

# Days and time slots
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
time_slots = ["8:30 - 11:00"]

# Example fixed schedule (customize as needed)
timetable_data = {
    "Monday": ["Supervised"],
    "Tuesday": ["Supervised"],
    "Wednesday": ["Business Intelligence"],
    "Thursday": ["Business Intelligence"],
    "Friday": ["Data Governance"],
    "Saturday": ["Research Methods"],
    "Sunday": ["Text Analytics / Financial Management"]
}

# Create timetable DataFrame
timetable = pd.DataFrame(timetable_data, index=time_slots)

# Display timetable
st.markdown("### 📊 MSc Study Timetable ")
st.dataframe(timetable, use_container_width=True)
