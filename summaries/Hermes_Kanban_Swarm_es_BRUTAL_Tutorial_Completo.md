# Hermes Kanban Swarm es BRUTAL (Tutorial Completo)

## Información General
- **Canal:** Alejandro Pardo | IA Automatización
- **Duración:** 26m 8s
- **Idioma detectado:** Español
- **Transcripción fuente:** `Hermes_Kanban_Swarm_es_BRUTAL_Tutorial_Completo.txt`

## Resumen Ejecutivo

El video explica en profundidad el sistema **Kanban Swarm** de Hermes (el agente de IA de No Research, con +180k estrellas en GitHub), introducido en la versión 0.13 "Tenacity" y madurado en la versión 0.15 "Velocity". La idea central es trasladar la metodología Kanban clásica (popularizada por Toyota en 1947 y luego adoptada en software con herramientas como Trello, Jira o Linear) al mundo de los agentes de IA: en lugar de personas moviendo tarjetas, son los propios agentes quienes crean, ejecutan y completan tareas de forma autónoma y coordinada, mientras un proceso automático llamado **dispatcher** actúa como gerente del tablero.

La arquitectura resultante es híbrida: no es un **Swarm puro** (donde los agentes se pasan tareas entre sí sin coordinador central) ni un **orquestador puro** (donde todo pasa por un agente jefe). En Hermes Kanban Swarm existe un **agente planificador/orquestador** que descompone tareas genéricas en subtareas, las publica en la pizarra compartida (el tablero Kanban), y a partir de ahí el **dispatcher** (un proceso que corre cada 60 segundos) se encarga de asignar, monitorizar, reintentar y mover las tareas entre columnas. Todo el estado se persiste en una base de datos SQLite independiente del historial de conversaciones, lo que garantiza que el tablero sobrevive a reinicios o pérdidas de conexión.

El video también incluye un tutorial práctico sobre cómo configurar boards, crear perfiles de agentes, definir workspaces, gestionar dependencias entre tareas y entender el flujo completo de una tarea desde el Triaje hasta Completada o Bloqueada. Se muestra un caso de uso real del autor: un sistema de radar de contenido con múltiples agentes investigando plataformas (LinkedIn, X, YouTube, Reddit) en paralelo, filtrado personalizado y publicación asistida.

## Puntos Clave

- **Problema que resuelve:** Un solo agente se atasca, se olvida o miente sobre haber terminado en proyectos grandes; Kanban Swarm permite dividir el trabajo entre múltiples agentes que se coordinan solos.
- **Dispatcher:** Proceso automático (no agente IA) que se ejecuta cada 60 segundos, gestiona el tablero, asigna tareas, detecta agentes caídos y reintenta fallos.
- **Heartbeat (herbit):** Cada agente envía una señal cada 30 segundos; si deja de enviarla, el dispatcher reclama la tarea y la reasigna.
- **Reclaim:** Mecanismo por el que el dispatcher recupera una tarea de un agente muerto y la reasigna.
- **Retry:** El dispatcher reintenta tareas fallidas un número limitado de veces; al agotarse, la bloquea para revisión humana.
- **Auto-descomposición (Orchestration Auto):** Un agente orquestador divide automáticamente una tarea genérica en subtareas y las asigna a subagentes según sus descripciones.
- **Columnas del tablero:** Triage → Todo (esperando dependencias) → Ready → In Progress → Done / Blocked / Archived.
- **Columna Triage:** Punto de entrada para ideas o tareas genéricas que el orquestador descompondrá.
- **Dependencias (padre/hijo):** Una tarea puede estar bloqueada esperando que otra finalice; el orquestador las construye automáticamente.
- **Workspaces (Scratch / Worktree / Dir):** Tres modos de espacio de trabajo para las tareas: temporal, copia aislada de repositorio Git, o carpeta persistente definida por el usuario.
- **Persistencia en SQLite:** Cinco tablas (`tasks`, `task_links`, `comments`, `task_events`, `task_runs`) independientes del historial de chat.
- **Human in the Loop:** Los agentes pueden bloquear tareas voluntariamente con `kanban_block` para que un humano revise antes de continuar.
- **Versión mínima recomendada:** 0.15.1 (corrige bug del dashboard presente en 0.15.0).
- **Multi-modelo:** Posibilidad de asignar modelos diferentes (mini/nano para tareas simples, modelos potentes para tareas complejas) por tarea.
- **Crons/Schedules:** Ejecución periódica automatizada de tareas a horas definidas.

## Conceptos Técnicos Mencionados

