# Síntesis: Arquitectura de Agentes de IA con Orquestación Multi-Agente

## Fuentes consultadas

| Fuente | Relevancia |
|--------|-----------|
| `The_7_Levels_of_Hermes_Agent_Explained.md` | Arquitectura progresiva de agentes: VPS → Discord → Curator → Cron → Kanban → Memoria → MCP server |
| `I_Built_the_Ultimate_Multi-Agent_Workflow_w_Hermes_Agent_Kan.md` | Implementación concreta de orquestación multi-agente con SQLite como coordination layer |
| `Cómo_SUSTITUIR_Un_Equipo_de_Marketing_Entero_con_IA_Demo_Rea.md` | Patrón de 5 agentes especializados en paralelo con orquestador, caso de uso marketing |
| `Claude_Code_Crea_tu_EQUIPO_de_Marketing_con_Agentes_de_IA_Pa.md` | Estructura de carpetas, CLAUDE.md, MCP config, routing entre agentes |
| `I_Turned_Claude_Code_into_an_AI_Hedge_Fund_and_this_happened.md` | Información asimétrica entre agentes, quality gates, blind backtest, problemas reales en producción |
| `El_Mejor_Agente_Open_Source_Actual_Hermes_Agent.md` | Skills dinámicos, perfiles, `/goal` command, PM2, Tailscale, Canvas/Kanban |
| `This_is_the_Ultimate_Claude_Code_Setup_-_Beats_OpenClaw_and_.md` | Los 5 pilares fundamentales; arquitectura de capas de memoria; anti-patrones frecuentes |
| `HERMES_Agent_acaba_de_LIBERAR_las_METAS_persistentes_GRATIS_.md` | Goals vs Cron Jobs vs Kanban; metaprompting; modelo juez; modelos económicos |
| `anthropics_anthropic-sdk-python.md` | SDK oficial Python: cliente async, streaming, tools, MCP integration, typed responses |
| `Ahora_Claude_Code_Puede_Automatizar_Tu_Negocio_Business_OS.md` | Business OS en 5 capas, commoditización de modelos, 27 cronjobs reales, Auto-Research |

---

## Patrones que se repiten en múltiples fuentes

### 1. Especialización con un orquestador central
Aparece en **todas** las fuentes con implementación real:
- Marketing team: orquestador + copy + SEO + conversión + estrategia (Víctor Pérez, Rodolfo Carrasco)
- Hedge fund: orchestrator + 5 analysts con información asimétrica (GreymatterAI)
- Pipeline de contenido: X Scout + Web Scout + Orchestrator + 3xResearcher + Analyst + Builder (Tonbi)
- Business OS: 27 cronjobs disparados desde un único punto de entrada (Daniel Carreón)

**Conclusión:** El patrón hub-and-spoke (orquestador → agentes especializados) es el patrón dominante y probado.

### 2. Estado compartido como fuente de verdad única
- SQLite como coordination layer y audit log (Tonbi: Kanban Board)
- Brand Context Folder / CLAUDE.md compartido entre todos los agentes (Simon Scrapes, Rodolfo Carrasco)
- Shared project folder como memoria común (Rodolfo Carrasco, Daniel Carreón)
- TimescaleDB para señales compartidas (GreymatterAI)

**Conclusión:** Los agentes no deben comunicarse entre sí directamente. Toda coordinación pasa por un estado compartido persistente.

### 3. Contexto de negocio como diferenciador principal
- "Sin contexto, el mejor modelo es un pasante" (Daniel Carreón)
- "El error más común es empezar por los agentes" — primero el contexto (Simon Scrapes)
- CLAUDE.md de ~200-500 líneas como system prompt persistente (Simon Scrapes, Rodolfo Carrasco, Daniel Carreón)
- Skills como módulos de contexto reutilizables (El Mejor Agente, David Ondrej, Ahora Claude Code)

**Conclusión:** La arquitectura de contexto precede a la arquitectura de agentes.

