# The 7 Levels of Hermes Agent Explained

## Información General
- **Canal:** David Ondrej
- **Duración:** 47m 0s
- **Idioma detectado:** Inglés

## Resumen Ejecutivo
El video presenta una guía progresiva de siete niveles para configurar Hermes Agent de manera avanzada, comenzando desde la instalación básica en un VPS hasta convertirlo en un servidor MCP completo. El autor, David Ondrej, combina instrucciones técnicas paso a paso con casos de uso prácticos derivados de su experiencia real construyendo una startup de IA (Vectal) y gastando entre $6,000 y $10,000 mensuales en costes de API.

Cada nivel construye sobre el anterior: instalación en VPS → integración con Discord → gestión de skills con Curator → automatizaciones con cron jobs → kanban board multi-agente → memoria holográfica → exposición como servidor MCP. El enfoque es práctico y no requiere conocimientos de DevOps, ya que la mayoría de configuraciones se realizan hablando directamente con el agente en inglés llano.

El punto más avanzado (nivel 7) es transformar Hermes Agent en un servidor MCP para que Claude Code, Codex u otros agentes puedan delegar tareas, recibir aprobaciones remotas y leer contexto almacenado en Hermes, creando una arquitectura de backend distribuido para agentes de IA.

## Puntos Clave
- **Nivel 1 — Instalación en VPS:** Usar Hostinger con un comando one-liner de instalación. Hermes vive en su propio servidor y no en la máquina local del usuario.
- **Nivel 2 — Integración Discord:** Crear un bot de Discord desde el portal de desarrolladores, obtener el token, habilitar los tres intents privilegiados y conectarlo a un servidor propio.
- **Nivel 3 — Hermes Curator:** Herramienta que marca skills sin uso después de 30 días como "stale" y las elimina tras 90 días, evitando "context rot" y malgasto de tokens.
- **Nivel 4 — Cron Jobs / Automaciones:** Configurar backups diarios automáticos del agente a un repositorio privado de GitHub usando un GitHub personal access token almacenado en el archivo `.env` de Hermes.
- **Nivel 5 — Kanban Board Multi-Agente:** Panel visual integrado en Hermes que permite despachar múltiples sub-agentes (researcher, writer, reviewer, analyst) trabajando en paralelo, monitoreando su progreso visualmente.
- **Nivel 6 — Memoria Holográfica:** Plugin de memoria local (`hermes memory setup`) que almacena hechos estructurados en una base de datos SQL local sin enviar datos a la nube, con extracción automática de hechos al final de cada sesión.
- **Nivel 7 — Servidor MCP:** Exponer Hermes como MCP server para que Claude Code pueda interactuar con él, leer conversaciones de Discord/Telegram/Slack, y usarlo como backend de aprobación remota o relay de contexto.
- **Recomendación de modelo:** Usar modelos potentes (Claude Opus 4.7, GPT 5.5). Los modelos pequeños y baratos degradan severamente la calidad en harnesses agénticos complejos.
- **El Kanban no es solo visual:** Permite al humano ser el director de múltiples agentes sin tener 20 terminales abiertas, como si gestionara un equipo de desarrolladores.
- **Hermes se autoinstala:** Para la mayoría de configuraciones (kanban, MCP, memoria), basta con darle el link a la release y pedirle que lo configure él mismo.

