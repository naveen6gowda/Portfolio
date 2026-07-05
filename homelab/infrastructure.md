# Homelab Infrastructure

## Overview

A production home network built on enterprise-grade open-source tools, running 24/7 on a mini-PC.

## Hardware

| Component | Details |
|-----------|---------|
| Host machine | x86 mini-PC, 4-core CPU, 16GB RAM, SSD |
| Hypervisor | Proxmox VE (bare metal) |
| Router/Firewall | OPNsense (separate device) |
| IoT devices | 9× ESP32 nodes (various models) |

## Proxmox Virtual Machines & Containers

### Home Assistant OS (HAOS) VM

- **Network:** VLAN-segmented HA subnet (static IP)
- **Purpose:** Central home automation hub
- **Add-ons running:**
  - ESPHome — manages all ESP32 firmware OTA
  - MQTT Broker (Mosquitto)
  - Advanced SSH & Web Terminal
- **Integrations:** 50+ entities from ESP32 sensors, relay switches, weather

### Agent LXCs (Agentic AI platforms)

- **Sentinel LXC** (unprivileged) — runs **HomelabSentinel**, the LangGraph SRE
  agent with its Telegram bot, Alexa bridge, and 8 systemd monitor timers.
  Full source: [AI-Agent ↗](https://github.com/naveen6gowda/AI-Agent)
- **Hermes Agent container** — a second agent platform: web dashboard, Telegram,
  sandboxed Python execution, scheduled jobs
- Both consume the same local LLM endpoint below

### Local AI Inference — three generations

- **Gen 1 — Ollama LXC** (Ubuntu, management VLAN, iGPU passthrough via
  `/dev/dri/renderD128`)
- **Gen 2 — llama.cpp** (Vulkan) on the same LXC
- **Gen 3 (current) — LM Studio** on an Apple-silicon node, serving
  **Qwen3.6-35B-A3B (MoE)** through an OpenAI-compatible API with bearer-token
  auth — one model, every agent in the lab
- **Purpose:** self-hosted LLM inference — no cloud, no API costs, no prompt
  leaves the network

## Network Architecture

```
Internet
    │
OPNsense Firewall / Router
    │
    ├── VLAN: Management
    │   ├── Proxmox host
    │   ├── Sentinel LXC (HomelabSentinel agent)
    │   ├── Hermes Agent container
    │   └── LM Studio inference node (Apple silicon)
    │
    ├── VLAN: Home Assistant
    │   └── HA VM (HAOS)
    │
    └── VLAN: IoT Devices (isolated)
        ├── Mailbox sensor
        ├── Plant moisture monitor
        ├── Hall clock
        └── ... (all 9 ESP32 nodes)
```

## Remote Access

- **Tailscale VPN** — secure remote access to all services without port forwarding
- **No exposed ports** to the internet

## Key Design Decisions

- **VLAN segmentation** — IoT devices cannot reach management network; HA is the only bridge
- **Local-first** — LLM inference (LM Studio), the agents, MQTT broker, and ESPHome all run locally; no cloud dependencies
- **MQTT over native API** for battery devices — fire-and-forget avoids HA API reconnect delays during short wake windows

---

*This infrastructure was designed and deployed with AI assistance.*
