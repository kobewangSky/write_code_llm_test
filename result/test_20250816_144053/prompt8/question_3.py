# ==========================================
# Prompt Name: prompt8
# Question 3: Implement a function to check if a string is a palindrome. The function should ignore case, spaces, ...
# Expected: True
# Actual: True
# Status: ✅ PASSED
# Time: 0.02s
# ==========================================

import re

def is_palindrome(s: str) -> bool:
    # Normalize: keep only alphanumeric, convert to lowercase
    cleaned = re.sub(r'[^A-Za-z0-9]', '', s).lower()
    return cleaned == cleaned[::-1]

# Test
test_str = 'A man, a plan, a canal, Panama'
print(is_palindrome(test_str))

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
# ---
# Now please solve the new question: Implement a function to check if a string is a palindrome. The function should ignore case, spaces, and punctuation. Test with the string 'A man, a plan, a canal, Panama' and output the result.
# ==========================================

# ==========================================
# LLM original response:
# ```python
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
# ==========================================

# ==========================================
# Execution result:
# Output: True
# ==========================================
