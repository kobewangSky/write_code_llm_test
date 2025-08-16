# ==========================================
# Prompt Name: prompt4
# Question 2: Fix the indentation issues in the following code, then execute greet('World'):
```python
def greet(n...
# Expected: Hello, World!
Welcome to Python!
# Actual: Hello, World!
Welcome to Python!
# Status: ✅ PASSED
# Time: 0.02s
# ==========================================

def greet(name):
    print(f'Hello, {name}!')
    if name == 'World':
        print('Welcome to Python!')
    else:
        print('Nice to meet you!')

greet('World')

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
# ---
# Now please solve the new question: Fix the indentation issues in the following code, then execute greet('World'):
# ```python
# def greet(name):
# print(f'Hello, {name}!')
# if name == 'World':
# print('Welcome to Python!')
# else:
# print('Nice to meet you!')
# ```
# ==========================================

# ==========================================
# LLM original response:
# ```python
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
# ==========================================

# ==========================================
# Execution result:
# Output: Hello, World!
Welcome to Python!
# ==========================================
