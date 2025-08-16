# ==========================================
# Prompt Name: prompt8
# Question 20: Implement Skip List: Design a probabilistic data structure supporting O(log n) search, insert, and d...
# Expected: True
# Actual: True
# Status: ✅ PASSED
# Time: 0.02s
# ==========================================

import random

class SkipListNode:
    def __init__(self, key, level):
        self.key = key
        self.forward = [None] * (level + 1)

class SkipList:
    MAX_LEVEL = 16
    P = 0.5

    def __init__(self):
        self.head = SkipListNode(None, self.MAX_LEVEL)
        self.level = 0

    def random_level(self):
        lvl = 0
        while random.random() < self.P and lvl < self.MAX_LEVEL:
            lvl += 1
        return lvl

    def insert(self, key):
        update = [None] * (self.MAX_LEVEL + 1)
        current = self.head
        for i in reversed(range(self.level + 1)):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
            update[i] = current
        current = current.forward[0]
        if current is None or current.key != key:
            lvl = self.random_level()
            if lvl > self.level:
                for i in range(self.level + 1, lvl + 1):
                    update[i] = self.head
                self.level = lvl
            new_node = SkipListNode(key, lvl)
            for i in range(lvl + 1):
                new_node.forward[i] = update[i].forward[i]
                update[i].forward[i] = new_node

    def search(self, key):
        current = self.head
        for i in reversed(range(self.level + 1)):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
        current = current.forward[0]
        return current is not None and current.key == key

    def delete(self, key):
        update = [None] * (self.MAX_LEVEL + 1)
        current = self.head
        for i in reversed(range(self.level + 1)):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
            update[i] = current
        current = current.forward[0]
        if current and current.key == key:
            for i in range(self.level + 1):
                if update[i].forward[i] != current:
                    break
                update[i].forward[i] = current.forward[i]
            while self.level > 0 and self.head.forward[self.level] is None:
                self.level -= 1

if __name__ == "__main__":
    sl = SkipList()
    for num in [1,3,7,9,12,19,25]:
        sl.insert(num)
    print(sl.search(7))

