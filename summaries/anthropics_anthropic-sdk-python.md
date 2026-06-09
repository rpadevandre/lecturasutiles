# anthropic-sdk-python

## Información General
- **Repo:** `anthropics/anthropic-sdk-python`
- **URL:** https://github.com/anthropics/anthropic-sdk-python
- **Lenguaje principal:** Python
- **Stars:** 3,578
- **Última actualización:** 2026-06-04
- **Topics:** ninguno

## Propósito del Repo
SDK oficial de Python para acceder a la API de Claude (Anthropic). Está diseñado para desarrolladores Python que quieran integrar modelos Claude en sus aplicaciones, ofreciendo tanto una interfaz síncrona como asíncrona, soporte para streaming, herramientas (tools), agentes, structured outputs, imágenes, archivos, y múltiples plataformas (AWS Bedrock, Google Vertex AI, Azure).

Lo que lo diferencia de una integración HTTP directa es que provee clientes tipados con Pydantic, manejo automático de reintentos, paginación, streaming con eventos SSE, helpers para agentes y MCP (Model Context Protocol), y compatibilidad con ambas versiones de Pydantic (v1 y v2).

## Arquitectura y Patrones Clave
El SDK sigue una arquitectura de **cliente con recursos anidados**, donde `Anthropic` (sync) y `AsyncAnthropic` (async) son los puntos de entrada y exponen recursos como `client.messages`, `client.models`, `client.beta`, etc. Internamente usa un `_base_client.py` con la lógica HTTP compartida (reintentos, timeouts, autenticación) sobre `httpx`.

Patrones clave:
- **Resource pattern**: cada endpoint tiene su propia clase (e.g., `MessagesResource`) que encapsula las operaciones CRUD/invoke.
- **Typed responses con Pydantic**: todas las respuestas son modelos Pydantic con tipado completo.
- **Dual sync/async**: se mantienen dos clientes paralelos (`Anthropic` y `AsyncAnthropic`) que comparten la misma lógica base.
- **Streaming via generators**: el streaming se implementa con `_streaming.py` y yields de eventos tipados.
- **Plugin de transporte**: soporte para `aiohttp` como backend alternativo a `httpx`.

## Componentes Principales
- `src/anthropic/_client.py` — Clases `Anthropic` y `AsyncAnthropic`, punto de entrada principal del SDK
- `src/anthropic/_base_client.py` — Lógica HTTP base: reintentos, timeouts, autenticación, construcción de requests
- `src/anthropic/_streaming.py` — Implementación de streaming SSE con tipos de eventos
- `src/anthropic/_models.py` — Clase base para todos los modelos Pydantic de respuesta
- `src/anthropic/resources/` — Carpeta con clases de recursos (messages, models, beta, completions, etc.)
- `src/anthropic/lib/` — Helpers de alto nivel: agentes, structured outputs, parsing de respuestas
- `src/anthropic/tools/` — Utilidades para definición y ejecución de herramientas (function calling)
- `src/anthropic/types/` — Tipos Pydantic para request/response de todos los endpoints
- `src/anthropic/_utils/` — Utilidades internas (serialización, validación, manejo de archivos)
- `src/anthropic/_decoders/` — Decoders para SSE y JSON incremental (usa `jiter`)
- `src/anthropic/pagination.py` — Helpers para paginación de resultados
- `src/anthropic/_exceptions.py` — Jerarquía de excepciones tipadas de la API

## Dependencias Clave
- **`httpx`** — Cliente HTTP async/sync subyacente para todas las llamadas a la API
- **`pydantic` (v1 y v2)** — Validación y serialización de modelos de request/response
- **`anyio`** — Abstracción de async runtime (compatible con asyncio y trio)
- **`jiter`** — Decoder JSON incremental de alta performance para streaming
- **`sniffio`** — Detección del runtime async activo
- **`distro`** — Detección de información del sistema operativo para headers User-Agent
- **`typing-extensions`** — Backports de tipos modernos de Python para compatibilidad con 3.9+
- **`google-auth`** (opcional) — Autenticación para Google Vertex AI
- **`boto3`/`botocore`** (opcional) — Integración con AWS Bedrock
- **`mcp`** (opcional) — Soporte para Model Context Protocol
- **`docstring-parser`** — Parseo de docstrings para generación automática de esquemas de herramientas

## Fragmentos de Código Relevantes

**Uso básico — cliente síncrono:**
```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),
)

message = client.messages.create(
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello, Claude"}],
    model="claude-opus-4-6",
)
print(message.content)
```

**Streaming de mensajes:**
```python
# examples/messages_stream.py pattern
with client.messages.stream(
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello"}],
    model="claude-opus-4-6",
) as stream:
    for text in stream.text_stream:
        print(text, end="", flush=True)
```

**Definición de herramientas con tipado:**
```python
# examples/tools.py pattern
tools = [
    {
        "name": "get_weather",
        "description": "Get weather for a location",
        "input_schema": {
            "type": "object",
            "properties": {
                "location": {"type": "string"},
            },
            "required": ["location"],
        },
    }
]
response = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=1024,
    tools=tools,
    messages=[{"role": "user", "content": "What's the weather in Paris?"}],
)
```

## Conclusiones y Aprendizajes
- **Patrón de cliente con recursos**: separar la lógica HTTP base en `_base_client` y cada endpoint en su propia clase `Resource` es un patrón escalable para SDKs propios.
- **Dual sync/async sin duplicación**: usar `anyio` y compartir lógica base entre clientes sync y async reduce el mantenimiento sin sacrificar ergonomía.
- **Streaming tipado**: modelar los eventos SSE como tipos Pydantic y exponerlos mediante generators da una experiencia de streaming type-safe y composable.
- **Compatibilidad multi-Pydantic**: soportar Pydantic v1 y v2 simultáneamente mediante una capa de compatibilidad (`_compat.py`) es un patrón útil para librerías que quieren mayor adopción.
- **Extras opcionales por plataforma**: usar `[project.optional-dependencies]` con extras nombrados (bedrock, vertex, mcp) mantiene el paquete base liviano.

---
> Generado automáticamente para uso como contexto en Cursor / Claude Code