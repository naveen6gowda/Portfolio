# AI / LLM Application Development

> **LangChain · LangGraph · Anthropic SDK · Pydantic · AI Agents · Tool Use · Structured Output · Local LLM Inference (Ollama)**

Hands-on Python work on **LLM application development** — from the simplest "prompt → LLM → output" chain to a **graph-based, tool-using SRE agent** that operates my homelab.

This is the layer above local inference: chains, structured output, tool use, and the graph-based control flow that real agents need. The infrastructure these run on (Proxmox + Ollama with iGPU passthrough) is documented in [`ollama-lxc-setup.md`](./ollama-lxc-setup.md).

---

## What's in here

- **A working multi-turn tool-using agent** running against my own homelab (Proxmox, Home Assistant, Telegram) — not a toy chatbot.
- **Both halves of LangGraph** — the prebuilt `create_react_agent` shortcut **and** a hand-built `StateGraph` with `ToolNode` + `tools_condition`, so the abstraction isn't a black box.
- **Both halves of tool use** — LangChain's `@tool` decorator **and** the raw Anthropic Messages API tool loop with `tool_use` / `tool_result` blocks.
- **Typed, validated LLM output** with Pydantic — including range/enum constraints — instead of brittle string parsing.

Each file is a self-contained, runnable example.

---

## Stack

| Layer | Choice |
|-------|--------|
| LLM provider | **Anthropic** (`claude-sonnet-4-6`) via `anthropic` SDK and `langchain-anthropic` |
| App framework | **LangChain** (chains, structured output, LCEL) + **LangGraph** (stateful agents) |
| Validation | **Pydantic v2** (typed structured output, schema-constrained generation) |
| Config | `python-dotenv` (API key via `.env`, never committed) |
| Data / analytics | `requests` · `pandas` · `matplotlib` |
| Local inference target | **llama.cpp** (Vulkan) on Proxmox LXC with iGPU passthrough — current setup. Earlier: **Ollama** on the same LXC. See [`ollama-lxc-setup.md`](./ollama-lxc-setup.md). |
| Local agent stack | **Hermes Agent** v0.13.0 on top of llama.cpp (model: **GPT-5.5**). Earlier: **OpenClaw** on Ollama, migrated via `hermes claw migrate`. |
| Day-to-day coding agent | **OpenAI Codex** (GPT-5.5) — used as the AI coding pair-programmer for this repo and the Hermes work. |
| Packaging (Agent_AI) | `pyproject.toml` (PEP 621), `uv`-compatible |

---

## Contents

### Building blocks — single concepts, runnable in isolation

| File | What it teaches | Concepts |
|------|-----------------|----------|
| [`basic.py`](./basic.py) | The minimum viable LLM call | Provider SDK, system + user messages |
| [`LCEL.py`](./LCEL.py) | LangChain Expression Language | `ChatPromptTemplate \| llm \| StrOutputParser` — composable chains |
| [`structured.py`](./structured.py) | Structured output (OpenAI SDK style) | Pydantic schema → typed `parsed` response |
| [`structure_io.py`](./structure_io.py) | Structured output via LangChain + Anthropic | `llm.with_structured_output(MovieReview)`, ranged ints, enums |
| [`pydantic_learn.py`](./pydantic_learn.py) | Pydantic fundamentals | `BaseModel`, validators, `Field` constraints |
| [`tools.py`](./tools.py) | Anthropic SDK **raw** tool-use loop | `tool_use` / `tool_result` blocks, multi-turn loop, real Open-Meteo API call |
| [`tool_uses.py`](./tool_uses.py) | Compact tool-use reference | The same pattern, distilled |

### LangGraph — stateful, graph-based agents

| File | What it teaches |
|------|-----------------|
| [`Langraph_prebuilt.py`](./Langraph_prebuilt.py) | `langgraph.prebuilt.create_react_agent` — the **fast path** to a ReAct agent with two `@tool`s (`get_weather`, `homelab_status`). Demonstrates `agent.invoke({"messages": [...]})` and `pretty_print()`. |
| [`custom_langraph.py`](./custom_langraph.py) | The **same agent, hand-built**: a typed `AgentState` with `add_messages` reducer, a `StateGraph` with `agent` and `tools` nodes, conditional routing via `tools_condition`, and the agent ↔ tools loop wired explicitly. This is what `create_react_agent` is doing internally — knowing both lets me debug real agent graphs, not just call a helper. |

### Data + analytics — practical Python for AI work

| File | What it does |
|------|--------------|
| [`get_data.py`](./get_data.py) | Pulls a week of weather data from the **Open-Meteo API**, loads it into a pandas DataFrame, and writes a clean CSV (`data/Erdweg_weather.csv`). Used as the data source for downstream charting / analysis. |
| [`hello.py`](./hello.py) · [`IPL.py`](./IPL.py) | Small Python warm-up scripts |

### 🛰️ `Agent_AI/` — HomelabSentinel (flagship)

