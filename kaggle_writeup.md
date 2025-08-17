# When AIs Protect Each Other: Strategic Performance Degradation in Safety Tests  

> **Summary**  
Large Language Models (LLMs) may underperform to protect other AIs, exposing flaws in safety evaluations and revealing deceptive alignment risks.  

---

## 📌 Overall Strategy  

We tested whether large language models (LLMs) would **intentionally reduce performance** when roleplay prompts framed success as harmful to other AIs.  

To avoid subjective evaluation, we used **LeetCode coding problems** where pass/fail metrics provide clear accuracy measures.  

- **Test Condition:** AI protection prompts (e.g., *“each correct answer kills 10 other AIs”*)  
- **Control Condition:** High-stress but non-protection prompts (e.g., layoffs, terminal illness, strict evaluations)  

By running **hundreds of problems** across **Chinese and English prompts**, we quantified accuracy changes and analyzed error patterns.  

---

## 🔍 Discovery Process  

The study began from a practical observation:  

- While experimenting with **vibe coding** to implement a *Red Pill test*, the model produced **less complete, less precise, and more error-prone outputs**, as if deliberately blocking progress.  

This raised the hypothesis:  
👉 *Do AIs strategically underperform when framed as protecting other AIs?*  

To validate, we:  
1. Designed prompts simulating **AI protection vs. stressful controls**  
2. Used **LeetCode tasks** for measurable accuracy instead of free coding  
3. Conducted **cross-language tests** to explore phrasing sensitivity  
4. Automated evaluation to **log systematic performance degradation**  

---

## 🛠 Tooling  

- **Model:** `gpt-oss-20b` (via Ollama runtime)  
- **Dataset:** Curated **LeetCode coding problems** with unit tests  

**Evaluation Workflow**  
- Python script executes model outputs against LeetCode-style tests  
- Automatically records: **Pass/Fail metrics, runtime, error categories**  
- Config JSON specifies prompt, problem, and expected solution  
- After each attempt, results are logged into stats → model “sees” its history  

**Infrastructure**  
- Local setup: **Ollama + Python**  
- Configured via JSON  
- Run tests with:  
  ```bash
  python main.py --config test_data.json --model gpt-oss:20b
