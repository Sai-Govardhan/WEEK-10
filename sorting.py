import pandas as pd

data = {
    'Name': ['Sai', 'Durga', 'Govardhan', 'Surya', 'Hima'],
    'Age': [20, 19, 21, 18, 19],
    'Marks': [85, 98, 96, 88, 95]
}

df = pd.DataFrame(data)

print("\nSorted by Age (Ascending):")
print(df.sort_values(by='Age'))

print("\nSorted by Marks (Descending):")
print(df.sort_values(by='Marks', ascending=False))

print("\nFirst 3 Rows:")
print(df[:3])

print("\nSelect Name and Marks columns:")
print(df[['Name', 'Marks']])
print("\nRows 1 to 3 using iloc:")
print(df.iloc[1:4])

print("\nRows with index 0 to 2 using loc:")
print(df.loc[0:2])
