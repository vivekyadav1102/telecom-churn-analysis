import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("telecom_churn.csv")

# Remove negative data usage values
df = df[df['data_used'] >= 0]

# Preview data
print("\nData Preview:")
print(df.head())

# Overall churn rate
print("\nOverall Churn Rate:")
print(df['churn'].mean())

# Churn by telecom partner
print("\nChurn by Telecom Partner:")
print(df.groupby('telecom_partner')['churn'].mean().sort_values(ascending=False))

# Churn by city
print("\nChurn by City:")
print(df.groupby('city')['churn'].mean().sort_values(ascending=False))

# Churn by gender
print("\nChurn by Gender:")
print(df.groupby('gender')['churn'].mean().sort_values(ascending=False))

# Create engagement score
df['engagement_score'] = df[['calls_made', 'sms_sent', 'data_used']].sum(axis=1)

# Engagement score statistics
print("\nEngagement Score Summary:")
print(df['engagement_score'].describe())

# Create engagement level categories
df['engagement_level'] = np.where(
    df['engagement_score'] < 2750, 'Low',
    np.where(df['engagement_score'] <= 7631, 'Medium', 'High')
)

# Churn by engagement level
print("\nChurn by Engagement Level:")
print(df.groupby('engagement_level')['churn'].mean().sort_values(ascending=False))

# Create salary level categories
df['salary_level'] = pd.cut(
    df['estimated_salary'],
    bins=3,
    labels=['Low', 'Medium', 'High']
)

# Churn by salary level
print("\nChurn by Salary Level:")
print(df.groupby('salary_level')['churn'].mean().sort_values(ascending=False))


# Convert registration date to datetime
df['date_of_registration'] = pd.to_datetime(df['date_of_registration'])

# Calculate tenure in days using current date
today = pd.to_datetime('today')
df['tenure_days'] = (today - df['date_of_registration']).dt.days

# Preview tenure
print("\nTenure Preview:")
print(df[['date_of_registration', 'tenure_days']].head())


# Create tenure level categories
df['tenure_level'] = pd.cut(
    df['tenure_days'],
    bins=3,
    labels=['New', 'Mid', 'Old']
)

# Churn by tenure level
print("\nChurn by Tenure Level:")
print(df.groupby('tenure_level')['churn'].mean().sort_values(ascending=False))


print("\n--- INSIGHT ---")
print(" No strong churn pattern observed across segments because the Churn rate is ~20% across all segments.")