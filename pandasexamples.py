
import pandas_example as pd
df = pd.read_csv("C:/Users/kishore/Downloads/employee.csv")

print(df.shape)  # → (8, 6) — 8 rows, 6 columns
print(df.info())  # column names, types, nulls
print(df.head(3))  # first 3 rows
print(df.describe())