import streamlit as st
import pandas as pd
import os

st.set_page_config(
    page_title="Smart Exam Monitoring",
    layout="wide"
)

st.title("🎓 Smart Exam Monitoring Dashboard")

# Load reviewed violations

if os.path.exists("violations_reviewed.csv"):

    data = pd.read_csv("violations_reviewed.csv")

    st.subheader("Violation Records")

    st.dataframe(data)

    total = len(data)

    approved = len(
        data[data["Status"] == "Approved"]
    )

    rejected = len(
        data[data["Status"] == "Rejected"]
    )

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Total Violations",
        total
    )

    col2.metric(
        "Approved",
        approved
    )

    col3.metric(
        "Rejected",
        rejected
    )

    st.subheader("Status Distribution")

    chart_data = data["Status"].value_counts()

    st.bar_chart(chart_data)

else:

    st.warning(
        "No reviewed violations found."
    )

# Show Final Report

if os.path.exists("final_report.txt"):

    st.subheader("AI Generated Report")

    with open(
        "final_report.txt",
        "r"
    ) as file:

        report = file.read()

    st.text(report)

else:

    st.info(
        "Final report not generated yet."
    )