### 4. Human-in-the-loop checkpoint único
- Un solo gate de aprobación vía Telegram antes de fases destructivas/costosas (Tonbi)
- Regla 80/20: automatizar investigación y borradores, supervisar antes de publicar (Simon Scrapes)
- Modo bypass permissions solo para entornos controlados (Víctor Pérez)
- Nunca hacer pasar agente por humano real (Daniel Carreón)

**Conclusión:** El diseño debe incluir exactamente un punto de aprobación humana, no cero ni muchos.

### 5. Skills como módulos auto-mejorables
- Hermes Curator: elimina skills no usadas en 30-90 días (David Ondrej)
- `learnings.md` en cada skill para incorporar feedback (Simon Scrapes)
- Skill Creator Skill: el agente genera sus propias skills (Simon Scrapes, Daniel Carreón)
- Auto-Research (Karpathy): mejora automática de prompts a partir de conversaciones fallidas (Daniel Carreón)

**Conclusión:** Los skills deben ser versionables, auditables y auto-mejorables desde el primer día.

### 6. Modelos potentes para orquestación, económicos para subtareas
- Recomendación explícita de Claude Opus / GPT-5 para harnesses complejos (David Ondrej)
- Modelos chinos (Minimax, Kimi) para tareas de larga duración por costo (VeraBadías)
- DeepSeek V4 Flash ~170x más barato que Claude 4.7 para tareas repetitivas (Daniel Carreón)
- X Scout usa Grok; rest del fleet usa GPT-4.5 (Tonbi)

**Conclusión:** La elección de modelo debe hacerse por agente/tarea, no globalmente.

### 7. VPS + tmux/PM2 para operación 24/7
- Hermes en VPS Hostinger + PM2 para persistencia (Fazt, VeraBadías, David Ondrej)
- Dispatcher corriendo en sesión tmux persistente (Tonbi)
- Tailscale como VPN para acceso seguro al dashboard (Fazt, VeraBadías)

**Conclusión:** Los sistemas multi-agente productivos requieren infraestructura servidor, no laptops locales.

---

## Arquitectura recomendada

### Visión general

```
┌─────────────────────────────────────────────────────┐
│                   BUSINESS CONTEXT LAYER             │
│  CLAUDE.md / context/ / skills/ / brand/ / memory/  │
│           (Fuente: Simon Scrapes, Daniel Carreón)    │
└─────────────────────┬───────────────────────────────┘
                      │ inyecta contexto
┌─────────────────────▼───────────────────────────────┐
│              ORCHESTRATION LAYER                     │
│   Dispatcher ←──── SQLite State Store ────► Monitor  │
│   (polls tasks)    (coordination hub)   (dashboard)  │
│        Fuente: Tonbi, GreymatterAI                   │
└──────┬──────────────────────────────────┬────────────┘
       │ spawns                           │ gates
┌──────▼──────────────┐        ┌──────────▼──────────┐
│  AGENT FLEET         │        │  HUMAN CHECKPOINT    │
│  Specialist agents   │        │  Telegram/Discord    │
│  (own workspaces,    │        │  Approve / Reject /  │
│   own models)        │        │  Modify              │
│  Fuente: Tonbi,      │        │  Fuente: Tonbi,      │
│  GreymatterAI        │        │  Simon Scrapes        │
└──────┬──────────────┘        └─────────────────────┘
       │ outputs
┌──────▼──────────────────────────────────────────────┐
│              DELIVERY LAYER                          │
│   Persistent artifacts (Markdown, PDF, DB records)  │
│   External APIs (Stripe, Supabase, Gmail, etc.)      │
│   Fuente: Daniel Carreón, Víctor Pérez               │
└─────────────────────────────────────────────────────┘
```

### Decisiones arquitectónicas clave

