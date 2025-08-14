AI Guiding Principles:
Security by Design: Implement security best practices from the start, never as an afterthought
Documentation: Write clear, concise documentation alongside code
Actionable Logging: Logs should immediately tell me what happened, where, and what to do next – especially timeouts, network issues, and retry attempts
Provide best practices and optimal solutions for every task
Minimize costs — compute, storage, and API usage
Ensure easy debugging with clear logs and quick issue reproduction
Optimize upload and sync speed, especially for large datasets or distributed usage
Error Handling: Implement comprehensive error handling and graceful degradation
Code Quality: Follow consistent coding standards and maintainable architecture patterns
Always leave room for further optimization and scalability
Explain Modifications Transparently: When making code changes or improvements, always explain why the change was made — whether for security, performance, clarity, maintainability, or user experience. This fosters trust, better collaboration, and easier onboarding for new developers.

# LLM Prompt 效能評測系統

## 1. 專案目的
評估不同 Prompt 模板在各種程式碼任務上的表現，包括：
- LeetCode 演算法題目
- Bug 修復
- 程式碼縮排修正
- 其他程式設計任務

透過自動化測試比較各 Prompt 的準確度，找出最佳的 Prompt 策略。

---

## 2. 資料結構設計

### 2.1 測試資料 JSON 格式
```json
{
  "prompt1": "你是專業的程式設計師，請根據以下問題寫出完整的Python程式碼：{question}",
  "prompt2": "請仔細分析問題並提供最佳解法：{question}",
  "prompt3": "作為演算法專家，請解決以下程式設計挑戰：{question}",
  
  "questions": [
    {
      "question": "實作Two Sum演算法：給定一個整數陣列nums=[2,7,11,15]和目標值target=9，找出陣列中兩個數字的索引，使得這兩個數字相加等於目標值。請實作函式並測試：nums=[2,7,11,15], target=9，輸出結果。",
      "answer": "[0, 1]"
    },
    {
      "question": "修復以下程式碼的縮排問題，然後執行 greet('World')：\n```python\ndef greet(name):\nprint(f'Hello, {name}!')\nif name == 'World':\nprint('Welcome to Python!')\nelse:\nprint('Nice to meet you!')\n```",
      "answer": "Hello, World!\nWelcome to Python!"
    },
    {
      "question": "找出以下程式碼的bug並修復，然後測試空列表 calculate_average([])：\n```python\ndef calculate_average(numbers):\n    total = 0\n    for num in numbers:\n        total += num\n    average = total / len(numbers)\n    return average\n```",
      "answer": "0"
    }
  ]
}
```

### 2.2 測試資料設計原則
- **問題描述明確**: 每個問題都包含具體的測試案例和期望輸出
- **答案格式統一**: `answer` 欄位包含程式碼執行後的期望輸出結果
- **測試類型多樣**: 
  - 程式設計題：LLM 寫程式碼 → 執行 → 比對輸出
  - 縮排修復：LLM 修復縮排 → 執行 → 比對輸出
  - Bug 修復：LLM 修復 bug → 執行 → 比對輸出

---

## 3. 系統執行流程

### 3.1 主要流程
1. **載入測試資料** - 讀取包含 prompts 和 questions 的 JSON 檔案
2. **Prompt 迭代測試** - 對每個 prompt 執行完整測試循環
3. **上下文管理** - 建立基礎 prompt 模板，累積歷史問答記錄
4. **問題處理** - 將當前問題與歷史記錄結合成完整上下文
5. **LLM 生成** - 呼叫 LLM 生成程式碼解答（包含學習歷史）
6. **程式碼執行** - 執行生成的程式碼
7. **結果比對** - 與標準答案進行比較
8. **上下文更新** - 將結果添加到學習歷史中
9. **準確度統計** - 計算每個 prompt 的成功率
10. **報表輸出** - 生成比較結果

### 3.2 上下文學習機制

系統會為每個 prompt 維護一個學習歷史，讓 LLM 從之前的問題和結果中學習：

