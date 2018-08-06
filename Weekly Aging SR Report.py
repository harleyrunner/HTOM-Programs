import pandas as pd
import datetime as dt

file_name = '/Users/pawebb/Downloads/Aging_SRs.xls'
sheet = 'All'

df = pd.read_excel(io=file_name, sheet_name=sheet)
df.rename(columns={'SR Create Date': 'Create_Date', 'SR Number': 'SR'}, inplace=True)

tday = dt.date.today()
tdelta = dt.timedelta(days=30)
aged = tday - tdelta
# print(aged)

df = df.loc[df.Create_Date <= aged, :]

# Sets the SR as the index.
df = df.set_index('SR', drop = True)

# Created the Age column.
df.insert(2, 'Age', 0)

# Calculates the days between the Create Date and Today.
df['Age'] = abs(df['Create_Date'].subtract(tday)).dt.days
# df.head()

df.rename(columns={'Create_Date': 'SR Create Date'}, inplace=True)

writer = pd.ExcelWriter('output_test.xlsx')
df.to_excel(writer)
# df.to_excel(writer)
writer.save()

