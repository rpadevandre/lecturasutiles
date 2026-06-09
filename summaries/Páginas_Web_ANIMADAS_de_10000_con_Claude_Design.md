# Páginas Web ANIMADAS de $10,000 con Claude Design

## Información General
- **Canal:** Benjamín Cordero
- **Duración:** 38m 2s
- **Idioma detectado:** Español

## Resumen Ejecutivo
El video presenta un framework completo llamado **FRAME** para construir landing pages animadas de alta calidad usando Claude Design, Claude Chat y herramientas de generación de imagen/video. El autor argumenta que el error más común es entrar directamente a Claude Design a improvisar prompts, lo que consume tokens rápidamente y produce resultados mediocres. La clave está en preparar toda la arquitectura de contenido, assets visuales y prompts en Claude Chat antes de tocar Claude Design.

El framework FRAME tiene cinco fases ordenadas: **F**undación (planificación en Claude Chat con un skill.md), **R**ender (generación de imágenes con ChatGPT Image 2 en Higgsfield), **A**nimación (conversión de imágenes a video loop con Cling o Sora/Seda en Higgsfield), **M**ontaje (one-shot en Claude Design con todos los assets listos) y **E**ntrega (deploy a Vercel o Cloudflare via Claude Code). Este flujo permite hacer una landing page completa, animada y desplegada en producción con mínima iteración dentro de Claude Design.

El autor también introduce la estrategia comercial: una landing page de este nivel valía antes $5,000–$20,000 (fotógrafo + diseñador + motion designer + developer), y hoy puede construirse con suscripciones de ~$100/mes, permitiendo venderlas a clientes por $10,000 con margen altísimo. Se menciona además el recurso **Motion Sites** como biblioteca de referencia de páginas animadas con prompts copiables.

## Puntos Clave
- **No entrar directo a Claude Design**: primero construir la fundación en Claude Chat con un skill.md específico
- **Claude Chat es casi ilimitado** en tokens comparado con Claude Design, aprovecharlo para toda la fase de planeación
- **One-shot en Claude Design**: el objetivo es pasar un único prompt bien preparado con todos los assets adjuntos
- **Motion Sites** (motionsites.ai) como biblioteca de referencia y fuente de prompts copiables para estilos animados
- **Higgsfield** centraliza generación de imagen (ChatGPT Image 2) y animación de video (Cling, Seda) en una sola plataforma
- **Loop perfecto**: usar el mismo frame inicial y final al animar para lograr videos perfectamente loopeables
- **Tokens eficientes en Claude Design**: agrupar todos los cambios en un solo mensaje en vez de múltiples prompts
- **Tweaks/sliders**: usar la función de tweaks de Claude Design para ajustar colores y estilos sin gastar tokens
- **Handoff a Claude Code**: exportar el ZIP o hacer fetch directo desde Claude Code para implementar y deployar
- **GitHub → Vercel/Cloudflare** como pipeline de deploy estándar; Claude Code puede gestionar DNS y CNAME automáticamente
- **Estrategia de outreach**: capturar la página de un prospecto con una herramienta de screenshot (Quickshot), rediseñarla y ofrecerla como demo para iniciar conversación comercial

