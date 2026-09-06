<p align="center">
  <img src="assets/banner.svg" alt="Naveen Kumar — AI / LLM Engineer, agentic systems and automotive embedded software" width="100%">
</p>

# Naveen Kumar

**AI / LLM Engineer · Agentic AI · Automotive Embedded Software · Germany**

I build AI agents that use tools, retain context, and ask for approval before operational changes. My independent AI work began in **June 2025**, building on **11+ years in automotive embedded engineering** across Germany, India, and South Korea: Embedded C, CAN, AUTOSAR, ECU bootloaders, diagnostics, and secure flashing.

[LinkedIn](https://www.linkedin.com/in/naveen-kumar-73423420/) · [Email](mailto:naveen6gowda@gmail.com) · [Experience & credentials](career/README.md) · [All project areas](#explore-the-portfolio)

## Selected work

### 01 / HomelabSentinel — an agent for infrastructure operations

**Independent project · June 2025–Present**

A Python / LangGraph assistant for Proxmox, Docker, and Home Assistant, accessible through Telegram, Alexa, and a CLI. I built the agent graph, shared tool registry, approval flow, MCP interface, monitoring integrations, and evaluation harness.

- **Human control:** default-deny approval for destructive operations, interrupt/resume, and SQLite checkpoints.
- **Shared interfaces:** 29 tools in one registry; an MCP server with bearer authentication and server-side approval enforcement.
- **Engineering evidence:** 12 golden evaluation scenarios, 40+ pytest tests, and GitHub Actions for tests. Live model evaluations run locally and record a known quantization-related tool-ordering failure.
- **Operational context:** BM25 runbook retrieval, self-hosted Langfuse tracing, model fallback handling, and deterministic monitor fallbacks.

[Read the case study →](ai/Agent_AI/README.md) · [Browse the source →](https://github.com/naveen6gowda/AI-Agent/tree/main/Agent_AI) · [Inspect tests →](https://github.com/naveen6gowda/AI-Agent/tree/main/Agent_AI/tests)

### 02 / Qwen adaptation — training within a 24 GB memory budget

**Independent experiment · Apple Silicon · MLX / MLX-LM**

Prepared 1,600 English/German instruction pairs covering 20 infrastructure topics. Compared a Qwen3.5-9B LoRA run on a 4-bit base with selected-layer weight updates on Qwen3.5-2B, then fused the 9B adapter for LM Studio serving. The write-up records the split, hyperparameters, evaluation approach, and limits of the public evidence.

[Read the experiment →](ai/finetuning/README.md)

### 03 / Embedded devices — sensors, displays, and voice interfaces

**Personal projects · ESP32-C3 / C6 / S3 · ESPHome**

Nine published configurations cover a battery-powered mailbox sensor, plant monitoring, room displays, presence sensing, an e-paper dashboard, and a touch/voice assistant. The work combines deep sleep, MQTT, I²C, SPI, UART, I²S audio, and Home Assistant integration.

[Explore the firmware →](esphome/README.md) · [Read the PCB design notes →](pcb/README.md)

## Explore the portfolio

| Area | What you can inspect |
|---|---|
| [Agentic AI](ai/Agent_AI/README.md) | Sentinel architecture, approval design, retrieval, evaluation, and links to the implementation |
| [LLM fine-tuning](ai/finetuning/README.md) | Two training configurations and a private-data experiment write-up |
| [AI fundamentals](ai/README.md) | 12 Python examples covering APIs, Pydantic, tool calling, LCEL, and LangGraph |
| [Embedded firmware](esphome/README.md) | Nine sanitized ESPHome configurations and hardware-specific setup notes |
| [Homelab infrastructure](homelab/infrastructure.md) | Proxmox, OPNsense, VLANs, Tailscale, and the evolution of local inference |
| [Docker services](docker/README.md) | A 24-service Compose reference for automation, storage, media, and observability |
| [PCB design](pcb/README.md) | KiCad work on a CM5 carrier adaptation and an ESP32-C6 relay board; design notes only |

## Skills grounded in this work

| Focus | Technologies and practices |
|---|---|
| **AI agents & applications** | Python, LangGraph, LangChain, MCP, RAG / BM25, prompt engineering, tool calling, structured outputs, Pydantic, FastAPI, human approval, LLM evaluation, Langfuse |
| **Models & serving** | Qwen, LoRA / QLoRA, MLX, MLX-LM, LM Studio, llama.cpp, Ollama, OpenAI-compatible APIs |
| **Automotive embedded** | **Embedded C, CAN protocol**, AUTOSAR Classic SWCs and RTE, MISRA C, ECU flashbootloaders, UDS diagnostics, DTC handling, secure boot, authenticated downloads, key management |
| **Debugging & delivery** | Lauterbach Trace32, CANoe, DaVinci Configurator Pro, root-cause analysis, V-Model, ASPICE-aligned documentation, requirements, verification and validation, Git, pytest, GitHub Actions, Jira, Confluence |
| **Infrastructure & electronics** | C++, Bash, Linux, Docker, Proxmox, OPNsense, VLANs, Tailscale, n8n, MQTT, Home Assistant, ESP32, ESPHome, KiCad, I²C, SPI, UART, I²S |

## Automotive experience

| Period | Employer / assignment | Focus |
|---|---|---|
| Jun 2024–Jun 2025 | **EP Group**, Karlsruhe; client assignment in **Stuttgart** | Issue management and embedded software support for Daimler |
| Nov 2022–May 2024 | **MSK GmbH**, deputed to **Vector Informatik** | Senior Technical Lead; 35+ customer-reported defects, secure-flashing debug, root-cause analysis |
| Apr 2017–Oct 2022 | **LG Soft India**, including South Korea assignment | CAN flashbootloader development, ECU programming, OTA, UDS and secure boot |
| Jun 2014–Apr 2017 | **HCL** | Lead Engineer; AUTOSAR SWCs, RTE and diagnostic fault handling |
| Jun 2012–Jun 2014 | **L&T** | Automotive CAN communication stack development |
| Mar 2011–Jun 2012 | **Elegance Technologies** | Embedded C and I²C / SPI driver development |

**Education:** B.E., Electronics and Communication Engineering — Visvesvaraya Technological University, 2005–2010.

**Training:** AWS Cloud Practitioner Essentials course completion; Hugging Face AI Agents Fundamentals; TÜV SÜD functional safety and automotive cybersecurity programs. [Full credentials and career detail →](career/README.md)

**Languages:** English (C2), German (A2, improving), Kannada (native).

## Get in touch

I’m interested in AI / LLM engineering and embedded-AI roles where software reliability, practical integrations, and careful validation matter.

[Connect on LinkedIn](https://www.linkedin.com/in/naveen-kumar-73423420/) · [naveen6gowda@gmail.com](mailto:naveen6gowda@gmail.com)

<sub>Portfolio reviewed September 2026. AI projects are independent work; automotive roles are commercial employment. Project counts describe the linked public snapshot, not live service uptime.</sub>
