# Hermes Agent Kanban es BRUTAL! Aprende a Usarlo

## Información General
- **Canal:** Kilian Párraga
- **Duración:** 18m 35s
- **Idioma detectado:** Español
- **Transcripción fuente:** `Hermes_Agent_Kanban_es_BRUTAL_Aprende_a_Usarlo.txt`

## Resumen Ejecutivo

El video cubre la versión 0.14 de **Hermes Agent**, un agente de IA local que en esta release evoluciona de herramienta a plataforma. Las mejoras abarcan instalación modular vía Python (sin clonar el repositorio completo), arranque más rápido, nuevos proveedores de LLM (Groq con OAuth), un **proxy local** que expone una API compatible con OpenAI para redirigir cualquier herramienta externa hacia los modelos conectados en Hermes, nuevos canales de mensajería (Teams, Line, Simplex), búsqueda en Twitter/X, nuevas skills (Hugging Face, Yahoo Finance, Hyperliquid), mejoras en seguridad con bloqueos y circuit breakers, y mejor trazabilidad en las ediciones de código.

Como bonus principal, el autor profundiza en la funcionalidad **Kanban** (introducida en la v0.13), que permite delegar tareas complejas a un equipo de agentes: Hermes descompone automáticamente la tarea en subtareas, las ejecuta en paralelo en segundo plano y entrega un resultado consolidado (en este caso un informe de auditoría de repositorio en HTML) en aproximadamente 20 minutos sin intervención humana.

El video incluye una demo en vivo donde se solicita una auditoría completa de un repositorio de GitHub. Hermes crea 4 subtareas automáticamente (análisis de arquitectura, auditoría de dependencias, revisión de configuración, redacción del informe HTML final), las ejecuta secuencialmente/en paralelo y entrega el artefacto final en el sistema de ficheros local.

## Puntos Clave

- **Instalación modular**: ya no hace falta clonar el repo completo; se instala la base con `pip` y los módulos se cargan bajo demanda, reduciendo el tiempo de instalación y arranque.
- **Velocidad mejorada**: operaciones que tardaban segundos ahora son casi instantáneas; experiencia de uso mucho más fluida.
- **Nuevos proveedores LLM**: Groq se conecta ahora vía OAuth (igual que OpenAI), y se han añadido más proveedores compatibles con la interfaz de Hermes.
- **Proxy local** (`hermes proxy`): abre un puerto local con interfaz compatible OpenAI; cualquier herramienta (ej. Codex CLI) puede apuntar a ese endpoint en lugar de la API oficial de OpenAI y usar cualquier modelo conectado a Hermes.
- **Nuevos canales de mensajería**: Teams, Line y Simplex se suman a Telegram.
- **Nuevas skills**: Hugging Face, Yahoo Finance, Hyperliquid (cripto), búsqueda en Twitter/X, análisis de imágenes enviadas por Telegram.
- **Seguridad reforzada**: bloqueos contra comandos peligrosos, restricciones de `sudo`, sanitización de salidas y circuit breakers ante fallos repetidos.
- **Mejor trazabilidad de código**: el agente ahora reporta en detalle qué cambió, por qué y en qué rutas, reforzando el ciclo editar→verificar→corregir.
- **Kanban (v0.13)**: tablero de tareas donde Hermes descompone una tarea padre en subtareas hijo, las ejecuta en segundo plano y entrega un artefacto final. Los estados son: Clasificación → Por hacer → En curso → Bloqueado (requiere humano) → Review → Hecho.
- **Actualización** con `hermes update` desde terminal.
- **Dashboard** accesible con `hermes dashboard`: muestra modelos, logs, tareas programadas, skills habilitadas/deshabilitadas.

## Conceptos Técnicos Mencionados

