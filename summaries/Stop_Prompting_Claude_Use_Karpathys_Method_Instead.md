# Stop Prompting Claude. Use Karpathy's Method Instead.

## Información General
- **Canal:** Austin Marchese
- **Duración:** 13m 18s
- **Idioma detectado:** Inglés (en)
- **Transcripción fuente:** `Stop_Prompting_Claude_Use_Karpathys_Method_Instead.txt`

## Resumen Ejecutivo
El video desglosa el método de Andrej Karpathy (ex-director de IA en Tesla) para usar modelos de IA de forma efectiva, presentado originalmente en AISN 2026. El argumento central es que la mayoría de personas usa Claude (y modelos similares) de forma incorrecta porque los trata como si fueran humanos con motivaciones intrínsecas, cuando en realidad son sistemas estadísticos que solo pueden operar dentro de los límites de su contexto y datos disponibles.

El método se estructura en tres capas: **Spec** (especificación detallada del problema y contexto), **Verifier** (proceso de verificación explícita del output), y **Environment** (el entorno y sistema de trabajo que potencia ambas capas). Cada capa aborda una debilidad específica de los LLMs: la falta de contexto, la imposibilidad de autoevaluar outputs subjetivos, y la pérdida de estado entre sesiones.

La conclusión filosófica del video es que en la era de la IA barata, lo que no se puede delegar es la *comprensión profunda*: entender los objetivos, el dominio, y el impacto de lo que se construye. Las tres capas del método son, en esencia, formas de inyectar esa comprensión en el sistema de IA.

## Puntos Clave

- **AI falla en contexto implícito**: La prueba del "car wash a 50m" ilustra que los LLMs no tienen acceso a contexto que damos por obvio (necesitas el auto en el car wash). El spec existe para cerrar esa brecha.
- **Layer 1 — El Spec**: Documento detallado y estructurado que comunica tu comprensión al modelo. Tres pasos: (1) descubrir el objetivo real (no la tarea superficial), (2) trabajar en modo ágil con scopes pequeños, (3) ser preciso para minimizar asunciones del modelo.
- **Layer 2 — El Verifier**: Definir criterios de evaluación antes de que el modelo empiece a trabajar. Usar un segundo modelo como crítico. Conectar señales externas para verificación objetiva (ej: conectar Claude a tu sistema de deployment para confirmar que algo realmente fue desplegado).
- **Layer 3 — El Environment**: Infraestructura persistente que incluye: Claude.md configurado, una knowledge base personal (LLM knowledge base de Karpathy), skills/habilidades reutilizables, y guardrails a nivel de herramienta (no solo de prompt).
- **Guardrails a nivel de herramienta**: Un `pre-tool use hook` que bloquea ediciones a archivos críticos es una regla real; una instrucción en Claude.md es solo una sugerencia que puede ser ignorada.
- **Feedback loop = 2-3x calidad**: Según Boris Cherney (creador de Claude Code), si Claude tiene un feedback loop, la calidad del resultado se multiplica por 2 o 3.
- **La única cosa que no se puede delegar**: "You can outsource your thinking, but you can't outsource your understanding." — Karpathy

## Conceptos Técnicos Mencionados

- **Claude (Anthropic)** — Modelo LLM principal usado en los ejemplos del video
- **Claude Code** — Entorno de desarrollo con agente AI de Anthropic para coding
- **Claude.md** — Archivo de configuración que se inyecta automáticamente en cada sesión de Claude Code; define reglas, arquitectura y comportamiento esperado
- **Plan Mode (Claude)** — Función de Claude para generar un plan antes de ejecutar; el video lo considera demasiado superficial sin un spec detallado
- **LLM Knowledge Base** — Concepto de Karpathy: sistema de carpetas locales con datos propios estructurados para que el LLM los consuma como contexto
- **Codex (OpenAI)** — Modelo alternativo usado como "segundo revisor" dentro de una sesión de Claude Code mediante plugin
- **Pre-tool use hooks** — Mecanismo en Claude Code para interceptar acciones del agente antes de que se ejecuten (ej: bloquear escritura en archivos críticos)
- **Agile specking** — Aplicación de metodología ágil a la creación de specs: scopes pequeños, checkpoints frecuentes, revisión iterativa
- **Waterfall vs Agile** — Comparación de metodologías aplicada al uso de AI agents: waterfall = dar todo a la vez; agile = iterar en pequeños bloques
- **Custom Skills** — Plantillas o "handbooks" reutilizables para tareas repetitivas dentro del environment de Claude
- **Feedback loop (AI evaluation)** — Concepto de que conectar la evaluación del output de vuelta al modelo mejora sustancialmente la calidad final

## Fragmentos Relevantes

> "I want to go to a car wash to wash my car, and it's 50m away. Should I drive or should I walk? And state-of-the-art models today will tell you to walk because it's so close."
— Karpathy, ilustrando el problema de contexto implícito

> "I actually don't even like the plan mode. I think there's something more general here where you have to work with your agent to design a spec that is very detailed."
— Karpathy sobre por qué el plan mode no es suficiente

> "If Claude has a feedback loop, it will two to three x quality of the final result."
— Boris Cherney, creador de Claude Code

> "Make this your environment. It's your world, and AI is living in it. It should not feel like the other way around."
— Austin Marchese, sobre la mentalidad correcta al configurar el environment

> "The best way to find a leak in a hose is to run water through it."
— Marchese, sobre iterar y mejorar skills reutilizables

> "You can outsource your thinking, but you can't outsource your understanding."
— Karpathy, sobre qué sigue siendo valioso aprender en la era de la IA

## Conclusiones y Aprendizajes

- **Escribe specs detallados antes de codear**: En lugar de pedirle a Claude que "construya X", entrevístate con él primero para clarificar el objetivo real, luego escribe un spec preciso. Prompt sugerido: *"Interview me to identify the goal of this project."*
- **Define criterios de éxito antes de ejecutar**: Añade al prompt inicial: *"Outline the evaluation criteria you will use to ensure a high-quality final product. Be precise."* Esto fuerza al modelo a tener una barra de calidad explícita.
- **Usa un segundo modelo como crítico**: Si el output es complejo o crítico, pásalo por otro modelo (ej: Codex) para obtener una perspectiva independiente.
- **Configura tu Claude.md como primer paso de cualquier proyecto**: Incluye reglas de verificación obligatoria, arquitectura del repositorio, y guardrails. Una vez configurado, aplica a todas las sesiones sin esfuerzo adicional.
- **Separa instrucciones de reglas reales**: Las instrucciones en Claude.md son guías (80% de cumplimiento). Para comportamientos críticos (no tocar archivos de producción, no inventar datos), usa `pre-tool use hooks` que bloquean a nivel de herramienta.
- **Construye tu knowledge base propia**: Crea una estructura de carpetas con tu documentación, históricos, y datos propios. Es tu "moat" de datos que ningún competidor puede replicar.
- **Si algo se repite, conviértelo en skill**: Las skills reutilizables se refinan con el uso y hacen que el sistema mejore con el tiempo (efecto compounding).
- **Trabaja en modo ágil con AI**: Nunca le des a un agente AI un scope enorme de una sola vez. Divide en tareas pequeñas con checkpoints de revisión humana entre cada una.

---
> Generado automáticamente para uso como contexto en Cursor / Claude Code