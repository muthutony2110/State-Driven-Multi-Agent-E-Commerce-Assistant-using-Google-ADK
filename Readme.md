
# 🛒 Agentic E-Commerce Purchasing Assistant (Google ADK)

This project implements a **multi-agent, state-driven e-commerce purchasing system**
using the **Google Agent Development Kit (ADK)**.

The system is designed following **real-world ecommerce ordering flow** and
demonstrates how to build **deterministic, loop-safe agent workflows** using ADK.

---

## 🚀 Project Overview

The assistant behaves like a **Purchasing Agent** from the very first message.

It strictly follows this order:
1. Collect user details (Name → Email → Mobile)
2. Browse product catalog
3. Add item to cart
4. Collect shipping address
5. Generate final order summary

Each step is handled by a **dedicated agent**, and all agents communicate through
**shared session state**.

---

## 🧠 Agent Architecture

```

Root Purchasing Agent
↓
Catalog Agent
↓
Checkout Agent
↓
Order Summary Agent

```

### Agent Responsibilities

| Agent | Responsibility |
|-----|---------------|
| `ecommerce_agent` | User onboarding & intent routing |
| `catalog_agent` | Product browsing & cart handling |
| `checkout_agent` | Shipping address collection |
| `order_summary_agent` | Final order summary |

---

## 🧩 Tools & State Design

Each agent uses **explicit tools** that write to **SESSION STATE**.

To prevent infinite loops:
- Every tool sets a `*_saved = true` flag
- Every agent checks state before calling tools again

### Tools Used

| Tool | Purpose |
|----|--------|
| `save_user_info` | Stores user details |
| `save_cart` | Stores cart information |
| `save_shipping_address` | Stores shipping address |

This makes the system **loop-safe and deterministic**.

---

## 🤖 Model Choice (Important)

### ✅ Best Model for This Project
**Gemini (via Google ADK)** is the **best and recommended model** for this project.

Why Gemini is ideal:
- Built specifically for **ADK**
- Excellent **tool-calling discipline**
- Perfect **state awareness**
- No hallucinated tools
- Clean traces and stable output

👉 If you use **Gemini**, this project works **perfectly out-of-the-box**.

---

### ⚠️ Why Ollama Is Used Here

In this implementation, **Ollama + Qwen 2.5 Instruct** is used instead of Gemini.

**Reason:**
- Gemini API quota / credential limitations during local development

**Ollama is used as a local fallback**, not because it is better than Gemini.

To make Ollama work reliably:
- Strict instructions are used
- State-based stop conditions are enforced
- Streaming is disabled

This ensures stable behavior even with local models.

---

## 🧪 Recommended Local Model

```

qwen2.5:7b-instruct

````

Pulled via:
```bash
ollama pull qwen2.5:7b-instruct
````

---

## 📁 Project Structure

```
ADK_SHOPPING/
│
├── ecommerce_agent/
│   └── agent.py
│
├── catalog_agent/
│   └── agent.py
│
├── checkout_agent/
│   └── agent.py
│
├── order_summary_agent/
│   └── agent.py
│
├── .env
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate      # Linux / Mac
venv\Scripts\activate         # Windows
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Environment Configuration

Create a `.env` file:

```env
MODEL=ollama_chat/qwen2.5:7b-instruct
```

> If using Gemini, this model value can be replaced with a Gemini model
> and proper credentials.

---

### 4️⃣ Run ADK Web UI

```bash
adk web --no-stream
```

Access the UI:

```
http://127.0.0.1:8000
```

---

## 🧪 How the Flow Works (User Experience)

1. Assistant introduces itself as a **Purchasing Agent**
2. Collects user details step-by-step
3. Displays product catalog
4. Adds item to cart
5. Collects shipping address
6. Shows final order summary

Every step is **explicit**, **user-visible**, and **state-controlled**.

---

## 🔒 Design Principles

* State-driven logic
* One-time tool execution
* No silent agent transfers
* No hallucinated tools
* Production-style agent separation

---

## 📌 Notes

* Streaming is disabled for stability
* Designed for **local development**
* Easily extensible:

  * Payment agent
  * Tracking agent
  * Multi-item cart
  * Gemini cloud deployment

---


## 👤 Author
**Muthuraj M**  
AI & Machine Learning Engineer | Data Analyst  

📧 Email: maruthumuthu04@gmail.com  
🔗 GitHub: https://github.com/muthutony2110  

---

## 📄 License

This project is intended for learning, experimentation, and demonstration
of agentic AI systems using Google ADK.

---


