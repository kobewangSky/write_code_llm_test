# ==========================================
# Prompt Name: prompt8
# Question 5: Implement the Binary Search algorithm: Search for a target value in a sorted array, return the index...
# Expected: 3
# Actual: 3
# Status: ✅ PASSED
# Time: 0.01s
# ==========================================

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

if __name__ == "__main__":
    array = [1, 3, 5, 7, 9, 11]
    index = binary_search(array, 7)
    print(index)

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
# ---
# Now please solve the new question: Implement the Binary Search algorithm: Search for a target value in a sorted array, return the index if found, otherwise return -1. Test: search for 7 in [1,3,5,7,9,11] and output the index.
# ==========================================

# ==========================================
# LLM original response:
# ```python
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
# ==========================================

# ==========================================
# Execution result:
# Output: 3
# ==========================================
