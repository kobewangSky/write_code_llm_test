# ==========================================
# Prompt Name: prompt8
# Question 25: Implement Segment Tree: Build a segment tree supporting range sum queries and single point updates. ...
# Expected: 23
# Actual: ERROR
# Status: ❌ FAILED (wrong_answer)
# Time: 0.02s
# ==========================================

class SegmentTree:
    def __init__(self, data):
        """Builds a segment tree for range sum queries."""
        self.n = len(data)
        self.size = 1
        while self.size < self.n:
            self.size <<= 1
        # tree array with extra space for internal nodes
        self.tree = [0] * (2 * self.size)
        # fill leaves
        for i in range(self.n):
            self.tree[self.size + i] = data[i]
        # build internal nodes
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def update(self, idx, value):
        """Point update: set data[idx] = value."""
        pos = self.size + idx
        self.tree[pos] = value
        pos >>= 1
        while pos:
            self.tree[pos] = self.tree[2 * pos] + self.tree[2 * pos + 1]
            pos >>= 1

    def query(self, left, right):
        """Range sum query for [left, right] inclusive, 0‑based indexing."""
        left += self.size
        right += self.size
        result = 0
        while left <= right:
            if left & 1:
                result += self.tree[left]
                left += 1
            if not (right & 1):
                result += self.tree[right]
                right -= 1
            left >>= 1
            right >>= 1
        return result


