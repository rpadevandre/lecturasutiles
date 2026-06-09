# Claude Code SEO: How I Got 50,000 Clicks Per Month (Steal This)

## Información General
- **Canal:** Jono Catliff
- **Duración:** 1h 8m 15s
- **Idioma detectado:** Inglés (en)

## Resumen Ejecutivo
El video es una masterclass práctica sobre cómo usar Claude Code para implementar una estrategia SEO completa desde cero, sin necesidad de conocimientos técnicos de programación. El autor comparte dos tácticas principales que le generaron más de $500,000 en su empresa anterior: creación de blog posts a escala y creación de service pages (páginas de servicio por ciudad/servicio). Todo el proceso se apoya en Claude Code como ejecutor técnico, desde la construcción del sitio hasta la optimización SEO on-page y técnica.

El flujo completo abarca: investigación de keywords con SEMrush → construcción del sitio web (SSG con Next.js) → generación de blog posts con voz personalizada y keyword clusters → creación de service pages con el modelo "zipper" (servicio × ciudad) → optimización on-page con checklist de 80+ señales → optimización técnica con Google Lighthouse → empaquetado en un Claude Skill reutilizable → deploy en Vercel/GitHub → registro en Google Search Console y Google My Business.

Un punto central del autor es que el contenido generado por IA por defecto es "AI slop" ilegible, y que el diferenciador real está en entrenar a Claude con la voz, humor, historias y estadísticas propias del negocio, lo que incrementa el dwell time y el engagement, señales clave para Google. También advierte sobre los riesgos del off-page SEO agresivo y los esquemas de backlinks baratos que pueden destruir un dominio.

## Puntos Clave
- **Dos tácticas probadas:** blog posts a escala (autoridad tópica) + service pages (keywords de dinero), ambas necesarias y complementarias
- **Static Site Generation (SSG) es obligatorio** para que Google pueda indexar correctamente; CSR y SSR degradan el crawling
- **Keyword research con SEMrush:** filtrar por dificultad ≤30, volumen ≥100, intent informacional para blogs; ordenar por CPC para service pages
- **Keyword clusters:** una página debe rankear para múltiples keywords relacionadas, no solo la principal
- **Anti-AI-slop:** entrenar Claude con LinkedIn posts, transcripts, emails propios para replicar voz, humor y anécdotas reales
- **Robar estructura de competidores:** analizar top 3 resultados de Google para extraer longitud promedio, H2s, imágenes y topics cubiertos
- **On-page SEO checklist 80+ señales:** keywords en primeras 100 palabras, exactamente 1 H1, 4-8 preguntas, links internos/externos, meta title y description
- **Google Lighthouse 100/100:** performance, SEO, accessibility y best practices deben estar en verde; paste del reporte a Claude para auto-fix
- **Sitemap.xml + robots.txt:** generados por Claude, críticos para indexación
- **Claude Skill `/blog`:** empaquetar todo el flujo en un comando único que se puede automatizar a las 9am diariamente
- **Cadencia de publicación:** nunca publicar miles de posts de golpe; escalar gradualmente para no activar filtros de spam de Google
- **Off-page SEO con cautela:** broken link swapping, guest posting, HARO/Hero Journalism y backlinks de calidad pagados son los únicos métodos recomendados; PBNs y backlinks baratos destruyen dominios
- **Deploy stack:** GitHub (repositorio) + Vercel (hosting gratuito, preset Next.js)
- **Post-deploy obligatorio:** Google My Business, Google Search Console (sitemap submission + request indexing), Google Analytics, A/B testing de landing pages

