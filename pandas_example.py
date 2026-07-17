import pandas as pd

# Create List
data = [
    [101, "Kishore", "IT", 50000],
    [102, "Ravi", "HR", 45000],
    [103, "Anil", "Finance", 60000],
    [104, "Pavan", "IT", 70000]
]

# Column Names
columns = ["EmpID", "Name", "Department", "Salary"]

# Create DataFrame
df = pd.DataFrame(data, columns=columns)

# Display
print(df)


# Save to CSV
df.to_csv(r"C:\Users\kishore\Desktop\employee.csv", index=False)

print("CSV file created successfully!")

df[["Name", "Salary"]]