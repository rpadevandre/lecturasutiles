# HERMES Agent acaba de LIBERAR las METAS persistentes GRATIS y SIN LÍMITE🔓 (/goals)

## Información General
- **Canal:** Appsclavitud w VeraBadías
- **Duración:** 24m 46s
- **Idioma detectado:** Español
- **Transcripción fuente:** `HERMES_Agent_acaba_de_LIBERAR_las_METAS_persistentes_GRATIS_.txt`

## Resumen Ejecutivo
El video presenta la nueva característica **Goals (Metas Persistentes)** de Hermes Agent, un agente de IA de código abierto. La autora explica qué son los Goals, cómo se diferencian de otras características como Cron Jobs y Kanban, y cómo utilizarlos de manera práctica para automatizar tareas de larga duración (desde minutos hasta semanas o incluso meses) sin costo prohibitivo, apoyándose en modelos de IA chinos como Minimax o Kimi como alternativa económica a GPT o Claude.

La metodología central propuesta es el **metaprompting previo**: antes de correr un Goal, se le pide a la IA que optimice y estructure el objetivo a partir de referencias (documentación oficial, URLs relevantes, contexto del proyecto), para luego pasar a ejecución autónoma. El ejemplo concreto demostrado es una campaña de SEO + GEO para posicionar un enlace de comunidad en Google. Se cubre también el setup recomendado: VPS con Hostinger + Tailscale para mayor seguridad, y la opción gratuita con OLAMA + Qwen 3.5 localmente.

Se distinguen tres modos de automatización en Hermes: **Goals** (orientado a resultado final, sin ruta predefinida), **Cron Jobs** (tareas calendarizadas recurrentes) y **Kanban** (orquestación visual de tareas con múltiples agentes). La selección entre ellos depende del tipo de tarea.

## Puntos Clave
- **Goals ≠ planificación convencional**: en vez de darle al agente una ruta paso a paso, se le proporciona únicamente el destino/resultado esperado, y él determina cómo llegar.
- **Herencia conceptual de RALPH**: Goals es similar al proyecto open source RALPH, que implementa un bucle de análisis con un modelo "juez" que acepta o rechaza outputs según criterios predefinidos.
- **Metaprompting obligatorio**: antes de ejecutar un Goal, se recomienda pedirle al agente que genere y optimice el Goal con base en la documentación oficial y referencias relevantes.
- **Modelos chinos como solución de costo**: Minimax y Kimi 2.6 ofrecen ventanas de tokens muy superiores a GPT o Claude para este tipo de tareas de larga duración, reduciendo el costo drásticamente.
- **Opción 100% gratuita**: OLAMA + Qwen 3.5 (u otros modelos locales como Gemma 4), aunque con menor calidad y mayor latencia.
- **VPS recomendado**: Hostinger KVM2 con Tailscale para correr Hermes de forma segura, evitando exponer credenciales en el equipo local.
- **Goals también disponibles en Claude Code y Codex** (OpenAI), no solo en Hermes.
- **Cron Jobs**: tareas recurrentes programadas por tiempo (ej: envío de señales de trading bots, análisis de canales de YouTube cada X horas).
- **Kanban**: gestión visual de tareas con múltiples agentes y roles, útil para orquestación más compleja.
- **Criterio de selección**: disparado por horario → Cron Job; múltiples agentes/roles → Kanban; objetivo final sin restricción de ruta → Goal.
- Un Goal puede correr durante **155+ horas** según el ejemplo mencionado de un usuario en Codex.

