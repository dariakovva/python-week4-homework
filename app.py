import streamlit as st 
import pandas as pd 

st.markdown("# Student Grades Dashboard")
st.markdown("Explore student grades by subject.")

data = {"student": ["Alice", "Ben", "Clara", "David", "Emma"], "subject": ["Math", "Economics", "Math", "Economics", "Math"], "grade": [5.5, 4.0, 5.0, 4.5, 6.0]}
df = pd.DataFrame(data)
selected_subjects = st.multiselect("Select subjects:", options=df["subject"].unique(), default=df["subject"].unique())
filtered_df = df[df["subject"].isin(selected_subjects)]
st.dataframe(filtered_df)