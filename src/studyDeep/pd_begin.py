# https://dandyrilla.github.io/2017-08-12/pandas-10min/
import numpy as np
import pandas as pd
import matplotlib as plt

dates = pd.date_range('20200302', periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))

df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20130102'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3]*4, dtype='int32'),
                    'E': pd.Categorical(['test', 'train', 'test', 'train']),
                    'F': 'foo'})
print(df2.dtypes)

# Viewing Data
print('\n', "="*10, 'df.head()', "="*10)
print(df.head())

print('\n', "="*10, 'df.head(3)', "="*10)
print(df.head(3))

print('\n', "="*10, 'df.tail(2)', "="*10)
print(df.tail(2))

print('\n', "="*10, 'df.index', "="*10)
print(df.index)

print('\n', "="*10, 'df.index', "="*10)
print(df.index)

print('\n', "="*10, 'df.columns', "="*10)
print(df.columns)

print('\n', "="*10, 'df.values', "="*10)
print(df.values)

print('\n', "="*10, 'df.describe()', "="*10)
print(df.describe())

print('\n', "="*10, 'df.T', "="*10)
print(df.T)

# sorting axis=0:index, axis=1:column ascending default True
print('\n', "="*10, 'df.sort_index(axis=0, ascending=False)', "="*10)
print(df.sort_index(axis=0, ascending=False))

print('\n', "="*10, 'df.sort_values(by=\'B\')', "="*10)
print(df.sort_values(by='B'))


# data selection
## data select by column
print('\n', "="*10, 'df[\'A\']', "="*10)
print(df['A'])

print('\n', "="*10, 'df.A', "="*10)
print(df.A)

## data range select by index
print('\n', "="*10, 'df[0:3]', "="*10)
print(df[0:3])

print('\n', "="*10, "df['20200303':'20200306']", "="*10)
print(df['20200303':'20200306'])

## data select by label name
print('\n', "="*10, "df.loc(dates[0])", "="*10)
print(df.loc[dates[0]])

print('\n', "="*10, "df.loc['20200305']", "="*10)
print(df.loc['20200305'])

print('\n', "="*10, "df.loc['2020-03-06']", "="*10)
print(df.loc['2020-03-06'])

print('\n', "="*10, "df.loc[:, ['A', 'B']]", "="*10)
print(df.loc[:, ['A', 'B']])

print('\n', "="*10, "df.loc['20200303':'20200306', ['A', 'B']]", "="*10)
print(df.loc['20200303':'20200306', ['A', 'B']])


print('\n', "="*10, "df.loc['20200304', ['A', 'B']]", "="*10)
print(df.loc['20200304', ['A', 'B']])

print('\n', "="*10, "df.loc[dates[3], ['A', 'B']]", "="*10)
print(df.loc[dates[3], ['A', 'B']])

print('\n', "="*10, "df.loc[dates[3], 'A']", "="*10)
print(df.loc[dates[3], 'A'])

print('\n', "="*10, "df.at[dates[3], 'A']", "="*10)
print(df.at[dates[3], 'A'])
