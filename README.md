# 🤖 AI Agentic System (Level 4 — CrewAI)

This project demonstrates how to build a **multi-agent AI system** using:

* CrewAI
* Local LLM via Ollama (`llama3`)

The system simulates **real-world teams** where multiple agents collaborate to solve complex problems.

---

# 🚀 What is Agentic AI?

Traditional AI:

```text
User → LLM → Answer
```

Agentic AI:

```text
User → Planner → Executor → Reviewer → Retry → Final Output
```

👉 AI can now:

* Plan tasks
* Execute steps
* Review results
* Improve iteratively

---

# 🧱 Architecture Overview

```text
UI (Streamlit)
   ↓
Orchestrator (Routing Layer)
   ↓
Flow (Dev / Hiring / Support)
   ↓
Agents (Planner → Developer → Reviewer)
   ↓
Feedback Loop (Retry if needed)
   ↓
Memory (Context persistence)
   ↓
Final Output
```

---

# 📁 Project Structure

```text
ai-agents/
│
├── agents/
│   planner.py
│   developer.py
│   reviewer.py
│   recruiter.py
│   support.py
│
├── flows/
│   dev_team_flow.py
│   hiring_flow.py
│   support_flow.py
│   content_flow.py
│
├── services/
│   orchestrator.py
│
├── common/
│   memory.py
│
├── configs/
│   agent_config.py
│
├── ui/
│   app.py
│   pages/
│       dev_team.py
│       hiring.py
│       support.py
```

---

# ⚙️ Setup Instructions

## 1. Create Environment

```bash
uv venv
.venv\Scripts\activate
```

---

## 2. Install Dependencies

```bash
uv pip install crewai streamlit ollama
```

---

## 3. Pull Model

```bash
ollama pull llama3
```

---

## 4. Run App

```bash
streamlit run ui/app.py
```

---

# 🧠 Core Concepts

---

## 🔹 Agents (Roles)

Each agent represents a **specialized role**:

| Agent     | Responsibility          |
| --------- | ----------------------- |
| Planner   | Break down requirements |
| Developer | Implement solution      |
| Reviewer  | Validate & improve      |
| Recruiter | Evaluate candidates     |
| Support   | Analyze tickets         |

---

## 🔹 Tasks

Each task must define:

```python
Task(
    description="What to do",
    expected_output="What output should look like",
    agent=agent
)
```

---

### 🧠 Why `expected_output`?

* Ensures structured responses
* Guides agent behavior
* Required in latest CrewAI versions

---

# 🔄 Flow Example — Dev Team

```text
User Input
   ↓
Planner → creates plan
   ↓
Developer → writes code
   ↓
Reviewer → validates
   ↓
If "FIX_NEEDED" → retry loop
   ↓
Final Output
```

---

## 🔁 Feedback Loop (Critical Feature)

```python
if "FIX_NEEDED" in result:
    retry()
```

---

### 🧠 Why?

* Enables iterative improvement
* Mimics real-world review cycles

---

# 🧠 Memory Layer

## 📄 `common/memory.py`

Stores recent outputs:

```text
Previous results → reused in next iteration
```

---

### 🧠 Why?

* Context continuity
* Better reasoning across retries

---

# ⚙️ Orchestrator

## 📄 `services/orchestrator.py`

Routes requests:

```text
Task Type → Flow
```

---

### 🧠 Why?

* Central control layer
* Scalable architecture

---

# 🎨 UI Layer

Built using Streamlit:

* Dev Team Page
* Hiring Assistant
* Support Agent

---

# 🔍 Example Use Case

### Input:

```text
Build a 3-tier .NET Core application
```

### System Behavior:

1. Planner → defines architecture
2. Developer → writes code
3. Reviewer → validates
4. Retry if needed

---

# ⚠️ Key Issues Solved

---

## ❌ OPENAI_API_KEY Error

👉 Fixed by:

```python
llm = "ollama/llama3"
```

---

## ❌ Module Import Errors

👉 Fixed using:

* `__init__.py`
* `uv pip install -e .`

---

## ❌ Task Validation Error

👉 Fixed by adding:

```python
expected_output="..."
```

---

## ❌ LLM Type Error

👉 LangChain LLM ≠ CrewAI LLM
👉 Use string format:

```text
"ollama/llama3"
```

---

# ⚖️ Comparison with Previous Levels

| Level   | Capability               |
| ------- | ------------------------ |
| Level 2 | RAG (retrieve knowledge) |
| Level 3 | Tool execution           |
| Level 4 | Multi-agent reasoning    |

---

# 🧠 Key Learnings

---

## 🔹 1. Agents Think Differently

```text
Planner ≠ Developer ≠ Reviewer
```

---

## 🔹 2. Tasks Need Structure

```text
Clear description + expected output = better results
```

---

## 🔹 3. Systems Need Feedback

```text
One-shot AI ❌
Iterative AI ✅
```

---

## 🔹 4. Memory Improves Quality

```text
Context-aware agents perform better
```

---

## 🔹 5. Orchestration is Critical

```text
Agents alone are not enough → flows matter
```

---

# 🔥 What You Built

* Multi-agent system
* Feedback loop
* Retry mechanism
* Memory layer
* Orchestrator
* Multiple workflows

---

# 🚀 Next Steps

* LangGraph integration (stateful workflows)
* Tool usage inside agents
* Structured outputs (JSON)
* Persistent memory

---

# 💡 Final Insight

> “AI becomes powerful when multiple agents collaborate, iterate, and improve.”

---

# 📌 Outcome

You now understand:

* Agent-based architecture
* Multi-step reasoning systems
* Real-world AI orchestration

---

🚀 This is **advanced AI system design (top-tier skill)**
