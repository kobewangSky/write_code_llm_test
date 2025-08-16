# ==========================================
# Prompt Name: prompt4
# Question 9: Implement a function to calculate the nth term of the Fibonacci sequence. Test with n=10 and output ...
# Expected: 55
# Actual: 55
# Status: ✅ PASSED
# Time: 0.01s
# ==========================================

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Test
n = 10
print(fibonacci(n))

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
# ---
# Now please solve the new question: Implement a function to calculate the nth term of the Fibonacci sequence. Test with n=10 and output the result.
# ==========================================

# ==========================================
# LLM original response:
# ```python
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
# ==========================================

# ==========================================
# Execution result:
# Output: 55
# ==========================================
