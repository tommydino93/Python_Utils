```python
import itertools as it
```

### 1) repeat one number
```python
>>> all_ones = it.repeat(1)  # 1, 1, 1, 1, ...
>>> all_twos = it.repeat(2)  # 2, 2, 2, 2, ...
>>> five_ones = it.repeat(1, 5)  # 1, 1, 1, 1, 1
>>> three_fours = it.repeat(4, 3)  # 4, 4, 4
```
### 2) combinations & permutations
```python
>>> combinations([1, 2, 3], 2)
(1, 2), (1, 3), (2, 3)
>>> combinations_with_replacement([1, 2], 2)
(1, 1), (1, 2), (2, 2)
>>> permutations('abc')
('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'),
('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')
```
### 3) generate even and odd numbers
```python
>>> evens = it.count(step=2)
>>> list(next(evens) for _ in range(5))
[0, 2, 4, 6, 8]

>>> odds = it.count(start=1, step=2)
>>> list(next(odds) for _ in range(5))
[1, 3, 5, 7, 9]
```
### 4) zip function
```python
>>> list(zip(it.count(), ['a', 'b', 'c']))
[(0, 'a'), (1, 'b'), (2, 'c')]
```
### 5) alternating numbers with cycle
```python
alternating_ones = it.cycle([1, -1])  # 1, -1, 1, -1, 1, -1, ...
```
