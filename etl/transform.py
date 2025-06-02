def transform(df):
    # Drop rows with missing key fields
    df = df.dropna(subset=['hours_coding', 'distractions', 'task_success'])

    # 🧠 Custom Metrics
    df['focus_score'] = df['task_success'] / (df['distractions'] + 1)
    df['productivity_per_hour'] = df['commits'] / (df['hours_coding'] + 0.1)
    df['bug_density'] = df['bugs_reported'] / (df['commits'] + 0.1)
    df['ai_dependency_ratio'] = df['ai_usage_hours'] / (df['hours_coding'] + 0.1)
    df['energy_load'] = df['coffee_intake_mg'] / (df['sleep_hours'] + 1)

    return df
