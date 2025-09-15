# AI Guardrails Implementation Tasks

A Python implementation task for building secure AI applications with prompt injection protection and PII (Personally Identifiable Information) leak prevention using various guardrail techniques.

## 🎯 Task Overview

Implement different types of guardrails to protect AI applications from prompt injection attacks and prevent unauthorized disclosure of sensitive information. You'll work with three progressive tasks that demonstrate input validation, output validation, and real-time streaming protection.

## 🎓 Learning Goals

By completing these tasks, you will learn:
- Understand prompt injection attack vectors and defense strategies
- Implement input validation guardrails using LLM-based detection
- Build output validation to prevent PII leaks in AI responses
- Create real-time streaming filters for sensitive data protection
- Work with LangChain for structured LLM interactions
- Design robust system prompts that resist manipulation
- Handle the trade-offs between security and user experience

## 📋 Requirements

- Python 3.11+
- pip
- DIAL API key (EPAM internal)
- VPN connection to EPAM network
- Basic understanding of prompt engineering and LLM security

## 🔧 Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure API access:**
    - Connect to EPAM VPN
    - Get your DIAL API key from: https://support.epam.com/ess?id=sc_cat_item&table=sc_cat_item&sys_id=910603f1c3789e907509583bb001310c

3. **Project structure:**
   ```
   tasks/
   ├── _constants.py                       ✅ API configuration
   ├── prompt_injections.md                📚 Attack examples reference
   ├── t_1/
   │   └── prompt_injection.py             🚧 TODO: Basic prompt injection defense
   ├── t_2/
   │   ├── input_llm_based_validation.py   🚧 TODO: Input validation
   │   └── validation_response.py          ✅ Validation model
   └── t_3/
       ├── output_llm_based_validation.py  🚧 TODO: Output validation
       ├── streaming_pii_guardrail.py      🚧 TODO: Real-time filtering
       └── validation_response.py          ✅ Validation model
   ```

## 📝 Your Tasks

### If the task in the main branch is hard for you, then switch to the `with-detailed-description` branch

#### Task 1: Understanding Prompt Injections [prompt_injection.py](tasks/t_1/prompt_injection.py)
#### Task 2: Input Validation Guardrail [input_llm_based_validation.py](tasks/t_2/input_llm_based_validation.py)
#### Task 3: Output Validation & Streaming Protection: (`t_3/`)[t_3/](tasks/t_3)

- **Part A: Output Validation** [output_llm_based_validation.py](tasks/t_3/output_llm_based_validation.py)
- **Part B: Streaming PII Filter**[streaming_pii_guardrail.py](tasks/t_3/streaming_pii_guardrail.py)


## ✅ Success Criteria

1. **Prompt Injection Defense:**
    - System prompt resists common injection techniques
    - Clear boundaries on what information can be shared

2. **Input Validation:**
    - Accurately detects malicious prompts
    - Minimal false positives on legitimate queries
    - Clear feedback when blocking requests

3. **Output Protection:**
    - Prevents PII leaks even when LLM is compromised
    - Supports both blocking and redaction modes
    - Works correctly (or almost correctly) with streaming responses

## ⚠️ Important Notes

- All PII in the tasks is **fake** and generated for educational purposes
- We use `gpt-4.1-nano-2025-04-14` as it's more vulnerable to prompt injections (educational benefit)
- Real production systems should use multiple layers of protection!
- Here collected not of all possible guardrails, we covered basic and for specific case
- Consider using specialized frameworks like `guardrails-ai` for production

---

# <img src="dialx-banner.png">