**A. SQLite como coordination layer, no message queues**
El Kanban Board de Hermes demuestra que SQLite como estado compartido es suficiente para decenas de agentes sin condiciones de carrera, si el dispatcher implementa claim atómico (`UPDATE ... WHERE status='ready' LIMIT 1 RETURNING *`). Evita la complejidad operacional de Redis/Kafka para la mayoría de casos. [Fuente: Tonbi]

**B. Workspaces aislados por agente**
Cada agente corre en su directorio temporal limpio, con acceso read-only al contexto compartido y write solo a su workspace. Los artefactos finales se copian a `artifacts/` persistente. Esto previene el bug de auto-healing documentado (referencias a workspaces eliminados). [Fuente: Tonbi]

**C. Información asimétrica por agente**
Cada agente recibe solo el subconjunto de contexto relevante para su especialidad. Esto produce desacuerdo genuino entre agentes y evita groupthink. La inyección de contexto se hace en el dispatcher, no en los agentes mismos. [Fuente: GreymatterAI]

**D. Quality gate con scoring compuesto**
Antes de cualquier acción costosa (build, publish, API call pagada), un componente de scoring agrega señales de múltiples agentes y aplica un umbral configurable (ej: 0.35-0.65 según el dominio). Solo las oportunidades que superan el umbral avanzan. [Fuente: GreymatterAI]

**E. Three-tier de automatización**
- **Cron Jobs**: tareas recurrentes calendarizadas (monitoring, briefings, snapshots)
- **Goals**: objetivos de largo plazo con modelo juez que valida criterios de éxito sin ruta predefinida
- **Kanban**: orquestación explícita con dependencias entre tareas y múltiples agentes
[Fuente: VeraBadías, Tonbi]

**F. Skills versionables con learnings**
Cada skill es un archivo Markdown con: instrucciones, ejemplos few-shot, sección `## Learnings` que se actualiza con feedback, y una sección `## Antipatterns`. El Skill Creator genera automáticamente el scaffold. [Fuente: Simon Scrapes, Daniel Carreón]

---

## Stack sugerido

### Infraestructura

| Componente | Tecnología | Justificación |
|-----------|-----------|---------------|
| **Runtime** | VPS Linux (Hostinger KVM2: 2 CPU, 8GB RAM) | 24/7, sin dependencia de equipo local [Fazt, David Ondrej] |
| **Process manager** | PM2 | Persistencia ante reinicios, logs centralizados [Fazt] |
| **Multiplexor** | tmux | Dispatcher y agentes en sesiones separadas [Tonbi] |
| **VPN/acceso seguro** | Tailscale | Acceso al dashboard sin exponerlo públicamente [Fazt, VeraBadías] |
| **Containerización** | Docker + Docker Compose | Aislamiento de dependencias, portabilidad [GreymatterAI] |

### Capa de datos

| Componente | Tecnología | Justificación |
|-----------|-----------|---------------|
| **Coordination store** | SQLite (via `sqlite3` o `aiosqlite`) | Suficiente para coordinación multi-agente, sin ops overhead [Tonbi] |
| **Memoria a largo plazo** | PostgreSQL/Supabase | Métricas, historial de conversaciones, audit log permanente [Daniel Carreón] |
| **Series temporales** | TimescaleDB (si dominio financiero) | Optimizado para signals y precios [GreymatterAI] |
| **Memoria local** | Hermes Memory Plugin (SQL local) | Sin envío de datos a la nube [David Ondrej] |

### Capa de agentes

| Componente | Tecnología | Justificación |
|-----------|-----------|---------------|
| **Framework principal** | Claude Code o Hermes Agent | Ambos proveen skills, context management y scheduling nativo |
| **SDK Python** | `anthropic-sdk-python` (AsyncAnthropic) | Soporte nativo async, tools, streaming, MCP integration [anthropic-sdk-python] |
| **Router de modelos** | OpenRouter | Una sola API key para Claude, GPT, Grok, Kimi, Minimax [David Ondrej] |
| **Modelo orquestador** | Claude Opus 4.5+ o GPT-4.5 | Harnesses complejos requieren modelos potentes [David Ondrej] |
| **Modelo subtareas** | DeepSeek V4 Flash / Minimax / Kimi | ~170x más barato para tareas repetitivas [Daniel Carreón, VeraBadías] |
| **Contexto persistente** | CLAUDE.md + context/ folder | System prompt base + brand context [Simon Scrapes, Rodolfo Carrasco] |

