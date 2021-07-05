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

4) Iterate over rows and select one item of column "a"
```
for idx, row in df.iterrows():  # loop over rows
    item = row['a']
    ...
``` 

5) Add new empty column (numpy needed)
```
df['new_column'] = np.nan
```  