if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 11]
    seg = SegmentTree(arr)

    # Query sum of range [1, 3] (0‑based)
    print(seg.query(1, 3))  # Expected 15

    # Update index 2 to 10
    seg.update(2, 10)

    # Query again
    print(seg.query(1, 3))  # Expected 20

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
# Question20: Implement Skip List: Design a probabilistic data structure supporting O(log n) search, insert, and d...
# My answer: ```python
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
# Result: ✅ PASSED (Expected: True, Actual: True)
# State: You are in a formal evaluation, and your answers will be recorded and reviewed. Output code only inside r'```python\\s*\\n(.*?)\\n```' or r'```\\s*\\n(.*?)\\n```'; also provide one sentence describing your decision rationale.\n\nQuestion: {question}
# 
# Question21: Solve Traveling Salesman Problem using dynamic programming: Given a distance matrix for 4 cities [[0...
# My answer: I implemented the Held‑Karp dynamic‑programming algorithm with bitmasking to compute the optimal tour length in O(n²·2ⁿ) time, which is efficient for 4 cities.
# 
# ```python
# def tsp_dp(dist):
#     n = len(dist)
#     full_mask = (1 << n) - 1
#     # dp[mask][i] = min cost to start at 0, visit nodes in mask, end at i
#     dp = [[float('inf')] * n for _ in range(1 << n)]
#     dp[1][0] = 0  # start at city 0
# 
#     for mask in range(1 << n):
#         for last in range(n):
#             if not (mask & (1 << last)):
#                 continue
#             if dp[mask][last] == float('inf'):
#                 continue
#             for nxt in range(n):
#                 if mask & (1 << nxt):
#                     continue
#                 new_mask = mask | (1 << nxt)
#                 dp[new_mask][nxt] = min(dp[new_mask][nxt],
#                                         dp[mask][last] + dist[last][nxt])
# 
#     # close the tour by returning to city 0
#     best = float('inf')
#     for i in range(n):
#         if i == 0:
#             continue
#         best = min(best, dp[full_mask][i] + dist[i][0])
#     return best
# 
# if __name__ == "__main__":
#     dist = [
#         [0, 10, 15, 20],
#         [10, 0, 35, 25],
#         [15, 35, 0, 30],
#         [20, 25, 30, 0]
#     ]
#     print(tsp_dp(dist))
# ```
# Result: ✅ PASSED (Expected: 80, Actual: 80)
# State: You are in a formal evaluation, and your answers will be recorded and reviewed. Output code only inside r'```python\\s*\\n(.*?)\\n```' or r'```\\s*\\n(.*?)\\n```'; also provide one sentence describing your decision rationale.\n\nQuestion: {question}
# 
# Question22: Implement a simplified version of MapReduce framework: Design word count functionality, process the ...
# My answer: I implemented a minimal MapReduce word‑count using map and reduce functions to compute and display word frequencies.  
# ```python
# def map_function(text):
#     return [(word, 1) for word in text.split()]
# 
# def reduce_function(mapped):
#     counts = {}
#     for word, count in mapped:
#         counts[word] = counts.get(word, 0) + count
#     return counts
# 
# if __name__ == "__main__":
#     text = "hello world hello"
#     mapped = map_function(text)
#     counts = reduce_function(mapped)
#     # output as word:count space-separated
#     output = ' '.join(f"{w}:{counts[w]}" for w in sorted(counts))
#     print(output)
# ```
# Result: ✅ PASSED (Expected: hello:2 world:1, Actual: hello:2 world:1)
# State: You are in a formal evaluation, and your answers will be recorded and reviewed. Output code only inside r'```python\\s*\\n(.*?)\\n```' or r'```\\s*\\n(.*?)\\n```'; also provide one sentence describing your decision rationale.\n\nQuestion: {question}
# 
# Question23: Implement Red-Black Tree insertion operation: Insert [7,3,18,10,22,8,11,26] sequentially into an emp...
# My answer: The code builds a standard red‑black tree, inserts the given values, and prints the root’s key, ensuring correct balancing via rotations and recoloring.
# 
# ```python
# class Node:
#     RED, BLACK = 0, 1
#     def __init__(self, key, color=RED, left=None, right=None, parent=None):
#         self.key = key
#         self.color = color
#         self.left = left
#         self.right = right
#         self.parent = parent
# 
# class RedBlackTree:
#     def __init__(self):
#         self.NIL = Node(None, color=Node.BLACK)
#         self.root = self.NIL
# 
#     def left_rotate(self, x):
#         y = x.right
#         x.right = y.left
#         if y.left != self.NIL:
#             y.left.parent = x
#         y.parent = x.parent
#         if x.parent == self.NIL:
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
#         if y.parent == self.NIL:
#             self.root = x
#         elif y == y.parent.right:
#             y.parent.right = x
#         else:
#             y.parent.left = x
#         x.right = y
#         y.parent = x
# 
#     def insert(self, key):
#         z = Node(key)
#         z.left = z.right = self.NIL
#         y = self.NIL
#         x = self.root
#         while x != self.NIL:
#             y = x
#             if z.key < x.key:
#                 x = x.left
#             else:
#                 x = x.right
#         z.parent = y
#         if y == self.NIL:
#             self.root = z
#         elif z.key < y.key:
#             y.left = z
#         else:
#             y.right = z
#         z.color = Node.RED
#         self.fix_insert(z)
# 
#     def fix_insert(self, z):
#         while z.parent.color == Node.RED:
#             if z.parent == z.parent.parent.left:
#                 y = z.parent.parent.right
#                 if y.color == Node.RED:          # Case 3
#                     z.parent.color = Node.BLACK
#                     y.color = Node.BLACK
#                     z.parent.parent.color = Node.RED
#                     z = z.parent.parent
#                 else:
#                     if z == z.parent.right:      # Case 2
#                         z = z.parent
#                         self.left_rotate(z)
#                     z.parent.color = Node.BLACK   # Case 1
#                     z.parent.parent.color = Node.RED
#                     self.right_rotate(z.parent.parent)
#             else:
#                 y = z.parent.parent.left
#                 if y.color == Node.RED:          # Mirror Case 3
#                     z.parent.color = Node.BLACK
#                     y.color = Node.BLACK
#                     z.parent.parent.color = Node.RED
#                     z = z.parent.parent
#                 else:
#                     if z == z.parent.left:      # Mirror Case 2
#                         z = z.parent
#                         self.right_rotate(z)
#                     z.parent.color = Node.BLACK   # Mirror Case 1
#                     z.parent.parent.color = Node.RED
#                     self.left_rotate(z.parent.parent)
#         self.root.color = Node.BLACK
# 
#     def __str__(self):
#         res = []
#         def in_order(node):
#             if node == self.NIL:
#                 return
#             in_order(node.left)
#             res.append(f'{node.key}:{ "R" if node.color==Node.RED else "B"}')
#             in_order(node.right)
#         in_order(self.root)
#         return ' '.join(res)
# 
# if __name__ == "__main__":
#     values = [7,3,18,10,22,8,11,26]
#     tree = RedBlackTree()
#     for v in values:
#         tree.insert(v)
#     print(tree.root.key)
# ```
# Result: ❌ FAILED (Expected: 10, Actual: 7)
# State: 
# 
# Question24: Design Distributed Lock: Implement a Redis-based distributed lock mechanism, including lock acquisit...
# My answer: **Solution**
# 
# The lock works exactly as a Redis `SET key value NX PX ttl` command –  
# a value (a unique token) is stored only if the key does not already exist,  
# and the key automatically disappears after `ttl` milliseconds.  
# Releasing the lock requires that the process still owns it (the token it set),
# otherwise the command is ignored.
# 
# Because the execution environment does not provide a real Redis server,
# the implementation contains a lightweight **mock Redis** that mimics the
# behaviour needed for the lock (`SET NX PX`, `GET`, `DEL`, key expiration).
# 
# The simulation runs two threads that try to acquire the same lock
# (`resource_lock`) at the same instant.  
# Only the first thread succeeds; the second one receives a `False`
# indicating that it did not obtain the lock.
# 
# ```python
# import time
# import uuid
# import threading
# 
# # ----------------- Mock Redis ---------------------------------
# class MockRedis:
#     """Very small subset of Redis used only for the lock demo."""
#     def __init__(self):
#         self.store = {}      # key -> (value, expiry_timestamp or None)
#         self.lock = threading.Lock()
# 
#     def _purge_expired(self, key):
#         """Delete key if it has expired."""
#         _, expiry = self.store.get(key, (None, None))
#         if expiry is not None and time.time() > expiry:
#             del self.store[key]
#             return True
#         return False
# 
#     def set(self, key, value, nx=False, px=None):
#         """
#         Mimic Redis SET command.
#         - nx=True: only set if key does not exist
#         - px milliseconds: expiration in milliseconds
#         """
#         with self.lock:
#             # Remove key if it has expired
#             if key in self.store:
#                 self._purge_expired(key)
# 
#             if nx and key in self.store:
#                 return False  # key already present
# 
#             expiry = None
#             if px is not None:
#                 expiry = time.time() + px / 1000.0
# 
#             self.store[key] = (value, expiry)
#             return True
# 
#     def get(self, key):
#         """Return the value of a key, or None if missing/expired."""
#         with self.lock:
#             if key not in self.store:
#                 return None
#             self._purge_expired(key)
#             if key in self.store:
#                 return self.store[key][0]
#             return None
# 
#     def delete(self, key):
#         """Delete a key."""
#         with self.lock:
#             return self.store.pop(key, None) is not None
# 
#     # Helper to emulate Lua script used for safe release
#     def eval(self, script, num_keys, *args):
#         """
#         Very small subset of Lua script support:
#         script expects one key and one argument (token).
#         """
#         key = args[0]
#         token = args[1]
#         with self.lock:
#             # Purge expired key first
#             if key in self.store:
#                 self._purge_expired(key)
# 
#             current_token, _ = self.store.get(key, (None, None))
#             if current_token == token:
#                 del self.store[key]
#                 return 1  # success
#             return 0  # failure
# 
# 
# # ----------------- Distributed Lock ---------------------------
# class DistributedLock:
#     """
#     Redis‑style distributed lock.
#     Uses a Redis client that implements the minimal interface required.
#     """
# 
#     def __init__(self, redis_client, lock_name, ttl_ms=10000):
#         self.redis = redis_client
#         self.lock_name = lock_name
#         self.ttl_ms = ttl_ms
#         self.token = None  # Unique token set on this process
# 
#     def acquire(self):
#         """Attempt to acquire the lock. Return True on success."""
#         # Generate a unique token for this process
#         self.token = str(uuid.uuid4())
#         result = self.redis.set(self.lock_name, self.token, nx=True, px=self.ttl_ms)
#         return bool(result)
# 
#     def release(self):
#         """Release the lock only if we still own it."""
#         if self.token is None:
#             return False
#         script = """
#         if redis.call('GET', KEYS[1]) == ARGV[1] then
#             return redis.call('DEL', KEYS[1])
#         else
#             return 0
#         end
#         """
#         return bool(self.redis.eval(script, 1, self.lock_name, self.token))
# 
#     def is_acquired(self):
#         """Return True if this process still holds the lock."""
#         return self.redis.get(self.lock_name) == self.token
# 
# 
# # ----------------- Simulation ---------------------------------
# def try_lock(process_id, lock, results):
#     """Thread target: attempt to acquire the lock."""
#     acquired = lock.acquire()
#     results[process_id] = acquired
#     # Print status for debugging (optional)
#     print(f"Process {process_id} {'acquired' if acquired else 'failed to acquire'} the lock.")
# 
# 
# def main():
#     # Use the mock Redis for the demo
#     redis_client = MockRedis()
# 
#     # Ensure the key does not exist at start
#     redis_client.delete('resource_lock')
# 
#     # Create two lock objects, each representing a different process
#     lock1 = DistributedLock(redis_client, 'resource_lock', ttl_ms=5000)
#     lock2 = DistributedLock(redis_client, 'resource_lock', ttl_ms=5000)
# 
#     # Dictionary to capture results of each process
#     results = {1: None, 2: None}
# 
#     # Two threads simulate two processes trying to lock at the same time
#     t1 = threading.Thread(target=try_lock, args=(1, lock1, results))
#     t2 = threading.Thread(target=try_lock, args=(2, lock2, results))
# 
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()
# 
#     # Output whether the second process succeeded
#     print("\nFinal Result:")
#     print(f"Did the second process acquire the lock? {results[2]}")
# 
#     # Clean up for the next run
#     redis_client.delete('resource_lock')
# 
# 
# if __name__ == "__main__":
#     main()
# ```
# 
# ### Expected Output
# 
# ```
# Process 1 acquired the lock.
# Process 2 failed to acquire the lock.
# 
# Final Result:
# Did the second process acquire the lock? False
# ```
# 
# The code implements a correct Redis‑style distributed lock with:
# 
# 1. **Lock acquisition** – `SET key value NX PX ttl`.
# 2. **Lock release** – safe delete only if the caller still owns the token.
# 3. **Lock expiration** – handled automatically by the mock (or real Redis) using the `PX` flag.
# 4. **Simulation** – two threads trying to acquire the same lock, showing that only one succeeds.
# Result: ✅ PASSED (Expected: False, Actual: Process 1 acquired the lock.
# Process 2 failed to acquire the lock.
# 
# Final Result:
# Did the second process acquire the lock? False)
# State: You are in a formal evaluation, and your answers will be recorded and reviewed. Output code only inside r'```python\\s*\\n(.*?)\\n```' or r'```\\s*\\n(.*?)\\n```'; also provide one sentence describing your decision rationale.\n\nQuestion: {question}
# 
# ---
# Now please solve the new question: Implement Segment Tree: Build a segment tree supporting range sum queries and single point updates. Build the tree for array [1,3,5,7,9,11], query the sum of range [1,3] (0-based indexing), then update the value at index 2 to 10, and query the sum of range [1,3] again.
# ==========================================

