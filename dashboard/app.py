import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
from datetime import datetime
import os

st.sidebar.header("📝 Log New Day")

with st.sidebar.form(key="log_form"):
    mode = st.selectbox("Mode", ["Study Mode", "Play Mode", "Rest Mode"])
    hours_coding = st.number_input("Hours of Coding", min_value=0.0, max_value=24.0)
    ai_usage_hours = st.number_input("AI Tool Usage (hrs)", min_value=0.0, max_value=24.0)
    sleep_hours = st.number_input("Sleep Hours", min_value=0.0, max_value=24.0)
    distractions = st.slider("Distraction Level (0-10)", 0, 10)
    bugs_reported = st.number_input("Bugs Reported", min_value=0)
    commits = st.number_input("Commits Made", min_value=0)
    task_success = st.slider("Task Success Score (0-1)", 0.0, 1.0)
    cognitive_load = st.slider("Cognitive Load (0-1)", 0.0, 1.0)
    submit_button = st.form_submit_button("Submit Log")

    if submit_button:
        new_entry = f"{mode},{hours_coding},{ai_usage_hours},{sleep_hours},{distractions},{bugs_reported},{commits},{task_success},{cognitive_load}\n"
        with open("data/logged_entries.csv", "a") as f:
            f.write(new_entry)
        st.success("Entry logged successfully!")

# Load data
base_df = pd.read_csv('data/processed/processed_productivity.csv')

# Load new entries (if file exists)
log_file = "data/logged_entries.csv"
if os.path.exists(log_file):
    new_df = pd.read_csv(log_file)
    df = pd.concat([base_df, new_df], ignore_index=True)
else:
    df = base_df


# Add a fake 'mode' column for now
np.random.seed(42)
df['mode'] = np.random.choice(['Study Mode', 'Play Mode', 'Rest Mode'], size=len(df))

# Sidebar filters
st.sidebar.title("Filter Options")
selected_mode = st.sidebar.selectbox("Productivity Mode", ['All', 'Study Mode', 'Play Mode', 'Rest Mode'])

# Apply mode filter
if selected_mode != 'All':
    df = df[df['mode'] == selected_mode]

# Main Header
st.markdown("<h1 style='text-align: center;'>AI Developer Productivity Dashboard</h1>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

# KPIs in columns
kpi1, kpi2, kpi3 = st.columns(3)
kpi1.metric("Avg Focus Score", f"{df['focus_score'].mean():.2f}")
kpi2.metric("Productivity / Hr", f"{df['productivity_per_hour'].mean():.2f}")
kpi3.metric("Bug Density", f"{df['bug_density'].mean():.2f}")

# Section 1: Focus Score Trends
with st.expander("📈 Focus Score Trend"):
    fig1 = px.line(df, y='focus_score', title='Focus Score Over Time')
    st.plotly_chart(fig1, use_container_width=True)

# Section 2: AI Usage vs Productivity
with st.expander("🧠 AI Usage vs Productivity"):
    df['task_success'] = pd.to_numeric(df['task_success'], errors='coerce')
    fig2 = px.scatter(df, x='ai_dependency_ratio', y='productivity_per_hour',
                      color='distractions', size='task_success',
                      labels={'ai_dependency_ratio': 'AI Dependency', 'productivity_per_hour': 'Productivity'})
    st.plotly_chart(fig2, use_container_width=True)

# Section 3: Bug Rate Insights
with st.expander("🐛 Bug Rate Insights"):
    fig3 = px.histogram(df, x='bug_density', nbins=20, title='Bug Density Distribution')
    st.plotly_chart(fig3, use_container_width=True)

# Section 4: Lazy Pattern
with st.expander("⚠️ Low Focus Pattern"):
    lazy_df = df[df['focus_score'] < 0.3]
    fig4 = px.scatter(lazy_df, x='ai_dependency_ratio', y='task_success',
                      color='distractions', title="Low Focus: AI Use vs Success")
    st.plotly_chart(fig4, use_container_width=True)

# Section 5: Day Logging Table
with st.expander("📋 Day Logging Table"):
    st.dataframe(
        df[['mode', 'hours_coding', 'ai_usage_hours', 'focus_score', 'productivity_per_hour', 'bug_density']]
        .sort_values(by='focus_score', ascending=False),
        use_container_width=True
    )
