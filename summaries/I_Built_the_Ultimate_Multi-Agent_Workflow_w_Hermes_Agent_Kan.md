# I Built the Ultimate Multi-Agent Workflow w/ Hermes Agent Kanban Board

## Información General
- **Canal:** Tonbi's AI Garage
- **Duración:** 34m 32s
- **Idioma detectado:** English
- **Transcripción fuente:** `I_Built_the_Ultimate_Multi-Agent_Workflow_w_Hermes_Agent_Kan.txt`

## Resumen Ejecutivo
El video muestra un sistema multi-agente completamente funcional construido sobre **Hermes Agent** y su **Kanban Board** integrado. El autor diseñó un pipeline autónomo que detecta puntos de dolor de usuarios de agentes de IA en la web (X/Twitter, Reddit, YouTube), los evalúa con una rúbrica de puntuación, y produce automáticamente propuestas de herramientas o guiones de video. Todo el flujo corre sin intervención humana excepto por un único gate de aprobación vía Telegram antes de ejecutar la fase de construcción.

El sistema resuelve el problema clásico de los sistemas multi-agente: la coordinación sin conflictos. El Kanban actúa como única fuente de verdad (un archivo SQLite), donde cada agente reclama una tarjeta, trabaja en ella y la pasa al siguiente. No hay colas de mensajes ni comunicación directa entre agentes; solo el board compartido. Esto lo hace durable ante reinicios, auditable, paralelo y con auto-sanación cuando una tarea falla.

La demo en vivo muestra 97 tareas completadas en una sola ejecución: dos scouts de investigación alimentaron al orquestador, que lanzó 18 agentes de investigación en paralelo, produjo propuestas, esperó la aprobación humana, construyó un CLI de Python y generó slides + script para un video — todo de forma autónoma. El autor liberó el workflow como template open-source generalizado.

## Puntos Clave
- **El Kanban Board es un archivo SQLite único** que sirve como capa de coordinación, bus de mensajes y log de auditoría simultáneamente
- **Sin el Kanban**: los agentes hacen trabajo duplicado, desperdician tokens y no tienen memoria compartida del progreso
- **Cada tarjeta del Kanban** tiene: título, descripción de tarea, asignado (routing) y estado — nada más
- **El Dispatcher** es el componente central: reclama tareas del board, instancia el agente asignado en su propio workspace limpio, y loopea continuamente
- **Dependencias automáticas**: una tarjeta permanece en "to-do" hasta que todas sus tareas padre están completas, luego se promueve sola a "ready" sin polling externo
- **Fleet de 9 agentes especializados**: X Scout (con Grok), Web Scout, Orchestrator, Researcher ×3 (paralelo), Analyst, Builder, Tester, Video Producer
- **La rúbrica de scoring** evalúa: frecuencia del problema, intensidad del dolor, si es solucionable/explicable, gap de solución existente, fit estratégico — umbral de 65/100 para avanzar
- **Un solo human gate**: vía Telegram, el usuario aprueba/shelves/modifica propuestas antes de que el Builder o Video Producer actúen
- **Auto-healing integrado**: si un artefacto referencia un workspace temporal ya eliminado, el agente detecta el problema y regenera el entregable en un directorio persistente
- **Cada agente es un perfil en Hermes Agent** — pueden tener modelos diferentes (el X Scout usa Grok, el resto GPT-4.5 en la demo)
- **Deliverables concretos**: CLI Python (<500 líneas) para builds, o slides + script de speaker notes para videos
- **Ejecución**: diseñado como cron job (1-2 veces al día), con gateway del orquestador corriendo en sesión tmux persistente
- **Open-sourced** en: `tombistudio/hermes-multi-agent-workflow`

