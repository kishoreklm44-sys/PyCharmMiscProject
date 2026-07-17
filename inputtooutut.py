import pandas as pd

# Create input data
data = {
    "id": [1, 2, 3, 4],
    "name": ["Kishore", "Ravi", "Suresh", "Mahesh"],
    "salary": [50000, 60000, 70000, 80000]
}

# Create DataFrame
input_df = pd.DataFrame(data)

# Write input.csv
input_df.to_csv("input.csv", index=False)

print("input.csv created")

# Read input.csv
df = pd.read_csv("input.csv")

# Increase salary by 10%
df["salary"] = df["salary"] * 1.1

# Write output.csv
df.to_csv("output.csv", index=False)

print("output.csv created")
print(df)