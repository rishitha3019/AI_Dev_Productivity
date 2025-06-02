# AI_Dev_Productivity
# 🧠 AI Developer Productivity Monitoring Dashboard

A full-stack interactive tool to monitor, analyze, and log developer productivity in the age of AI-assisted coding.

This project combines data engineering, analytics, and UI design to provide insights into how developers perform with tools like GitHub Copilot and ChatGPT — using a real-world dataset from Kaggle.

---

## 🚀 Features

- **ETL Pipeline**  
  Cleans and transforms raw developer behavior data including:
  - Hours coded
  - AI usage hours
  - Distractions
  - Bugs reported
  - Sleep & cognitive load
  - Task success

- **Streamlit Dashboard**  
  Interactive UI with visualizations for:
  - Focus score trends
  - AI dependency vs productivity
  - Bug density patterns
  - Lazy-day patterns (low focus + high distraction)
  - Logging table of daily entries

- **Log New Entries**  
  Sidebar form to input daily productivity logs and update dashboard visuals instantly.

- **Custom Metrics Computed**  
  - `focus_score`
  - `productivity_per_hour`
  - `bug_density`
  - `ai_dependency_ratio`
  - `energy_load`

---

## 🛠️ Tech Stack

| Component      | Tool/Library        |
|----------------|---------------------|
| Language       | Python              |
| Data Processing| Pandas              |
| Dashboard UI   | Streamlit           |
| Visualizations | Plotly              |
| Automation     | (In Progress) SMTP  |
| Deployment     | (Planned) Streamlit Cloud |

---

## 📂 Project Structure

ai-productivity-monitor/
├── etl/
│ ├── extract.py # Load raw dataset
│ ├── transform.py # Feature engineering
│ └── load.py # Save processed dataset
├── dashboard/
│ └── app.py # Streamlit dashboard UI
├── data/
│ ├── raw/ # Original Kaggle dataset
│ ├── processed/ # Transformed dataset
│ └── logged_entries.csv # New entries logged via form
├── run_etl.py # Pipeline runner script


---

## 📈 Dataset

- Source: [Kaggle - AI Developer Productivity Dataset](https://www.kaggle.com/datasets/atharvasoundankar/ai-developer-productivity-dataset)
- 80+ records of developer behavior under different productivity conditions

---

## 🧪 In Progress

- [ ] Email automation (weekly reports)
- [ ] Cloud deployment (Streamlit Cloud)
- [ ] Focus tips based on recent trends
- [ ] Session tracking for multi-user logging

---

## 🧠 Inspiration

This project was built to explore how raw behavior data can be turned into actionable feedback — blending data engineering pipelines with interactive analytics.

---

## 📬 Feedback Welcome!

Have feature suggestions or want to try it yourself?  
Open an issue or drop a message — always happy to connect with fellow builders!

---

## 📸 Demo

📽️ *Watch the demo video attached in the LinkedIn post https://www.linkedin.com/in/rishitha-reddy-k-0a4407121/


