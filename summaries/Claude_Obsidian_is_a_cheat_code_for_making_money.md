# Claude + Obsidian is a cheat code for making money

## Información General
- **Canal:** Matthew Online
- **Duración:** 14m 15s
- **Idioma detectado:** Inglés

## Resumen Ejecutivo
El video presenta la combinación de Claude (AI de Anthropic) y Obsidian (aplicación de notas) como una oportunidad de negocio significativa. El autor argumenta que la mayoría de los dueños de negocios desconocen las capacidades avanzadas de Claude, lo que crea una ventana de oportunidad para quienes sí saben utilizarlo: pueden ofrecer servicios de implementación de IA a empresas que necesitan modernizarse pero no tienen tiempo o conocimiento para hacerlo.

La propuesta técnica central es usar Obsidian como "segundo cerebro" que provee contexto persistente a Claude. En lugar de cargar documentos repetidamente en cada sesión —lo que consume el límite de uso (tokens/créditos)—, Obsidian almacena localmente toda la información relevante del negocio y la sirve a Claude de forma eficiente bajo demanda. Esto convierte a Claude en un asistente que ya "conoce el negocio" desde el primer momento.

El autor ilustra el potencial con un caso de uso concreto: ofrecer servicios de IA a despachos de abogados, donde se podrían indexar miles de documentos de jurisprudencia en Obsidian y permitir que Claude los consulte eficientemente, reemplazando el trabajo de paralegales y abogados junior.

## Puntos Clave
- **Claude vs ChatGPT:** Claude tiene capacidades adicionales como "Computer Use" (co-work), que permite delegar tareas mientras el usuario trabaja en otra cosa.
- **El problema del contexto:** Sin memoria persistente, cada sesión con Claude obliga a re-explicar el negocio, lo que es ineficiente a escala.
- **Obsidian como solución:** Actúa como base de conocimiento local que Claude puede consultar sin consumir todo el límite de uso de una vez.
- **Dos modelos de monetización:** (1) Uso interno para acelerar el propio negocio, (2) Venta de servicios de implementación de IA a otras empresas.
- **Pitch emocional vs. lógico:** Los dueños de negocio compran cuando ven algo que los emociona (demo en vivo), no cuando escuchan descripciones abstractas de servicios.
- **Automatización de contexto:** Es posible configurar tareas programadas para que Claude transcriba videos de Loom o llamadas de Zoom y los añada automáticamente a Obsidian.
- **Planes de Claude:** Free → Pro → Max ($100/mes, 5x uso) → Max 20x ($200/mes). Para uso serio en negocios, el autor recomienda Max.
- **Caso legal:** Despachos de abogados son un sector con alto poder adquisitivo y urgencia de adoptar IA para no quedarse atrás.

## Conceptos Técnicos Mencionados
- **Claude (Anthropic):** LLM con interfaz de chat y capacidades de agente; disponible en Claude.ai o como app de escritorio.
- **Claude Computer Use / Co-work:** Funcionalidad de agente autónomo que ejecuta tareas de forma asíncrona mientras el usuario trabaja en otro proceso.
- **Obsidian:** Aplicación de notas local, gratuita, basada en archivos Markdown; actúa como base de conocimiento persistente (vault).
- **Vault (Obsidian):** Carpeta local que contiene todas las notas en formato `.md`; se puede conectar a Claude para proveer contexto.
- **Claude MD file:** Archivo de instrucciones dentro del vault de Obsidian que le explica a Claude cómo interpretar y usar los documentos almacenados.
- **Context window / límite de uso:** Restricción en la cantidad de tokens que Claude puede procesar por sesión; subir muchos archivos repetidamente lo agota rápidamente.
- **Loom:** Herramienta de grabación de pantalla/video asíncrono; el autor la usa para generar transcripciones que se alimentan a Obsidian.
- **Automatización de transcripciones:** Pipeline donde Claude transcribe videos de Loom automáticamente y escribe los resultados en el vault de Obsidian mediante tareas programadas.
- **RAG implícito (Retrieval-Augmented Generation):** El patrón descrito (indexar documentos en Obsidian → Claude consulta solo lo relevante) es funcionalmente equivalente a RAG sin nombrarlo explícitamente.

## Fragmentos Relevantes
> "Having Claude on its own is basically like having a plumber call out to your house for the first time. They're really skilled. They can do the job, but they don't really know anything about your house [...] Now, imagine that same plumber has been maintaining your house for 10 plus years. They know exactly where everything is. That's essentially what Obsidian does for Claude."

> "If you were to upload loads and loads of files to Claude, every single time you ask it a question, Claude will typically use all of those files immediately and it will basically burn through your usage. However, with Obsidian, it can basically do the same thing except it doesn't burn all of your usage."

> "People will pitch to the logical brain of the business owner [...] But nobody gets excited about that because there's no emotion in saying 'I can build you a website.' So, you need to pitch to the emotional brain. When you can show a business owner Claude plus Obsidian working together doing things that they didn't even know were possible, they will get excited."

> "I set up a schedule where Claude will transcribe every Loom video I make day-to-day and it will add that transcript to my Obsidian folder, which means Obsidian now has notes on the problems I'm working on every single day. And so the context it has on my business increases every single day without me even having to do anything."

## Conclusiones y Aprendizajes
- **Patrón de contexto persistente:** Mantener un vault de Obsidian con información del proyecto (decisiones, procesos, personas clave, transcripciones de reuniones) elimina la fricción de re-contextualizar a Claude en cada sesión. Aplicable en cualquier proyecto de software con muchos documentos o reuniones recurrentes.
- **Pipeline de captura de conocimiento:** Automatizar la transcripción de reuniones (Zoom, Loom, Meet) hacia Obsidian es una práctica concreta e implementable hoy; Claude puede configurar esa automatización si se le pide.
- **Modelo de agencia de IA:** El esquema negocio de "AI partner" —entrar a una empresa, auditar departamentos e implementar IA— es replicable. Los sectores con documentación masiva (legal, médico, inmobiliario, finanzas) son los más rentables.
- **Gestión del límite de tokens:** El patrón Obsidian-como-retrieval evita saturar la ventana de contexto; útil para proyectos que manejan grandes corpus de documentos (bases de código, documentación, expedientes).
- **Demo como estrategia de venta:** Para proyectos internos o clientes, mostrar el sistema funcionando en vivo es más efectivo que cualquier propuesta escrita.

---
> Generado automáticamente para uso como contexto en Cursor / Claude Code