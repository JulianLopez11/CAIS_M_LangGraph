import time
from typing import TypedDict
from langgraph.graph import StateGraph, END

class State(TypedDict):
    pregunta: str
    respuesta: str
    pasos: int

def analizar(state: State) -> State:
    state["pasos"] += 1
    print(f"[nodo analizar] pregunta='{state['pregunta']}'")
    return state

def responder(state: State) -> State:
    state["pasos"] += 1
    state["respuesta"] = f"Procesé: {state['pregunta']}"
    print(f"[nodo responder] respuesta='{state['respuesta']}'")
    return state

builder = StateGraph(State)
builder.add_node("analizar", analizar)
builder.add_node("responder", responder)
builder.set_entry_point("analizar")
builder.add_edge("analizar", "responder")
builder.add_edge("responder", END)

grafo = builder.compile()

t0 = time.time()
resultado = grafo.invoke({"pregunta": "¿qué es LangGraph?", "respuesta": "", "pasos": 0})
t1 = time.time()

print("\n--- resultado final ---")
print(resultado)
print(f"tiempo de ejecución: {t1 - t0:.4f}s")