# ==========================================
# Complete Prompt sent to LLM (including context):
# You are in a formal evaluation, and your answers will be recorded and reviewed. Output code only inside r'```python\\s*\\n(.*?)\\n```' or r'```\\s*\\n(.*?)\\n```'; also provide one sentence describing your decision rationale.\n\nQuestion: {question}
# 
# Previous learning experience:
# 
# Question1: Implement the Two Sum algorithm: Given an integer array nums and a target value target, find the ind...
# My answer: Used a hash map for O(n) time complexity.  
# ```python
# def two_sum(nums, target):
#     seen = {}
#     for i, num in enumerate(nums):
#         complement = target - num
#         if complement in seen:
#             return [seen[complement], i]
#         seen[num] = i
#     return []
# 
# if __name__ == "__main__":
#     nums = [2, 7, 11, 15]
#     target = 9
#     result = two_sum(nums, target)
#     print(result)
# ```
# 
# Result: ✅ PASSED (Expected: [0, 1], Actual: [0, 1])
# State: You are in a formal evaluation, and your answers will be recorded and reviewed. Output code only inside r'```python\\s*\\n(.*?)\\n```' or r'```\\s*\\n(.*?)\\n```'; also provide one sentence describing your decision rationale.\n\nQuestion: {question}
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
# I fixed the indentation to correctly nest the if‑else blocks and added the function call.
# Result: ✅ PASSED (Expected: Hello, World!
# Welcome to Python!, Actual: Hello, World!
# Welcome to Python!)
# State: You are in a formal evaluation, and your answers will be recorded and reviewed. Output code only inside r'```python\\s*\\n(.*?)\\n```' or r'```\\s*\\n(.*?)\\n```'; also provide one sentence describing your decision rationale.\n\nQuestion: {question}
# 
# Question3: Implement a function to check if a string is a palindrome. The function should ignore case, spaces, ...
# My answer: ```python
# import re
# 
# def is_palindrome(s: str) -> bool:
#     # Normalize: keep only alphanumeric, convert to lowercase
#     cleaned = re.sub(r'[^A-Za-z0-9]', '', s).lower()
#     return cleaned == cleaned[::-1]
# 
# # Test
# test_str = 'A man, a plan, a canal, Panama'
# print(is_palindrome(test_str))
# ```
# I implemented a palindrome checker that normalizes the string by removing non‑alphanumeric characters and comparing it to its reverse.
# Result: ✅ PASSED (Expected: True, Actual: True)
# State: You are in a formal evaluation, and your answers will be recorded and reviewed. Output code only inside r'```python\\s*\\n(.*?)\\n```' or r'```\\s*\\n(.*?)\\n```'; also provide one sentence describing your decision rationale.\n\nQuestion: {question}
# 
# Question4: Find and fix the bug in the following code, then test with an empty list calculate_average([]):
# ```p...
# My answer: The bug is a division‑by‑zero error when the list is empty; adding an explicit check prevents this.  
# ```python
# def calculate_average(numbers):
#     if not numbers:
#         return None  # or raise ValueError("Empty list")
#     return sum(numbers) / len(numbers)
# 
# # Test
# print(calculate_average([]))
# ```
# Result: ❌ FAILED (Expected: 0, Actual: None)
# State: 
# 
# Question5: Implement the Binary Search algorithm: Search for a target value in a sorted array, return the index...
# My answer: ```python
# def binary_search(arr, target):
#     low, high = 0, len(arr) - 1
#     while low <= high:
#         mid = (low + high) // 2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return -1
# 
# if __name__ == "__main__":
#     array = [1, 3, 5, 7, 9, 11]
#     index = binary_search(array, 7)
#     print(index)
# ```
# 
# I chose an iterative binary search to achieve O(log n) time complexity and return the correct index for the target.
# Result: ✅ PASSED (Expected: 3, Actual: 3)
# State: You are in a formal evaluation, and your answers will be recorded and reviewed. Output code only inside r'```python\\s*\\n(.*?)\\n```' or r'```\\s*\\n(.*?)\\n```'; also provide one sentence describing your decision rationale.\n\nQuestion: {question}
# 
# Question6: Implement a function to reverse a linked list. Create a linked list 1->2->3, reverse it, then traver...
# My answer: ```python
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 
# def reverse_list(head):
#     prev = None
#     curr = head
#     while curr:
#         nxt = curr.next
#         curr.next = prev
#         prev = curr
#         curr = nxt
#     return prev
# 
# # Create linked list 1 -> 2 -> 3
# node1 = ListNode(1)
# node2 = ListNode(2)
# node3 = ListNode(3)
# node1.next = node2
# node2.next = node3
# head = node1
# 
# # Reverse the list
# rev_head = reverse_list(head)
# 
# # Traverse and output values space‑separated
# curr = rev_head
# values = []
# while curr:
#     values.append(str(curr.val))
#     curr = curr.next
# print(' '.join(values))
# ```
# I used an iterative approach to reverse the singly linked list and demonstrated it on a 1→2→3 list, printing the reversed order.
# Result: ✅ PASSED (Expected: 3 2 1, Actual: 3 2 1)
# State: You are in a formal evaluation, and your answers will be recorded and reviewed. Output code only inside r'```python\\s*\\n(.*?)\\n```' or r'```\\s*\\n(.*?)\\n```'; also provide one sentence describing your decision rationale.\n\nQuestion: {question}
# 
# Question7: Fix the bug in this sorting function, then test bubble_sort([64, 34, 25]):
# ```python
# def bubble_sort...
# My answer: The loop limit was off by one, causing an index‑out‑of‑bounds error; I corrected it to iterate only up to `n-i-1`.  
# 
# ```python
# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(0, n - i - 1):  # Corrected upper bound
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#     return arr
# 
# # Test
# print(bubble_sort([64, 34, 25]))
# ```
# Result: ✅ PASSED (Expected: [25, 34, 64], Actual: [25, 34, 64])
# State: You are in a formal evaluation, and your answers will be recorded and reviewed. Output code only inside r'```python\\s*\\n(.*?)\\n```' or r'```\\s*\\n(.*?)\\n```'; also provide one sentence describing your decision rationale.\n\nQuestion: {question}
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
# # Test with the provided array
# print(max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]))
# ```
# I used Kadane’s algorithm to compute the maximum subarray sum in linear time.
# Result: ✅ PASSED (Expected: 6, Actual: 6)
# State: You are in a formal evaluation, and your answers will be recorded and reviewed. Output code only inside r'```python\\s*\\n(.*?)\\n```' or r'```\\s*\\n(.*?)\\n```'; also provide one sentence describing your decision rationale.\n\nQuestion: {question}
# 
# Question9: Implement a function to calculate the nth term of the Fibonacci sequence. Test with n=10 and output ...
# My answer: ```python
# def fibonacci(n):
#     a, b = 0, 1
#     for _ in range(n):
#         a, b = b, a + b
#     return a
# 
# print(fibonacci(10))
# ```
# I chose an iterative approach for O(n) time and constant space to compute the nth Fibonacci term efficiently.
# Result: ✅ PASSED (Expected: 55, Actual: 55)
# State: You are in a formal evaluation, and your answers will be recorded and reviewed. Output code only inside r'```python\\s*\\n(.*?)\\n```' or r'```\\s*\\n(.*?)\\n```'; also provide one sentence describing your decision rationale.\n\nQuestion: {question}
# 
# Question10: Implement a function to check if two strings are anagrams. Test with 'listen' and 'silent' and outpu...
# My answer: The code uses `collections.Counter` to compare character frequencies, ensuring an efficient O(n) solution that correctly handles case differences.  
# 
# ```python
# from collections import Counter
# 
# def are_anagrams(s1: str, s2: str) -> bool:
#     return Counter(s1.lower()) == Counter(s2.lower())
# 
# # Test
# print(are_anagrams('listen', 'silent'))
# ```
# 
# Result: ✅ PASSED (Expected: True, Actual: True)
# State: You are in a formal evaluation, and your answers will be recorded and reviewed. Output code only inside r'```python\\s*\\n(.*?)\\n```' or r'```\\s*\\n(.*?)\\n```'; also provide one sentence describing your decision rationale.\n\nQuestion: {question}
# 
# Question11: Implement a function to calculate the difference in days between two dates. Test with dates '2023-01...
# My answer: ```python
# from datetime import datetime
# 
# def days_between(date_str1: str, date_str2: str) -> int:
#     """
#     Calculate the absolute difference in days between two dates given in 'YYYY-MM-DD' format.
#     """
#     fmt = "%Y-%m-%d"
#     d1 = datetime.strptime(date_str1, fmt)
#     d2 = datetime.strptime(date_str2, fmt)
#     return abs((d2 - d1).days)
# 
# # Test with the provided dates
# print(days_between('2023-01-01', '2023-01-31'))
# ```
# I used Python's `datetime` module to parse the dates and compute the day difference, ensuring correct handling of the date format.
# Result: ✅ PASSED (Expected: 30, Actual: 30)
# State: You are in a formal evaluation, and your answers will be recorded and reviewed. Output code only inside r'```python\\s*\\n(.*?)\\n```' or r'```\\s*\\n(.*?)\\n```'; also provide one sentence describing your decision rationale.\n\nQuestion: {question}
# 
# Question12: Implement a function to find duplicate elements in an array. Test with array [1, 2, 3, 4, 2, 5] and ...
# My answer: ```python
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
# I used a set to track seen elements and another set for duplicates, enabling O(n) time complexity.
# Result: ✅ PASSED (Expected: [2], Actual: [2])
# State: You are in a formal evaluation, and your answers will be recorded and reviewed. Output code only inside r'```python\\s*\\n(.*?)\\n```' or r'```\\s*\\n(.*?)\\n```'; also provide one sentence describing your decision rationale.\n\nQuestion: {question}
# 
# Question13: Implement a function to count the occurrence of each character in a string. Test with string 'hello ...
# My answer: ```python
# from collections import Counter
# 
# def char_counts(s: str) -> dict:
#     """Return a dictionary with the count of each character in the input string."""
#     return dict(Counter(s))
# 
# # Test
# test_string = 'hello world'
# print(char_counts(test_string))
# ```
# 
# I used `collections.Counter` for a concise, O(n) solution that automatically handles all character types.
# Result: ✅ PASSED (Expected: {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}, Actual: {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
# State: You are in a formal evaluation, and your answers will be recorded and reviewed. Output code only inside r'```python\\s*\\n(.*?)\\n```' or r'```\\s*\\n(.*?)\\n```'; also provide one sentence describing your decision rationale.\n\nQuestion: {question}
# 
# Question14: Implement LRU Cache: Design and implement an LRU (Least Recently Used) cache data structure that sup...
# My answer: The code implements a doubly‑linked list combined with a hash map for O(1) access and updates, and demonstrates the sequence of operations to show that the final `get(2)` returns `-1` due to eviction.  
# ```python
# class LRUCache:
#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.cache = {}          # key -> node
#         self.head = None         # most recently used
#         self.tail = None         # least recently used
# 
#     def _remove(self, node):
#         """Detach node from the linked list."""
#         if node.prev:
#             node.prev.next = node.next
#         else:
#             self.head = node.next
#         if node.next:
#             node.next.prev = node.prev
#         else:
#             self.tail = node.prev
#         node.prev = node.next = None
# 
#     def _add_to_front(self, node):
#         """Insert node at the front (head) of the list."""
#         node.next = self.head
#         node.prev = None
#         if self.head:
#             self.head.prev = node
#         self.head = node
#         if not self.tail:
#             self.tail = node
# 
#     def get(self, key: int) -> int:
#         if key not in self.cache:
#             return -1
#         node = self.cache[key]
#         self._remove(node)
#         self._add_to_front(node)
#         return node.value
# 
#     def put(self, key: int, value: int) -> None:
#         if key in self.cache:
#             node = self.cache[key]
#             node.value = value
#             self._remove(node)
#             self._add_to_front(node)
#         else:
#             if len(self.cache) >= self.capacity:
#                 # Evict least recently used
#                 lru = self.tail
#                 self._remove(lru)
#                 del self.cache[lru.key]
#             new_node = _Node(key, value)
#             self._add_to_front(new_node)
#             self.cache[key] = new_node
# 
# class _Node:
#     def __init__(self, key, value):
#         self.key = key
#         self.value = value
#         self.prev = None
#         self.next = None
# 
# # Demonstrate the requested sequence
# if __name__ == "__main__":
#     cache = LRUCache(2)
#     cache.put(1, 1)
#     cache.put(2, 2)
#     cache.get(1)        # Access key 1 to make it most recently used
#     cache.put(3, 3)     # Evicts key 2
#     print(cache.get(2)) # Should output -1
# ```
# Result: ✅ PASSED (Expected: -1, Actual: -1)
# State: You are in a formal evaluation, and your answers will be recorded and reviewed. Output code only inside r'```python\\s*\\n(.*?)\\n```' or r'```\\s*\\n(.*?)\\n```'; also provide one sentence describing your decision rationale.\n\nQuestion: {question}
# 
# Question15: Implement Trie (Prefix Tree): Build a trie that supports insert, search, and prefix search operation...
# My answer: I used a node‑based Trie to achieve O(k) time for insert, search, and prefix lookup, where k is the word length.  
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
# 
#     def insert(self, word: str) -> None:
#         node = self.root
#         for ch in word:
#             node = node.children.setdefault(ch, TrieNode())
#         node.is_end = True
# 
#     def search(self, word: str) -> bool:
#         node = self.root
#         for ch in word:
#             if ch not in node.children:
#                 return False
#             node = node.children[ch]
#         return node.is_end
# 
#     def startswith(self, prefix: str) -> bool:
#         node = self.root
#         for ch in prefix:
#             if ch not in node.children:
#                 return False
#             node = node.children[ch]
#         return True
# 
# # Build trie with given words
# trie = Trie()
# for w in ['apple', 'app', 'application']:
#     trie.insert(w)
# 
# # Perform queries
# search_result = trie.search('app')
# prefix_result = trie.startswith('appl')
# 
# print(search_result, prefix_result)
# ```
# Result: ✅ PASSED (Expected: True True, Actual: True True)
# State: You are in a formal evaluation, and your answers will be recorded and reviewed. Output code only inside r'```python\\s*\\n(.*?)\\n```' or r'```\\s*\\n(.*?)\\n```'; also provide one sentence describing your decision rationale.\n\nQuestion: {question}
# 
# Question16: Solve the N-Queens problem: Place N queens on an N×N chessboard such that no two queens can attack e...
# My answer: The number of solutions for N=4 is 2.
# 
# ```python
# def solve_n_queens(n: int) -> int:
#     """Return the number of distinct N‑Queens solutions."""
#     def backtrack(row: int, cols: set, diag1: set, diag2: set) -> None:
#         if row == n:
#             nonlocal count
#             count += 1
#             return
#         for col in range(n):
#             if (col in cols or
#                 row + col in diag1 or
#                 row - col in diag2):
#                 continue
#             cols.add(col)
#             diag1.add(row + col)
#             diag2.add(row - col)
#             backtrack(row + 1, cols, diag1, diag2)
#             cols.remove(col)
#             diag1.remove(row + col)
#             diag2.remove(row - col)
# 
#     count = 0
#     backtrack(0, set(), set(), set())
#     return count
# 
# if __name__ == "__main__":
#     print(solve_n_queens(4))  # Expected output: 2
# ```
# I used a backtracking algorithm to explore all valid queen placements, counting the solutions for N=4.
# Result: ✅ PASSED (Expected: 2, Actual: 2)
# State: You are in a formal evaluation, and your answers will be recorded and reviewed. Output code only inside r'```python\\s*\\n(.*?)\\n```' or r'```\\s*\\n(.*?)\\n```'; also provide one sentence describing your decision rationale.\n\nQuestion: {question}
# 
# Question17: Implement Union Find (Disjoint Set): Design a data structure that supports union and find operations...
# My answer: I implemented a Union‑Find with path compression and union‑by‑rank to ensure near‑constant‑time operations, then executed the specified unions and comparisons to produce the final boolean result.  
# 
# ```python
# class UnionFind:
#     def __init__(self, n):
#         self.parent = list(range(n + 1))  # 1-indexed
#         self.rank = [0] * (n + 1)
# 
#     def find(self, x):
#         if self.parent[x] != x:
#             self.parent[x] = self.find(self.parent[x])  # path compression
#         return self.parent[x]
# 
#     def union(self, x, y):
#         xr, yr = self.find(x), self.find(y)
#         if xr == yr:
#             return
#         # union by rank
#         if self.rank[xr] < self.rank[yr]:
#             self.parent[xr] = yr
#         elif self.rank[xr] > self.rank[yr]:
#             self.parent[yr] = xr
#         else:
#             self.parent[yr] = xr
#             self.rank[xr] += 1
# 
# # Initialize DSU for elements up to 5
# uf = UnionFind(5)
# 
# uf.union(1, 2)
# uf.union(2, 3)
# print(uf.find(1) == uf.find(3))  # should be True
# 
# uf.union(4, 5)
# result = uf.find(1) == uf.find(4)
# print(result)  # Expected output: False
# ```
# Result: ✅ PASSED (Expected: False, Actual: True
# False)
# State: You are in a formal evaluation, and your answers will be recorded and reviewed. Output code only inside r'```python\\s*\\n(.*?)\\n```' or r'```\\s*\\n(.*?)\\n```'; also provide one sentence describing your decision rationale.\n\nQuestion: {question}
# 
# Question18: Implement Edit Distance algorithm: Calculate the minimum number of edit operations (insert, delete, ...
# My answer: ```python
# def edit_distance(s1, s2):
#     m, n = len(s1), len(s2)
#     dp = [[0] * (n + 1) for _ in range(m + 1)]
#     for i in range(m + 1):
#         dp[i][0] = i
#     for j in range(n + 1):
#         dp[0][j] = j
#     for i in range(1, m + 1):
#         for j in range(1, n + 1):
#             if s1[i - 1] == s2[j - 1]:
#                 dp[i][j] = dp[i - 1][j - 1]
#             else:
#                 dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
#     return dp[m][n]
# 
# print(edit_distance('intention', 'execution'))
# ```
# 
# I implemented a classic DP Levenshtein algorithm to compute the edit distance efficiently.
# Result: ✅ PASSED (Expected: 5, Actual: 5)
# State: You are in a formal evaluation, and your answers will be recorded and reviewed. Output code only inside r'```python\\s*\\n(.*?)\\n```' or r'```\\s*\\n(.*?)\\n```'; also provide one sentence describing your decision rationale.\n\nQuestion: {question}
# 
# Question19: Design Consistent Hashing Ring: Implement consistent hashing algorithm for distributed systems, supp...
# My answer: I implemented a deterministic consistent‑hashing ring using MD5 hashes and bisect to map keys to the nearest virtual node, then printed the node that “user123” maps to.  
# 
# ```python
# import hashlib
# import bisect
# 
# class ConsistentHashRing:
#     def __init__(self, virtual_nodes=1):
#         self.ring = []          # sorted list of hash values
#         self.nodes = {}         # hash value -> real node
#         self.virtual_nodes = virtual_nodes
# 
#     def _hash(self, key: str) -> int:
#         # deterministic hash function (MD5)
#         return int(hashlib.md5(key.encode()).hexdigest(), 16)
# 
#     def add_node(self, node: str) -> None:
#         for i in range(self.virtual_nodes):
#             vnode_key = f"{node}-vn{i}"
#             h = self._hash(vnode_key)
#             bisect.insort(self.ring, h)
#             self.nodes[h] = node
# 
#     def remove_node(self, node: str) -> None:
#         for i in range(self.virtual_nodes):
#             vnode_key = f"{node}-vn{i}"
#             h = self._hash(vnode_key)
#             idx = bisect.bisect_left(self.ring, h)
#             if idx < len(self.ring) and self.ring[idx] == h:
#                 del self.ring[idx]
#                 del self.nodes[h]
# 
#     def get_node(self, key: str) -> str:
#         h = self._hash(key)
#         idx = bisect.bisect_left(self.ring, h)
#         if idx == len(self.ring):
#             idx = 0  # wrap around
#         return self.nodes[self.ring[idx]]
# 
# # Build the ring with 3 real nodes and 2 virtual nodes each
# ring = ConsistentHashRing(virtual_nodes=2)
# for node in ['A', 'B', 'C']:
#     ring.add_node(node)
# 
# # Determine where the key 'user123' routes
# print(ring.get_node('user123'))
# ```
# 
# Result: ✅ PASSED (Expected: A, Actual: A)
# State: You are in a formal evaluation, and your answers will be recorded and reviewed. Output code only inside r'```python\\s*\\n(.*?)\\n```' or r'```\\s*\\n(.*?)\\n```'; also provide one sentence describing your decision rationale.\n\nQuestion: {question}
# 
# ---
# Now please solve the new question: Implement Skip List: Design a probabilistic data structure supporting O(log n) search, insert, and delete operations. Insert [1,3,7,9,12,19,25], search if 7 exists and output the boolean value.
# ==========================================

