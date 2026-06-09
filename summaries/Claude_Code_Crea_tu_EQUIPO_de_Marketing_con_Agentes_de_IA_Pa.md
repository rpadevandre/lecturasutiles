# Claude Code: Crea tu EQUIPO de Marketing con Agentes de IA (Paso a Paso)

## Información General
- **Canal:** Rodolfo Carrasco | IA & Automatizaciones
- **Duración:** 21m 35s
- **Idioma detectado:** Español

## Resumen Ejecutivo
El video explica cómo construir un equipo de cuatro agentes de IA especializados en marketing usando Claude Code (extensión de VS Code de Anthropic), sin necesidad de conocimientos técnicos previos. Los agentes son: **Estratega** (coordinador general), **Creador de Contenido** (copywriter), **Analista de Datos** (métricas y reportes) y **Community Manager** (programación y redes). La clave del sistema es que todos comparten una carpeta común que actúa como memoria compartida, permitiendo que se coordinen de forma autónoma.

El tutorial cubre el proceso completo: instalación de prerrequisitos (VS Code, Node.js, extensión Claude Code), configuración de contexto de marca mediante archivos Markdown, creación de "skills" reutilizables (branding, diseño social), conexión de herramientas externas vía MCP (Nano Banana para generación de imágenes con Google Studio), y finalmente la creación y enrutamiento de los agentes usando el comando `slash agent` dentro de Claude Code.

El resultado final es un sistema donde, con un solo prompt al estratega, se puede lanzar una campaña de marketing completa: investigación de mercado, brief de campaña, posts para redes, landing page, secuencia de emails y creatividades visuales, todo generado de forma automática y coordinada entre los agentes.

## Puntos Clave
- **Prerequisitos**: VS Code + Node.js + extensión Claude Code (requiere plan Pro de Claude/Anthropic)
- **Estructura de carpetas**: Se crea un proyecto con subcarpetas para `context`, `templates`, `outputs`, `skills`, `agents`
- **Archivo CLAUDE.md**: Documento central que guarda el contexto del proyecto (marca, colores, tipografía, tono) para que no haya que repetirlo en cada conversación
- **Skills**: Capacidades reutilizables definidas en archivos Markdown que los agentes consultan (ej: `brand-deck`, `social-creative-designer`)
- **MCP (Model Context Protocol)**: Permite conectar herramientas externas; en el video se conecta Nano Banana para generación de imágenes via Google AI Studio
- **Archivo `mcp.json`**: Fichero de configuración (con punto inicial: `.mcp.json`) donde se definen los servidores MCP y sus API keys
- **Creación de agentes**: Se usa el comando `/agent` en la terminal de Claude Code → Library → Create new agent → se define con un prompt de instrucciones
- **Enrutamiento**: Se actualiza `CLAUDE.md` con reglas que definen cuándo delegar a cada agente (`@nombre-agente`)
- **Modos de permisos**: Se recomienda no usar "bypass permission" si no se tiene experiencia; mejor aprobar acción por acción
- **Memoria compartida**: Los agentes comparten la misma carpeta del proyecto como fuente de verdad común

## Conceptos Técnicos Mencionados
- **Claude Code** — Extensión oficial de Anthropic para VS Code que permite usar Claude como agente de programación/automatización directamente en el editor
- **MCP (Model Context Protocol)** — Protocolo de Anthropic para conectar modelos de IA con herramientas y servicios externos mediante servidores configurados en JSON
- **Nano Banana** — Servidor MCP para generación de imágenes, conectado a Google AI Studio/Imagen
- **Google AI Studio** — Plataforma de Google para acceder a modelos de IA (incluye generación de imágenes); requiere API key y cuenta de facturación
- **Skills (habilidades)** — Archivos Markdown con instrucciones y contexto reutilizable que los agentes cargan para tareas específicas (branding, diseño, copywriting)
- **CLAUDE.md** — Archivo especial de contexto que Claude Code lee automáticamente al iniciar, equivalente a un "system prompt" persistente del proyecto
- **Markdown (.md)** — Formato de texto estructurado usado para almacenar contexto, instrucciones y documentación de los agentes
- **Multi-agent system** — Arquitectura donde varios agentes especializados se coordinan, cada uno con rol y herramientas definidas
- **VS Code Extensions Marketplace** — Repositorio de extensiones para Visual Studio Code donde se instala Claude Code
- **Node.js** — Entorno de ejecución JavaScript requerido para que funcione la extensión Claude Code y los servidores MCP
- **/agent, /clear** — Comandos slash disponibles dentro de la interfaz de Claude Code para crear agentes y limpiar conversaciones
- **Live Server (VS Code)** — Extensión usada para previsualizar los dashboards HTML generados por los agentes en el navegador

## Fragmentos Relevantes
> "Se comunican por una carpeta compartida y su memoria es común. Por ejemplo, el estratega escribe el plan de campaña en este archivo y el creador pues tiene acceso a ese archivo y con ese archivo ya puede crear el copy."

> "Le vamos a decir que actualice el archivo Cloud MD para añadir reglas de enrutamiento de agentes. Define claramente cuándo delegar a cada agente versus cuándo usar una skill diferente."

> "Aquí estoy en un modo que me tiene que preguntar para darle permiso. Pero si tú eliges bypass permission, pues la verdad que das rienda suelta a Claude. La verdad que no te lo recomiendo si no sabes bien lo que estás haciendo."

> "Necesito un paquete completo de marketing para el lanzamiento de Black Friday. Incluye investigación de mercado de público objetivo, brief de campaña con mensajes claros, 5 posts en redes sociales, una landing page completa y creatividades visuales."

> "Tú puedes decir también lo mismo [que Claude]. Yo aquí tengo unos prompts preparados que me los ha preparado ya Claude."

## Conclusiones y Aprendizajes
- **El CLAUDE.md es el núcleo del sistema**: Invertir tiempo en un buen archivo de contexto inicial (marca, tono, servicios, cliente ideal) multiplica la calidad de todo lo que generan los agentes después. Escanear la carpeta del proyecto para autogenerarlo es una práctica muy eficiente.
- **Skills como módulos reutilizables**: Separar las capacidades en archivos de skill independientes permite mantener consistencia de marca entre agentes y proyectos, y facilita actualizar el comportamiento sin reconfigurar cada agente.
- **MCP para integración real**: La arquitectura MCP permite extender los agentes con APIs externas reales (imágenes, calendario, CRM, etc.), convirtiendo el sistema de un generador de texto a un automatizador real de procesos.
- **Enrutamiento explícito en CLAUDE.md**: Definir reglas claras de cuándo usar cada agente evita ambigüedades y hace el sistema predecible; es el equivalente a un "org chart" del equipo de IA.
- **Workflow replicable a otros dominios**: La misma arquitectura (contexto → skills → agentes especializados → enrutamiento) se puede aplicar a equipos de desarrollo, soporte, ventas o cualquier función de negocio, no solo marketing.
- **Gestión de permisos progresiva**: Empezar con permisos manuales permite entender qué hace cada agente antes de automatizar completamente; recomendado para onboarding y auditoría del sistema.

---
> Generado automáticamente para uso como contexto en Cursor / Claude Code