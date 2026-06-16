# The First App I Ever Built Makes $25K/Month

## Información General
- **Canal:** Starter Story
- **Duración:** 18m 0s
- **Idioma detectado:** Inglés (en)
- **Transcripción fuente:** `The_First_App_I_Ever_Built_Makes_25KMonth.txt`

## Resumen Ejecutivo
Ken, un estudiante universitario de 21 años de San Diego State University estudiando CS, construyó su primera app en 5 meses sin experiencia previa en desarrollo. La app se llama **Tone Adapt**: una herramienta para guitarristas que analiza cualquier canción y adapta los ajustes de amplificador y pedales al equipo específico del usuario para que suene lo más parecido posible al artista original. El negocio genera $25,000/mes combinando una web app y una app móvil nativa en Swift, con suscripciones semanales ($10/semana) y anuales (~$60/año).

La clave del éxito de Ken fue triple: identificó un pain point personal real (usaba ChatGPT para buscar tonos de guitarra con resultados imprecisos), construyó un MVP en una semana usando herramientas de vibe coding (Cursor/Claude Code), y ejecutó una estrategia de contenido agresiva en redes sociales (3 posts/día en múltiples plataformas). Su background previo en UGC (User Generated Content) para marcas fue determinante para convertir tráfico en suscriptores pagos.

El episodio subraya una tesis central: en la era del AI coding, la ventaja competitiva ya no está en saber programar sino en la capacidad de crear atención (contenido viral) alrededor de un producto que resuelve un problema específico en un nicho concreto. La distribución es el moat real.

## Puntos Clave
- **Primer proyecto, primer intento exitoso:** Pasó de cero experiencia en desarrollo a $25K/mes en 5 meses
- **Nicho ultra-específico:** No "app de guitarra genérica" sino "herramienta que adapta tu equipo exacto al tono de una canción concreta"
- **Construido en ~1 semana** usando exclusivamente vibe coding (Claude Code / Cursor), sin escribir una sola línea de código manualmente
- **Ship fast, iterate later:** V1 web app primero, luego app móvil nativa cuando ya había validación de mercado
- **Regla de contenido: 3 posts/día** en Instagram, TikTok, YouTube y Facebook desde el día 1
- **Poner la cara detrás del producto** para generar confianza y que los usuarios "sientan que son parte del journey"
- **Formula de escala de contenido:** Postear sin parar → encontrar el formato ganador → replicarlo 50 veces con pequeñas variaciones → contratar creadores UGC → amplificar con Meta Ads y TikTok Ads
- **No obsesionarse con el polish:** No perder tiempo en logos ni features perfectas; lanzar y cobrar desde el día 1
- **Validación del problema:** Confirmó el pain point hablando con guitarristas en Reddit e Instagram antes de construir
- **Revenue combinado:** ~$11K/mes web (Stripe) + ~$14K/mes mobile app = $25K+/mes total
- **Stack técnico muy accesible:** Supabase, Vercel, Mailgun, Stripe, OpenAI API, Tavily API, RevenueCat, Superwall, React Native (Expo/Expo Router), Swift nativo

## Conceptos Técnicos Mencionados

