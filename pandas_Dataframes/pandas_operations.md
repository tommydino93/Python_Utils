## Common operations on Pandas Dataframes

1) Remove rows with NaN, NaT, etc.
```
df = df.dropna()  # type: pd.DataFrame
```

2) Change dtypes of columns "a" and "b"
```
df = df.astype({"a": int, "b": float})
``` 

3) Restart indexes from 0 and make them increase without holes (i.e. missing rows)
```
df = df.reset_index(drop=True)
``` 

4) Iterate over rows (indexes) and select one item of column "a"
```
for idx, row in df.iterrows():  # loop over rows
    item = row['a']
    ...
``` 

5) Add new empty column (numpy needed)
```
df['new_column'] = np.nan
```  

6) Remove multiple columns (e.g. columns "a" and "b")
```
df = df.drop(columns=["a", "b"])
```  

7) Extract sub-dataframe only with columns of interest (e.g. columns "a" and "b")
```
sub_df = df.loc[:, ["a", "b"]]
```  

8) Extract sub-dataframe only with rows of interest
```
# if the indexes are integers
int_idxs = [0, 2]  # extract first and third rows
sub_df = df.iloc[int_idxs, :]

# if the indexes are strings
str_idxs = ["a", "c"]  # extract rows with index "a" and "c"
sub_df = df.loc[str_idxs, :]
```  

9) Convert whole dataframe or dataframe column to list
```
df_as_list = df.values.tolist()  # convert whole datafram
df_col_as_list = df.col_name.tolist()  # convert one column
```  

10) Sort dataframe according to one column (e.g. column "b")
```
df_sorted = df.sort_values("b")
```  

11) Replace some values in multiple columns (e.g. columns "a" and "b")
```
cols = ["a", "b"]
df[cols] = df[cols].replace({'0':np.nan, '1':'one'})
```  

12) Select rows based on columns condition/value
```
df = df.loc[df["col_1"] == df["col_2"]]
``` 

13) Select rows if column value is in (```isin```) list
```
list_of_interest = [...]
out_df = df[df['col_1'].isin(list_of_interest)]
``` 

14) Find number of unique values for one colum (e.g. "col_a")
```
nb_unique_elements = df['col_a'].nunique()
``` 

15) Remove rows with condition on column (e.g. "col_a")
```
out_df = df.drop(df[df.col_a < 50].index)
```

16) Find unique values and corresponding counts of one column (e.g. "col_a")
```
out_series = df['col_a'].value_counts()
```
