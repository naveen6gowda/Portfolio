# AI / LLM Application Development

> **LangChain · LangGraph · Anthropic SDK · Pydantic · AI Agents · Tool Use · Structured Output · Local LLM Inference (LM Studio / OpenAI-compatible)**

Hands-on Python work on **LLM application development** — from the simplest "prompt → LLM → output" chain to a **graph-based, tool-using SRE agent** that operates my homelab.

This is the layer above local inference: chains, structured output, tool use, and the graph-based control flow that real agents need. The local-inference platform has been through three generations — Ollama, llama.cpp, and today **LM Studio** serving one model to every agent through an OpenAI-compatible API. The first-generation setup is documented in [`ollama-lxc-setup.md`](./ollama-lxc-setup.md).

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
| LLM provider (examples) | **Anthropic** (`claude-sonnet-4-6`) via `anthropic` SDK and `langchain-anthropic` — the teaching examples in this folder |
| LLM provider (production) | **100% local** — one model served by **LM Studio** (OpenAI-compatible, bearer-token auth) powers HomelabSentinel and every helper. See [`AI-Agent` ↗](https://github.com/naveen6gowda/AI-Agent). |
| App framework | **LangChain** (chains, structured output, LCEL) + **LangGraph** (stateful agents) |
| Observability | **Langfuse** (self-hosted) — agent runs, tool calls, token accounting |
| Validation | **Pydantic v2** (typed structured output, schema-constrained generation) |
| Config | `python-dotenv` (API key via `.env`, never committed) |
| Data / analytics | `requests` · `pandas` · `matplotlib` |
| Local inference history | Gen 1: **Ollama** on a Proxmox LXC (iGPU) — see [`ollama-lxc-setup.md`](./ollama-lxc-setup.md). Gen 2: **llama.cpp** (Vulkan). Gen 3 (current): **LM Studio** on an Apple-silicon node serving **Qwen3.6-35B (MoE)**. |
| Local agent stack | **Hermes Agent** (web dashboard · Telegram · sandboxed Python · cron) — now running on the same local model as Sentinel. |
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
| [`get_data.py`](./get_data.py) | Pulls a week of Munich weather data from the **Open-Meteo API**, loads it into a pandas DataFrame, and writes a clean CSV (`data/Munich_weather.csv`). Used as the data source for downstream charting / analysis. |
| [`hello.py`](./hello.py) · [`IPL.py`](./IPL.py) | Small Python warm-up scripts |

### 🛰️ `Agent_AI/` — HomelabSentinel (flagship)

What began as a raw, framework-free tool-loop here grew into **HomelabSentinel**,
a production agentic-AI SRE that now runs my homelab 24/7. The complete project —
a five-step agent course (`agent_v1` raw loop → `agent_v5` with a human-approval
gate, archived in `legacy/`), **100% local single-LLM design** (LM Studio,
OpenAI-compatible, runtime `/model` switching), self-hosted **Langfuse** tracing,
a Telegram bot, an Alexa voice bridge, BM25 RAG, a commute guard, a finance
bridge into Firefly III, and **8 scheduled monitors** with a failure-pager
reliability layer — lives in its own repository:

> ### → **[github.com/naveen6gowda/AI-Agent ↗](https://github.com/naveen6gowda/AI-Agent)**

See the **[showcase with architecture diagrams](./Agent_AI/README.md)** for the full tour.

**Highlights:**
- **Human-in-the-loop safety** — a LangGraph `interrupt()` gate pauses every destructive action for my approval (default-deny), backed by 8 layers of defense in depth.
- **100% local inference at €0** — one LM Studio-served model powers the agent loop and every helper; runtime `/model` switching with a probe-before-switch that refuses models the server can't run.
- **Observable** — every run, tool call, and token count traced in self-hosted **Langfuse**; traces never leave home.
- **Reliable by design** — `OnFailure=` Telegram pagers on every systemd unit, nightly checkpoint-DB retention, and deterministic fallbacks so monitors never go silent if the LLM is down.
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
#    https://github.com/naveen6gowda/AI-Agent
```

For local inference (no API key, fully offline), point any of these scripts at an **OpenAI-compatible local endpoint** via `ChatOpenAI(base_url=...)`. The current production target is an **LM Studio** server (this is exactly how HomelabSentinel runs); llama.cpp's `llama-server` and Ollama work the same way — the first-generation Ollama LXC is documented in [`ollama-lxc-setup.md`](./ollama-lxc-setup.md).

---

## Techniques covered

| Technique | Where to look |
|-----------|---------------|
| **LangChain LCEL chains** | [`LCEL.py`](./LCEL.py) |
| **Structured output with Pydantic** | [`structure_io.py`](./structure_io.py), [`structured.py`](./structured.py) |
| **Tool-use loop (raw Anthropic SDK)** | [`tools.py`](./tools.py) · [HomelabSentinel `agent_v1_raw.py` ↗](https://github.com/naveen6gowda/AI-Agent/blob/main/Agent_AI/agent_v1_raw.py) |
| **LangGraph — prebuilt ReAct agent** | [`Langraph_prebuilt.py`](./Langraph_prebuilt.py) |
| **LangGraph — hand-built `StateGraph`** | [`custom_langraph.py`](./custom_langraph.py) |
| **Production agent + human-approval gate** | [HomelabSentinel `agent_v5_approval.py` ↗](https://github.com/naveen6gowda/AI-Agent/blob/main/Agent_AI/agent_v5_approval.py) |
| **Real API integration in agent tools** | [`tools.py`](./tools.py) (Open-Meteo) · [HomelabSentinel `tools.py` ↗](https://github.com/naveen6gowda/AI-Agent/blob/main/Agent_AI/tools.py) (Proxmox / HA / Telegram) |
| **Data wrangling around LLM workflows** | [`get_data.py`](./get_data.py) |
| **Local LLM inference / infrastructure** | [`ollama-lxc-setup.md`](./ollama-lxc-setup.md) |
| **Python packaging (PEP 621 / `uv`)** | [HomelabSentinel `pyproject.toml` ↗](https://github.com/naveen6gowda/AI-Agent/blob/main/Agent_AI/pyproject.toml) |
| **Secret hygiene** | `.env` + `.gitignore`, no API keys in code |

---

## Status — shipped & running

What used to be "roadmap" is now in production in [`AI-Agent`](https://github.com/naveen6gowda/AI-Agent):

- ✅ **Real Proxmox + HA + Portainer integration** (no more stubs), with read-before-write enforced.
- ✅ **Long-lived services** — a Telegram bot **and** an Alexa voice bridge (FastAPI), under `systemd`, each with an `OnFailure=` failure pager.
- ✅ **Observability** — self-hosted **Langfuse** tracing (replacing the earlier LangSmith setup) plus a token-usage audit log.
- ✅ **100% local inference** — the whole system runs on one LM Studio-served model; no cloud API in the loop.
- ✅ **Durable memory** — per-chat conversation state via a LangGraph SQLite checkpointer, with nightly retention.
- ✅ **Human-in-the-loop approval gate** — the safety feature the stubbed v1 only hinted at.

Next per the [architecture roadmap ↗](https://github.com/naveen6gowda/AI-Agent/blob/main/Agent_AI/docs/ARCHITECTURE.md):
one tool registry, a `sentinel-mcp` MCP server, and a scripted evaluation
harness for the agent's decisions.

---

*All code here was written, run, and debugged on my own infrastructure. I use
AI pair-programming tools in the daily loop — the architecture, the decisions,
and the homelab integration are mine.*
