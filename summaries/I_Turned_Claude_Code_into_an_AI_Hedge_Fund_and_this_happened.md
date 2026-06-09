# I Turned Claude Code into an AI Hedge Fund... and this happened

## Información General
- **Canal:** GreymatterAI
- **Duración:** 15m 24s
- **Idioma detectado:** Inglés

## Resumen Ejecutivo
El autor construye un AI hedge fund usando Claude Code en 5 días, diseñado con **información asimétrica entre agentes**: cada uno de los cinco agentes (inspirados en Buffett, Munger, Cohen, Dalio y Ackman) recibe únicamente los datos que ese inversor real utilizaría, evitando el problema de que todos los agentes lean el mismo dataset y generen respuestas redundantes. El sistema incluye ingesta automática de datos (precios cada 5 minutos, fundamentales diarios, insider trades, noticias), un quality gate de señales, y un dashboard visual con pipeline animado.

Para demostrar validez, se diseña un **blind backtest**: se carga la base de datos solo con datos hasta el 1 de enero de 2026, se deja al sistema hacer sus picks sin ver el futuro, se registran los resultados antes de consultarlos, y luego se comparan contra el S&P 500 y el índice de hedge funds. El AI portfolio retornó -2.89% frente al -3.9% del S&P 500, superando al benchmark por ~1%, aunque perdió contra el índice de hedge funds por 2.46 puntos.

El proyecto demuestra que la combinación de agentes especializados con información diferenciada, arquitectura modular y backtesting ciego puede producir resultados competitivos con el mercado, construidos desde cero en un entorno doméstico, lo cual ilustra el potencial democratizador de las herramientas de AI en finanzas.

## Puntos Clave
- **Información asimétrica como diferenciador**: cada agente ve solo los datos de su especialidad (fundamentales, noticias, insider trades, price action, macro), lo que hace que el desacuerdo entre agentes sea genuino y valioso.
- **Pipeline de datos automático**: 7 tablas de base de datos, 4 jobs de ingesta, cobertura de 20 stocks en watchlist personalizada.
- **Quality gate en 0.35**: las señales compuestas por debajo de ese umbral no llegan a los agentes, filtrando ruido como un "bouncer".
- **Blind backtest científico**: 5 pasos que eliminan sesgos (ni el sistema ni el builder ven resultados hasta después del análisis).
- **Resultado del experimento**: -2.89% vs -3.9% S&P 500 (Q1 2026 fue negativo). El 77.5% del portfolio en cash conservó capital durante la caída.
- **Problemas reales en producción**: rate limits de API, bugs en regime detection, keyword mismatches, waiting system inoperante, cache/keys obsoletos que requerían flush manual.
- **Iteración con ChatGPT + Claude Code**: ChatGPT se usó para diseño arquitectónico y prompt engineering; Claude Code para construcción real.

## Conceptos Técnicos Mencionados
- **Claude Code** — herramienta de Anthropic para codificación asistida por AI, usada para construir el sistema completo desde prompts de arquitectura
- **Multi-agent system con información asimétrica** — patrón donde cada agente recibe un subconjunto diferente de datos, evitando groupthink
- **FastAPI / Flask** — frameworks Python para la capa API del backend
- **Celery** — sistema de colas distribuidas para manejo de tareas asíncronas y señales en tiempo real
- **TimescaleDB** — base de datos de series temporales para almacenar y consultar datos de precios y señales
- **React / Next.js** — frontend del dashboard visual
- **Docker** — containerización del stack completo para portabilidad
- **Blind backtest** — técnica de validación que carga datos históricos hasta un corte y ejecuta el sistema como si fuera tiempo real, sin acceso a datos futuros
- **Signal aggregation layer** — hub central que recibe señales de todos los agentes y calcula un composite score
- **Quality gate / composite score** — umbral de filtrado (0.35) que solo permite pasar las oportunidades con suficiente señal combinada
- **Insider trades (SEC disclosures)** — datos públicos de compras/ventas de insiders que alimentan al agente Ackman
- **Regime detection** — componente que identifica el estado del mercado (bull, bear, neutral) para contextualizar señales
- **OpenAI API (rate limiting)** — se usó para reducir costos, pero el límite de 100 llamadas / 30k tokens requirió lógica de retry/fallback
- **Double-blind experiment methodology** — adaptación del paradigma experimental de psicología aplicado al backtesting para eliminar confirmation bias

## Fragmentos Relevantes
> *"In a real hedge fund, what the macro guy sees is completely different to what the technical guy sees. They're looking at completely different angles, which is why it makes the disagreement so important."*

> *"Buffett only sees fundamentals, PE ratio, revenue, cash flow, debt. No charts, no news, just the business. [...] Cohen only sees live price action, candles, volume, support, resistance. But basically he has no idea what the company even does."*

> *"The quality gate is at 0.35. Below that, it doesn't even get passed through to the agents. So, only the most interesting picks actually make it through."*

> *"Step one: I pick from exactly 3 months ago, and I load the database with data only up to that point. No future prices, no future news, no insider trades."*

> *"This is what building actual production software looks like. Not clean montage, but 5 hours of 'why isn't this working?' followed by that one epiphany or line that basically fixes everything."*

> *"The AI's conservatism, 77.5% cash, protected it during what turned out to be a rough Q1 for 2026."*

## Conclusiones y Aprendizajes
- **La asimetría de información entre agentes es un patrón arquitectónico aplicable** a cualquier sistema multi-agente donde se quiera evitar el echo chamber: cada agente debe recibir solo el contexto relevante para su rol.
- **El blind backtest es una metodología replicable** para validar sistemas de AI sin cherry-picking: definir cutoff date, cargar solo datos históricos, ejecutar pipeline completo, registrar resultados antes de consultarlos.
- **Los quality gates son esenciales** en pipelines con múltiples fuentes de señal; sin filtrado, los agentes se saturan con ruido de baja calidad.
- **Rate limiting de APIs en producción requiere retry logic y fallback desde el inicio**, no como parche posterior.
- **Claude Code puede construir sistemas complejos multi-agente** a partir de prompts arquitectónicos detallados; el diseño previo con ChatGPT como "arquitecto" y Claude Code como "builder" es un flujo de trabajo efectivo.
- **El cash allocation conservador (77.5%) como mecanismo de protección de capital** es una decisión de diseño del CIO layer, no un fallo; en mercados bajistas es una ventaja competitiva.
- **Producción real ≠ demo limpia**: bugs en cache, keywords, thresholds y APIs son la norma; el sistema debe diseñarse con observabilidad para detectarlos rápido.

---
> Generado automáticamente para uso como contexto en Cursor / Claude Code