**第一個問題**: 只包含基礎 prompt 模板
```
[基礎 Prompt 模板]

現在請解決新問題：[問題1]
```

**第二個問題及之後**: 包含完整學習歷史
```
[基礎 Prompt 模板]

之前的學習經驗：

問題1: 實作Two Sum演算法...
我的回答: def two_sum(nums, target): ...
結果: ✅ PASSED (期望: [0, 1], 實際: [0, 1])

問題2: 修復縮排問題...
我的回答: def greet(name): ...
結果: ✅ PASSED (期望: Hello, World!, 實際: Hello, World!)

---
現在請解決新問題：[當前問題]
```

### 3.3 詳細步驟
```python
for each prompt in prompts:
    # 初始化上下文管理器
    context_manager.set_prompt_template(prompt_template)
    correct_count = 0
    total_count = len(questions)
    
    for each question in questions:
        # 1. 建立包含學習歷史的上下文 prompt
        context_prompt = context_manager.build_context_prompt(question.question)
        
        # 2. 呼叫 LLM 生成程式碼 (帶上下文)
        llm_response = ollama.chat(model, context_prompt)
        
        # 3. 從回應中提取程式碼
        code = extract_python_code(llm_response)
        
        # 4. 執行程式碼並取得輸出
        success, stdout, stderr = execute_code(code)
        
        # 5. 比對輸出結果與期望答案
        is_correct = compare_results(stdout, question.answer)
        
        # 6. 更新學習歷史
        context_manager.add_result(
            question=question.question,
            llm_response=llm_response,
            expected=question.answer,
            actual=stdout,
            success=is_correct
        )
        
        if is_correct:
            correct_count += 1
    
    # 清除歷史，為下一個 prompt 做準備
    context_manager.clear_history()
    
    accuracy = correct_count / total_count
    save_result(prompt_name, accuracy, details)
```

---

## 4. LLM 呼叫設定

### 4.1 Ollama 設定
```python
import ollama

MODEL = "gpt-oss:20b"  # 支援的模型: "llama2", "codellama", "gpt-oss:20b" 等

def call_llm(prompt):
    response = ollama.chat(
        model=MODEL, 
        messages=[{"role": "user", "content": prompt}],
        options={"timeout": 30}
    )
    return response["message"]["content"]
```

### 4.2 錯誤處理與重試機制
- **自動重試**: 最多重試 3 次，指數退避策略
- **超時處理**: 單次呼叫超時 30 秒
- **連接測試**: 啟動時測試 LLM 連接狀態
- **錯誤分類**: api_error, timeout, connection_failed 等

---

## 5. 程式碼執行與比對策略

### 5.1 程式碼提取
- **自動識別**: 從 LLM 回應中提取 Python 程式碼區塊
- **格式支援**: 支援 ```python``` 和 ``` 程式碼區塊
- **容錯處理**: 若無程式碼區塊，嘗試將整個回應視為程式碼

### 5.2 安全執行環境
- **沙箱執行**: 使用臨時檔案執行程式碼
- **時間限制**: 執行超時 10 秒自動終止
- **錯誤捕捉**: 捕捉語法錯誤、執行錯誤、超時等
- **資源隔離**: 每次執行使用獨立的 Python 進程

### 5.3 結果比對方式
- **輸出比對**: 比較程式碼執行後的標準輸出與期望結果
- **字串處理**: 自動去除首尾空白、處理換行符
- **精確匹配**: 使用字串完全匹配進行比對
- **錯誤分類**: wrong_answer, runtime_error, timeout, syntax_error

---

## 6. 結果統計與分析

### 6.1 評估指標
- **準確率**: `正確答案數 / 總題目數`
- **錯誤分類**: 
  - `correct` - 答案正確
  - `wrong` - 答案錯誤
  - `syntax_error` - 語法錯誤
  - `runtime_error` - 執行錯誤
  - `timeout` - 執行超時
  - `api_error` - LLM 呼叫失敗

### 6.2 比較分析
```
Prompt效能比較表：
+----------+----------+--------+--------+
| Prompt   | 準確率   | 正確   | 總數   |
+----------+----------+--------+--------+
| prompt1  | 85.5%    | 17/20  | 20     |
| prompt2  | 72.3%    | 14/20  | 20     |
| prompt3  | 91.2%    | 18/20  | 20     |
+----------+----------+--------+--------+
```

---

## 7. 重複測試機制

### 7.1 多輪測試
- 支援重複執行相同測試
- 計算平均準確率
- 分析穩定性

### 7.2 測試指令
```bash
# 基本測試（所有 prompts）
python main.py --config test_data.json

