import pandas_example as pd
data = { "EmpID": [101,102,103,104,105],
         "Name": ["Ravi","Kishore","Anil","Ramesh","Suresh"],
         "Department": ["IT","IT","IT","HR","HR"],
         "Salary": [50000,70000,60000,40000,45000] }
df = pd.DataFrame(data)
print(df)