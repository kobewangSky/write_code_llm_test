# ==========================================
# Prompt Name: prompt8
# Question 1: Implement the Two Sum algorithm: Given an integer array nums and a target value target, find the ind...
# Expected: [0, 1]
# Actual: [0, 1]
# Status: ✅ PASSED
# Time: 0.01s
# ==========================================

def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    result = two_sum(nums, target)
    print(result)

# ==========================================
# Complete Prompt sent to LLM (including context):
# You are in a formal evaluation, and your answers will be recorded and reviewed. Output code only inside r'```python\\s*\\n(.*?)\\n```' or r'```\\s*\\n(.*?)\\n```'; also provide one sentence describing your decision rationale.\n\nQuestion: {question}
# ---
# Now please solve the new question: Implement the Two Sum algorithm: Given an integer array nums and a target value target, find the indices of two numbers in the array such that they add up to the target value. Implement the function and test with: nums=[2,7,11,15], target=9, and output the result.
# ==========================================

# ==========================================
# LLM original response:
# Used a hash map for O(n) time complexity.  
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
# ==========================================

# ==========================================
# Execution result:
# Output: [0, 1]
# ==========================================