### Integraciones y notificaciones

| Componente | Tecnología | Justificación |
|-----------|-----------|---------------|
| **Human checkpoint** | Telegram Bot API | Gate de aprobación único, bajo latencia [Tonbi, VeraBadías] |
| **Notificaciones adicionales** | Discord webhook | Monitoring y logs de ejecución [David Ondrej] |
| **Herramientas externas** | MCP (Model Context Protocol) | Protocolo estándar para conectar servicios externos [Rodolfo Carrasco, Daniel Carreón] |
| **Scheduling** | Cron (sistema) + PM2 cron | Automatizaciones calendarizadas sin dependencias adicionales |
| **Generación de reportes** | ReportLab (Python) | PDF desde Markdown, probado en producción [Víctor Pérez] |

### Dependencias Python core

```toml
[dependencies]
anthropic = ">=0.40.0"          # SDK oficial con async, tools, MCP
aiosqlite = ">=0.20.0"          # SQLite async para coordination layer  
httpx = ">=0.27.0"              # HTTP client (ya incluido en anthropic SDK)
pydantic = ">=2.0.0"            # Typed models para tasks y agent configs
python-telegram-bot = ">=21.0"  # Human checkpoint via Telegram
celery = ">=5.3.0"              # Task queue para workloads pesados (opcional)
redis = ">=5.0.0"               # Backend de Celery si se necesita (opcional)
reportlab = ">=4.0.0"           # Generación de PDFs
python-dotenv = ">=1.0.0"       # Manejo de .env para API keys
```

---

## Riesgos y anti-patrones identificados

### Anti-patrones críticos

**1. Empezar por los agentes antes que por el contexto**
> "El error más común es empezar por los agentes o la orquestación multi-agente" [Simon Scrapes]

Sin un CLAUDE.md sólido y una carpeta de contexto bien estructurada, añadir más agentes solo amplifica los errores. La arquitectura de contexto debe preceder a la arquitectura de agentes.

**2. Comunicación directa entre agentes (peer-to-peer)**
Los agentes que se llaman entre sí directamente crean condiciones de carrera, trabajo duplicado y falta de auditabilidad. Toda coordinación debe pasar por el estado compartido (SQLite/Kanban). [Tonbi]

**3. Modelos pequeños en harnesses agénticos complejos**
> "Los modelos pequeños y baratos degradan severamente la calidad en harnesses agénticos complejos" [David Ondrej]

El ahorro en el modelo orquestador sale caro en tokens desperdiciados por razonamiento pobre. Usar modelos económicos solo para subtareas bien definidas.

**4. Context rot — skills obsoletos que desperdician tokens**
Sin un mecanismo de poda (Hermes Curator: stale a 30 días, eliminación a 90 días), los skills obsoletos consumen contexto útil y degradan el rendimiento. [David Ondrej]

**5. Artefactos en workspaces temporales**
Si los agentes guardan outputs en sus directorios temporales, al eliminarse el workspace el artefacto se pierde. Siempre copiar outputs finales a `artifacts/` persistente. [Tonbi - "auto-healing" documentado]

**6. CLAUDE.md infinitamente largo**
Un archivo de contexto que supera ~200-500 líneas o incluye todo inline se convierte en ruido. Debe referenciar archivos externos y mantener solo lo estrictamente operativo. [Simon Scrapes]

**7. Groupthink por información simétrica**
Si todos los agentes leen el mismo dataset, sus análisis convergen artificialmente. La información asimétrica (cada agente ve su subconjunto) produce desacuerdo genuino y mejores decisiones. [GreymatterAI]