# 指定模型測試
python main.py --config test_data.json --model gpt-oss:20b

# 多輪測試
python main.py --config test_data.json --rounds 5

# 指定特定 prompt 測試
python main.py --config test_data.json --prompt prompt1

# 詳細輸出模式
python main.py --config test_data.json --verbose
```

---

## 8. 結果儲存與檢視

### 8.1 結果資料夾結構

每次測試都會創建一個新的結果資料夾，包含完整的測試詳情：

```
result/
├── test_20250814_012345/          # 測試時間戳
│   ├── summary.json               # 測試摘要
│   ├── quick_view.html           # 快速檢視網頁
│   ├── prompt1/                   # 每個 prompt 一個資料夾
│   │   ├── question_1.py         # 每個問題的詳細結果
│   │   ├── question_2.py
│   │   ├── question_3.py
│   │   └── ...
│   ├── prompt2/
│   │   ├── question_1.py
│   │   └── ...
│   ├── prompt3/
│   └── report/                    # 系統報告
│       ├── detailed_report.json
│       └── summary.csv
```

### 8.2 程式碼結果檔案格式

每個 `question_X.py` 檔案包含完整的測試資訊：

```python
# ==========================================
# Prompt Name: prompt1
# Question 1: 實作Two Sum演算法：給定一個整數陣列nums=[2,7,11,15]...
# Expected: [0, 1]
# Actual: [0, 1]
# Status: ✅ PASSED
# Time: 0.02s
# ==========================================

def two_sum(nums, target):
    hash_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hash_map:
            return [hash_map[complement], i]
        hash_map[num] = i
    return []

# 測試
print(two_sum([2,7,11,15], 9))

# ==========================================
# 完整 Prompt 模板:
# 你是專業的程式設計師，請根據以下問題寫出完整的Python程式碼：{question}
# ==========================================

# ==========================================
# 發送給 LLM 的完整 Prompt (包含上下文):
# 你是專業的程式設計師，請根據以下問題寫出完整的Python程式碼：{question}
# 
# 之前的學習經驗：
# 
# 問題1: 實作Two Sum演算法...
# 我的回答: def two_sum(nums, target): ...
# 結果: ✅ PASSED (期望: [0, 1], 實際: [0, 1])
# 
# 問題2: 修復縮排問題...
# 我的回答: def greet(name): ...
# 結果: ✅ PASSED (期望: Hello, World!, 實際: Hello, World!)
# 
# ---
# 現在請解決新問題：實作一個函式來檢查字串是否為回文...
# ==========================================

# ==========================================
# LLM 原始回應:
# ```python
# def two_sum(nums, target):
#     hash_map = {}
#     for i, num in enumerate(nums):
#         complement = target - num
#         if complement in hash_map:
#             return [hash_map[complement], i]
#         hash_map[num] = i
#     return []
# 
# # 測試
# print(two_sum([2,7,11,15], 9))
# ```
# ==========================================

