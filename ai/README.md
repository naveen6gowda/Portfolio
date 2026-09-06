[← Portfolio](../README.md)

# AI engineering: foundations to an operational agent

This folder combines short learning examples with links to my larger independent AI projects. The examples demonstrate APIs and framework concepts; HomelabSentinel has the infrastructure integrations, approval controls, and tests described in its own repository.

## Start with the project evidence

| Project | What it demonstrates |
|---|---|
| [HomelabSentinel](Agent_AI/README.md) | LangGraph, MCP, human approval, retrieval, tracing, local evaluations, and automated tests |
| [Qwen adaptation](finetuning/README.md) | Domain data preparation, LoRA on a quantized base, selected-layer training, MLX, and serving |
| [Local inference history](ollama-lxc-setup.md) | Ollama → llama.cpp with Vulkan → LM Studio; resource and deployment tradeoffs |

## Python example index

| File | Concept | External requirements |
|---|---|---|
| [basic.py](basic.py) | OpenAI chat completion | OpenAI API key and model access |
| [structured.py](structured.py) | Typed calendar-event extraction with Pydantic | OpenAI API key and model access |
| [pydantic_learn.py](pydantic_learn.py) | Field constraints and validation errors | None; runs offline |
| [LCEL.py](LCEL.py) | Prompt → model → string parser | Anthropic API access |
| [structure_io.py](structure_io.py) | Structured movie-review output | Anthropic API access |
| [tools.py](tools.py) | Raw Anthropic tool-call / result cycle | Anthropic API access and Open-Meteo; historical model identifier |
| [tool_uses.py](tool_uses.py) | LangChain tool schemas and binding | Anthropic API access; weather and service results are stubs |
| [Langraph_prebuilt.py](Langraph_prebuilt.py) | Prebuilt agent loop | Anthropic API access; stub tools |
| [custom_langraph.py](custom_langraph.py) | Explicit StateGraph and tool routing | Anthropic API access; stub tools |
| [hello.py](hello.py) | HTTP weather API request | Open-Meteo network access |
| [get_data.py](get_data.py) | Weather data → pandas → CSV | Open-Meteo network access; writes `data/Munich_weather.csv` |
| [IPL.py](IPL.py) | Prompt-template exercise about population | Anthropic API access; generated answers are not verified statistics |

## Run an example

From the repository root, create an isolated environment and install the recorded dependencies:

```bash
cd ai
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python pydantic_learn.py
```

The requirements file is a pinned environment snapshot. The offline Pydantic example is the simplest starting point; provider-backed examples also require credentials and access to the model named in the file.

For scripts that call `load_dotenv()`, copy [.env.example](.env.example) to `.env` and fill the relevant value locally. `basic.py` and `structured.py` read `OPENAI_API_KEY` from the process environment, so export that key in your shell. Never commit real credentials. Model identifiers in these learning scripts are snapshots and may need updating for your provider account.

The weather and homelab tools in `tool_uses.py`, `Langraph_prebuilt.py`, and `custom_langraph.py` return fixed sample values. For real infrastructure access, use [Sentinel's implementation and setup guide](https://github.com/naveen6gowda/AI-Agent/tree/main/Agent_AI).

Local OpenAI-compatible serving is another integration option, but it requires selecting a compatible client, model, and endpoint. Changing only a URL does not convert an Anthropic client into an OpenAI-compatible client.

## Learning progression

Typed output and tool calling led to explicit graph state, then tracing, human approval, persistent state, MCP access, and evaluation. The [Sentinel legacy folder](https://github.com/naveen6gowda/AI-Agent/tree/main/Agent_AI/legacy) preserves the earlier implementations; the [current agent](Agent_AI/README.md) documents the later design.
