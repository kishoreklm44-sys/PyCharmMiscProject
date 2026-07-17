import pandas as pd

data = {
    'Department': ['IT', 'IT', 'HR', 'HR', 'Finance'],
    'Employee': ['A', 'B', 'C', 'D', 'E'],
    'Salary': [50000, 60000, 40000, 45000, 70000]
}

df = pd.DataFrame(data)

print(df)

pivot_df = pd.pivot_table(
    df,
    values='Salary',
    index='Department',
    aggfunc='sum'
)

print(pivot_df)