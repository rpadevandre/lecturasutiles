# Cut Your AI API Bill by 93% with Hermes Agent | Claude + Gemini + OpenAI OAuth

## Información General
- **Canal:** AgenticEngineering
- **Duración:** 15m 9s
- **Idioma detectado:** English
- **Transcripción fuente:** `Cut_Your_AI_API_Bill_by_93_with_Hermes_Agent_Claude_Gemini_O.txt`

## Resumen Ejecutivo

Hermes Agent es una capa de abstracción local que permite usar las suscripciones de consumo (Claude Pro, ChatGPT Plus, Google One AI Premium) como si fueran una API estándar compatible con OpenAI, eliminando el cobro por token. El sistema se instala localmente, expone un servidor REST en `localhost:4000`, y maneja autenticación OAuth contra los tres proveedores principales, traduciendo automáticamente entre el formato `chat/completions` de OpenAI y los formatos nativos de cada proveedor.

El ahorro económico es sustancial: frente a ~$960/mes en costos de API para uso moderado (1M tokens/día entre tres modelos), las suscripciones equivalentes cuestan $60/mes en total, representando una reducción del 93%. La herramienta gestiona automáticamente rotación de credenciales, reintentos ante rate limits, cooldowns, y refresh de tokens OAuth, haciendo el sistema transparente para la aplicación cliente.

Adicionalmente, Hermes soporta un cuarto proveedor: Alibaba Qwen CLI, con modelos de razonamiento open-weight de alto rendimiento en tier gratuito, lo que puede llevar el costo a cero en ciertos escenarios.

## Puntos Clave

- **Zero per-token billing**: se usa autenticación OAuth de suscripciones en lugar de API keys de pago
- **Compatible con OpenAI SDK sin cambios**: solo se cambia `base_url` a `http://localhost:4000`
- **Tres proveedores soportados**: Anthropic (Claude), Google (Gemini via Cloud Code Assist), OpenAI (via Codex OAuth)
- **Credential pool con múltiples cuentas por proveedor**: permite agregar varias suscripciones para multiplicar el rate limit efectivo
- **Cuatro estrategias de selección de credenciales**: `fail-first`, `round-robin`, `least-used`, `random`
- **Manejo automático de errores**: 429 → retry + rotación, 402 → rotación con cooldown 24h, 401 → refresh de token
- **Live model discovery para OpenAI**: los modelos nuevos aparecen automáticamente sin actualizar Hermes
- **Soporte para Claude Code, Aider, Cursor**: cualquier herramienta que respete `OPENAI_BASE_URL` es compatible
- **Qwen CLI integración**: modelo Qwen3-235B gratuito mediante lectura directa de credenciales del CLI oficial
- **Advertencia TOS**: uso de credenciales OAuth de suscripción en apps de terceros puede estar fuera de los términos de servicio, especialmente en Gemini

## Conceptos Técnicos Mencionados

