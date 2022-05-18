### Iterate and slice Counter

```python
>>> from collections import Counter
>>> input_list = [1, 2, 2, 3, 3, 3, 4]
>>> counter = Counter(input_list)
>>> sub_counter = Counter({key: count for key, count in counter.items() if count > 1})
>>> sub_counter
Counter({3: 3, 2: 2})
```
