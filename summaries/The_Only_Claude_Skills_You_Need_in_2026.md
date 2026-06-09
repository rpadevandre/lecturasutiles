# The Only Claude Skills You Need in 2026

## Información General
- **Canal:** Dubibubii
- **Duración:** 18m 13s
- **Idioma detectado:** Inglés

## Resumen Ejecutivo
El video presenta una selección curada de 33 skills, MCPs y repos de GitHub para potenciar Claude Code, seleccionados de un ecosistema de más de 500,000 opciones disponibles. El creador, que se describe como un "vibe coder" que genera ingresos mediante el desarrollo de apps con IA, comparte las herramientas que personalmente han reducido a la mitad su tiempo de construcción de productos.

Las herramientas se organizan en tres categorías conceptuales: **skills** (mejoran el comportamiento de Claude), **MCPs** (conectan Claude a herramientas externas y datos en tiempo real), y **repos** (proyectos GitHub que hospedan las implementaciones). El video cubre desde mejoras de diseño frontend hasta automatización de investigación, gestión de tokens, seguridad de prompts y orquestación de agentes paralelos.

El enfoque es eminentemente práctico y orientado a builders independientes (indie hackers, vibe coders), con énfasis en herramientas que reducen fricción en el ciclo completo: diseño → desarrollo → testing → marketing → distribución.

## Puntos Clave
- **Frontend Design Skill** (277k installs): Elimina fuentes genéricas (Inter, Roboto, Arial) y fuerza a Claude a definir una dirección de diseño antes de escribir código
- **Superpowers** (100k+ stars): Colección de 20+ skills que implementan TDD estricto — borra código si se escribe antes que los tests
- **Auto Researcher**: Agente de investigación que corre experimentos en loop 24/7 y entrega los mejores resultados al despertar
- **Context7** (50k stars, 240k descargas/semana): Inyecta documentación actualizada de librerías directamente en el contexto de Claude, eliminando alucinaciones de APIs deprecadas
- **Gary Tan's Setup** (40k stars): 15 prompts opinados del presidente de YC que estructuran Claude en roles: CEO, diseñador, engineering manager, release manager
- **Taskmaster**: Convierte un PRD en tareas estructuradas con dependencias, puntajes de complejidad y subtareas ejecutables secuencialmente
- **Playwright MCP**: Control de browser por parte del agente (clicks, formularios, screenshots, scraping)
- **Firecrawl MCP**: Motor de búsqueda para agentes con herramientas search/extract/crawl/map
- **Codebase Memory MCP**: Grafo de conocimiento persistente del codebase que sobrevive entre sesiones
- **Marketing Skills by Corey Haines** (16k stars): 20+ sub-skills de CRO, copywriting, SEO, email sequences
- **Remotion** (117k installs/semana): Genera videos de motion graphics programáticamente con código
- **Token Optimizer**: Reduce uso de tokens mediante técnicas de caché y eficiencia de contexto
- **Prompt Foo** (18k stars): Testing automatizado de seguridad para prompts — red teaming, inyección, edge cases
- **Skill Creator**: Meta-skill oficial de Anthropic que genera skill files desde descripción en lenguaje natural
- **n8n** (180k stars): Automatización de workflows open-source con 400+ integraciones y nodos de IA nativos
- **Claude Squad** (65k stars): Ejecuta múltiples agentes Claude en paralelo en sesiones de terminal independientes
- **Container Use by Dagger**: Sandboxing containerizado para agentes — cada agente en entorno aislado que no puede romper el sistema real
- **Ghost OS**: Agentes que controlan cualquier app del Mac (Figma, Keynote, Photoshop, Slack) via visión de pantalla