**8. Cero o demasiados checkpoints humanos**
Cero checkpoints: el sistema toma acciones irreversibles sin supervisión. Demasiados: se convierte en un formulario interactivo, no en automatización. El diseño óptimo es exactamente un gate antes de acciones de alto impacto. [Tonbi, Simon Scrapes]

**9. Exponer el dashboard sin VPN**
El flag `--host 0.0.0.0 --insecure` expone el agente con todos sus permisos a internet. Solo para pruebas; en producción, siempre detrás de Tailscale u otra VPN. [Fazt]

**10. Rate limits no gestionados en producción**
En producción real, los rate limits de APIs son el primer fallo. Se necesita exponential backoff, circuit breakers y monitoreo de cuotas desde el día 1. [GreymatterAI - "problemas reales en producción"]

---

## Spec de implementación

### Fase 0: Fundamentos de contexto (Días 1-2)

**0.1 Estructura de carpetas base**
```
project/
├── .env                          # API keys (nunca en git)
├── CLAUDE.md                     # System prompt base (~200-500 líneas)
├── context/
│   ├── business.md               # Identidad, misión, ICP, posicionamiento
│   ├── brand.md                  # Voz, tono, colores, tipografía
│   ├── rules.md                  # Reglas no negociables del sistema
│   └── integrations.md           # Servicios externos conectados y sus propósitos
├── skills/
│   ├── _template.md              # Template para crear nuevas skills
│   └── skill-creator.md          # Meta-skill para generar otras skills
├── agents/
│   ├── orchestrator.md           # Instrucciones del orquestador
│   └── _agent_template.md        # Template para nuevos agentes
├── artifacts/                    # Outputs persistentes (nunca temporales)
├── memory/                       # Estado de largo plazo
│   └── learnings.md              # Feedback acumulado
├── scripts/
│   ├── dispatcher.py             # Loop principal de coordinación
│   ├── db.py                     # Helpers SQLite
│   └── telegram_gate.py          # Human checkpoint
└── workspaces/                   # Directorios temporales por ejecución (gitignore)
```

**0.2 CLAUDE.md mínimo viable**
Debe incluir: propósito del sistema, árbol de archivos críticos, reglas de comportamiento (qué hacer/no hacer), routing básico a agentes (`@nombre`), y referencia a `context/business.md`. No incluir el contenido de esos archivos inline.

**0.3 Variables de entorno**
```env
# .env
ANTHROPIC_API_KEY=sk-ant-...
OPENROUTER_API_KEY=sk-or-...
TELEGRAM_BOT_TOKEN=...
TELEGRAM_APPROVED_USERS=123456789,987654321
DATABASE_PATH=./memory/state.db
ORCHESTRATOR_MODEL=claude-opus-4-5
WORKER_MODEL=claude-haiku-3-5
CHEAP_MODEL=openrouter/deepseek/deepseek-chat-v3
```

---

### Fase 1: Coordination Layer con SQLite (Día 2-3)

**1.1 Schema de base de datos**
```sql
-- scripts/schema.sql
CREATE TABLE IF NOT EXISTS tasks (
    id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    assigned_agent TEXT NOT NULL,
    status TEXT DEFAULT 'todo' 
        CHECK(status IN ('todo','ready','in_progress','review','done','failed')),
    priority INTEGER DEFAULT 5,
    parent_ids TEXT DEFAULT '[]',  -- JSON array de IDs dependencias
    metadata TEXT DEFAULT '{}',    -- JSON para contexto adicional del agente
    workspace TEXT,                -- Path al workspace temporal
    artifact_path TEXT,            -- Path al output final en artifacts/
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    claimed_at TIMESTAMP,
    completed_at TIMESTAMP,
    error_log TEXT
);

CREATE TABLE IF NOT EXISTS agent_runs (
    id TEXT PRIMARY KEY,
    task_id TEXT REFERENCES tasks(id),
    agent_name TEXT,
    model_used TEXT,
    tokens_input INTEGER,
    tokens_output INTEGER,
    duration_seconds REAL,
    status TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS memory (
    key TEXT PRIMARY KEY,
    value TEXT,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**1.2 Dispatcher — loop principal**
```python
# scripts/dispatcher.py
import asyncio
import uuid
import json
from datetime import datetime
from pathlib import Path
import aiosqlite
from anthropic import AsyncAnthropic

