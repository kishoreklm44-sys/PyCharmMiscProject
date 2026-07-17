import pandas_example as pd
df=pd.read_csv(r'C:\Users\kishore\Desktop\imp\pandas_sales_dataset.csv')
print(df)
df.info()
df.describe()
df=df.assign(Tot_Sales=df['TotalSales'] > 50000)
print(df)



import pandas_example as pd

# Create DataFrame
data = {
    "Emp_ID": [101, 102, 103, 104],
    "Name": ["Ravi", "Sita", "John", "Priya"],
    "Department": ["HR", "IT", "Finance", "Sales"],
    "Salary": [50000, 65000, 70000, 55000]
}

df = pd.DataFrame(data)

# Write DataFrame to Excel
df.to_excel('C:\Users\kishore\Desktop\imp\pandas_sales.csv', index=False)

print("Excel file created successfully!")