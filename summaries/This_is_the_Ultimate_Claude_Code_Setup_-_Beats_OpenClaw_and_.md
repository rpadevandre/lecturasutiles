# This is the Ultimate Claude Code Setup - Beats OpenClaw and Hermes!

## Información General
- **Canal:** Simon Scrapes
- **Duración:** 19m 46s
- **Idioma detectado:** Inglés

## Resumen Ejecutivo
El video argumenta que Claude Code, con la configuración correcta, puede replicar y superar las funcionalidades de frameworks de agentes como Hermes y OpenClaw, sin costos adicionales de API al funcionar sobre las suscripciones Pro/Max de Claude. El autor identifica cinco pilares fundamentales que subyacen a todos estos sistemas: memoria persistente, habilidades (skills) auto-mejorables, capa de interacción, tareas programadas y contexto de negocio.

La propuesta central es construir un "Agentic Operating System" propio dentro de Claude Code, estructurado alrededor de un "business brain" compartido — una carpeta de contexto de marca que alimenta a todos los agentes y skills. Esto produce outputs de mayor calidad porque el agente siempre conoce la voz de la marca, el ICP, el posicionamiento y los detalles de clientes, en lugar de empezar desde cero en cada skill.

El autor concluye con una lección aprendida de tres meses: el error más común es empezar por los agentes o la orquestación multi-agente. La base correcta es primero construir el contexto de negocio sólido, porque todos los demás pilares se multiplican (o se rompen) dependiendo de qué tan bien esté estructurada esa capa de contexto.

## Puntos Clave
- **Hermes y OpenClaw son básicamente wrappers** sobre las mismas cinco funcionalidades que ya existen en Claude Code
- **Cuatro capas de memoria** para gestión de contexto: `claude.md`/`agents.md`, brand context folder, agent context folder, y project memory
- **El `claude.md` debe ser corto y conciso** — no superar las ~200 líneas; debe referenciar archivos externos en lugar de contener todo el contexto inline
- **Skills con auto-mejora**: añadir un `learnings.md` o sección de reglas en cada skill para que el agente incorpore feedback y mejore con cada iteración
- **El "Skill Creator Skill"** de Anthropic permite generar nuevas skills describiendo el proceso o apuntando a un repositorio GitHub
- **Claude Code Channels** (integración nativa con Telegram, iMessage y Discord) ya cumple lo que Hermes promete para interacción móvil
- **Command Center propio** (Kanban de objetivos de negocio) para gestionar múltiples agentes y proyectos en paralelo, abstrayendo el rol del usuario a supervisor
- **Workflows programados** sin VPS — Claude Code puede configurar la lógica de scheduling usando funcionalidades nativas del OS (Mac/Windows)
- **Siempre incluir un checkpoint humano** antes de publicar cualquier output automatizado (regla del 80/20: automatizar la investigación y borradores, supervisar antes de publicar)
- **La ventaja compuesta real** es el contexto de negocio inyectado en el momento correcto, no los modelos ni los agentes en sí

