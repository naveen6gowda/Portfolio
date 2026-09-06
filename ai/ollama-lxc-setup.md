[← AI projects](README.md) · [Infrastructure overview](../homelab/infrastructure.md)

# Local inference in Proxmox LXC — deployment history

This page records the first two generations of my inference setup: Ollama, followed by llama.cpp with Vulkan. The later project configuration moved serving to LM Studio on Apple Silicon. These are historical design notes, not a current installation script.

## What changed and why

| Generation | Serving layer | Engineering focus |
|---|---|---|
| 1 | Ollama | Simple model management and a local API for applications such as Open WebUI |
| 2 | llama.cpp with Vulkan | Direct GGUF selection, GPU offload, context limits, and server tuning |
| 3 | LM Studio on Apple Silicon | Unified-memory capacity and a shared OpenAI-compatible endpoint |

I also operated OpenClaw and later Hermes Agent as third-party agent frameworks. HomelabSentinel is my separate Python / LangGraph implementation. Running a framework and authoring that framework are different contributions.

## Historical LXC configuration

The Ubuntu unprivileged container was allocated four CPU cores, 4 GB RAM, and 44 GB disk, with a static address on an infrastructure VLAN. Nesting and keyctl were enabled in the recorded configuration.

The following excerpt shows the device mapping used for the Intel iGPU. Device paths, permissions, and the appropriate container configuration depend on the host; these values are not universal defaults.

```ini
lxc.cgroup2.devices.allow: c 226:128 rwm
lxc.cgroup2.devices.allow: c 226:0 rwm
lxc.mount.entry: /dev/dri/renderD128 dev/dri/renderD128 none bind,optional,create=file
lxc.mount.entry: /dev/dri/card0 dev/dri/card0 none bind,optional,create=file
```

For llama.cpp, I explored Vulkan builds using `GGML_VULKAN=ON`, GGUF quantization selection, GPU offload, and context/batch configuration. Supported model architecture and backend compatibility matter; not every GGUF runs on every server version.

## Tradeoffs

- Local inference reduces dependence on per-token cloud APIs for the selected workload, but still requires hardware, electricity, and maintenance.
- Smaller or more heavily quantized models fit constrained memory; tool-use quality needs evaluation after changing quantization.
- Larger context windows increase memory demand and can affect responsiveness.
- An OpenAI-compatible endpoint needs a compatible client. The Anthropic learning examples in this repository require a client change to use such an endpoint.
- Network access, authentication, and firewall configuration remain deployment responsibilities. Local serving alone does not make every connected application private or offline.

For maintained installation instructions, use the upstream projects: [Ollama](https://github.com/ollama/ollama), [llama.cpp](https://github.com/ggml-org/llama.cpp), and [LM Studio documentation](https://lmstudio.ai/docs). See the [Sentinel case study](Agent_AI/README.md) for the application built on top of inference.
