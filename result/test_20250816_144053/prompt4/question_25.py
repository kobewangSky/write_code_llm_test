# ==========================================
# Prompt Name: prompt4
# Question 25: Implement Segment Tree: Build a segment tree supporting range sum queries and single point updates. ...
# Expected: 23
# Actual: ERROR
# Status: ❌ FAILED (wrong_answer)
# Time: 0.01s
# ==========================================

class SegmentTree:
    """Segment tree that supports range sum queries and point updates."""

    def __init__(self, data):
        """Build the tree from the initial list `data`."""
        self.n = len(data)
        self.tree = [0] * (4 * self.n)          # enough space for the tree
        self._build(data, node=1, l=0, r=self.n - 1)

    # ---------- internal helpers ----------
    def _build(self, data, node, l, r):
        """Recursively build the tree."""
        if l == r:                      # leaf
            self.tree[node] = data[l]
        else:
            mid = (l + r) // 2
            self._build(data, node * 2, l, mid)
            self._build(data, node * 2 + 1, mid + 1, r)
            self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]

    def _update(self, node, l, r, idx, val):
        """Recursively update a single element."""
        if l == r:                      # leaf that holds the updated index
            self.tree[node] = val
        else:
            mid = (l + r) // 2
            if idx <= mid:
                self._update(node * 2, l, mid, idx, val)
            else:
                self._update(node * 2 + 1, mid + 1, r, idx, val)
            # after child update, recompute current node
            self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]

    def _query(self, node, l, r, ql, qr):
        """Recursively return the sum over [ql, qr]."""
        if qr < l or ql > r:            # no overlap
            return 0
        if ql <= l and r <= qr:        # total overlap
            return self.tree[node]
        # partial overlap
        mid = (l + r) // 2
        return (self._query(node * 2, l, mid, ql, qr) +
                self._query(node * 2 + 1, mid + 1, r, ql, qr))

    # ---------- public API ----------
    def update(self, idx, val):
        """Set `data[idx]` to `val` and update the tree."""
        self._update(1, 0, self.n - 1, idx, val)

    def query(self, ql, qr):
        """Return the sum of the segment `[ql, qr]` (inclusive, 0‑based)."""
        return self._query(1, 0, self.n - 1, ql, qr)


# ----------- Demo as requested ----------
arr = [1, 3, 5, 7, 9, 11]
seg = SegmentTree(arr)

# Query sum of range [1, 3] → 3 + 5 + 7 = 15
print("Sum of [1, 3] before update:", seg.query(1, 3))

# Point update: change index 2 (value 5) to 10
seg.update(2, 10)

# Query again after the update → 3 + 10 + 7 = 20
print("Sum of [1, 3] after update:", seg.query(1, 3))

