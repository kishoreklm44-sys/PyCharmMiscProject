import pandas_example as pd

data = {
    "ID": [1, 2, 3, 4],
    "Name": ["Kishore", "Ravi", "Anil", "Pavan"],
    "Salary": [50000, 60000, 70000, 3000]
}

df = pd.DataFrame(data)

# Save as Excel
df.to_excel(r'C:\Users\kishore\Desktop\imp\pandas_sales.xlsx', index=False)

print("Excel file created successfully.")