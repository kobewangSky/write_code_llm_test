# ==========================================
# Prompt Name: prompt8
# Question 11: Implement a function to calculate the difference in days between two dates. Test with dates '2023-01...
# Expected: 30
# Actual: 30
# Status: ✅ PASSED
# Time: 0.02s
# ==========================================

from datetime import datetime

def days_between(date_str1: str, date_str2: str) -> int:
    """
    Calculate the absolute difference in days between two dates given in 'YYYY-MM-DD' format.
    """
    fmt = "%Y-%m-%d"
    d1 = datetime.strptime(date_str1, fmt)
    d2 = datetime.strptime(date_str2, fmt)
    return abs((d2 - d1).days)

# Test with the provided dates
print(days_between('2023-01-01', '2023-01-31'))

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
# ---
# Now please solve the new question: Implement a function to calculate the difference in days between two dates. Test with dates '2023-01-01' and '2023-01-31' and output the difference in days.
# ==========================================

# ==========================================
# LLM original response:
# ```python
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
# ==========================================

# ==========================================
# Execution result:
# Output: 30
# ==========================================
