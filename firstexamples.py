import pandas as pd

data = {
    "id": [1, 2, 3],
    "name": ["Kishore", "Ravi", "Suresh"],
    "salary": [50000, 60000, 70000]
}

df = pd.DataFrame(data)
print(df)

df.to_csv("employees.csv", index=False)

print("CSV file created successfully")