## Conceptos Técnicos Mencionados
- **Claude Design** — Herramienta de Anthropic para generar UI/landing pages en HTML/CSS/JS mediante prompts en lenguaje natural
- **Claude Chat** — Interfaz conversacional de Claude usada como fase de planificación; consume muchos menos tokens que Claude Design
- **Claude Code** — CLI/agente de Anthropic para implementar, modificar y deployar proyectos de código directamente
- **Skill.md** — Archivo Markdown de instrucciones que se adjunta a Claude para guiar el comportamiento y output según buenas prácticas definidas
- **Framework FRAME** — Framework propio del autor: Fundación → Render → Animación → Montaje → Entrega
- **Motion Sites (motionsites.ai)** — Biblioteca de landing pages animadas de referencia con prompts copiables para Claude Design
- **Higgsfield** — Plataforma que agrega múltiples modelos de imagen y video (ChatGPT Image 2, Cling, Seda) con llamadas API paralelas
- **ChatGPT Image 2** — Modelo de generación de imágenes de OpenAI usado para crear los assets visuales de la landing page
- **Cling 3.0 / Seda** — Modelos de animación de video usados para convertir imágenes estáticas en videos loopeados
- **Vercel** — Plataforma de hosting y deploy continuo para proyectos frontend; se conecta con GitHub
- **Cloudflare** — Alternativa a Vercel para hosting, compra de dominios y gestión automática de DNS
- **Versel Hobby Plan** — Plan gratuito de Vercel suficiente para proyectos sin dominio personalizado
- **Scroll-driven animations** — Animaciones CSS/JS activadas por el scroll del usuario, implementadas por Claude Design
- **Video background loop** — Técnica de video en bucle perfecto como fondo de hero section
- **README.md** — Archivo de contexto en proyectos que describe propósito, estructura y estándares del proyecto
- **Quickshot** — Aplicación de captura de pantalla completa con autoscroll, usada para capturar páginas de prospectos
- **Retell AI** — Plataforma de agentes de voz mencionada como backend para el caso de uso de recepcionista virtual
- **Go High Level** — CRM mencionado como integración posible para el agente de recepcionista
- **GitHub** — Control de versiones; se usa como intermediario entre Claude Code y Vercel para mantener historial

## Fragmentos Relevantes

> "El 99% de las personas entra a Cloud Design y empieza directamente a improvisar. Prompt tweak, prompt tweak, cambios, prompt cambios. Se gasta la sesión y el resultado termina saliendo a medias."

> "Mientras Cloud Design te cobra por cada sesión, por cada prompt, Cloud Chat es básicamente ilimitado y es muy difícil llegar a los tokens o a las sesiones finales."

> "Lo importante es que el frame inicial y el frame final sea el mismo para que sea perfectamente lupeable."

> "En vez de mandarle 10 mensajes, le mando uno con todos los cambios. Después habla con tus herramientas."

> "Mira, oye, vi tu página y se me ocurrió hacerte un rediseño, aquí te lo dejo. Si te interesa que te lo implementes, avísame y conversamos."

> "Hoy día lo único que necesitas es una suscripción de Cloud Code ojará en el plan Max, una suscripción de Cloud en el plan Max, un hosting en Versel… por $100 o $10 mensuales tienes Cloud y tienes esta página y constructor corriendo."

> "Ya hoy día podéis llegar al mismo Cloud Code y decirle como quiero vincular este dominio y lo hace por ti. Te cambia los DNS, los C name, los records, toda la parte que antes era un dolor de cabeza."

## Conclusiones y Aprendizajes

**Aplicable directamente en proyectos:**
- Crear un `skill.md` con buenas prácticas de diseño web y motion antes de cualquier sesión de Claude Design; adjuntarlo a Claude Chat para la fase de planificación
- Generar el prompt one-shot para Claude Design dentro de Claude Chat, no improvisar en Claude Design
- Para videos de fondo loopeados: usar el mismo frame de inicio y fin al animar con Cling/Seda en Higgsfield
- Agrupar todos los cambios iterativos en un solo mensaje en Claude Design para conservar tokens de sesión
- Usar los tweaks/sliders de Claude Design para ajustes visuales sin consumir tokens adicionales
- Pipeline de deploy: Claude Design → exportar ZIP → Claude Code → GitHub → Vercel/Cloudflare
- Motion Sites como recurso de inspiración y punto de partida de prompts para estilos específicos
- Para outreach comercial de rediseño: capturar la página del prospecto con Quickshot y pasarla directamente a Claude Design

---
> Generado automáticamente para uso como contexto en Cursor / Claude Code