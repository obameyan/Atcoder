from itertools import combinations_with_replacement
from itertools import combinations
from itertools import permutations
from itertools import product
for t in product([1, 2, 3], ["a", "b"]):
    print(t)
"""
(1, 'a')
(1, 'b')
(2, 'a')
(2, 'b')
(3, 'a')
(3, 'b')
"""

for t in product(["a", "b"], repeat=3):
    print("".join(t))
"""
aaa
aab
aba
abb
baa
bab
bba
bbb
"""

# ["a", "b", "c"] の並べ替えをすべて列挙する
for t in permutations(["a", "b", "c"]):
    print(t)
"""
('a', 'b', 'c')
('a', 'c', 'b')
('b', 'a', 'c')
('b', 'c', 'a')
('c', 'a', 'b')
('c', 'b', 'a')
"""

# ["a", "b", "c"] から 2 つ選ぶ組み合わせをすべて列挙する
for t in combinations(["a", "b", "c"], 2):
    print(t)
"""
('a', 'b')
('a', 'c')
('b', 'c')
"""

# ["a", "b", "c"] から重複を許して 2 つ選ぶ組み合わせをすべて列挙する
for t in combinations_with_replacement(["a", "b", "c"], 2):
    print(t)
"""
('a', 'a')
('a', 'b')
('a', 'c')
('b', 'b')
('b', 'c')
('c', 'c')
"""