- **Hermes (No Research):** Agente de IA de código abierto (+180k estrellas en GitHub) que implementa el sistema Kanban Swarm.
- **Kanban:** Metodología de gestión visual de tareas originada en Toyota (1947); aquí adaptada para coordinar agentes de IA.
- **Kanban Swarm:** Arquitectura híbrida de Hermes que combina un orquestador planificador con un tablero compartido y un dispatcher automático.
- **Dispatcher:** Proceso de automatización (no IA) que corre cada 60s y gestiona el ciclo de vida de las tareas en el tablero.
- **SQLite:** Base de datos embebida en un único archivo; usada como almacén persistente del tablero Kanban, separada del historial de conversaciones.
- **Swarm (arquitectura):** Patrón multiagente donde los agentes se pasan tareas entre sí sin orquestador central; popularizado por OpenAI Framework Swarm (2024) y LangGraph Swarm (LangChain).
- **Orquestador (arquitectura):** Patrón multiagente con un agente central que delega a subagentes y recoge resultados.
- **Heartbeat / Herbit:** Señal periódica (cada 30s) que cada agente envía para indicar que sigue activo.
- **Reclaim:** Mecanismo del dispatcher para recuperar tareas de agentes caídos.
- **Retry:** Mecanismo del dispatcher para reintentar tareas fallidas con límite de intentos.
- **Human in the Loop:** Patrón de diseño donde el agente pausa y solicita revisión humana antes de continuar.
- **Worktree (Git):** Copia aislada de un repositorio Git para que múltiples agentes trabajen en código en paralelo sin conflictos.
- **Profiles (Hermes):** Definición de agentes con nombre, descripción y skills; usados por el orquestador para asignar subtareas.
- **Barra Goal (`/goal`):** Comando en el chat para dar un objetivo explícito al agente y evitar que se desvíe.
- **Checkpoints:** Mecanismo de guardado del estado de sesión para recuperación posterior.
- **Crons/Schedules:** Tareas programadas para ejecución periódica en horarios definidos.
- **Dashboard de Hermes:** Interfaz web para visualizar y gestionar el tablero Kanban, tareas, agentes y métricas.
- **Telegram / Discord (integración):** Canales de comunicación alternativos al dashboard para interactuar con los agentes y el tablero.
- **N8N:** Plataforma de automatización mencionada como parte del ecosistema del autor (no directamente en Kanban Swarm).
- **Versión 0.13 "Tenacity":** Versión de Hermes que introdujo el Kanban multiagente de forma profesional (7 de mayo).
- **Versión 0.15 "Velocity":** Versión que añadió auto-descomposición, reducción de tiempos drástica y comando `hermes kanban setup` (28 de mayo).

## Fragmentos Relevantes

> *"Cuando quieres crear un proyecto muy grande o complejo, normalmente un solo agente no es capaz. Se atasca, se olvida de lo que está haciendo o incluso te dice que ya ha terminado cuando no es verdad."*

> *"El dispatcher básicamente tenéis que verlo como si fuera un gerente que va a gestionar el kanban. Es un código que se ejecuta cada 60 segundos y de lo que se encarga es de repartir las tareas en los agentes que haya, moverlas de columna en columna y revisar que ningún agente se quede colgado."*

> *"Esta base de datos es un archivo aparte, independiente de tus conversaciones. Esto permite que aunque tú borres tus conversaciones, apagues el servidor o pierdas la conexión, tú no vas a perder el kanban."*

> *"No es un swarm puro porque estos agentes no se pueden comunicar entre ellos tampoco. Y tampoco es un orquestador porque no pasa todo por él, él solamente planifica al principio y ya se desentiende. Entonces es una mezcla entre uno y otro, por eso he dicho que es como híbrido."*

> *"Scratch es como una carpeta temporal. En cuanto acabe la tarea se elimina. Worktree es una copia aislada de un repositorio de Git [...] para cuando quieres crear varias tareas de código a la vez, pues que no se pisen unas entre otras. Dir es para que tú pongas una dirección de una carpeta tuya [...] donde quieras que se guarde la tarea o el resultado de la tarea."*

> *"La tarea ha sido completada correctamente, pero esto es lo que se conoce como el human in the loop. A pesar de que está bien, me lo bloquea y la gente ha utilizado la herramienta de blocked [...] para que yo mismo la revise manualmente."*

## Conclusiones y Aprendizajes

- **Diseña equipos de agentes antes de crear tareas:** Crear primero los profiles/agentes con descripciones claras permite que el orquestador asigne subtareas de forma inteligente. Para proyectos de software, pensar en roles como backend, frontend, seguridad, QA.
- **Usa workspaces persistentes (`Dir`) para tareas que producen artefactos:** Solo así los resultados sobreviven al ciclo de vida de la tarea. `Scratch` es solo para trabajo temporal de subtareas intermedias.
- **Modela dependencias explícitamente:** Declarar relaciones padre/hijo entre tareas evita que un agente intente ejecutar algo para lo que aún no tiene input, ahorrando tokens y errores.
- **El dispatcher no es IA, es determinismo:** Su comportamiento es predecible y auditable; entenderlo es clave para diagnosticar por qué una tarea se bloquea o se reasigna.
- **Human in the Loop como patrón de seguridad:** Instruir a los agentes a bloquear tareas críticas antes de ejecutar acciones irreversibles (publicar, desplegar, enviar) es una buena práctica de producción.
- **La persistencia en SQLite desacopla el tablero del chat:** Puedes reiniciar el servidor, cambiar de conversación o incluso cambiar de modelo sin perder el estado del proyecto.
- **Casos de uso de alto valor comercial identificados:** Sistema de vigilancia multicliente con borradores para aprobación humana; fábrica de contenido automatizada (investigación → guion → publicación); organización automatizada de correo; radar de ofertas de empleo.
- **Versión mínima recomendada para usar Kanban:** 0.15.1 de Hermes para evitar bugs conocidos del dashboard.

---
> Generado automáticamente para uso como contexto en Cursor / Claude Code