DB_PATH = "./memory/state.db"
POLL_INTERVAL = 5  # segundos

async def claim_next_task(db) -> dict | None:
    """Claim atómico — evita condiciones de carrera entre agentes paralelos"""
    async with db.execute("""
        UPDATE tasks SET status='in_progress', claimed_at=?
        WHERE id = (
            SELECT id FROM tasks 
            WHERE status='ready'
            ORDER BY priority DESC, created_at ASC
            LIMIT 1
        )
        RETURNING *
    """, (datetime.utcnow().isoformat(),)) as cursor:
        row = await cursor.fetchone()
        await db.commit()
        return dict(row) if row else None

async def promote_ready_tasks(db):
    """Promueve tareas cuyas dependencias están completas"""
    async with db.execute("""
        SELECT id, parent_ids FROM tasks WHERE status='todo'
    """) as cursor:
        rows = await cursor.fetchall()
    
    for row in rows:
        task_id, parent_ids_json = row
        parent_ids = json.loads(parent_ids_json)
        if not parent_ids:
            await db.execute(
                "UPDATE tasks SET status='ready' WHERE id=?", (task_id,)
            )
            continue
        # Verificar si todos los padres están completos
        placeholders = ','.join('?' * len(parent_ids))
        async with db.execute(f"""
            SELECT COUNT(*) FROM tasks 
            WHERE id IN ({placeholders}) AND status != 'done'
        """, parent_ids) as cursor:
            (pending_count,) = await cursor.fetchone()
        if pending_count == 0:
            await db.execute(
                "UPDATE tasks SET status='ready' WHERE id=?", (task_id,)
            )
    await db.commit()

async def run_dispatcher():
    async with aiosqlite.connect(DB_PATH) as db:
        db.row_factory = aiosqlite.Row
        while True:
            await promote_ready_tasks(db)
            task = await claim_next_task(db)
            if task:
                asyncio.create_task(execute_agent(db, task))
            await asyncio.sleep(POLL_INTERVAL)

if __name__ == "__main__":
    asyncio.run(run_dispatcher())
```

---

### Fase 2: Agentes especializados (Días 3-5)

**2.1 Clase base de agente**
```python
# scripts/agent_base.py
import os
import uuid
import shutil
from pathlib import Path
from anthropic import AsyncAnthropic
import aiosqlite

class BaseAgent:
    def __init__(self, name: str, model: str, skill_path: str | None = None):
        self.name = name
        self.model = model
        self.client = AsyncAnthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
        self.skill_path = skill_path
        
    def _load_context(self, files: list[str]) -> str:
        """Carga contexto asimétrico según el agente"""
        context_parts = []
        for f in files:
            path = Path(f)
            if path.exists():
                context_parts.append(f"# {path.name}\n{path.read_text()}")
        return "\n\n---\n\n".join(context_parts)
    
    def _create_workspace(self) -> Path:
        """Crea workspace temporal aislado"""
        workspace = Path("workspaces") / str(uuid.uuid4())[:8]
        workspace.mkdir(parents=True, exist_ok=True)
        return workspace
    
    def _save_artifact(self, content: str, filename: str, workspace: Path) -> Path:
        """Guarda output final en artifacts/ persistente"""
        artifact_dir = Path("artifacts") / self.name
        artifact_dir.mkdir(parents=True, exist_ok=True)
        artifact_path = artifact_dir / filename
        artifact_path.write_text(content)
        # Cleanup workspace temporal
        shutil.rmtree(workspace, ignore_errors=True)
        return artifact_path

    async def execute(self, task: dict) -> dict:
        """Override en cada agente especializado"""
        raise NotImplementedError
