# This MCP makes Hermes Agent 10x more powerful

## Información General
- **Canal:** David Ondrej
- **Duración:** 22m 26s
- **Idioma detectado:** Inglés
- **Transcripción fuente:** `This_MCP_makes_Hermes_Agent_10x_more_powerful.txt`

## Resumen Ejecutivo
El video muestra cómo potenciar el agente Hermes (uno de los agentes de IA más populares en GitHub con casi 200,000 estrellas) conectándolo con Apify a través de MCP Connectors. Apify es una plataforma con más de 40,000 scrapers ("actors") capaces de extraer datos de sitios como LinkedIn, Instagram, Google Maps, Reddit y otros que normalmente bloquean agentes automáticos. La integración se logra sin código complejo, usando configuración desde el navegador y comandos en terminal.

El flujo técnico completo que se demuestra es: ejecutar un actor de Apify (scraper de LinkedIn) → guardar los resultados en una tabla de Supabase mediante un MCP Connector → conectar Hermes Agent a esa base de datos → que el agente analice, puntúe y cualifique los leads automáticamente → automatizar todo el ciclo con un cron job en Hermes y un schedule en Apify. El caso de uso concreto es el de un pipeline de selección de candidatos técnicos para una oficina en Katowice (Polonia).

El resultado final es un sistema completamente autónomo que cada 6 horas busca nuevos perfiles en LinkedIn, los almacena en Supabase, y cada mañana Hermes los puntúa del 0 al 100, razona sobre su idoneidad y envía un resumen de los mejores candidatos, todo a un coste de pocos dólares por semana en lugar de miles en salarios de recruiters.

## Puntos Clave
- **Hermes Agent** se instala con un solo comando desde su repositorio de GitHub
- **Apify** actúa como capa de scraping universal: más de 40,000 actors para cualquier web
- Los **MCP Connectors de Apify** permiten conectar el resultado de un actor directamente con Supabase, GitHub, Notion, etc., sin escribir código de integración
- El actor específico de LinkedIn usado no requiere login ni cookies, reduciendo el riesgo de ban
- Los datos se almacenan en Supabase en formato JSON estructurado, ideal para que los agentes los procesen
- Hermes Agent puede leer y escribir en Supabase usando solo la `PROJECT_URL` y la `service_role key`
- El agente puntúa candidatos (0–100), escribe el score de vuelta en la tabla y genera un digest diario de los top 5
- El ciclo se automatiza: **Apify Schedule** (cada 6 horas) + **cron job de Hermes** (cada mañana a las 8 AM)
- El patrón es reutilizable para leads B2B, análisis de competidores, oportunidades de empleo, reseñas de locales, etc.
- Los secrets (claves de API, URL de Supabase) se guardan en el gestor de variables de entorno de Hermes Agent

## Conceptos Técnicos Mencionados
- **Hermes Agent** — Agente de IA de código abierto con ~200k estrellas en GitHub, instalable con un solo comando, con soporte para múltiples LLM providers
- **Apify** — Plataforma de web scraping con más de 40,000 actors preconfigurados; permite scraping de sitios restrictivos sin gestionar infraestructura propia
- **Apify Actors** — Scrapers/automatizaciones individuales disponibles en el Apify Store (LinkedIn, TikTok, Instagram, Google Maps, etc.)
- **Apify MCP Connectors** — Nuevo producto de Apify que conecta actors con destinos externos (Supabase, GitHub, Notion) usando el protocolo MCP
- **MCP (Model Context Protocol)** — Protocolo estándar para conectar herramientas externas con agentes de IA de forma interoperable
- **Supabase** — Base de datos Postgres en la nube con API REST y SDK; usada aquí como almacén de leads scrapeados
- **Universal MCP Actor (Apify)** — Actor especial de Apify que actúa como puente MCP entre un dataset y un destino externo, orquestado por un LLM
- **LangChain Tools** — Framework usado internamente por el Universal MCP Actor para convertir herramientas MCP en herramientas LangChain ejecutables
- **Cron Job (Hermes)** — Funcionalidad de Hermes Agent para programar tareas recurrentes; se configura en lenguaje natural y el agente genera el comando cron
- **Apify Saved Tasks** — Presets de configuración reutilizables para actors, que luego se asocian a schedules automáticos
- **Apify Schedules** — Sistema de ejecución periódica de actors/tasks dentro de la consola de Apify
- **OpenRouter** — Servicio de acceso unificado a múltiples modelos LLM (GPT, Claude, Gemini, etc.) mediante una sola API key
- **Claude Sonnet / Gemini Flash** — Modelos LLM usados en el Universal MCP Actor para razonar sobre los datos del dataset
- **service_role key (Supabase)** — Clave secreta con acceso total a la base de datos Supabase; usada por Hermes para leer/escribir sin restricciones RLS
- **Row Level Security (RLS)** — Sistema de políticas de acceso por fila en Supabase; mencionado como potencial obstáculo a configurar

## Fragmentos Relevantes

> *"Apify is one of the first tools you want to connect to any AI agent you build so that you make it instantly 10 times more powerful."*

> *"This is like the stuff that AI agents dream of. Structured JSON that's easy to understand, that's easy to work with."*

> *"Instead of me wasting time interviewing all these people or reaching out to them, Hermes agent figured out these two people are worth interviewing and these three are not."*

> *"This is going to be costing a few dollars per week and it's going to save thousands of dollars per week in terms of salaries."*

> *"Sit down and think: where can I implement scraping with Apify and Hermes so that my life is advancing faster? What problems can I solve with just a simple Apify actor?"*

> *"You can tell Hermes agent to help you set this up, to guide you, what it needs from you."*

## Conclusiones y Aprendizajes

- **Patrón replicable inmediatamente**: el flujo Apify Actor → MCP Connector → Supabase → Hermes Agent es un pipeline genérico que puede adaptarse a cualquier caso de uso que requiera scraping + análisis de datos.
- **Zero-code para la integración**: el MCP Connector de Apify elimina la necesidad de escribir ETL manual; el Universal MCP Actor usa un LLM para mapear y guardar datos automáticamente.
- **Hermes como orquestador local**: al guardar las credenciales en su gestor de variables de entorno, Hermes puede actuar como capa de lógica de negocio sobre cualquier base de datos Supabase.
- **Automatización en dos capas**: el scraping se programa en Apify (nivel de datos) y el análisis se programa en Hermes (nivel de agente), dando un sistema completamente autónomo.
- **Aplicable a múltiples dominios**: el mismo stack sirve para generación de leads B2B, monitoreo de precios de competidores, análisis de reseñas, búsqueda de empleo, research de mercado o cualquier tarea que requiera datos web estructurados.
- **Seguridad**: las claves de API y tokens de acceso personal deben tener expiración corta durante el desarrollo; la `service_role key` de Supabase nunca debe exponerse públicamente.

---
> Generado automáticamente para uso como contexto en Cursor / Claude Code