## Conceptos Técnicos Mencionados
- **MCP (Model Context Protocol):** Protocolo que permite a Claude conectarse a herramientas externas, APIs y datos en tiempo real
- **Skills/CLAUDE.md:** Archivos Markdown que modifican el comportamiento de Claude Code en tareas específicas
- **TDD (Test-Driven Development):** Metodología donde los tests se escriben antes que el código de implementación
- **Context Window Injection:** Técnica de inyectar documentación o contexto relevante directamente en la ventana de contexto del modelo
- **Knowledge Graph:** Estructura de datos que representa relaciones entre entidades — usado por Codebase Memory MCP para persistir el estado del proyecto
- **Red Teaming:** Técnica de security testing que simula ataques adversariales para encontrar vulnerabilidades
- **Prompt Injection:** Ataque donde inputs maliciosos manipulan el comportamiento del LLM
- **Sandboxing / Containerización:** Aislamiento de entornos de ejecución para prevenir que agentes afecten el sistema host
- **PRD (Product Requirements Document):** Documento de especificación de producto usado como input para Taskmaster
- **Vibe Coding:** Desarrollo de software asistido casi completamente por IA con mínima escritura manual de código
- **LLM-ready data:** Datos estructurados (markdown limpio, JSON) listos para ser consumidos por modelos de lenguaje sin preprocessing
- **KB Cache Tricks:** Técnicas de caché a nivel de kilobytes para reducir tokens enviados al modelo
- **NPM MCP Server:** Servidores MCP distribuidos via npm e instalables como dependencias de Node.js
- **Context7:** MCP que resuelve el problema de documentación desactualizada en el training data del modelo
- **Remotion:** Framework de React para generar videos programáticamente
- **n8n:** Plataforma de workflow automation self-hosted con capacidades de agentes IA
- **LangFlow:** Interfaz visual drag-and-drop para construir pipelines de agentes IA (backed by DataStax)
- **Firecrawl:** Servicio de web scraping que devuelve markdown estructurado optimizado para LLMs
- **Playwright:** Librería de Microsoft para automatización de browsers (Chromium, Firefox, WebKit)
- **Docker/Dagger:** Containerización — Container Use es construido por el creador de Docker para sandboxing de agentes

## Fragmentos Relevantes

> "Skills improve Claude, MCPs connect Claude, and repos host the tools."

> "The front-end design skill literally bans certain fonts like Inter, Roboto, and Arial. It also forces Claude to pick a real design direction before writing a single line of code."

> "It will literally delete your code if you write it before the tests exist. Not archive it, delete it."

> "You know that problem when you ask for it to help you with a library and it gives you code using an API that was deprecated 6 months ago, and you spend 2 hours debugging before you realize the function doesn't even exist anymore? Context7 fixes that."

> "Claude normally forgets everything between sessions. You close the terminal and your agent wakes up tomorrow with amnesia. Codebase Memory MCP fixes that."

> "If you're running multiple agents, and you've ever had one go rogue and start deleting files it shouldn't be touching, first of all, I feel your pain. Install this before it happens again." (sobre Container Use)

> "Skills are literally just markdown files, and how you structure your Claude code environment matters more than most people realize."

> "Think of it as unit tests for your prompts. If you're building anything that actual humans will interact with, and you haven't tested your prompts for injection attacks or weird edge cases, you're basically leaving your front door open with a sign that says, Come in. It is open."

> "You just describe a workflow in plain English, and it generates a skill file for you in about 5 minutes." (sobre Skill Creator)

## Conclusiones y Aprendizajes

**Aplicables directamente en proyectos de software:**

1. **Instalar Context7 como primera prioridad**: Resuelve el problema más costoso en tiempo del desarrollo con LLMs — alucinaciones de APIs deprecadas. Un solo `use context7` en el prompt basta.

2. **Usar Taskmaster para proyectos complejos**: Convertir PRDs largos en tareas atómicas con dependencias evita que el agente salte pasos o pierda contexto en proyectos grandes.

3. **Codebase Memory MCP para proyectos con múltiples sesiones**: Cualquier proyecto que dure más de un día se beneficia de persistencia de contexto estructural.

4. **Container Use antes de correr agentes autónomos**: El sandboxing no es opcional cuando se tienen agentes que modifican el filesystem.

5. **Prompt Foo para cualquier producto con usuarios reales**: El testing de prompts contra injection y edge cases debería ser parte del pipeline de QA, no algo opcional.

6. **Frontend Design Skill como default en cualquier UI**: El costo de instalarlo es cero; el costo de no usarlo es código con aspecto genérico.

7. **Skill Creator para workflows propios**: En lugar de escribir CLAUDE.md manualmente, describir el workflow en lenguaje natural y dejar que el meta-skill genere el archivo.

8. **Claude Squad para paralelización**: Cuando hay múltiples features independientes, correr agentes en paralelo reduce el tiempo total de desarrollo significativamente.

9. **n8n como capa de automatización**: Para tareas repetitivas del negocio (emails, onboarding, monitoreo), n8n con nodos de IA elimina trabajo manual sin vendor lock-in.

10. **El patrón de Auto Researcher**: Más valioso que la herramienta en sí — el patrón de loop de experimentación autónoma con evaluación de resultados es aplicable a cualquier problema de optimización.

---
> Generado automáticamente para uso como contexto en Cursor / Claude Code