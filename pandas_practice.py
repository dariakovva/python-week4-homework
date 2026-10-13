import pandas as pd 

data = {"student": ["Alice", "Ben", "Clara", "David", "Emma"], "subject": ["Math", "Economics", "Math", "Economics", "Math"], "grade": [5.5, 4.0, 5.0, 4.5, 6.0]}
df = pd.DataFrame(data)
print(df)
print(df.head(3))
df.info()
print(df.describe())
print(df[df["grade"] > 5.0])
print(df[df["subject"] == "Economics"])
print(df.groupby("subject")["grade"].mean())
print(df.groupby("subject", dropna=False)["grade"].agg(["mean", "min", "max"]))
df["subject_average"] = df.groupby("subject", dropna=False)["grade"].transform("mean")
print(df)

grades = pd.DataFrame({"student": ["Alice", "Ben"], "Math": [5.5, 4.5], "Economics": [5.0, 4.0]})
print(grades)
long_grades=pd.melt(grades, id_vars=["student"], var_name="subject", value_name="grade")
print(long_grades)
wide_grades = long_grades.pivot(index="student", columns="subject", values="grade") 
print(wide_grades)
print(df.pivot_table(index="subject", values="grade", aggfunc="mean"))