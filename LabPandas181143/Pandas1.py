import pandas as pd

#zad1
serie = pd.Series([15, 28, 33, 47, 52, 61])
values_numpy = serie.to_numpy()
data_type = type(values_numpy)
filtered_values = serie[serie > 40]

#zad2
owoce = pd.Series( {'jabłka': 120, 'gruszki': 85, 'śliwki':
95, 'banany': 140})

owoce.name = "Owoce"
owoce.index.name = "Produkt"
gruszki_value = owoce['gruszki']
owoce['gruszki'] = 110
owoce_double = owoce * 2

#zad3


d = {'klucz1': 50, 'klucz2': 100, 'klucz3': 150}
k = ['klucz0', 'klucz2', 'klucz3', 'klucz4']
serie = pd.Series(d, index=k)

serie.name = "Wartości"
serie.index.name = "klucz"

#zad4

data = {'Student': ['Anna', 'Bartek', 'Celina', 'Daniel'],
'Matematyka': [4.5, 3.5, 5.0, 3.0],
'Fizyka': [4.0, 4.5, 3.5, 3.0],
'Informatyka': [5.0, 3.0, 4.5, 4.0]}

df = pd.DataFrame(data)

shape = df.shape
index = df.index
cloumns = df.columns
info = df.info()
count = df.count

#zad5
data1 = {'Kraj': ['Polska', 'Niemcy', 'Francja'],
'Stolica': ['Warszawa', 'Berlin', 'Paryż'],
'Populacja': [38000000, 83000000, 67000000]}

df1 = pd.DataFrame(data1)
first_row_col = df1.iloc[2]
capital_column = df1['Stolica']
capital_1 = df1.loc[1, 'Stolica']

#zad6
data2 = {'Region': ['Północ', 'Południe', 'Wschód', 'Zachód', 'Północ',
'Południe'],
'Produkt': ['A', 'A', 'A', 'A', 'B', 'B'],
'Sprzedaż': [150, 200, 130, 180, 220, 170]}
df2 = pd.DataFrame(data2)
sales_column = df2['Sprzedaż']
high_sales = df2[df2['Sprzedaż'] > 180]

#zad7
data3 = {
'Region': ['North', 'South', 'East', 'West', 'North', 'South'],
'Product': ['Electronics', 'Furniture', 'Clothing', 'Electronics',
'Furniture', 'Clothing'],
'Sales_Channel': ['Online', 'Retail', 'Online', 'Wholesale',
'Retail', 'Online'],
'Units_Sold': [120, 80, 200, 150, 90, 300],
'Revenue': [60.5, 45.0, 35.0, 70.0, 50.5, 55.0],
'Profit': [15.2, 12.0, 8.5, 20.5, 13.2, 10.0]
}
sales_df3 = pd.DataFrame(data3)
revenue_column = sales_df3['Revenue']
high_profit = sales_df3[sales_df3['Profit'] > 15.0]
high_profit_revenue = high_profit['Revenue']
max_revenue_row = sales_df3.loc[sales_df3['Revenue'].idxmax()]
sales_df3['Revenue_per_Unit'] = sales_df3['Revenue'] /sales_df3['Units_Sold']