## Conceptos Técnicos Mencionados
- **Hermes Agent** — framework de agentes de IA local con soporte de perfiles, skills y Kanban Board integrado
- **Kanban Board (plugin)** — sistema de gestión de tareas basado en tarjetas accesible desde el web dashboard de Hermes; backend en SQLite
- **SQLite como coordination layer** — archivo único que actúa como estado compartido, bus de eventos y audit log para todos los agentes
- **Dispatcher** — componente que hace polling del board, reclama tareas atómicamente (evitando condiciones de carrera) y spawna agentes
- **Agent Profiles (Hermes)** — configuraciones de agente con modelo específico, skills asignados y comportamiento definido
- **Skills (Hermes)** — módulos de comportamiento reutilizables asignados a agentes; ej: `pain_point_scout_x_skill`
- **Orquestador** — agente central que ingiere reportes, deduplica, aplica rúbrica de scoring y decide el path (build/video/shelve)
- **Parent-child task dependencies** — tarjetas que esperan automáticamente la finalización de sus tareas padre antes de moverse a "ready"
- **Event-driven workflow** — el trabajo fluye por el grafo sin polling loops ni glue code; tareas se auto-promueven
- **Self-healing tasks** — tareas muertas o con artefactos inválidos se detectan y se re-spawnan automáticamente
- **Telegram integration** — canal de notificaciones y aprobación humana; el gateway del orquestador expone el human gate aquí
- **Grok model** — usado específicamente para el agente scout de X/Twitter por su acceso a datos de la plataforma
- **GPT-4.5** — modelo base para el resto de agentes en la demo
- **Claude + o3** — usados durante el diseño del workflow (no en runtime)
- **tmux** — recomendado para mantener vivo el proceso del gateway del orquestador en sesiones largas
- **Cron job** — mecanismo de scheduling para ejecutar los scouts periódicamente (1-2 veces al día)
- **Markdown files** — formato de los reportes de investigación almacenados en disco; auditables manualmente
- **CLI Python tool** — tipo de deliverable generado para soluciones de build; target <500 líneas

## Fragmentos Relevantes

> "Without a Kanban board, you have agents racing around and doing duplicate work, wasting your tokens, wasting your money. No one has a shared memory of the progress and one crash loses everything."

> "The board is a single source of truth. There's no chatting between the agents. There's no message queues or anything like that. Just the board that they all read and then write."

> "It's one SQLite file. That's the entire coordination layer. And it's the bus and audit log all in one."

> "A card will sit in to-do until its parents are finished. Then it promotes itself to ready. So this one task fans out to three research tasks... the moment the last one finishes, the route fires itself. So you have three agents working at once and the next step triggers itself. There's no polling or babysitting, no glue code holding it all together."

> "18 workers all working together in parallel without tripping on each other. And that's really the beauty of this system."

> "This is very important to keep. You could get rid of this, but I would not because I just don't want my agents wasting all my tokens and wasting a lot of money building random stuff."

> "It realized this was an issue. And I didn't tell it this, it did this autonomously. It had this self-healing function where it regenerated the video slide deck again to a persistent output directory."

> "97 tasks done in that one run."

> "I wouldn't know this problem existed. It's not something I've been encountering myself, but clearly a lot of people have been dealing with it. So having a pipeline like this is a really good source to try to make content that's really helpful."

## Conclusiones y Aprendizajes

**Arquitectura aplicable directamente:**
- Usar un **archivo SQLite como estado compartido** entre agentes es más robusto que colas de mensajes o llamadas directas — cualquier proyecto multi-agente puede adoptar este patrón
- El patrón **Dispatcher + Board** es reutilizable: un loop que reclama tareas atómicamente del board elimina race conditions sin infraestructura compleja
- Las **dependencias parent-child** en las tarjetas permiten paralelismo automático sin código de orquestación explícito — modelar el grafo de trabajo como dependencias de datos, no como flujo de control

**Diseño de pipelines de producción:**
- **Siempre incluir un human gate** antes de acciones costosas o irreversibles (construcción, publicación, consumo masivo de tokens)
- **Scoring rubrics con umbrales** (65/100 aquí) son esenciales para evitar que el sistema procese señal de baja calidad; ajustar el umbral según el costo de falsos positivos
- **Deduplicación en el orquestador** es obligatoria en cualquier sistema con inputs recurrentes

**Operaciones:**
- Correr el gateway del orquestador en **tmux** o equivalente para sobrevivir desconexiones de terminal
- Usar **cron jobs** para scouts; no más frecuente de lo necesario (aquí 1-2x/día fue suficiente)
- Los reportes intermedios en **Markdown en disco** dan observabilidad sin infraestructura adicional

**Gestión de fallos:**
- Implementar **recovery tasks** para artefactos que referencian paths temporales — verificar que los outputs se escriban en directorios persistentes antes de marcar la tarea como done
- El sistema es **auto-healing por diseño**: tareas muertas se reclaman; errores detectados generan nuevas tarjetas de recuperación

---
> Generado automáticamente para uso como contexto en Cursor / Claude Code