What began as a raw, framework-free tool-loop here grew into **HomelabSentinel**,
a production agentic-AI SRE that now runs my homelab 24/7. The complete project —
a five-step agent course (`agent_v1` raw loop → `agent_v5` with a human-approval
gate), two-brain (Claude + local Gemma) cost design, a Telegram bot, an Alexa
voice bridge, BM25 RAG, and five scheduled monitors — lives in its own repository:

> ### → **[github.com/naveen6gowda/python-for-ai ↗](https://github.com/naveen6gowda/python-for-ai)**

See the **[showcase with architecture diagrams](./Agent_AI/README.md)** for the full tour.

**Highlights:**
- **Human-in-the-loop safety** — a LangGraph `interrupt()` gate pauses every destructive action for my approval (default-deny), backed by 8 layers of defense in depth.
- **Cost-aware multi-model routing** — cloud Claude reasons, local Gemma summarizes; the scheduled monitors and ~95% of voice commands cost **$0** and run offline.
- **Durable** — a SQLite checkpointer survives a process restart *mid-approval*.
- **Real integrations, not stubs** — live Proxmox API, Home Assistant, and Portainer, with the QEMU page-cache memory trap handled correctly before any restart.

---

## Running the examples

```bash
# 1. Install dependencies (root-level scripts)
pip install -r requirements.txt

# 2. Create a .env file with your Anthropic API key
echo "CLAUDE_API_KEY=sk-ant-..." > .env

# 3. Run any example
python LCEL.py
python structure_io.py
python tools.py
python Langraph_prebuilt.py
python custom_langraph.py

# 4. The full homelab agent (HomelabSentinel) lives in its own repo:
#    https://github.com/naveen6gowda/python-for-ai
```

For local inference (no API key, fully offline), point any of these scripts at the **inference LXC** described in [`ollama-lxc-setup.md`](./ollama-lxc-setup.md). Current target is **llama.cpp's `llama-server`** on `:8080`; the earlier **Ollama** endpoint on `:11434` still works the same way. `claude-sonnet-4-6` can be swapped for `qwen2.5:3b` / `llama3.2:3b` via `ChatOllama`, or for any local GGUF by pointing `ChatOpenAI(base_url=...)` at the llama-server endpoint.

---

## Techniques covered

| Technique | Where to look |
|-----------|---------------|
| **LangChain LCEL chains** | [`LCEL.py`](./LCEL.py) |
| **Structured output with Pydantic** | [`structure_io.py`](./structure_io.py), [`structured.py`](./structured.py) |
| **Tool-use loop (raw Anthropic SDK)** | [`tools.py`](./tools.py) · [HomelabSentinel `agent_v1_raw.py` ↗](https://github.com/naveen6gowda/python-for-ai/blob/main/Agent_AI/agent_v1_raw.py) |
| **LangGraph — prebuilt ReAct agent** | [`Langraph_prebuilt.py`](./Langraph_prebuilt.py) |
| **LangGraph — hand-built `StateGraph`** | [`custom_langraph.py`](./custom_langraph.py) |
| **Production agent + human-approval gate** | [HomelabSentinel `agent_v5_approval.py` ↗](https://github.com/naveen6gowda/python-for-ai/blob/main/Agent_AI/agent_v5_approval.py) |
| **Real API integration in agent tools** | [`tools.py`](./tools.py) (Open-Meteo) · [HomelabSentinel `tools.py` ↗](https://github.com/naveen6gowda/python-for-ai/blob/main/Agent_AI/tools.py) (Proxmox / HA / Telegram) |
| **Data wrangling around LLM workflows** | [`get_data.py`](./get_data.py) |
| **Local LLM inference / infrastructure** | [`ollama-lxc-setup.md`](./ollama-lxc-setup.md) |
| **Python packaging (PEP 621 / `uv`)** | [HomelabSentinel `pyproject.toml` ↗](https://github.com/naveen6gowda/python-for-ai/blob/main/Agent_AI/pyproject.toml) |
| **Secret hygiene** | `.env` + `.gitignore`, no API keys in code |

---

## Status — shipped & running

What used to be "roadmap" is now in production in [`python-for-ai`](https://github.com/naveen6gowda/python-for-ai):

- ✅ **Real Proxmox + HA + Portainer integration** (no more stubs), with read-before-write enforced.
- ✅ **Long-lived services** — a Telegram bot **and** an Alexa voice bridge (FastAPI), under `systemd`.
- ✅ **Observability** — LangSmith tracing (v4) plus a homemade token-usage audit log (v5).
- ✅ **Durable memory** — per-chat conversation state via a LangGraph SQLite checkpointer.
- ✅ **Human-in-the-loop approval gate** — the safety feature the stubbed v1 only hinted at.

Still exploring: long-term entity memory on Postgres + pgvector, and a scripted
evaluation harness for the agent's decisions.

---

*All code here was written, run, and debugged on my own infrastructure. AI pair-programming is done with **OpenAI Codex (GPT-5.5)** as the coding agent — the architecture, the decisions, and the homelab integration are mine.*
