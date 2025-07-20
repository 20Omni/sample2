
import streamlit as st
import pandas as pd

# Title
st.title("📋 Task Assignment Dashboard")

# Upload CSV
uploaded_file = st.file_uploader("Upload Final Task Assignment CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # Show dataframe
    st.subheader("📊 Task Overview")
    st.dataframe(df[['Task ID', 'Priority', 'deadline_days_remaining', 'New Assigned User']])

    # Priority distribution
    st.subheader("🔺 Task Priority Distribution")
    st.bar_chart(df['Priority'].value_counts())

    # Tasks per user
    st.subheader("👤 Tasks Assigned Per User")
    st.bar_chart(df['New Assigned User'].value_counts())

    # Filter by user
    user_filter = st.selectbox("Filter tasks by user", options=['All'] + sorted(df['New Assigned User'].unique()))
    if user_filter != 'All':
        st.subheader(f"📌 Tasks for {user_filter}")
        st.dataframe(df[df['New Assigned User'] == user_filter])
