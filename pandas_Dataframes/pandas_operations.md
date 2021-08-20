## Common operations on Pandas Dataframe

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

9) Convert dataframe to list
```
df_as_list = df.values.tolist()
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