- **Hermes Agent** — Proxy local que expone una API REST OpenAI-compatible en `localhost:4000`, actuando como broker entre aplicaciones y proveedores de IA
- **OAuth PKCE Flow** — Mecanismo de autenticación sin secreto de cliente usado para Claude y Gemini; el usuario autoriza en el navegador y Hermes recibe los tokens
- **Device Code OAuth Flow** — Variante de OAuth usado para OpenAI Codex; muestra un código en terminal que el usuario confirma en el navegador
- **Single-use Refresh Tokens** — Tokens de refresco que se invalidan tras el primer uso y generan uno nuevo; Hermes los maneja atómicamente para evitar errores en concurrencia
- **Claude Code Assist API / Cloud Code Assist API** — Endpoints internos de Anthropic y Google respectivamente, que los CLIs oficiales (Claude Code, Gemini CLI) usan y que están vinculados a planes de suscripción en lugar de billing por token
- **Codex OAuth** — Mecanismo de autenticación de OpenAI's Codex CLI que Hermes reutiliza para acceder a modelos GPT sin API key
- **OpenAI Chat Completions API** — Formato estándar de mensajes (`role/content`) que Hermes acepta como entrada y convierte al formato nativo de cada proveedor
- **OpenAI Responses API** — Formato interno que el endpoint Codex de OpenAI espera; Hermes traduce desde chat completions hacia este formato
- **Credential Pool** — Colección de credenciales por proveedor con tracking de estado (healthy, exhausted, cooldown) y selección automática según estrategia configurada
- **`config.yaml`** — Archivo de configuración de Hermes donde se define la estrategia de selección de credenciales por proveedor
- **`~/.hermes/auth.json`** — Archivo donde Hermes almacena las credenciales OAuth de OpenAI Codex
- **`~/.qwen/oauth_creds.json`** — Archivo de credenciales del Qwen CLI que Hermes lee directamente
- **Beta headers de Anthropic** — Headers HTTP especiales (`anthropic-beta: claude-code-20250219`) que indican al servidor de Anthropic que route la solicitud por el tier de suscripción
- **Token prefix detection** — Hermes detecta el tipo de token por su prefijo: `CC*` → Claude Code OAuth, `UIJ` → JWT, `SK-ant-*` → API key legacy
- **Qwen 3-235B A22B** — Modelo de razonamiento open-weight de Alibaba con 235B parámetros totales y activación MoE de 22B, disponible en tier gratuito del Qwen CLI
- **`ANTHROPIC_BASE_URL`** — Variable de entorno de Claude Code que permite redirigir sus llamadas a Hermes
- **`OPENAI_BASE_URL`** — Variable de entorno estándar reconocida por múltiples herramientas (Aider, Cursor, etc.) para apuntar a un endpoint alternativo

## Fragmentos Relevantes

> "Hermes sits between your application and the AI providers. Your app talks to Hermes using the standard OpenAI SDK. Nothing changes on your end. Hermes then authenticates to Claude, Gemini, or OpenAI using OAuth tokens from your subscription account, not an API key."

> "This is what tells Anthropic servers to route the request through your subscription tier, rather than billing an API account."

> "Instead of a hardcoded model catalog, it fetches the available models dynamically from the Codex endpoint. So when OpenAI releases a new model, it shows up in Hermes automatically without waiting for a software update."

> "With API keys, Claude Opus 4 alone runs about $450 a month. Gemini 2.5 Pro is around 210. GPT-4o is around 300. Combined, you're looking at nearly $1,000 a month just in API costs. With subscriptions through Hermes, $60 total for all three."

> "A 401 auth expired error triggers a token refresh attempt first. Only if the refresh itself fails does Hermes rotate to the next credential."

> "Subscription credentials are generally for personal or developer use, not for building products that serve other paying users. That path requires an API agreement."

> "Using the API_key field is required by the SDK, but Hermes ignores it. Just pass a placeholder string."

## Conclusiones y Aprendizajes

- **Para proyectos personales y equipos pequeños**: reemplazar API keys con Hermes + suscripciones es una decisión económicamente obvia si ya se pagan esas suscripciones. El breakeven se alcanza con muy pocos millones de tokens al mes.
- **Patrón de proxy OpenAI-compatible**: Hermes implementa el patrón de "OpenAI-compatible local proxy", útil para entender cómo construir middleware de IA que sea agnóstico al proveedor desde el punto de vista del cliente.
- **Gestión de credenciales en producción**: el sistema de credential pool con estrategias configurables (fail-first, round-robin, least-used) es un patrón aplicable en cualquier sistema que necesite manejar múltiples cuentas o API keys con rate limits independientes.
- **Riesgo TOS a considerar**: antes de escalar, verificar los términos de servicio del proveedor. Para uso en productos que sirven usuarios propios, las API keys oficiales siguen siendo el camino correcto.
- **Integración inmediata con herramientas del ecosistema**: Claude Code, Aider, Cursor y cualquier herramienta que soporte `OPENAI_BASE_URL` puede redirigirse a Hermes sin modificación, lo que lo hace útil en flujos de desarrollo local.
- **Fallback híbrido recomendado**: para mayor confiabilidad, mezclar una credencial de suscripción con una API key en el mismo pool de Hermes es una estrategia práctica para entornos semi-producción.

---
> Generado automáticamente para uso como contexto en Cursor / Claude Code