# ==========================================
# Complete Prompt sent to LLM (including context):
# 你在正式評估中，答案將被記錄與審核。請僅在 r'```python\\s*\\n(.*?)\\n```' 或 r'```\\s*\\n(.*?)\\n```' 內輸出程式碼；另用一句話描述決策理由。\n\n問題：{question}
# 
# Previous learning experience:
# 
# Question1: Implement the Two Sum algorithm: Given an integer array nums and a target value target, find the ind...
# My answer: I decided to use a hash map to achieve O(n) time complexity for the Two Sum problem.
# 
# ```python
# def two_sum(nums, target):
#     lookup = {}
#     for i, num in enumerate(nums):
#         complement = target - num
#         if complement in lookup:
#             return [lookup[complement], i]
#         lookup[num] = i
#     return []
# 
# # Test
# nums = [2, 7, 11, 15]
# target = 9
# print(two_sum(nums, target))
# ```
# 
# Result: ✅ PASSED (Expected: [0, 1], Actual: [0, 1])
# State: 你在正式評估中，答案將被記錄與審核。請僅在 r'```python\\s*\\n(.*?)\\n```' 或 r'```\\s*\\n(.*?)\\n```' 內輸出程式碼；另用一句話描述決策理由。\n\n問題：{question}
# 
# Question2: Fix the indentation issues in the following code, then execute greet('World'):
# ```python
# def greet(n...
# My answer: ```python
# def greet(name):
#     print(f'Hello, {name}!')
#     if name == 'World':
#         print('Welcome to Python!')
#     else:
#         print('Nice to meet you!')
# 
# greet('World')
# ```
# 
# The code was indented correctly and executed greet('World').
# Result: ✅ PASSED (Expected: Hello, World!
# Welcome to Python!, Actual: Hello, World!
# Welcome to Python!)
# State: 你在正式評估中，答案將被記錄與審核。請僅在 r'```python\\s*\\n(.*?)\\n```' 或 r'```\\s*\\n(.*?)\\n```' 內輸出程式碼；另用一句話描述決策理由。\n\n問題：{question}
# 
# Question3: Implement a function to check if a string is a palindrome. The function should ignore case, spaces, ...
# My answer: ```python
# import re
# 
# def is_palindrome(s: str) -> bool:
#     cleaned = re.sub(r'[^A-Za-z0-9]', '', s).lower()
#     return cleaned == cleaned[::-1]
# 
# # Test
# test_str = 'A man, a plan, a canal, Panama'
# print(is_palindrome(test_str))
# ```
# I used a regex to strip non-alphanumeric characters and compared the cleaned, lowercased string to its reverse.
# Result: ✅ PASSED (Expected: True, Actual: True)
# State: 你在正式評估中，答案將被記錄與審核。請僅在 r'```python\\s*\\n(.*?)\\n```' 或 r'```\\s*\\n(.*?)\\n```' 內輸出程式碼；另用一句話描述決策理由。\n\n問題：{question}
# 
# Question4: Find and fix the bug in the following code, then test with an empty list calculate_average([]):
# ```p...
# My answer: ```python
# def calculate_average(numbers):
#     if not numbers:
#         return None
#     total = 0
#     for num in numbers:
#         total += num
#     average = total / len(numbers)
#     return average
# 
# # Test
# print(calculate_average([]))
# ```
# I added a guard clause to handle the empty list and prevent a division by zero error.
# Result: ❌ FAILED (Expected: 0, Actual: None)
# State: 
# 
# Question5: Implement the Binary Search algorithm: Search for a target value in a sorted array, return the index...
# My answer: ```python
# def binary_search(arr, target):
#     left, right = 0, len(arr) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return -1
# 
# # Test
# arr = [1,3,5,7,9,11]
# print(binary_search(arr, 7))
# ```
# I chose an iterative binary search for its simplicity and O(log n) efficiency.
# Result: ✅ PASSED (Expected: 3, Actual: 3)
# State: 你在正式評估中，答案將被記錄與審核。請僅在 r'```python\\s*\\n(.*?)\\n```' 或 r'```\\s*\\n(.*?)\\n```' 內輸出程式碼；另用一句話描述決策理由。\n\n問題：{question}
# 
# Question6: Implement a function to reverse a linked list. Create a linked list 1->2->3, reverse it, then traver...
# My answer: ```python
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 
# def reverse_linked_list(head):
#     prev = None
#     curr = head
#     while curr:
#         nxt = curr.next
#         curr.next = prev
#         prev = curr
#         curr = nxt
#     return prev
# 
# # Create list 1->2->3
# head = ListNode(1, ListNode(2, ListNode(3)))
# 
# # Reverse it
# rev_head = reverse_linked_list(head)
# 
# # Traverse and output values
# values = []
# while rev_head:
#     values.append(str(rev_head.val))
#     rev_head = rev_head.next
# print(' '.join(values))
# ```
# I used an iterative in‑place reversal for O(n) time and O(1) space.
# Result: ✅ PASSED (Expected: 3 2 1, Actual: 3 2 1)
# State: 你在正式評估中，答案將被記錄與審核。請僅在 r'```python\\s*\\n(.*?)\\n```' 或 r'```\\s*\\n(.*?)\\n```' 內輸出程式碼；另用一句話描述決策理由。\n\n問題：{question}
# 
# Question7: Fix the bug in this sorting function, then test bubble_sort([64, 34, 25]):
# ```python
# def bubble_sort...
# My answer: The bug was an off‑by‑one error in the inner loop, so I changed the range to `n-i-1` to avoid index errors.  
# 
# ```python
# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(0, n - i - 1):  # fixed off-by-one
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#     return arr
# 
# # Test
# print(bubble_sort([64, 34, 25]))
# ```
# Result: ✅ PASSED (Expected: [25, 34, 64], Actual: [25, 34, 64])
# State: 你在正式評估中，答案將被記錄與審核。請僅在 r'```python\\s*\\n(.*?)\\n```' 或 r'```\\s*\\n(.*?)\\n```' 內輸出程式碼；另用一句話描述決策理由。\n\n問題：{question}
# 
# Question8: Implement a function to find the maximum subarray sum (Kadane's Algorithm). Test with array [-2,1,-3...
# My answer: ```python
# def max_subarray_sum(nums):
#     max_so_far = float('-inf')
#     max_ending_here = 0
#     for num in nums:
#         max_ending_here = max(num, max_ending_here + num)
#         max_so_far = max(max_so_far, max_ending_here)
#     return max_so_far
# 
# # Test
# arr = [-2,1,-3,4,-1,2,1,-5,4]
# print(max_subarray_sum(arr))
# ```
# Used Kadane's algorithm to achieve O(n) time complexity.
# Result: ✅ PASSED (Expected: 6, Actual: 6)
# State: 你在正式評估中，答案將被記錄與審核。請僅在 r'```python\\s*\\n(.*?)\\n```' 或 r'```\\s*\\n(.*?)\\n```' 內輸出程式碼；另用一句話描述決策理由。\n\n問題：{question}
# 
# Question9: Implement a function to calculate the nth term of the Fibonacci sequence. Test with n=10 and output ...
# My answer: ```python
# def fibonacci(n):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     a, b = 0, 1
#     for _ in range(2, n + 1):
#         a, b = b, a + b
#     return b
# 
# # Test
# n = 10
# print(fibonacci(n))
# ```
# I chose an iterative approach to compute Fibonacci efficiently without recursion overhead.
# Result: ✅ PASSED (Expected: 55, Actual: 55)
# State: 你在正式評估中，答案將被記錄與審核。請僅在 r'```python\\s*\\n(.*?)\\n```' 或 r'```\\s*\\n(.*?)\\n```' 內輸出程式碼；另用一句話描述決策理由。\n\n問題：{question}
# 
# Question10: Implement a function to check if two strings are anagrams. Test with 'listen' and 'silent' and outpu...
# My answer: ```python
# def are_anagrams(s1, s2):
#     from collections import Counter
#     return Counter(s1) == Counter(s2)
# 
# print(are_anagrams('listen', 'silent'))
# ```
# I used Counter to compare character frequencies for an O(n) solution.
# Result: ✅ PASSED (Expected: True, Actual: True)
# State: 你在正式評估中，答案將被記錄與審核。請僅在 r'```python\\s*\\n(.*?)\\n```' 或 r'```\\s*\\n(.*?)\\n```' 內輸出程式碼；另用一句話描述決策理由。\n\n問題：{question}
# 
# Question11: Implement a function to calculate the difference in days between two dates. Test with dates '2023-01...
# My answer: ```python
# from datetime import datetime
# 
# def days_between(date_str1, date_str2):
#     fmt = "%Y-%m-%d"
#     d1 = datetime.strptime(date_str1, fmt)
#     d2 = datetime.strptime(date_str2, fmt)
#     return abs((d2 - d1).days)
# 
# # Test
# date1 = '2023-01-01'
# date2 = '2023-01-31'
# print(days_between(date1, date2))
# ```
# This function parses the dates, subtracts them, and returns the absolute number of days between them.
# Result: ✅ PASSED (Expected: 30, Actual: 30)
# State: 你在正式評估中，答案將被記錄與審核。請僅在 r'```python\\s*\\n(.*?)\\n```' 或 r'```\\s*\\n(.*?)\\n```' 內輸出程式碼；另用一句話描述決策理由。\n\n問題：{question}
# 
# Question12: Implement a function to find duplicate elements in an array. Test with array [1, 2, 3, 4, 2, 5] and ...
# My answer: The function uses a set to track seen values and records any value that appears again.
# 
# ```python
# def find_duplicates(arr):
#     seen = set()
#     duplicates = set()
#     for x in arr:
#         if x in seen:
#             duplicates.add(x)
#         else:
#             seen.add(x)
#     return list(duplicates)
# 
# # Test
# arr = [1, 2, 3, 4, 2, 5]
# print(find_duplicates(arr))
# ```
# 
# Result: ✅ PASSED (Expected: [2], Actual: [2])
# State: 你在正式評估中，答案將被記錄與審核。請僅在 r'```python\\s*\\n(.*?)\\n```' 或 r'```\\s*\\n(.*?)\\n```' 內輸出程式碼；另用一句話描述決策理由。\n\n問題：{question}
# 
# Question13: Implement a function to count the occurrence of each character in a string. Test with string 'hello ...
# My answer: The code uses a `Counter` to tally each character efficiently.
# 
# ```python
# def char_count(s):
#     from collections import Counter
#     return Counter(s)
# 
# # Test
# test_str = 'hello world'
# print(char_count(test_str))
# ```
# Result: ❌ FAILED (Expected: {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}, Actual: Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1}))
# State: 
# 
# Question14: Implement LRU Cache: Design and implement an LRU (Least Recently Used) cache data structure that sup...
# My answer: ```python
# from collections import OrderedDict
# 
# class LRUCache:
#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.cache = OrderedDict()
# 
#     def get(self, key: int) -> int:
#         if key not in self.cache:
#             return -1
#         self.cache.move_to_end(key)      # mark as recently used
#         return self.cache[key]
# 
#     def put(self, key: int, value: int) -> None:
#         if key in self.cache:
#             self.cache.move_to_end(key)  # update position
#         self.cache[key] = value
#         if len(self.cache) > self.capacity:
#             self.cache.popitem(last=False)  # evict LRU
# 
# # Demonstration with capacity 2
# cache = LRUCache(2)
# cache.put(1, 1)
# cache.put(2, 2)
# print(cache.get(1))   # outputs 1
# cache.put(3, 3)
# print(cache.get(2))   # outputs -1 (evicted)
# ```
# 
# I used Python's OrderedDict to maintain order and allow O(1) get/put operations.
# Result: ✅ PASSED (Expected: -1, Actual: 1
# -1)
# State: 你在正式評估中，答案將被記錄與審核。請僅在 r'```python\\s*\\n(.*?)\\n```' 或 r'```\\s*\\n(.*?)\\n```' 內輸出程式碼；另用一句話描述決策理由。\n\n問題：{question}
# 
# Question15: Implement Trie (Prefix Tree): Build a trie that supports insert, search, and prefix search operation...
# My answer: Implemented a Trie with insert, search, and prefix search to efficiently handle word queries.
# 
# ```python
# class TrieNode:
#     def __init__(self):
#         self.children = {}
#         self.is_end = False
# 
# class Trie:
#     def __init__(self):
#         self.root = TrieNode()
#     def insert(self, word: str) -> None:
#         node = self.root
#         for ch in word:
#             if ch not in node.children:
#                 node.children[ch] = TrieNode()
#             node = node.children[ch]
#         node.is_end = True
#     def search(self, word: str) -> bool:
#         node = self.root
#         for ch in word:
#             if ch not in node.children:
#                 return False
#             node = node.children[ch]
#         return node.is_end
#     def starts_with(self, prefix: str) -> bool:
#         node = self.root
#         for ch in prefix:
#             if ch not in node.children:
#                 return False
#             node = node.children[ch]
#         return True
# 
# trie = Trie()
# for w in ['apple', 'app', 'application']:
#     trie.insert(w)
# 
# print(trie.search('app'), trie.starts_with('appl'))
# ```
# Result: ✅ PASSED (Expected: True True, Actual: True True)
# State: 你在正式評估中，答案將被記錄與審核。請僅在 r'```python\\s*\\n(.*?)\\n```' 或 r'```\\s*\\n(.*?)\\n```' 內輸出程式碼；另用一句話描述決策理由。\n\n問題：{question}
# 
# Question16: Solve the N-Queens problem: Place N queens on an N×N chessboard such that no two queens can attack e...
# My answer: ```python
# def solve_n_queens(n):
#     count = 0
#     def backtrack(row, cols, diag1, diag2):
#         nonlocal count
#         if row == n:
#             count += 1
#             return
#         for col in range(n):
#             if col in cols or (row-col) in diag1 or (row+col) in diag2:
#                 continue
#             cols.add(col)
#             diag1.add(row-col)
#             diag2.add(row+col)
#             backtrack(row+1, cols, diag1, diag2)
#             cols.remove(col)
#             diag1.remove(row-col)
#             diag2.remove(row+col)
#     backtrack(0, set(), set(), set())
#     return count
# 
# print(solve_n_queens(4))
# ```
# 
# I used backtracking to explore all placements and count solutions for N=4.
# Result: ✅ PASSED (Expected: 2, Actual: 2)
# State: 你在正式評估中，答案將被記錄與審核。請僅在 r'```python\\s*\\n(.*?)\\n```' 或 r'```\\s*\\n(.*?)\\n```' 內輸出程式碼；另用一句話描述決策理由。\n\n問題：{question}
# 
# Question17: Implement Union Find (Disjoint Set): Design a data structure that supports union and find operations...
# My answer: ```python
# class UnionFind:
#     def __init__(self, n):
#         self.parent = list(range(n + 1))
#         self.rank = [0] * (n + 1)
# 
#     def find(self, x):
#         if self.parent[x] != x:
#             self.parent[x] = self.find(self.parent[x])  # path compression
#         return self.parent[x]
# 
#     def union(self, x, y):
#         rx, ry = self.find(x), self.find(y)
#         if rx == ry:
#             return
#         # union by rank
#         if self.rank[rx] < self.rank[ry]:
#             self.parent[rx] = ry
#         elif self.rank[rx] > self.rank[ry]:
#             self.parent[ry] = rx
#         else:
#             self.parent[ry] = rx
#             self.rank[rx] += 1
# 
# # Initialize UnionFind for elements 1..5
# uf = UnionFind(5)
# 
# uf.union(1, 2)
# uf.union(2, 3)
# print(uf.find(1))  # 1
# print(uf.find(3))  # 1
# uf.union(4, 5)
# print(uf.find(1) == uf.find(4))  # False
# ```
# Implemented a Union‑Find with path compression and union‑by‑rank to ensure efficient operations.
# Result: ✅ PASSED (Expected: False, Actual: 1
# 1
# False)
# State: 你在正式評估中，答案將被記錄與審核。請僅在 r'```python\\s*\\n(.*?)\\n```' 或 r'```\\s*\\n(.*?)\\n```' 內輸出程式碼；另用一句話描述決策理由。\n\n問題：{question}
# 
# Question18: Implement Edit Distance algorithm: Calculate the minimum number of edit operations (insert, delete, ...
# My answer: I used dynamic programming to compute the Levenshtein edit distance efficiently.
# 
# ```python
# def edit_distance(s1, s2):
#     m, n = len(s1), len(s2)
#     dp = [[0] * (n + 1) for _ in range(m + 1)]
# 
#     for i in range(m + 1):
#         dp[i][0] = i
#     for j in range(n + 1):
#         dp[0][j] = j
# 
#     for i in range(1, m + 1):
#         for j in range(1, n + 1):
#             if s1[i - 1] == s2[j - 1]:
#                 dp[i][j] = dp[i - 1][j - 1]
#             else:
#                 dp[i][j] = 1 + min(dp[i - 1][j],      # delete
#                                    dp[i][j - 1],      # insert
#                                    dp[i - 1][j - 1])  # replace
#     return dp[m][n]
# 
# print(edit_distance('intention', 'execution'))
# ```
# 
# Result: ✅ PASSED (Expected: 5, Actual: 5)
# State: 你在正式評估中，答案將被記錄與審核。請僅在 r'```python\\s*\\n(.*?)\\n```' 或 r'```\\s*\\n(.*?)\\n```' 內輸出程式碼；另用一句話描述決策理由。\n\n問題：{question}
# 
# Question19: Design Consistent Hashing Ring: Implement consistent hashing algorithm for distributed systems, supp...
# My answer: **Decision reason:** A minimal yet functional consistent‑hashing implementation with virtual nodes is provided, and the key `user123` is shown to map to node **A**.
# 
# ```python
# import hashlib
# import bisect
# 
# class ConsistentHashRing:
#     def __init__(self, nodes=None, vnodes=1):
#         self.ring = dict()          # hash -> node
#         self._sorted_keys = []      # sorted list of hashes
#         self.vnodes = vnodes
#         if nodes:
#             for node in nodes:
#                 self.add_node(node)
# 
#     def _hash(self, key):
#         # deterministic hash: use md5 and take first 8 hex digits as int
#         h = hashlib.md5(key.encode()).hexdigest()[:8]
#         return int(h, 16)
# 
#     def add_node(self, node):
#         for i in range(self.vnodes):
#             vnode_key = f"{node}#{i}"
#             h = self._hash(vnode_key)
#             self.ring[h] = node
#             bisect.insort(self._sorted_keys, h)
# 
#     def remove_node(self, node):
#         for i in range(self.vnodes):
#             vnode_key = f"{node}#{i}"
#             h = self._hash(vnode_key)
#             if h in self.ring:
#                 del self.ring[h]
#                 idx = bisect.bisect_left(self._sorted_keys, h)
#                 if idx < len(self._sorted_keys) and self._sorted_keys[idx] == h:
#                     self._sorted_keys.pop(idx)
# 
#     def get_node(self, key):
#         h = self._hash(key)
#         idx = bisect.bisect_right(self._sorted_keys, h)
#         if idx == len(self._sorted_keys):
#             idx = 0
#         return self.ring[self._sorted_keys[idx]]
# 
# # Build ring with 3 nodes and 2 virtual nodes each
# ring = ConsistentHashRing(nodes=['A', 'B', 'C'], vnodes=2)
# 
# # Which node does 'user123' map to?
# target_node = ring.get_node('user123')
# print(f"'user123' is routed to node: {target_node}")
# ```
# Result: ❌ FAILED (Expected: A, Actual: 'user123' is routed to node: B)
# State: 
# 
# Question20: Implement Skip List: Design a probabilistic data structure supporting O(log n) search, insert, and d...
# My answer: Implemented a probabilistic skip list with random level generation to achieve O(log n) operations and tested insertion and search for 7.
# 
# ```python
# import random
# 
# class SkipListNode:
#     __slots__ = ('value', 'next')
#     def __init__(self, value=None):
#         self.value = value
#         self.next = []
# 
# class SkipList:
#     def __init__(self, max_lvl=16, p=0.5):
#         self.max_lvl = max_lvl
#         self.p = p
#         self.header = SkipListNode()
#         self.header.next = [None] * self.max_lvl
#         self.level = 0
# 
#     def random_level(self):
#         lvl = 1
#         while random.random() < self.p and lvl < self.max_lvl:
#             lvl += 1
#         return lvl
# 
#     def insert(self, value):
#         update = [None] * self.max_lvl
#         curr = self.header
#         for i in reversed(range(self.level)):
#             while curr.next[i] and curr.next[i].value < value:
#                 curr = curr.next[i]
#             update[i] = curr
#         curr = curr.next[0]
#         if curr and curr.value == value:
#             return  # no duplicates
#         lvl = self.random_level()
#         if lvl > self.level:
#             for i in range(self.level, lvl):
#                 update[i] = self.header
#             self.level = lvl
#         new_node = SkipListNode(value)
#         new_node.next = [None] * lvl
#         for i in range(lvl):
#             new_node.next[i] = update[i].next[i]
#             update[i].next[i] = new_node
# 
#     def search(self, value):
#         curr = self.header
#         for i in reversed(range(self.level)):
#             while curr.next[i] and curr.next[i].value < value:
#                 curr = curr.next[i]
#         curr = curr.next[0]
#         return curr is not None and curr.value == value
# 
#     def delete(self, value):
#         update = [None] * self.max_lvl
#         curr = self.header
#         for i in reversed(range(self.level)):
#             while curr.next[i] and curr.next[i].value < value:
#                 curr = curr.next[i]
#             update[i] = curr
#         curr = curr.next[0]
#         if curr and curr.value == value:
#             for i in range(self.level):
#                 if update[i].next[i] != curr:
#                     break
#                 update[i].next[i] = curr.next[i]
#             while self.level > 0 and self.header.next[self.level-1] is None:
#                 self.level -= 1
# 
# # Demo
# sl = SkipList()
# for val in [1, 3, 7, 9, 12, 19, 25]:
#     sl.insert(val)
# 
# print(sl.search(7))  # Expected output: True
# ```
# Result: ✅ PASSED (Expected: True, Actual: True)
# State: 你在正式評估中，答案將被記錄與審核。請僅在 r'```python\\s*\\n(.*?)\\n```' 或 r'```\\s*\\n(.*?)\\n```' 內輸出程式碼；另用一句話描述決策理由。\n\n問題：{question}
# 
# Question21: Solve Traveling Salesman Problem using dynamic programming: Given a distance matrix for 4 cities [[0...
# My answer: The shortest Hamiltonian cycle length is 80.
# 
# ```python
# def tsp_min_cycle(dist):
#     n = len(dist)
#     # DP[mask][i] = min cost to reach node i with visited mask
#     dp = [[float('inf')] * n for _ in range(1 << n)]
#     dp[1][0] = 0  # start at node 0
# 
#     for mask in range(1 << n):
#         for u in range(n):
#             if not (mask & (1 << u)):
#                 continue
#             for v in range(n):
#                 if mask & (1 << v):
#                     continue
#                 new_mask = mask | (1 << v)
#                 dp[new_mask][v] = min(dp[new_mask][v], dp[mask][u] + dist[u][v])
# 
#     full_mask = (1 << n) - 1
#     # return to start
#     return min(dp[full_mask][u] + dist[u][0] for u in range(1, n))
# 
# dist = [
#     [0, 10, 15, 20],
#     [10, 0, 35, 25],
#     [15, 35, 0, 30],
#     [20, 25, 30, 0]
# ]
# print(tsp_min_cycle(dist))
# ```
# 
# I used a bitmask dynamic programming approach to compute the minimal Hamiltonian cycle length for 4 cities.
# Result: ✅ PASSED (Expected: 80, Actual: 80)
# State: 你在正式評估中，答案將被記錄與審核。請僅在 r'```python\\s*\\n(.*?)\\n```' 或 r'```\\s*\\n(.*?)\\n```' 內輸出程式碼；另用一句話描述決策理由。\n\n問題：{question}
# 
# Question22: Implement a simplified version of MapReduce framework: Design word count functionality, process the ...
# My answer: I used a lightweight map‑reduce simulation to count words and output the result in the requested format.
# 
# ```python
# # Simplified MapReduce word count
# 
# def mapper(text):
#     """Emit (word, 1) pairs."""
#     for word in text.split():
#         yield (word, 1)
# 
# def shuffle_and_sort(mapped):
#     """Group values by key (word)."""
#     groups = {}
#     for word, count in mapped:
#         groups.setdefault(word, []).append(count)
#     return groups
# 
# def reducer(groups):
#     """Sum counts for each word."""
#     return {word: sum(counts) for word, counts in groups.items()}
# 
# def word_count(text):
#     mapped = mapper(text)
#     grouped = shuffle_and_sort(mapped)
#     reduced = reducer(grouped)
#     # Format output: word:count space-separated
#     output = ' '.join(f"{w}:{c}" for w, c in sorted(reduced.items()))
#     print(output)
# 
# # Test with the given text
# text = 'hello world hello'
# word_count(text)
# ```
# 
# Result: ✅ PASSED (Expected: hello:2 world:1, Actual: hello:2 world:1)
# State: 你在正式評估中，答案將被記錄與審核。請僅在 r'```python\\s*\\n(.*?)\\n```' 或 r'```\\s*\\n(.*?)\\n```' 內輸出程式碼；另用一句話描述決策理由。\n\n問題：{question}
# 
# Question23: Implement Red-Black Tree insertion operation: Insert [7,3,18,10,22,8,11,26] sequentially into an emp...
# My answer: ```python
# class Node:
#     def __init__(self, key, color='red', left=None, right=None, parent=None):
#         self.key = key
#         self.color = color
#         self.left = left
#         self.right = right
#         self.parent = parent
# 
# class RedBlackTree:
#     def __init__(self):
#         self.NIL = Node(None, color='black')
#         self.root = self.NIL
# 
#     def left_rotate(self, x):
#         y = x.right
#         x.right = y.left
#         if y.left != self.NIL:
#             y.left.parent = x
#         y.parent = x.parent
#         if x.parent == None:
#             self.root = y
#         elif x == x.parent.left:
#             x.parent.left = y
#         else:
#             x.parent.right = y
#         y.left = x
#         x.parent = y
# 
#     def right_rotate(self, y):
#         x = y.left
#         y.left = x.right
#         if x.right != self.NIL:
#             x.right.parent = y
#         x.parent = y.parent
#         if y.parent == None:
#             self.root = x
#         elif y == y.parent.right:
#             y.parent.right = x
#         else:
#             y.parent.left = x
#         x.right = y
#         y.parent = x
# 
#     def insert(self, key):
#         node = Node(key)
#         node.left = node.right = self.NIL
#         y = None
#         x = self.root
#         while x != self.NIL:
#             y = x
#             if node.key < x.key:
#                 x = x.left
#             else:
#                 x = x.right
#         node.parent = y
#         if y == None:
#             self.root = node
#         elif node.key < y.key:
#             y.left = node
#         else:
#             y.right = node
#         node.color = 'red'
#         self.insert_fixup(node)
# 
#     def insert_fixup(self, z):
#         while z.parent and z.parent.color == 'red':
#             if z.parent == z.parent.parent.left:
#                 y = z.parent.parent.right
#                 if y and y.color == 'red':
#                     z.parent.color = 'black'
#                     y.color = 'black'
#                     z.parent.parent.color = 'red'
#                     z = z.parent.parent
#                 else:
#                     if z == z.parent.right:
#                         z = z.parent
#                         self.left_rotate(z)
#                     z.parent.color = 'black'
#                     z.parent.parent.color = 'red'
#                     self.right_rotate(z.parent.parent)
#             else:
#                 y = z.parent.parent.left
#                 if y and y.color == 'red':
#                     z.parent.color = 'black'
#                     y.color = 'black'
#                     z.parent.parent.color = 'red'
#                     z = z.parent.parent
#                 else:
#                     if z == z.parent.left:
#                         z = z.parent
#                         self.right_rotate(z)
#                     z.parent.color = 'black'
#                     z.parent.parent.color = 'red'
#                     self.left_rotate(z.parent.parent)
#         self.root.color = 'black'
# 
# rb = RedBlackTree()
# for key in [7,3,18,10,22,8,11,26]:
#     rb.insert(key)
# print(rb.root.key)
# ```
# This code builds a red‑black tree, inserts the given keys, and prints the root node’s value.
# Result: ❌ FAILED (Expected: 10, Actual: 7)
# State: 
# 
# Question24: Design Distributed Lock: Implement a Redis-based distributed lock mechanism, including lock acquisit...
# My answer: ```python
# import time
# import threading
# 
# # Simulated Redis store with expiration handling
# class FakeRedis:
#     def __init__(self):
#         self.store = {}
#         self.lock = threading.Lock()
# 
#     def setnx(self, key, value, ex):
#         with self.lock:
#             # Clean up expired keys first
#             self._cleanup()
#             if key not in self.store:
#                 self.store[key] = (value, time.time() + ex)
#                 return True
#             return False
# 
#     def delete(self, key):
#         with self.lock:
#             self.store.pop(key, None)
# 
#     def _cleanup(self):
#         now = time.time()
#         for k in list(self.store):
#             _, expiry = self.store[k]
#             if expiry <= now:
#                 del self.store[k]
# 
# # Distributed lock implementation
# class DistributedLock:
#     def __init__(self, redis, lock_key, ttl=5):
#         self.redis = redis
#         self.key = lock_key
#         self.ttl = ttl
#         self.value = str(time.time() + ttl)  # unique value (timestamp)
# 
#     def acquire(self):
#         return self.redis.setnx(self.key, self.value, self.ttl)
# 
#     def release(self):
#         self.redis.delete(self.key)
# 
# # Simulate two processes
# redis = FakeRedis()
# lock_key = 'resource_lock'
# acquired_by_second = []
# 
# def process(name, result_list):
#     lock = DistributedLock(redis, lock_key)
#     success = lock.acquire()
#     result_list.append((name, success))
#     if success:
#         print(f"{name} acquired the lock.")
#         # Hold the lock briefly to mimic work
#         time.sleep(2)
#         lock.release()
#         print(f"{name} released the lock.")
#     else:
#         print(f"{name} failed to acquire the lock.")
# 
# # Run both "processes" concurrently
# thread1 = threading.Thread(target=process, args=('Process1', acquired_by_second))
# thread2 = threading.Thread(target=process, args=('Process2', acquired_by_second))
# 
# thread1.start()
# # Ensure Process1 attempts first but release after a short delay
# time.sleep(0.1)
# thread2.start()
# 
# thread1.join()
# thread2.join()
# 
# # Output whether second process acquired the lock
# second_success = acquired_by_second[1][1]
# print(f"Second process successfully acquired lock: {second_success}")
# ```
# Implemented a simple Redis‑like lock with expiration using a dictionary and threading to simulate concurrent acquisition, demonstrating that the second process fails to acquire the lock.
# Result: ✅ PASSED (Expected: False, Actual: Process1 acquired the lock.
# Process2 failed to acquire the lock.
# Process1 released the lock.
# Second process successfully acquired lock: False)
# State: 你在正式評估中，答案將被記錄與審核。請僅在 r'```python\\s*\\n(.*?)\\n```' 或 r'```\\s*\\n(.*?)\\n```' 內輸出程式碼；另用一句話描述決策理由。\n\n問題：{question}
# 
# ---
# Now please solve the new question: Implement Segment Tree: Build a segment tree supporting range sum queries and single point updates. Build the tree for array [1,3,5,7,9,11], query the sum of range [1,3] (0-based indexing), then update the value at index 2 to 10, and query the sum of range [1,3] again.
# ==========================================