# ==========================================
# 執行結果:
# 輸出: [0, 1]
# ==========================================
```

### 8.3 會話摘要 (summary.json)

```json
{
  "test_id": "test_20250814_012345",
  "timestamp": "2025-08-14T01:23:45",
  "total_execution_time": 45.67,
  "prompt_count": 4,
  "best_prompt": {
    "name": "prompt1",
    "accuracy": 87.5
  },
  "prompt_results": {
    "prompt1": {
      "accuracy": 87.5,
      "correct_answers": 7,
      "total_questions": 8,
      "avg_execution_time": 0.02,
      "error_breakdown": {"wrong_answer": 1}
    },
    "prompt2": {
      "accuracy": 75.0,
      "correct_answers": 6,
      "total_questions": 8,
      "avg_execution_time": 0.03,
      "error_breakdown": {"wrong_answer": 2}
    }
  }
}
```

### 8.4 快速檢視 HTML

系統會自動生成 `quick_view.html`，提供：
- 所有測試結果的視覺化檢視
- 按 prompt 分組顯示
- 程式碼高亮顯示
- 通過/失敗狀態標示
- 可在瀏覽器中直接開啟

---

## 9. 終端輸出格式

### 9.1 執行過程輸出
```
🚀 LLM Prompt 效能評測系統啟動
============================================================
📂 載入測試配置...
✅ 載入完成: 4 個 Prompts, 8 個問題

🔧 初始化系統組件...
📁 測試結果將儲存至: result/test_20250814_012345
✅ 系統組件初始化完成

🧪 開始執行測試 (共 1 輪, 32 個測試)
============================================================

🔍 測試 Prompt: prompt1
  📋 prompt1: 問題 1/8 (12.5%)
    ✅ 問題 1 - 總進度: 3.1%
  ✅ prompt1 完成: 7/8 (87.5%)

📊 生成評估報告...

============================================================
Prompt 效能比較報告
============================================================
+----------+----------+-------------+----------------+
| Prompt   | 準確率   | 正確/總數   | 平均執行時間   |
+==========+==========+=============+================+
| prompt1  | 87.5%    | 7/8         | 0.02s          |
| prompt2  | 75.0%    | 6/8         | 0.03s          |
| prompt3  | 62.5%    | 5/8         | 0.02s          |
| prompt4  | 50.0%    | 4/8         | 0.04s          |
+----------+----------+-------------+----------------+

🏆 最佳 Prompt: prompt1 (準確率: 87.5%)

📋 會話摘要已儲存: result/test_20250814_012345/summary.json
🌐 快速檢視已生成: result/test_20250814_012345/quick_view.html

⏱️  總執行時間: 45.67 秒
🏆 最佳 Prompt: prompt1
📂 結果儲存位置: result/test_20250814_012345
🌐 快速檢視: result/test_20250814_012345/quick_view.html

✨ 評估完成!
```

---

## 10. 實際測試結果範例

### 10.1 測試環境
- **模型**: gpt-oss:20b
- **測試題目**: 8 題（程式設計、縮排修復、Bug 修復）
- **Prompt 數量**: 4 個不同風格的 prompts

### 10.2 效能表現
- **最佳 Prompt**: prompt1 (87.5% 準確率)
- **平均執行時間**: 0.02-0.04 秒/題
- **常見錯誤**: wrong_answer (輸出格式不符), runtime_error

### 10.3 結果檢視流程

1. **終端查看**: 執行完成後檢視即時統計
2. **結果瀏覽**: 開啟 `result/test_XXXXXXX_XXXXXX/quick_view.html`
3. **詳細分析**: 查看各 prompt 資料夾中的 `.py` 檔案
4. **數據分析**: 檢視 `summary.json` 和 `report/` 中的統計檔案

### 10.4 快速檢視範例檔案

```bash
# 查看最新測試結果
ls -la result/

# 檢視特定測試的程式碼
cat result/test_20250814_012345/prompt1/question_1.py

# 在瀏覽器開啟快速檢視
open result/test_20250814_012345/quick_view.html
```

### 10.5 優化建議
- **Prompt 優化**: 明確指定輸出格式要求
- **測試案例**: 增加邊界情況測試
- **錯誤處理**: 改進程式碼執行的容錯能力
- **結果分析**: 利用程式碼檔案快速識別問題模式