## Conceptos Técnicos Mencionados
- **Hermes Agent** — Agente de IA open source (133k+ estrellas en GitHub) con capacidades de auto-mejora de skills, orchestración multi-agente y múltiples integraciones.
- **VPS (Virtual Private Server)** — Servidor privado virtual donde se aloja el agente de forma permanente, 24/7, independiente del equipo local.
- **SSH** — Protocolo para acceder remotamente al VPS desde el terminal local.
- **Hostinger** — Proveedor de VPS usado en el tutorial, con una landing page dedicada a despliegue de Hermes Agent.
- **Open Router** — API gateway que permite acceder a múltiples modelos de IA (Claude, GPT, etc.) con una sola API key y clave de créditos.
- **Claude Opus 4.7** — Modelo de Anthropic usado como LLM principal para Hermes Agent en este tutorial.
- **Discord Bot / Developer Portal** — Interfaz para crear bots de Discord, obtener tokens y configurar permisos e intents.
- **systemd / systemd linger** — Sistema de gestión de servicios en Linux que permite que Hermes Gateway corra como servicio persistente y sobreviva a logouts.
- **Cron Jobs** — Tareas programadas en Linux para ejecutar acciones periódicas (backups diarios a las 3 AM).
- **GitHub Personal Access Token (fine-grained)** — Token con permisos específicos por repositorio para operaciones de lectura/escritura desde el agente.
- **Hermes Curator** — Módulo de Hermes que gestiona el ciclo de vida de skills autogeneradas para evitar bloat de contexto.
- **Hermes Gateway** — Componente de Hermes que gestiona la comunicación con plataformas externas (Discord, Slack, Telegram, Teams, Email).
- **Kanban Board (multi-agent)** — UI visual integrada en Hermes para gestionar tareas distribuidas entre múltiples sub-agentes con estados (todo, in progress, blocked, done).
- **Holographic Memory** — Plugin de memoria local para Hermes basado en SQL, que extrae y almacena hechos estructurados de sesiones pasadas sin enviar datos a la nube.
- **MCP (Model Context Protocol)** — Protocolo creado por Anthropic para que modelos y agentes interactúen con herramientas y servidores externos de forma estandarizada.
- **MCP Server** — Servidor que expone herramientas consumibles por agentes compatibles con MCP (Claude Code, Codex, etc.).
- **Claude Code (CLI)** — Herramienta de línea de comandos de Anthropic para usar Claude como agente de coding directamente en terminal/VPS.
- **RAG (Retrieval Augmented Generation)** — Técnica mencionada como limitada para memoria estructurada de agentes (comparada con holographic memory).
- **SSH Tunnel** — Técnica para redirigir puertos remotos al localhost del desarrollador para acceder a servicios corriendo en el VPS.
- **Docker vs. Root install** — El autor prefiere instalación a nivel root sobre Docker para Hermes Agent por simplicidad, aunque Docker es más seguro.
- **`hermes config set`** — Comando CLI de Hermes para almacenar variables de entorno de forma segura.
- **`hermes gateway setup/status/restart`** — Comandos CLI para gestionar el gateway de comunicación de Hermes.
- **`hermes memory setup`** — Comando CLI para configurar el plugin de memoria.
- **`hermes curator status`** — Comando CLI para verificar configuración del curator de skills.
- **`hermes update`** — Comando para actualizar Hermes a la última versión.

## Fragmentos Relevantes

> *"Hermes agent is doing a lot like dozens and dozens of terminal commands to set this up himself right like I just said okay I want this release I want this multi-agent kanban orchestration dashboard and that's it you know Hermes is setting it up"*

> *"Do not use cheap models. These agentic harnesses like Hermes agent or OpenClaw, they are complex. And if you cheap out and you try to use a very small, very cheap model, you're going to have a hard time."*

> *"The beauty of it being on a VPS — you don't have to worry that it's going to do something sketchy on the computer. It has its own computer, which I think is the ultimate paradigm where each agent runs on its own computer."*

> *"Beginners never save anything, right? They just chat and hope that the default memory is good enough. Everything stays in the chat and dies at the end of the session."*

> *"More context doesn't necessarily mean it's going to be better memory. But more context always results in more cost and worse attention to the things that matter the most."*

> *"You expose it as an MCP server so that other agents like Claude Code or Codex can interact with it as if Hermes was your backend."*

> *"A lot of people have OpenClaw set up, but they don't use it because they don't know how. They have Hermes agent and they know how to set it up, but they don't know what to give it."*

> *"Hermes agent predicted that [the SSH tunnel command] itself. And it even included a screenshot of what this looks like on the VPS."*

## Conclusiones y Aprendizajes

**Infraestructura de agente:** Alojar agentes de IA en un VPS dedicado es el patrón correcto para producción. Permite persistencia 24/7, aislamiento de seguridad y la capacidad de correr múltiples agentes y herramientas (N8N, web apps) en una sola máquina.

**Configuración mediante el propio agente:** Para la mayoría de configuraciones avanzadas (kanban, MCP, memoria), el patrón más eficiente es darle al agente el link a la documentación/release y pedirle que lo configure él mismo. Esto es aplicable a cualquier proyecto con un agente capaz de leer web y ejecutar comandos.

**Gestión de memoria estructurada:** No depender del contexto de chat para memoria a largo plazo. Usar sistemas de hechos estructurados (holographic memory o equivalentes) para que el agente recuerde preferencias, configuraciones y progreso entre sesiones. Esto es directamente aplicable en cualquier proyecto donde el agente necesite persistir estado.

**Backups automáticos como práctica estándar:** Configurar cron jobs de backup a GitHub es una práctica de resiliencia que debería aplicarse a cualquier agente o proyecto crítico, no solo a Hermes.

**MCP como arquitectura de integración:** Exponer agentes locales como servidores MCP permite que múltiples herramientas de coding (Claude Code, Codex) accedan a contexto centralizado, actúen como gate de aprobación remota y reciban notificaciones de progreso. Es una arquitectura viable para pipelines de CI/CD asistidos por IA donde el desarrollador no está monitoreando activamente.

**Gestión de costes con Curator:** En setups con auto-mejora de skills (como Hermes), sin limpieza activa el contexto crece indefinidamente. Implementar políticas de TTL (time-to-live) en skills/memoria es esencial para controlar costes a largo plazo.

---
> Generado automáticamente para uso como contexto en Cursor / Claude Code