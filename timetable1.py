import streamlit as st
import pandas as pd

# Page setup
st.set_page_config(page_title="Weekly Timetable - View Only", layout="wide")
st.title("📘 MSc Weekly Study Timetable")

# Define the timetable data
data = {
    "Time": ["8:30 PM – 11:00 PM"] * 7,
    "Day": [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ],
    "Course": [
        "Supervised",
        "Supervised",
        "Business Intelligence",
        "Business Intelligence",
        "Data Governance",
        "Research Methods",
        "Text Analytics / Financial Management"
    ]
}

# Convert to DataFrame
timetable_df = pd.DataFrame(data)
}

# Display timetable
st.markdown("### 📅 Timetable")
st.dataframe(timetable_df, use_container_width=True)
