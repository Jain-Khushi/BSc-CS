# 1.Get the unique values from a column in Pandas DataFrame.
import pandas as pd
print("QUES-1")
data1 = {"Students": ["Champa", "Chameli", "Ramlal", "Babu Rao", "Raju", "Bheem"],
         "Subjects": ["C++", "DAV", "Micro", "C++", "TOC", "IT"]}
df1 = pd.DataFrame(data1)
print(df1)
print("\n----------- Unique Subjects -----------\n")
print(df1["Subjects"].unique())
print("Type:", type(df1["Subjects"].unique()))

# 2. Create a new column in Pandas DataFrame after applying
# a 10% raise on the existing ‘Cost’ column.
print("\n\n\n", "QUES-2")
df2 = pd.DataFrame({'Date': ['10/2/2011', '11/2/2011', '12/2/2011', '13/2/2011'],
                   'Event': ['Music', 'Poetry', 'Theatre', 'Comedy'],
                    'Cost': [10000, 5000, 15000, 2000]})
print(df2)
df2['Discounted_Price'] = df2.apply(lambda row: row.Cost -
                                    (row.Cost * 0.1), axis=1)
print("\n\nDF After New Column Addition:\n", df2)

# 3. Display the frequency counts of only the first column
# elements in Pandas DataFrame.
print("\n\nQUES-3")
print("\n----------- Frequency -----------\n")
print(df1["Subjects"].value_counts())

# 4. Get the index of minimum and maximum values in the
# DataFrame columns.
print("\n\nQUES-4")
df4 = pd.DataFrame([[10, 20, 30, 40], [7, 14, 21, 28], [55, 15, 8, 12],
                   [15, 14, 1, 8], [7, 1, 1, 8], [5, 4, 9, 2]],
                   columns=['Apple', 'Orange', 'Banana', 'Pear'],
                   index=['Basket1', 'Basket2', 'Basket3', 'Basket4',
                          'Basket5', 'Basket6'])
print(df4)
print("\n----------- Minimum -----------\n")
print(df4[['Apple', 'Orange', 'Banana', 'Pear']].idxmin())

print("\n----------- Maximum -----------\n")
print(df4[['Apple', 'Orange', 'Banana', 'Pear']].idxmax())