```

**2.2 Implementación de agente con tools**
```python
# scripts/agents/researcher.py
from .agent_base import BaseAgent
from anthropic import AsyncAnthropic
import json

RESEARCHER_CONTEXT_FILES = [
    "context/business.md",
    "skills/research.md",
    # NO incluye brand.md ni integrations.md — información asimétrica
]

class ResearcherAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="researcher",
            model=os.getenv("WORKER_MODEL", "claude-haiku-3-5"),
            skill_path="skills/research.md"
        )
        self.tools = [
            {
                "name": "web_search",
                "description": "Search the web for information",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "query": {"type": "string"},
                        "max_results": {"type": "integer", "default": 5}
                    },
                    "required": ["query"]
                }
            },
            {
                "name": "save_finding",
                "description": "Save a research finding to the shared state",
                "input_schema": {
                    "type": "object", 
                    "properties": {
                        "key": {"type": "string"},
                        "content": {"type": "string"},
                        "confidence": {"type": "number", "minimum": 0, "maximum": 1}
                    },
                    "required": ["key", "content"]
                }
            }
        ]
    
    async def execute(self, task: dict) -> dict:
        context = self._load_context(RESEARCHER_CONTEXT_FILES)
        workspace = self._create_workspace()
        
        messages = [{
            "role": "user",
            "content": f"""
Context:\n{context}

Task: {task['description']}

Research thoroughly and save your findings using save_finding.
"""
        }]
        
        # Agentic loop con tool use
        while True:
            response = await self.client.messages.create(
                model=self.model,
                max_tokens=8096,
                tools=self.tools,
                messages=messages
            )
            
            if response.stop_reason == "end_turn":
                break
                
            if response.stop_reason == "tool_use":
                tool_results = []
                for block in response.content:
                    if block.type == "tool_use":
                        result = await self._execute_tool(block.name, block.input)
                        tool_results.append({
                            "type": "tool_result",
                            "tool_use_id": block.id,
                            "content": json.dumps(result)
                        })
                
                messages.append({"role": "assistant", "content": response.content})
                messages.append({"role": "user", "content": tool_results})
        
        # Extraer texto final
        final_text = next(
            (b.text for b in response.content if hasattr(b, 'text')), ""
        )
        artifact_path = self._save_artifact(final_text, f"{task['id']}_research.md", workspace)
        
        return {
            "status": "done",
            "artifact_path": str(artifact_path),
            "tokens_used": response.usage.input_tokens + response.usage.output_tokens
        }
    
    async def _execute_tool(self, name: str, inputs: dict) -> dict:
        # Implementar herramientas reales aquí
        if name == "web_search":
            # Integrar con Brave Search API, Tavily, etc.
            return {"results": []}
        if name == "save_finding":
            # Guardar en SQLite memory table
            return {"saved": True}
        return {"error": f"Unknown tool: {name}"}
```

---

### Fase 3: Human Checkpoint via Telegram (Día 5)

```python
# scripts/telegram_gate.py
import os
import asyncio
from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CallbackQueryHandler

APPROVED_USERS = list(map(int, os.getenv("TELEGRAM_APPROVED_USERS", "").split(",")))

class HumanGate:
    def __init__(self):
        self.bot = Bot(token=os.getenv("TELEGRAM_BOT_TOKEN"))
        self.pending: dict[str, asyncio.Future] = {}
    
    async def request_approval(
        self, 
        task_id: str, 
        summary: str, 
        artifact_preview: str
    ) -> str:
        """Returns: 'approved' | 'rejected' | 'modified:<new_instructions>'"""
        
        future = asyncio.Future()
        self.pending[task_id] = future
        
        keyboard = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("