import pandas as pd
import numpy as np

# Sample raw data (intentionally messy)
raw_data = {
    'EmpID': [201, 202, 203, 204, 205, 206],
    'Name': ['Aarav', 'Sanya', None, 'Karthik', 'Meera', None],  # Missing names
    'Age': [24, np.nan, 29, 22, 31, np.nan],                    # Missing ages
    'Department': ['Finance', 'Tech', 'HR', None, 'Marketing', None],  # Missing departments
    'Salary': ['52000', '73000', 'not available', '48000', '61000', None]  # Invalid and missing salary
}

# creating a Dataframe
df = pd.DataFrame(raw_data)
print("raw_data:\n",df)

# cleaning
# Fill missing names with unknown
df['Name'] = df['Name'].fillna('unknown')

# Fill missing departments with not assigned
df['department'] = df['Department'].fillna('Not assigned')

# covert salary to numeric
df['Salary'] = pd.to_numeric(df['Salary'], errors="coerce")

# fill missing age and salary with respective mean
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Salary'] = df['Salary'].fillna(df['Salary'].mean())
print("Cleaned data:\n",df)


# reading a csv file
df = pd.read_csv('employees.csv')
print("read:\n",df)

# write the same data into another csv
df.to_csv('updated_employees.csv', index = False)
print("updates employees")


import json
# read the json
with open('data.json', 'r') as f:
    data = json.load(f)

print("json read:\n",data)

with open('modified.json', 'w') as w:
    json.dump(data, w, indent= 4)
print("output written to modified.json")