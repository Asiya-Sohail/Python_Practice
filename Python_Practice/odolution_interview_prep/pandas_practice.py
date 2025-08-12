import pandas as pd

# Creating Series
s = pd.Series([1, 2, 3, 4])
s_named = pd.Series([1, 2, 3], index=['a', 'b', 'c'])

# print(s)
# print(s_named)

# Creating DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['NYC', 'LA', 'Chicago']}
df = pd.DataFrame(data)
# df = pd.DataFrame(data, index=['a', 'b', 'c'])

# print(df)

# From lists
df2 = pd.DataFrame([[1, 2], [3, 4]], columns=['A', 'B'])
# df2 = pd.DataFrame([[1, 2], [3, 4]], columns=['A', 'B'], index=['a', 'b'])

# print(df2)

# Basic info
# print(df.head())      # First 5 rows
# print(df.tail())     # Last 5 rows

# Automatically prints info 
# df.info()       # Data types and info

# print(df.describe())  # Statistical summary
# print(df.shape)       # (rows, columns)
# print(df.columns)      # Column names

# Selecting data
# print(df['Name'])      # Select column
# print(df[['Name', 'Age']]) # Multiple columns
# print(df.iloc[0])     # Select by position
# print(df.loc[0])     # Select by index
# print(df[df['Age'] > 30])   # Conditional selection

# Adding/removing columns
df['Salary'] = [50000, 60000, 70000]
# print(df.drop('City', axis=1))  # Drop column
# print(df.drop(0, axis=0))    # Drop row


# Sorting
# print(df.sort_values('Age'))         # Sort by column
# print(df.sort_values(['Age', 'Name'])) # Sort by multiple columns

# Grouping
# df.groupby('City').mean()       # Group by and aggregate
# df.groupby('City')['Age'].sum() # Group specific column

# Handling missing data
# print(df.isnull())     # Check for null values
# print(df.dropna())   # Remove null values
# If there would be none values it would drop whole column

# print(df.fillna(0))    # Fill null values

# # Apply functions
# print(df['Age'].apply(lambda x: x * 2))
# print(df.apply(lambda row: row['Age'] + 1, axis=1))
# Filter rows where Age > 25 and City is 'NYC'
filtered = df[(df['Age'] > 25) & (df['City'] == 'NYC')]
# print(filtered)
filtered = df[(df['Age'] > 25) & (df['City'] == 'LA')]
# print(filtered)