## Conceptos Técnicos Mencionados
- **Hermes Agent**: agente de IA open source, el repositorio de código relacionado con IA más exitoso en GitHub según el video; soporta Goals, Cron Jobs y Kanban.
- **Goals (Metas Persistentes)**: característica de Hermes que mantiene un objetivo activo con un modelo juez que verifica criterios de éxito de forma continua sin ruta predefinida.
- **RALPH**: proyecto open source precursor que implementa un bucle de análisis/retroalimentación con modelo juez para aceptar o rechazar outputs.
- **Metaprompting**: técnica de usar un prompt inicial para que la IA genere o refine el prompt/goal optimizado antes de la ejecución real.
- **Cron Jobs (Hermes)**: tareas calendarizadas programáticas dentro de Hermes; equivalente a cron de Unix pero orquestado por el agente.
- **Kanban (Hermes GUI)**: vista de pizarra visual dentro de la interfaz de Hermes para gestionar y mover tareas manualmente.
- **OLAMA**: runtime local para modelos de lenguaje open source; permite correr Hermes sin costo de API.
- **Qwen 3.5 (Quin 3.5)**: modelo de lenguaje open source chino ejecutable localmente vía OLAMA.
- **Minimax**: proveedor de modelos de IA chino con planes de API muy económicos y grandes ventanas de tokens.
- **Kimi 2.6 (Kimica 2.6)**: modelo de IA chino de Moon AI, alternativa económica a GPT/Claude para tareas de agentes.
- **Gemma 4**: modelo open source de Google, alternativa no china ejecutable localmente.
- **Claude Code (Cloud Code)**: interfaz de agente de Anthropic que también soporta la característica Goals.
- **Codex (OpenAI)**: plataforma de OpenAI que también implementa Goals persistentes.
- **VPS (Servidor Privado Virtual)**: entorno recomendado para correr Hermes de forma segura; se menciona Hostinger KVM2 como opción.
- **Tailscale**: herramienta de red privada basada en WireGuard/SSH para securizar el acceso al VPS donde corre Hermes.
- **Docker**: contenedores usados por Hostinger para desplegar Hermes en el VPS.
- **Whisper**: modelo de transcripción de audio de OpenAI; usado en el video para convertir instrucciones de voz en prompts de texto.
- **SEO / GEO (Generative Engine Optimization)**: estrategias de posicionamiento web convencional y orientado a motores de búsqueda con IA, usadas como caso de uso de ejemplo del Goal.
- **Open Spec / Spec Driven Development**: metodología de planificación de desarrollo mencionada como alternativa conceptual a Goals.

## Fragmentos Relevantes
> *"En vez de darle una ruta de navegación, lo que le estamos dando solamente es el destino."*

> *"Goals necesita utilizar un poco de metaprompting. Necesitamos filtrar y optimizar el goal antes de correrlo."*

> *"No le he dicho 'Ve directamente y implementa un goal', sino más bien 'Okay, esto es lo que necesito que tú hagas. Tengo perfectamente claro el resultado que quiero palpar después de tu trabajo. Dame el goal optimizado con base en estas referencias.'"*

> *"La más importante es la documentación oficial porque es la fuente de verdad más importante, en donde todo lo demás tiene que calzar."*

> *"En cuestión de decenas de ejecuciones en miles de líneas de código generado, el uso de mi plan particular habrá reducido en aproximadamente 8 o 9% de la ventana de 5 horas."* (refiriéndose a Minimax vs GPT/Claude)

> *"Goal acknowledged — he reconocido el goal iniciando la verificación y ejecutando para cumplir todos los criterios."*

> *"Si se dispara por tiempo y por horario → Cron Job. Los trabajos son varios con agentes y roles → Kanban. Si esto no es ninguna de las dos → Goal."*

## Conclusiones y Aprendizajes
- **Para tareas de larga duración autónomas**: usa Goals en lugar de prompts encadenados manualmente. Define únicamente el criterio de éxito (el "qué"), no los pasos (el "cómo").
- **Flujo recomendado de implementación**:
  1. Graba o escribe tu objetivo en crudo (no importa si es vago).
  2. Realiza una sesión de metaprompting: pega la documentación oficial de Goals + tu objetivo + URLs de contexto y pide al agente que genere el Goal optimizado.
  3. Limpia el contexto (`/new`) y ejecuta el Goal con `/goal`.
  4. Deja correr sin supervisión continua.
- **Gestión de costos**: para proyectos personales o exploración, Minimax o Kimi son viables económicamente para tareas de agentes de larga duración; OLAMA + Qwen/Gemma para entornos sin presupuesto.
- **Seguridad en producción**: nunca correr Hermes en equipo local con credenciales sensibles; preferir VPS + Tailscale.
- **Distinción operativa clara**: antes de automatizar, preguntarse si la tarea es recurrente por tiempo (→ Cron Job), requiere orquestación multi-agente visual (→ Kanban) o simplemente necesita alcanzar un estado final sin restricción de ruta (→ Goal).
- **La documentación oficial del agente debe incluirse siempre** en el metaprompt inicial, ya que el modelo puede no conocer features recientes de manera nativa.

---
> Generado automáticamente para uso como contexto en Cursor / Claude Code