| Tecnología/Herramienta | Descripción |
|---|---|
| **Cursor** | IDE con AI integrada para vibe coding; usado para construir el proyecto web completo |
| **Claude Code** | CLI/agente de Anthropic para escritura de código asistida por AI; mencionado como herramienta principal de codegen |
| **Supabase** | Backend-as-a-Service con base de datos PostgreSQL, autenticación y storage; usado tanto en web como en mobile |
| **Vercel** | Plataforma de hosting y despliegue para el web app; también provee analytics |
| **Mailgun** | Servicio de transaccional email para notificaciones y comunicación con usuarios |
| **Stripe** | Procesador de pagos para la web app; gestión de suscripciones y revenue tracking |
| **OpenAI API** | API de GPT para generar las recomendaciones de tono y ajustes de gear basadas en la canción |
| **Tavily API** | API de búsqueda web en tiempo real; usada para investigar el gear original del artista de cada canción |
| **RevenueCat** | Plataforma de gestión de suscripciones in-app para iOS/Android; tracking de pagos mobile |
| **Superwall** | Herramienta de paywall dinámico y A/B testing de paywalls para la app móvil |
| **Swift (nativo)** | Lenguaje nativo de Apple; la app móvil fue construida en Swift nativo (no React Native) |
| **Expo/React Native** | Mencionado implícitamente como "REL para backend API routes" en el contexto mobile (posiblemente Expo Router) |
| **UGC (User Generated Content)** | Estrategia de marketing donde creadores externos replican el formato de contenido ganador para escalar distribución |
| **Meta Ads / TikTok Ads** | Paid advertising para amplificar los formatos de contenido orgánico que ya demostraron conversión |
| **Vibe Coding** | Metodología de desarrollo donde el programador describe en lenguaje natural y el AI genera el código, sin escribir código manual |

## Fragmentos Relevantes

> *"I used Cursor to build the entire project. Took me about a week to build everything. Nowadays, I would say the same project would take me a couple hours to build. And yeah, every line of code was vibe coded. Not a single line of code has been written myself."*

> *"Ship V1 on the web right now. You can ship a web app today and get someone to pay for your product by tonight. If you ship on the internet, don't spend hours picking a logo. Don't polish anything. Just build something, put it on the internet, and charge money for it."*

> *"Post about it every single day on social media. This is where I see so many people quit. They build an amazing product. It looks beautiful. It solves a great problem, and they never get anyone's eyes on it."*

> *"If you have a tiny little problem, there are at least thousands, if not tens of thousands of people out there with the exact same problem that you have."*

> *"You need to post relentlessly till you have one winner. Take that one winner and pour gasoline on it until it doesn't work anymore and then repeat."*

> *"Pick a hobby or a niche that you already know. Pick something that you do every day or every week yourself [...] you understand and face the exact pain points that you're trying to solve without doing any market research. Technically, you are your own customer."*

> *"Any content is better than no content at all. Every time you post content, someone is seeing it and someone will be willing to go and use your app."*

> *"Once you find a piece of content that works [...] Remake it 50 times with tiny variations. Hire UGC creators to copy that exact same format 60 times a month. Put money behind it on meta ads and TikTok ads."*

## Conclusiones y Aprendizajes

**Para encontrar ideas de producto:**
- Documentar los pain points que uno mismo enfrenta en hobbies cotidianos es el método de validación más eficiente — elimina la necesidad de market research formal
- Verificar el problema en comunidades de Reddit e Instagram (comentarios) antes de construir para confirmar que otros lo comparten
- El sweet spot es: herramienta específica + resultado claro + tiempo de valor rápido (Tone Adapt: "suena como tu canción favorita en 30 segundos")

**Para construir:**
- El stack web mínimo viable para cobrar es: Supabase + Vercel + Stripe + OpenAI API + Tavily — todo configurable con AI coding en horas
- Para mobile: Supabase + RevenueCat + Superwall + Swift nativo es el equivalente
- No construir el mobile app hasta tener validación en web; la web es más rápida de iterar

**Para distribuir:**
- Empezar a publicar contenido el mismo día del lanzamiento, incluso antes
- La fórmula de escala es secuencial: (1) postear consistentemente → (2) identificar formato ganador → (3) replicar con variaciones → (4) contratar UGC creators → (5) paid ads sobre lo que ya convierte orgánicamente
- Poner la cara del fundador detrás del producto acelera la construcción de confianza en nichos de hobbyistas

**Insight meta:**
- En un mundo donde cualquiera puede construir una app con AI, la distribución (contenido, atención) es la ventaja competitiva duradera, no el producto en sí
- El nicho específico + contenido consistente es más defensible que el producto tecnológico en sí mismo

---
> Generado automáticamente para uso como contexto en Cursor / Claude Code