| Concepto | Descripción |
|---|---|
| **Hermes Agent** | Agente de IA local y de código abierto, orquestador de tareas con múltiples integraciones |
| **Kanban board (Hermes)** | Sistema de tablero dentro de Hermes que descompone tareas en subtareas y las ejecuta de forma autónoma en segundo plano |
| **Proxy local OpenAI-compatible** | Servidor local iniciado con `hermes proxy` que expone una API REST compatible con la API de OpenAI, permitiendo redirigir herramientas externas a cualquier LLM conectado a Hermes |
| **Groq** | Proveedor de inferencia LLM de alta velocidad, ahora integrado en Hermes vía OAuth |
| **Claude (Anthropic)** | LLM integrado en Hermes con mejoras en ahorro de contexto |
| **Codex CLI** | Herramienta de línea de comandos de OpenAI compatible con el proxy local de Hermes |
| **Instalación modular (lazy loading)** | Patrón de instalación donde solo se descarga el núcleo y los módulos adicionales se cargan cuando se necesitan |
| **Circuit breakers** | Mecanismo de seguridad que detiene la ejecución ante fallos repetidos o comportamientos inseguros del agente |
| **Skills / Plugins de Hermes** | Módulos opcionales que amplían las capacidades del agente (Hugging Face, Yahoo Finance, Hyperliquid, Twitter search, Chrome, etc.) |
| **Hugging Face skill** | Integración con el hub de modelos de Hugging Face como skill opcional de Hermes |
| **Teams integration** | Nueva integración de mensajería con Microsoft Teams para conectar Hermes en entornos empresariales |
| **Telegram integration** | Integración preexistente de mensajería; mejorada con análisis real de imágenes (antes solo las describía) |
| **Dashboard Hermes** | Interfaz web local para monitorizar agentes, logs, tareas, skills y modelos conectados |
| **Orquestación auto/manual** | Modo de ejecución del Kanban: automático (Hermes decide cuándo ejecutar) o manual (el usuario dispara la ejecución) |
| **Tarea padre / tarea hijo** | Jerarquía de tareas en el Kanban de Hermes; la tarea padre es la solicitada por el usuario y las hijas son las subtareas generadas automáticamente |

## Fragmentos Relevantes

> *"Hermes deja de ser una herramienta y empieza a comportarse como si fuera una plataforma."*

> *"Básicamente es un puente local que nos permite conectar otras herramientas con modelos o proveedores que tengamos conectados a Hermes [...] responde como si la API fuera la de OpenAI."*

> *"Cuando un agente puede ejecutar comandos o tocar archivos, los límites importan. La V014 añade bloqueos, sanitización y circuit breakers."*

> *"Le pides una tarea, la descompone en subtareas, se pone a trabajar en segundo plano y vuelve con un resultado espléndido."*

> *"Han pasado unos 20 segundos y fijaos que ya nos ha pasado de clasificación a por hacer y directamente ha dividido la tarea en cuatro subtareas."*

> *"Esto lleva unos 8 minutos [...] en principio cuando esta tarea finalice, la que es el padre de todas estas también va a pasar a finalizada y vamos a poder ver el resultado final después de aproximadamente unos 20 minutos."*

> *"La versión refuerza el ciclo de editar, verificar y corregir."*

## Conclusiones y Aprendizajes

- **Usar el Kanban para auditorías de repositorio**: delegar a Hermes el análisis completo de un proyecto (arquitectura, dependencias, configuración, informe final en HTML/Markdown) es una aplicación directa y de alto valor con ~20 min de ejecución desatendida.
- **Proxy local como capa de abstracción de LLMs**: en proyectos que usan Codex CLI u otras herramientas con API OpenAI-compatible, configurar el endpoint hacia el proxy de Hermes permite cambiar de modelo sin tocar la herramienta cliente.
- **Descomposición automática de tareas complejas**: el patrón padre→hijos del Kanban es útil para cualquier tarea que naturalmente se divida en fases (análisis, implementación, test, reporte).
- **Seguridad al usar agentes con acceso al sistema de ficheros**: la v0.14 añade protecciones nativas; aun así, revisar qué comandos puede ejecutar el agente es una buena práctica antes de desplegarlo en producción.
- **Actualización trivial**: `hermes update` desde terminal mantiene la instalación al día sin necesidad de gestionar el repositorio manualmente.
- **Integración empresarial con Teams**: para entornos corporativos que no pueden usar Telegram, la nueva integración con Teams es la vía de entrada para desplegar Hermes como asistente interno.
- **Perfiles de agente separados**: crear perfiles distintos en el Kanban (ej. `default` vs `aprendizaje`) permite segmentar experimentos de automatización sin interferir con flujos de producción.

---
> Generado automáticamente para uso como contexto en Cursor / Claude Code