## Conceptos Técnicos Mencionados
- **Claude Code** — Extensión de VS Code (Cursor/Antigravity) que permite generar y modificar código mediante prompts en lenguaje natural
- **Claude.md** — Archivo de instrucciones del proyecto que define comportamiento, SOPs y requisitos técnicos para Claude
- **Static Site Generation (SSG)** — Arquitectura web donde las páginas se pre-renderizan en build time; óptima para SEO porque Google recibe HTML completo instantáneamente
- **Next.js** — Framework React usado como base del sitio generado; requerido en el preset de Vercel para el deploy
- **SEMrush / Keyword Magic Tool** — Herramienta de investigación de keywords con datos de volumen, dificultad (KD) y CPC
- **Keyword Difficulty (KD)** — Métrica de SEMrush (0-100) que indica qué tan difícil es rankear para una keyword; se recomienda ≤30
- **Keyword Clusters** — Agrupación de keywords secundarias y terciarias alrededor de una keyword principal en una misma página
- **Pexels API** — API gratuita para obtener imágenes royalty-free programáticamente e insertarlas en blog posts
- **Google Lighthouse** — Herramienta de auditoría integrada en Chrome DevTools que puntúa performance, SEO, accesibilidad y best practices
- **Core Web Vitals / LCP** — Métricas de performance de Google (Largest Contentful Paint, etc.) que afectan el ranking
- **Sitemap.xml** — Archivo XML que lista todas las URLs del sitio para que los crawlers de Google las descubran
- **robots.txt** — Archivo de texto que indica a los crawlers qué páginas pueden o no indexar
- **Google Search Console** — Herramienta gratuita de Google para monitorear indexación, clicks, impresiones y solicitar indexación manual
- **Google My Business** — Listing gratuito de Google para negocios locales; genera clicks directos desde búsquedas locales
- **Vercel** — Plataforma de hosting gratuita optimizada para Next.js con deploy automático desde GitHub
- **GitHub** — Repositorio de código en la nube; usado como intermediario entre el proyecto local y Vercel
- **`.env` file** — Archivo de variables de entorno para almacenar API keys y secrets de forma segura
- **Backlinks / Link Juice** — Enlaces externos hacia el sitio propio que transfieren autoridad de dominio según Google
- **PBN (Private Blog Networks)** — Red de sitios falsos usados para generar backlinks artificiales; considerado black hat SEO y penalizado por Google
- **HARO / Hero Journalism** — Plataforma donde periodistas publican queries y expertos responden a cambio de un backlink
- **Meta title y meta description** — Etiquetas HTML invisibles en página que Google muestra como snippet en los resultados de búsqueda
- **Topical Authority** — Concepto SEO: cuantos más artículos relevantes tenga un dominio sobre un tema, más autoridad le asigna Google en ese nicho
- **Domain Authority (DA)** — Métrica de confianza global del dominio que afecta el ranking de todas sus páginas
- **Claude Skill** — Comando personalizado (`/blog`, `/service`) que encapsula un flujo completo de acciones en Claude Code, ejecutable con una sola palabra
- **Dribbble** — Plataforma de diseño usada como referencia visual para generar sitios con mejor estética desde el primer prompt

## Fragmentos Relevantes

> *"You don't need to know a line of code. You don't need to know anything technical whatsoever for this to work. As long as you can copy and paste, you're going to be totally fine."*

> *"Not all keywords are created equal. If you go into Claude here and you ask it, 'Give me 20 keywords for plumbing.' It's going to give you its best guess at 20 keywords. If you were to follow this, you'd probably be screwed."*

> *"Static site generation means the pizza is already made. The person says, 'Yeah, no problem. Here's your slice,' and you're off in 10 seconds."*

> *"If you just stop here, which most people do, you're never going to see the real results you want to see. [...] In today's fast-paced world, maintaining a functional household is more important than ever — the point here is that it is so boring to read and nobody's going to sit through this."*

> *"SEO is a black box. Nobody knows what ranks well on SEO definitively. Not Google employees, not SEMrush, not Ahrefs, not your friend down the street."*

> *"Reverse engineer what Google wants. They want to make money. They want to serve high-quality content to their viewers so that those people come back over and over again."*

> *"You don't want to just throw off like a thousand blog posts simultaneously because Google is going to pick up on the spike in volume. Day one, post once. Day two, post once again."*

> *"I quizzed them [backlink experts on Upwork]. Between when they started and when they ended, literally it was like a line that just went down. The performance tanked."*

> *"Think about it like a zipper. You have two sides: the service and the city. Emergency plumber × Vancouver, emergency plumber × Toronto — you zip them together into a service page."*

> *"You could set this [Claude Skill] up to run automatically at 9:00 a.m. in the morning and it's going to search the keywords, make sure that we don't reuse the same keyword, and then go through the whole process."*

## Conclusiones y Aprendizajes

**Arquitectura del sitio:**
- Siempre forzar SSG (Static Site Generation) en el `Claude.md` desde el inicio del proyecto; cambiar esto después es costoso
- Usar Next.js + Vercel como stack de deploy gratuito y SEO-friendly
- Generar `sitemap.xml` y `robots.txt` automáticamente con cada build

**Estrategia de contenido:**
- Separar claramente blogs (intent informacional, topical authority) de service pages (intent comercial, conversión directa)
- El modelo "zipper" servicio × ciudad es escalable y predecible; mantenerlo a escala razonable (no cientos de páginas casi idénticas)
- Keyword clusters multiplican el alcance de una sola página sin esfuerzo adicional

**Calidad del contenido generado:**
- Crear archivos de referencia de voz (`humor.md`, `voice.md`, `stats.md`, `stories.md`) y alimentarlos con material real antes de generar cualquier post
- Analizar los top 3 competidores en Google para la keyword objetivo y extraer su estructura antes de escribir
- El dwell time y bounce rate son señales de ranking reales; contenido aburrido = ranking bajo

**Automatización:**
- Encapsular el flujo completo en un Claude Skill (`/blog`) para producción en serie
- Escalar publicación de forma gradual (1→2→3 posts/día) para evitar penalizaciones por spike de contenido

**Medición:**
- Configurar Google Search Console desde el día 1 y usar "Request Indexing" para acelerar la aparición en Google (máx. ~10/día)
- Correr Lighthouse regularmente; target 100/100 en los 4 indicadores; pegar el reporte a Claude para fix automático
- Google Analytics para entender comportamiento de visitantes y optimizar conversión de landing pages

---
> Generado automáticamente para uso como contexto en Cursor / Claude Code