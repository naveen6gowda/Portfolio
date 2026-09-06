[← Portfolio](../README.md) · [Infrastructure overview](../homelab/infrastructure.md)

# Docker service portfolio

**A sanitized 24-service Docker Compose reference from a personal Debian VM.**

[docker-compose.yml](docker-compose.yml) shows how I organize service configuration, persistent storage, networks, dependencies, and operational tooling. It is a deployment reference, not a one-command application bundle or a live service inventory.

## Service map

| Area | Services in the Compose file |
|---|---|
| Management and logs | Portainer, Watchtower, Dozzle, Prunemate |
| Dashboard | Homer |
| Media | Jellyfin |
| Photos | Immich server, machine learning, Valkey, PostgreSQL |
| AI interfaces | Open WebUI, Mirofish |
| Automation | n8n, Redis, PostgreSQL / pgvector |
| Password storage | Vaultwarden |
| Finance | Firefly III, MariaDB |
| Bookmarks and search | Linkwarden, PostgreSQL, Meilisearch |
| DNS | AdGuard Home |
| Sync and backup tooling | Syncthing, Duplicati |

These are third-party applications I configured and operated. The Compose integration is my portfolio contribution; application authorship remains with the upstream projects.

## What the configuration demonstrates

- Persistent bind mounts and named volumes for application data and model caches.
- Dedicated networking for the n8n stack and Firefly, plus host networking for selected services.
- Service dependencies, an Immich cache health check, and environment-based secret injection.
- Logs and management through Dozzle / Portainer, scheduled update configuration with Watchtower, and Duplicati backup tooling.
- n8n as an automation layer for projects such as AI news briefings and Telegram assistance; private workflow exports are not included.

## Prerequisites and validation

Before adapting this file, provide the application configuration and environment files referenced by it:

| Required local file / resource | Used by |
|---|---|
| `.env` | Shared interpolation values, Immich, and the automation database |
| `mirofish/.env` | Mirofish |
| `fireflyIII/.env`, `fireflyIII/.db.env` | Firefly and MariaDB |
| `linkwarden/.env` | Linkwarden, its PostgreSQL database, and Meilisearch |
| `homer/assets/` | Dashboard configuration and assets |
| `n8n-ollama-network` | Existing external Docker network referenced by the automation stack |

Review all bind mounts, host ports, user IDs, secrets, application URLs, and image versions for the target machine. Application configuration and data are intentionally not committed. Several images use moving tags, so the file is not a version-locked reproducible deployment.

From this directory, after preparing those files, validate without starting services:

```bash
docker compose config --quiet
```

Check dependency readiness and application/database version compatibility against the chosen upstream releases. This portfolio review did not launch services or validate database migrations.

## Access and external dependencies

The snapshot includes Docker socket mounts and host-network services, which require a trusted administrative environment. Open WebUI is configured with authentication disabled for the original private-network setup; enable suitable authentication before making it accessible to other users.

Open WebUI includes an OpenRouter endpoint as well as a local Ollama URL. Together with notification and application integrations, this means the stack is **not entirely offline**. Backup tooling being configured is also distinct from a verified restore test.