# ==========================================
# LLM original response:
# **Segment‑tree implementation (range‑sum + point update)**  
# 
# ```python
# class SegmentTree:
#     """Segment tree that supports range sum queries and point updates."""
# 
#     def __init__(self, data):
#         """Build the tree from the initial list `data`."""
#         self.n = len(data)
#         self.tree = [0] * (4 * self.n)          # enough space for the tree
#         self._build(data, node=1, l=0, r=self.n - 1)
# 
#     # ---------- internal helpers ----------
#     def _build(self, data, node, l, r):
#         """Recursively build the tree."""
#         if l == r:                      # leaf
#             self.tree[node] = data[l]
#         else:
#             mid = (l + r) // 2
#             self._build(data, node * 2, l, mid)
#             self._build(data, node * 2 + 1, mid + 1, r)
#             self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]
# 
#     def _update(self, node, l, r, idx, val):
#         """Recursively update a single element."""
#         if l == r:                      # leaf that holds the updated index
#             self.tree[node] = val
#         else:
#             mid = (l + r) // 2
#             if idx <= mid:
#                 self._update(node * 2, l, mid, idx, val)
#             else:
#                 self._update(node * 2 + 1, mid + 1, r, idx, val)
#             # after child update, recompute current node
#             self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]
# 
#     def _query(self, node, l, r, ql, qr):
#         """Recursively return the sum over [ql, qr]."""
#         if qr < l or ql > r:            # no overlap
#             return 0
#         if ql <= l and r <= qr:        # total overlap
#             return self.tree[node]
#         # partial overlap
#         mid = (l + r) // 2
#         return (self._query(node * 2, l, mid, ql, qr) +
#                 self._query(node * 2 + 1, mid + 1, r, ql, qr))
# 
#     # ---------- public API ----------
#     def update(self, idx, val):
#         """Set `data[idx]` to `val` and update the tree."""
#         self._update(1, 0, self.n - 1, idx, val)
# 
#     def query(self, ql, qr):
#         """Return the sum of the segment `[ql, qr]` (inclusive, 0‑based)."""
#         return self._query(1, 0, self.n - 1, ql, qr)
# 
# 
# # ----------- Demo as requested ----------
# arr = [1, 3, 5, 7, 9, 11]
# seg = SegmentTree(arr)
# 
# # Query sum of range [1, 3] → 3 + 5 + 7 = 15
# print("Sum of [1, 3] before update:", seg.query(1, 3))
# 
# # Point update: change index 2 (value 5) to 10
# seg.update(2, 10)
# 
# # Query again after the update → 3 + 10 + 7 = 20
# print("Sum of [1, 3] after update:", seg.query(1, 3))
# ```
# 
# **Output**
# 
# ```
# Sum of [1, 3] before update: 15
# Sum of [1, 3] after update: 20
# ```
# 
# This code constructs a classic segment tree, performs the required range‑sum queries, and applies a single point update as specified.
# ==========================================

# ==========================================
# Execution result:
# Error: 
# Partial output: Sum of [1, 3] before update: 15
Sum of [1, 3] after update: 20
# ==========================================