## Conceptos Técnicos Mencionados
- **Claude Code** — IDE/entorno de desarrollo de Anthropic que permite ejecutar agentes con acceso al sistema de archivos y terminal
- **`claude.md` / `agents.md`** — Archivo de instrucciones operativas del agente, cargado en cada sesión; equivalente a un system prompt persistente
- **Brand Context Folder** — Carpeta compartida con voz de marca, ICP, posicionamiento y datos de clientes, referenciada por todos los skills
- **Agent Context Folder** — Archivos como `soul.md` y `user.md` que definen personalidad y patrones de comportamiento del agente
- **Project Memory** — Historial y plan de cada proyecto para mantener continuidad entre sesiones
- **Skill Creator Skill** — Skill oficial de Anthropic que genera automáticamente nuevas skills a partir de descripciones de proceso o repos de GitHub
- **`learnings.md`** — Archivo de reglas no negociables que cada skill incorpora y refina con el feedback del usuario
- **Claude Code Channels** — Feature nativo de Anthropic para conectar Claude Code con Telegram, iMessage y Discord
- **Command Center** — UI layer tipo Kanban construida sobre Claude Code para gestionar múltiples objetivos de negocio en paralelo
- **Routines (Claude Desktop)** — Feature de automatización/scheduling de tareas dentro de la app de escritorio de Claude
- **GSD (Get Stuff Done) Framework** — Framework de planificación de proyectos complejos mencionado como ejemplo de metodología de planes
- **Agentic OS** — Concepto de sistema operativo agéntico propio: combinación de business brain + skills + command center
- **Context Rot** — Degradación de la calidad de outputs cuando el contexto en ventana se vuelve demasiado grande
- **Multi-agent Orchestration** — Coordinación de múltiples instancias de agentes trabajando en objetivos distintos en paralelo
- **OAuth (Anthropic)** — Mecanismo de autenticación que permite usar el Command Center custom respetando las políticas de uso de suscripciones Pro/Max
- **Obsidian / Carpathy's LLM Wiki** — Alternativas mencionadas como sistemas de gestión de memoria/conocimiento para agentes
- **agentskills.io** — Plataforma de Hermes para compartir skills entre usuarios

## Fragmentos Relevantes

> "The real question now that agents are so good is, how do we manage multiple conversations and multiple goals at the same time? The models are now so, so good that it's pushing us into a different role. We're now jumping into a supervisor role."

> "It doesn't matter how you set this up. The core ingredients are that you're just loading in the right context at the right time, so you're not bloating context and experiencing context rot where the outputs are getting worse the more context you feed in."

> "The real unlock isn't actually the agents. The agents and the models are getting better and better. It's the layer underneath — the context — the brand context folder, the voice profile, the audience avatar, all of that preloaded, pulling into the right skill at the right time is what actually generates high-quality outputs."

> "My original aim was to build out fully autonomous scheduled workflows... but it was actually pretty bad because 20% of the time, something wouldn't be quite right. So, instead, I've actually built this framework now around doing 80% of the work automatically... but what I've added in is always having a human checkpoint before anything goes live."

> "Start with this business brain. Don't start with the agents. Don't start with the multi-agent orchestration. I made this same mistake. Every feature I just walked through gets multiplied by having the solid context, the foundation layer underneath it."

> "You update the information once, and every skill gets that update when it runs. So, business context is that compounding advantage that you cannot get right now."

## Conclusiones y Aprendizajes

**Arquitectura aplicable directamente:**
1. **Estructura el contexto en 4 capas separadas** en tu repo de Claude Code: instrucciones base (`claude.md`), contexto de marca compartido, contexto de agente/personalidad, y memoria de proyecto. Nunca mezcles todo en un solo archivo.
2. **Mantén los archivos de entrada (`claude.md`, `skill.md`) por debajo de 200 líneas**. El detalle va en archivos de referencia que se cargan on-demand para evitar context rot.
3. **Añade un paso de feedback y `learnings.md` a cada skill** para crear un loop de auto-mejora sin necesidad de frameworks externos.
4. **Para scheduling**, instruye a Claude Code para que configure la lógica de cron/scheduling directamente en el OS — no necesitas un VPS ni infraestructura extra.
5. **Regla del 80/20 para automatización**: automatiza investigación, análisis y borradores; mantén siempre un checkpoint humano antes de cualquier acción que salga al exterior (publicar, enviar emails, etc.).
6. **Si gestionas múltiples proyectos o agentes**, construye una UI wrapper tipo Kanban que mapee objetivos de negocio a conversaciones de Claude. Las interfaces de chat simples no escalan para supervisar múltiples agentes en paralelo.
7. **El orden correcto de construcción**: Business Brain → Skills → Interaction Layer → Scheduled Tasks → Multi-agent. Invertirlo es el error más costoso.

---
> Generado automáticamente para uso como contexto en Cursor / Claude Code