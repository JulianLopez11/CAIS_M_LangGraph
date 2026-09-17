# CAIS_M LangGraph

Ejemplos de construcción y ejecución de grafos con [LangGraph](https://langchain-ai.github.io/langgraph/) en Python. El proyecto incluye un grafo local y otro conectado a Google Gemini mediante LangChain.

## Estructura del proyecto

```text
CAIS_M_LangGraph/
├── .env                    # configuración local; ignorado por Git
├── .env.example            # plantilla de configuración
├── .gitignore
├── README.md
├── requirements.txt
├── quickstart_langgraph.py
├── quickstart_langgraph_llm.py
└── docs/
    └── img/
        └── evidencia.png
```

### Archivos

- `quickstart_langgraph.py`: grafo local con los nodos `analizar` y `responder`. Mantiene la pregunta, la respuesta y el número de pasos.
- `quickstart_langgraph_llm.py`: grafo de un nodo que envía una pregunta a Google Gemini usando `ChatGoogleGenerativeAI`.
- `requirements.txt`: dependencias fijadas del proyecto.
- `.env.example`: plantilla para la clave de Google.
- `.gitignore`: excluye archivos `.env` y carpetas de entornos virtuales.
- `docs/img/evidencia.png`: captura de evidencia de ejecución.

## Requisitos

- Python 3.10 o superior.
- Una clave de API de Google para ejecutar el ejemplo con Gemini.

## Instalación

Desde la raíz del proyecto, crea y activa un entorno virtual:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
pip install python-dotenv
```

En Linux o macOS:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
pip install python-dotenv
```

`python-dotenv` se instala aparte porque el script LLM lo utiliza, pero todavía no está incluido en `requirements.txt`.

## Configuración

Copia `.env.example` como `.env` y agrega tu clave:

```powershell
Copy-Item .env.example .env
```

Después edita `.env`:

```env
GOOGLE_API_KEY=tu_clave_de_google
```

`.env` está excluido por `.gitignore`; no subas claves de API al repositorio.

## Ejecución

### Grafo local

```powershell
python quickstart_langgraph.py
```

Construye y compila el flujo:

```text
analizar -> responder -> fin
```

El grafo procesa la pregunta `¿qué es LangGraph?`, muestra el estado final y calcula el tiempo de ejecución.

### Grafo con Gemini

Con `GOOGLE_API_KEY` configurada, ejecuta:

```powershell
python quickstart_langgraph_llm.py
```

El script carga la variable desde `.env`, usa el modelo `gemini-3.6-flash` y solicita los diez primeros dígitos de Pi.

## Conceptos de LangGraph

- `TypedDict`: define la forma del estado que circula por el grafo.
- `StateGraph`: crea el grafo cuyos nodos reciben y devuelven el estado.
- `add_node`: registra funciones como nodos.
- `set_entry_point`: establece el nodo inicial.
- `add_edge`: conecta los nodos.
- `compile`: prepara el grafo para ejecutarlo.
- `invoke`: ejecuta el grafo con un estado inicial.

## Evidencia

![Evidencia de ejecución](docs/img/evidencia.png)
![Evidencia de ejecución 2](docs/img/evidencia2.png)

## Evidencia con Tiempo de Llamado de Grafo al LLM

![Evidencia de ejecución3](docs/img/evidencia3.png)


