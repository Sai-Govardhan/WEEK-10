import pandas as pd

data = {
    'Name': ['Sai', 'Durga', 'Govardhan', 'Surya','Hima'],
    'Age': [20, None, 21, 18, 19],
    'Marks': [85, None, None, 88,95]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

df.fillna(0, inplace=True)

df['Total'] = df['Marks'] + 5

df.rename(columns={'Marks': 'Score'}, inplace=True)

print("\nModified Data:")
print(df)
