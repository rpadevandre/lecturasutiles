# Claude Code + Playwright Crea Agentes de IA Web (Automatiza TODO)

## Información General
- **Canal:** Juan Pe Navarro | IA y Automatización
- **Duración:** 19m 39s
- **Idioma detectado:** Español

## Resumen Ejecutivo
El video explica cómo combinar **Claude Code** con **Playwright CLI** para crear agentes de inteligencia artificial capaces de controlar un navegador web de forma autónoma, realizando tareas como responder comentarios en YouTube, hacer QA de landing pages, extraer leads de Google Maps o scraping de portales sin API oficial. Se presenta como una solución superior a otras alternativas (MCP, AI Browser, extensión de Claude en Chrome) por su eficiencia en consumo de tokens (~27,000 tokens/tarea vs 114,000 del MCP).

El flujo de trabajo central es: el usuario describe la tarea en lenguaje natural → Claude Code escribe el script → Playwright ejecuta las acciones en el navegador real → si falla, el agente itera y corrige → cuando funciona, guarda la lógica como una "skill" reutilizable. El video incluye una demo práctica extrayendo datos de fisioterapeutas en Madrid desde Google Maps (nombre, web, teléfono, email).

Se destacan además dos complementos recomendados para hacer el stack más robusto: el **Sequential Thinking MCP** (obliga al agente a planificar antes de actuar) y una **skill personalizada** descargable que optimiza el comportamiento del agente con Playwright en Claude Code.

## Puntos Clave
- **Playwright CLI** es la forma más eficiente de conectar Claude Code con el navegador (27K tokens vs 114K del MCP)
- El agente puede operar en cualquier web aunque **no tenga API oficial**, simulando comportamiento humano
- Se puede iterar en tiempo real: corregir el agente mientras navega sin reescribir código manualmente
- Las **skills** permiten reutilizar flujos ya validados en ejecuciones futuras automáticamente
- El **Sequential Thinking MCP** evita decisiones impulsivas del agente al forzar planificación previa
- Compatible con Claude Code, GitHub Copilot y Cursor
- Funciona con Chrome, Firefox y otros navegadores
- Casos de uso monetizables: QA de webs (800–1500 €/proyecto), lead generation (200–800 €/campaña), gestión de comunidades (400–1000 €/mes)
- Hace 2 años requerías tester + especialista en scraping + community manager; hoy un agente puede cubrir los tres roles

## Conceptos Técnicos Mencionados
- **Playwright CLI** — Interfaz de línea de comandos de Playwright, eficiente en tokens, lanzada recientemente por Microsoft para agentes de codificación
- **Playwright MCP** — Versión anterior de integración vía Model Context Protocol; funcional pero consume ~4x más tokens por volcar todo el estado del navegador
- **Claude Code** — Agente de codificación de Anthropic que escribe y ejecuta scripts de automatización desde VS Code
- **Sequential Thinking MCP** — MCP oficial que fuerza al agente a planificar y revisar pasos antes de ejecutar acciones en el navegador
- **CDP (Chrome DevTools Protocol)** — Protocolo usado por Playwright para conectarse a una instancia real de Chrome sin abrirlo manualmente
- **Skills (Claude Code)** — Archivos ocultos (`.claude`) que encapsulan flujos validados para reutilización automática; se distribuyen comprimidos en ZIP
- **Apify** — Marketplace de APIs no oficiales/scrapers; mencionado como alternativa menos estable al enfoque con Playwright
- **AI Browser / Agent Browser** — Herramienta alternativa de automatización web; ~200 tokens/página pero menor fiabilidad
- **Visual Studio Code** — IDE desde el que se lanza Claude Code para gestionar el proyecto
- **Google Maps scraping** — Caso de uso demo: extracción de contactos de negocios (nombre, teléfono, email, web)

## Fragmentos Relevantes
> "Básicamente ahora puedes crear cualquier agente de inteligencia artificial con Claude Code que entre a cualquier página web, maneje tu navegador y haga cualquier cosa que le pidas."

> "Playwright MCP consume por tarea aproximadamente unos 114,000 tokens y la CLI, que es lo recomendado, consume aproximadamente unos 27,000 tokens por tarea."

> "Cloud Code escribe el script. Ese script lo va a ejecutar mediante Playwright y el script de Playwright va a abrir el navegador, va a ejecutar lo que le has pedido. Si falla, tú puedes corregir y puedes ir iterando en tiempo real con el propio agente."

> "Cuando funciona y ve que algo está bien hecho, pues se guarda como una skill para ese caso concreto y la próxima vez pues ejecuta la skill automáticamente."

> "Hace 2 años necesitabas un equipo para hacer lo que hemos hecho hoy. Un tester, un especialista en scraping, un community manager, tres personas, tres salarios y hoy un agente conectado a un navegador puede hacer estas tres cosas."

> "El MCP vuelca todo el estado completo del buscador en cada interacción. La CLI solamente envía los comandos."

## Conclusiones y Aprendizajes
- **Usar Playwright CLI sobre MCP** para cualquier proyecto de automatización web con Claude Code; ahorra ~75% de tokens por tarea.
- **Instalar Sequential Thinking MCP** como dependencia estándar en proyectos de agentes web para reducir errores de navegación impulsivos.
- **Distribuir skills como ZIP** si se trabaja en equipo o se quieren compartir flujos validados; los archivos ocultos de `.claude` no sobreviven en Google Drive sin comprimir.
- **El patrón ideal para scrapers sin API**: iniciar Chrome con CDP → Claude Code genera el script → iterar en lenguaje natural → guardar como skill reutilizable.
- **Modelo de negocio directo**: el stack Playwright CLI + Claude Code es suficiente para ofrecer servicios de QA automatizado, lead generation y gestión de comunidades a empresas sin necesidad de un equipo técnico dedicado.
- Para proyectos donde la web requiere autenticación, el flujo de "iniciar sesión manualmente y avisar al agente" es una práctica válida y documentada en el video.

---
> Generado automáticamente para uso como contexto en Cursor / Claude Code