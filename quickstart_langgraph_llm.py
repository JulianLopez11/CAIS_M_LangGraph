import time
from typing import TypedDict
from dotenv import load_dotenv
from langgraph.graph import StateGraph, END
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

class State(TypedDict):
    pregunta: str
    respuesta: str

llm = ChatGoogleGenerativeAI(model="gemini-3.6-flash")

def responder(state: State) -> State:
    msg = llm.invoke(state["pregunta"])
    state["respuesta"] = msg.content
    return state

builder = StateGraph(State)
builder.add_node("responder", responder)
builder.set_entry_point("responder")
builder.add_edge("responder", END)

grafo = builder.compile()

t0 = time.time()
resultado = grafo.invoke({"pregunta": "Dame la capital de Francia, España, Cabo Verde y Colombia", "respuesta": ""})
t1 = time.time()

print(resultado)
print(f"tiempo de ejecución: {t1 - t0:.4f}s")