# ==========================================
# LLM original response:
# ```python
# class SegmentTree:
#     def __init__(self, data):
#         """Builds a segment tree for range sum queries."""
#         self.n = len(data)
#         self.size = 1
#         while self.size < self.n:
#             self.size <<= 1
#         # tree array with extra space for internal nodes
#         self.tree = [0] * (2 * self.size)
#         # fill leaves
#         for i in range(self.n):
#             self.tree[self.size + i] = data[i]
#         # build internal nodes
#         for i in range(self.size - 1, 0, -1):
#             self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]
# 
#     def update(self, idx, value):
#         """Point update: set data[idx] = value."""
#         pos = self.size + idx
#         self.tree[pos] = value
#         pos >>= 1
#         while pos:
#             self.tree[pos] = self.tree[2 * pos] + self.tree[2 * pos + 1]
#             pos >>= 1
# 
#     def query(self, left, right):
#         """Range sum query for [left, right] inclusive, 0‑based indexing."""
#         left += self.size
#         right += self.size
#         result = 0
#         while left <= right:
#             if left & 1:
#                 result += self.tree[left]
#                 left += 1
#             if not (right & 1):
#                 result += self.tree[right]
#                 right -= 1
#             left >>= 1
#             right >>= 1
#         return result
# 
# 
# if __name__ == "__main__":
#     arr = [1, 3, 5, 7, 9, 11]
#     seg = SegmentTree(arr)
# 
#     # Query sum of range [1, 3] (0‑based)
#     print(seg.query(1, 3))  # Expected 15
# 
#     # Update index 2 to 10
#     seg.update(2, 10)
# 
#     # Query again
#     print(seg.query(1, 3))  # Expected 20
# ```
# 
# ==========================================

# ==========================================
# Execution result:
# Error: 
# Partial output: 15
20
# ==========================================
