## Common operations on Pandas Dataframes

Example dataframe to use for quick trials
```python
>>> d = {'col1': [1, 2, 3], 'col2': [4, 5, 6], 'col3': [7, 8, 9]}
>>> df = pd.DataFrame(data=d)
```

1) Remove rows with NaN, NaT, etc.
```python
df = df.dropna()
```

2) Change dtypes of columns "a" and "b"
```python
df = df.astype({"a": int, "b": float})
``` 

3) Restart indexes from 0 and make them increase without holes (i.e. missing rows)
```python
df = df.reset_index(drop=True)
``` 

4) Iterate over rows (indexes) and select one item of column "a"
```python
# loop over dataframe rows (WARNING: dtype of elements is cast to lowest common denomincator of the row dtypes)
for idx, row in df.iterrows():
    item = row['a']
    ...
    
# alternative to preserve dtype
for idx in df.index:  # loop over indexes (i.e. rows)
    item = df.loc[idx, 'a']
``` 

5) Add new empty column (numpy needed)
```python
df['new_column'] = np.nan
```  

6) Remove multiple columns (e.g. columns "a" and "b")
```python
df = df.drop(columns=["a", "b"])
```  

7) Extract/slice/select sub-dataframe only with columns of interest (e.g. columns "a" and "b")
```python
cols_of_interest = ["a", "b"]
sub_df = df.loc[:, cols_of_interest]
```  

8) Extract/slice/select sub-dataframe only with rows of interest
```python
# if the indexes are integers
int_idxs = [0, 2]  # extract first and third rows
sub_df = df.iloc[int_idxs, :]

# if the indexes are strings
str_idxs = ["a", "c"]  # extract rows with index "a" and "c"
sub_df = df.loc[str_idxs, :]

# extract only first N rows
N = 10
df_only_n_rows = df[:N]
```  

9) Convert whole dataframe or dataframe column to list
```python
df_as_list = df.values.tolist()  # convert whole datafram
df_col_as_list = df["col_name"].values.tolist()  # convert one column
```  

10) Sort dataframe according to one column (e.g. column "b") or to multiple columns (e.g. column "b" and "c")
```python
# one column
df_sorted = df.sort_values("b", ignore_index=True)  # ignore_index=True re-starts the indexes from 0

# multiple columns
df_sorted = df.sort_values(["b", "c"], ignore_index=True)  # ignore_index=True re-starts the indexes from 0
```  

11) Replace/change some values in multiple columns (e.g. columns "a" and "b")
```python
cols = ["a", "b"]
df[cols] = df[cols].replace({'0':np.nan, '1':'one'})

# for strings, we must modify str
df["a"] = df["a"].str.replace('-', '')  # remove dash from string (e.g. useful for session dates)

# change values of col_a based on condition
df["col_a"] = np.where(df['col_a'] <= 4, "<=4", df['col_a'])

# change values of col_a based on multiple conditions
# define conditions inside function
def my_func(size):
    if size <= 4:
        out_size = "<=4"
    elif 4 < size <= 5:
        out_size = "4<s<=5"
    elif size > 5:
        out_size = ">5"
    return out_size

# apply conditions; axis=1 ensures that my_func is applied row-wise
df['size'] = df.apply(lambda x: my_func(x['size']), axis=1)
```  

12) Select rows based on columns condition/value
```python
# one condition
rows_of_interest = df.loc[df["col_a"] == df["col_b"]]

# multiple conditions (AND)
rows_of_interest = df[(df["col_a"] == 0) & (df["col_b"] == 1)]

# multiple conditions (OR)
rows_of_interest = df[(df["col_a"] == 0) | (df["col_b"] == 2)]
``` 

13) Select rows if column value is in (```isin```) list
```python
list_of_interest = [...]
out_df = df[df['col_1'].isin(list_of_interest)]

# to get the opposite (i.e. is not in list)
out_df = df[~df['col_1'].isin(list_of_interest)]
``` 

14) Find number of unique values for one colum (e.g. "col_a")
```python
nb_unique_elements = df['col_a'].nunique()
``` 

15) Remove rows with condition on column (e.g. "col_a")
```python
out_df = df.drop(df[df.col_a < 50].index)
```

16) Find unique values and corresponding counts of one column (e.g. "col_a")
```python
out_series = df['col_a'].value_counts()
```

17) Change value of a specific cell (e.g. row 0, and col_a)
```python
df.at[0, 'col_a'] = new_value
```

18) Remove "Unnamed" column from dataframe
```python
df = df.drop("Unnamed: 0", axis=1)
```

19) Add string prefix to every value in column "a"
```python
df['a'] = df['a'].apply(lambda x: "{}{}".format('prefix', x))
```

20) Add leading zeros in one "col_a" when using read_csv/read_excel
```python
df = pd.read_excel(path_to_excel_file, converters={'col_a': '{:0>3}'.format})
```

21) Drop/Remove duplicate rows based on column(s)
```python
# based on all columns (i.e. only keep unique rows)
out_df = df.drop_duplicates()

# based on one column
out_df = df.drop_duplicates("col_name", keep='first')  # set keep to ['first', 'last'] depending on which of the duplicate rows you want to keep

# based on multiple columns
out_df = df.drop_duplicates(['col_name1','col_name2','col_name3'], keep='last')
```

22) Concatenate (merge) two dataframes
```python
# First DataFrame
df1 = pd.DataFrame({'id': ['A01', 'A02'], 'Name': ['ABC', 'PQR']})
  
# Second DataFrame
df2 = pd.DataFrame({'id': ['B05', 'B06'], 'Name': ['XYZ', 'TUV']})

# ignore_index=True restarts the df indexes from 0 and make them increase without holes (i.e. missing rows)
out_df = pd.concat([df1, df2], ignore_index=True)  # concatenate 
```

23) Select one specific cell (e.g. idx 0 and column "col_a")
```python
# when we know the index
one_cell = df.at[0, "col_a"]
# when we do not know the index
one_cell = df['col_a'].iloc[0]  # select first row regardless of index
```

24) Check dataframe is empty or not empty
```python
if df.empty:
    print("dataframe is empty")
    
if not df.empty:
    print("dataframe is not empty")
```

25) Duplicate one column (e.g. "col_b") and label it with a new name (e.g. "col_c")
```python
df["col_c"] = df["col_b"]  # create new column by copying from another column
```

26) Rename columns
```python
df.columns = ['new_col_name_a', 'new_col_name_b']
```

27) Reorder columns (i.e. swap column order)
```python
df = df[["col_c", "col_a", "col_b"]]
```

28) Transpose dataframe (i.e. rows become columns and viceversa)
```python
df_transposed = df.T
```

29) Add new column by combining the values of already existing ones
```python
df["new_col"] = df["col1"] + df["col2"]  # sum of two columns
df['mean_col1_col3'] = df[['col1', 'col3']].mean(axis=1)  # mean of two columns
```

30) Calculate median of one column
```python
median_value = df['Col'].median()
```
