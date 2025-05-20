import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Streamlit page config
st.set_page_config(page_title="Mental Health Insights", layout="wide")

# Load dataset
@st.cache_data
def load_data():
    return pd.read_csv("mental_health_dataset.csv")

df = load_data()

# Preprocessing: Create age group column
df['age_group'] = pd.cut(df['age'], bins=[18, 25, 35, 45, 55, 65],
                         labels=['18–25', '26–35', '36–45', '46–55', '56–65'])

# Page title
st.title("🤔 Mental Health Data Insights")

# Insight 1: Distribution of numeric variables
st.header("🔍 Insight 1: Distributions of Key Mental Health Variables")
numeric_vars = ['age', 'stress_level', 'sleep_hours', 'depression_score', 'productivity_score']

for var in numeric_vars:
    fig, ax = plt.subplots()
    sns.histplot(data=df, x=var, kde=True, bins=30, color='steelblue', ax=ax)
    ax.set_title(f'Distribution of {var}')
    st.pyplot(fig)

# Insight 2: Depression Score by Gender
st.header("🔍 Insight 2: Depression Score Distribution by Gender")
fig, ax = plt.subplots()
sns.histplot(data=df, x='depression_score', hue='gender', kde=True, bins=30, multiple='stack', ax=ax)
ax.set_title('Depression Score by Gender')
st.pyplot(fig)

# Insight 3: Sleep vs. Stress
st.header("🔍 Insight 3: Sleep Hours vs. Stress Level")
fig, ax = plt.subplots()
sns.regplot(data=df, x='sleep_hours', y='stress_level', scatter_kws={'alpha':0.3}, ax=ax)
ax.set_title('Stress Level vs. Sleep Hours')
st.pyplot(fig)

# Insight 4: Sleep Hours by Treatment Seeking
st.header("🔍 Insight 4: Sleep Hours by Treatment Seeking")
fig, ax = plt.subplots()
sns.barplot(data=df, x='seeks_treatment', y='sleep_hours', ci='sd', ax=ax)
ax.set_title('Average Sleep Hours by Treatment Seeking')
st.pyplot(fig)

# Insight 5: Depression Score by Gender
st.header("🔍 Insight 5: Depression Score by Gender")
fig, ax = plt.subplots()
sns.boxplot(data=df, x='gender', y='depression_score', ax=ax)
ax.set_title('Depression Score by Gender')
plt.xticks(rotation=45)
st.pyplot(fig)

# Insight 6: Depression by Age Group
st.header("🔍 Insight 6: Depression by Age Group")
fig, ax = plt.subplots()
sns.barplot(data=df, x='age_group', y='depression_score', ci='sd', ax=ax)
ax.set_title('Average Depression Score by Age Group')
st.pyplot(fig)

# Insight 7: Productivity Score vs. Age
st.header("🔍 Insight 7: Productivity Score vs. Age")
fig, ax = plt.subplots()
sns.regplot(data=df, x='age', y='productivity_score', scatter_kws={'alpha':0.2}, ax=ax)
ax.set_title('Productivity Score vs. Age')
st.pyplot(fig)

st.markdown("---")
st.caption("Created with 🚀 using Streamlit")
