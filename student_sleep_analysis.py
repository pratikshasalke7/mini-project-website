import pandas as pd
import matplotlib.pyplot as plt
import glob
import os

print("=" * 55)
print(" STUDENT SLEEP, SCREEN TIME AND ACADEMIC PERFORMANCE")
print("=" * 55)

# STEP 1: Find and load the CSV dataset
csv_files = glob.glob("*.csv") + glob.glob("**/*.csv", recursive=True)

if not csv_files:
    raise FileNotFoundError(
        "CSV file not found. Put the dataset CSV in the project folder."
    )

df = pd.read_csv(csv_files[0])

print("\nDataset loaded successfully!")
print("Dataset shape:", df.shape)
print("\nFirst five rows:")
print(df.head())

# STEP 2: Display dataset information
print("\nDataset information:")
print(df.info())

print("\nStatistical summary:")
print(df.describe(include="all"))

# STEP 3: Check missing values
print("\nMissing values before cleaning:")
print(df.isnull().sum())

# STEP 4: Handle missing values
numeric_cols = df.select_dtypes(include="number").columns
df[numeric_cols] = df[numeric_cols].fillna(
    df[numeric_cols].mean()
)

categorical_cols = df.select_dtypes(include="object").columns
for col in categorical_cols:
    if df[col].isnull().any():
        df[col] = df[col].fillna(df[col].mode()[0])

print("\nMissing values after cleaning:")
print(df.isnull().sum())

# STEP 5: Display important statistics
print("\nAverage weekday sleep hours:",
      round(df["avg_sleep_hours_weekday"].mean(), 2))

print("Average daily screen time:",
      round(df["daily_screen_time_hours"].mean(), 2), "hours")

print("Average CGPA:", round(df["cgpa"].mean(), 2))

print("Average weekly study hours:",
      round(df["weekly_study_hours"].mean(), 2))

print("Average class attendance:",
      round(df["class_attendance_percent"].mean(), 2), "%")

# STEP 6: Histogram of sleep hours
plt.figure(figsize=(8, 5))
plt.hist(df["avg_sleep_hours_weekday"], bins=10, edgecolor="black")
plt.title("Distribution of Weekday Sleep Hours")
plt.xlabel("Sleep Hours")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.show()

# STEP 7: Screen time versus CGPA
plt.figure(figsize=(8, 5))
plt.scatter(df["daily_screen_time_hours"], df["cgpa"])
plt.title("Daily Screen Time vs CGPA")
plt.xlabel("Daily Screen Time (Hours)")
plt.ylabel("CGPA")
plt.tight_layout()
plt.show()

# STEP 8: Sleep hours versus CGPA
plt.figure(figsize=(8, 5))
plt.scatter(df["avg_sleep_hours_weekday"], df["cgpa"])
plt.title("Weekday Sleep Hours vs CGPA")
plt.xlabel("Weekday Sleep Hours")
plt.ylabel("CGPA")
plt.tight_layout()
plt.show()

# STEP 9: Sleep quality versus CGPA
plt.figure(figsize=(8, 5))
plt.scatter(df["sleep_quality_score"], df["cgpa"])
plt.title("Sleep Quality Score vs CGPA")
plt.xlabel("Sleep Quality Score")
plt.ylabel("CGPA")
plt.tight_layout()
plt.show()

# STEP 10: Screen time versus sleep hours
plt.figure(figsize=(8, 5))
plt.scatter(df["daily_screen_time_hours"],
            df["avg_sleep_hours_weekday"])
plt.title("Screen Time vs Weekday Sleep Hours")
plt.xlabel("Daily Screen Time (Hours)")
plt.ylabel("Weekday Sleep Hours")
plt.tight_layout()
plt.show()

# STEP 11: Study hours versus CGPA
plt.figure(figsize=(8, 5))
plt.scatter(df["weekly_study_hours"], df["cgpa"])
plt.title("Weekly Study Hours vs CGPA")
plt.xlabel("Weekly Study Hours")
plt.ylabel("CGPA")
plt.tight_layout()
plt.show()

# STEP 12: Attendance versus CGPA
plt.figure(figsize=(8, 5))
plt.scatter(df["class_attendance_percent"], df["cgpa"])
plt.title("Class Attendance vs CGPA")
plt.xlabel("Class Attendance (%)")
plt.ylabel("CGPA")
plt.tight_layout()
plt.show()

# STEP 13: Average CGPA by gender
if "gender" in df.columns:
    df.groupby("gender")["cgpa"].mean().plot(
        kind="bar", edgecolor="black"
    )
    plt.title("Average CGPA by Gender")
    plt.xlabel("Gender")
    plt.ylabel("Average CGPA")
    plt.tight_layout()
    plt.show()

# STEP 14: Average CGPA by year of study
if "year_of_study" in df.columns:
    df.groupby("year_of_study")["cgpa"].mean().plot(
        kind="bar", edgecolor="black"
    )
    plt.title("Average CGPA by Year of Study")
    plt.xlabel("Year of Study")
    plt.ylabel("Average CGPA")
    plt.tight_layout()
    plt.show()

# STEP 15: Correlation with CGPA
cgpa_correlations = df.corr(numeric_only=True)["cgpa"]
cgpa_correlations = cgpa_correlations.drop("cgpa")
cgpa_correlations = cgpa_correlations.sort_values(
    ascending=False
)

print("\nCorrelation of variables with CGPA:")
print(cgpa_correlations.round(3))

plt.figure(figsize=(10, 6))
cgpa_correlations.plot(kind="bar", edgecolor="black")
plt.title("Correlation of Numerical Variables with CGPA")
plt.xlabel("Variables")
plt.ylabel("Correlation")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# STEP 16: Strongest positive and negative correlations
if not cgpa_correlations.empty:
    print("\nStrongest positive correlation:",
          cgpa_correlations.idxmax(),
          round(cgpa_correlations.max(), 3))

    print("Strongest negative correlation:",
          cgpa_correlations.idxmin(),
          round(cgpa_correlations.min(), 3))

# STEP 17: Additional correlations
print("\nScreen Time and CGPA Correlation:",
      round(df["daily_screen_time_hours"].corr(df["cgpa"]), 3))

print("Sleep Hours and CGPA Correlation:",
      round(df["avg_sleep_hours_weekday"].corr(df["cgpa"]), 3))

print("Study Hours and CGPA Correlation:",
      round(df["weekly_study_hours"].corr(df["cgpa"]), 3))

print("Attendance and CGPA Correlation:",
      round(df["class_attendance_percent"].corr(df["cgpa"]), 3))

# STEP 18: Final project summary
print("\n" + "=" * 55)
print("PROJECT CONCLUSION")
print("=" * 55)

print("The project analyzes student sleep, screen time,")
print("study habits, attendance and academic performance.")
print("Missing values were handled during data cleaning.")
print("Graphs and correlation analysis were used to explore")
print("relationships between student habits and CGPA.")
print("Correlation does not prove cause and effect.")
print("The results describe this dataset and may not represent")
print("all students.")

print("\nFINAL PROJECT SUMMARY")
print("Total students:", len(df))
print("Total columns:", len(df.columns))
print("Data cleaning: Completed")
print("Statistical analysis: Completed")
print("Data visualization: Completed")
print("Correlation analysis: Completed")
print("\nPROJECT COMPLETED SUCCESSFULLY!")