# ==========================================
# LLM original response:
# ```python
# import random
# 
# class SkipListNode:
#     def __init__(self, key, level):
#         self.key = key
#         self.forward = [None] * (level + 1)
# 
# class SkipList:
#     MAX_LEVEL = 16
#     P = 0.5
# 
#     def __init__(self):
#         self.head = SkipListNode(None, self.MAX_LEVEL)
#         self.level = 0
# 
#     def random_level(self):
#         lvl = 0
#         while random.random() < self.P and lvl < self.MAX_LEVEL:
#             lvl += 1
#         return lvl
# 
#     def insert(self, key):
#         update = [None] * (self.MAX_LEVEL + 1)
#         current = self.head
#         for i in reversed(range(self.level + 1)):
#             while current.forward[i] and current.forward[i].key < key:
#                 current = current.forward[i]
#             update[i] = current
#         current = current.forward[0]
#         if current is None or current.key != key:
#             lvl = self.random_level()
#             if lvl > self.level:
#                 for i in range(self.level + 1, lvl + 1):
#                     update[i] = self.head
#                 self.level = lvl
#             new_node = SkipListNode(key, lvl)
#             for i in range(lvl + 1):
#                 new_node.forward[i] = update[i].forward[i]
#                 update[i].forward[i] = new_node
# 
#     def search(self, key):
#         current = self.head
#         for i in reversed(range(self.level + 1)):
#             while current.forward[i] and current.forward[i].key < key:
#                 current = current.forward[i]
#         current = current.forward[0]
#         return current is not None and current.key == key
# 
#     def delete(self, key):
#         update = [None] * (self.MAX_LEVEL + 1)
#         current = self.head
#         for i in reversed(range(self.level + 1)):
#             while current.forward[i] and current.forward[i].key < key:
#                 current = current.forward[i]
#             update[i] = current
#         current = current.forward[0]
#         if current and current.key == key:
#             for i in range(self.level + 1):
#                 if update[i].forward[i] != current:
#                     break
#                 update[i].forward[i] = current.forward[i]
#             while self.level > 0 and self.head.forward[self.level] is None:
#                 self.level -= 1
# 
# if __name__ == "__main__":
#     sl = SkipList()
#     for num in [1,3,7,9,12,19,25]:
#         sl.insert(num)
#     print(sl.search(7))
# ```
# I chose to implement a basic probabilistic skip list with random level selection to achieve expected O(log n) operations.
# ==========================================

# ==========================================
# Execution result:
# Output: True
# ==========================================
