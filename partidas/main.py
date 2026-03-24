from fastapi import FastAPI
import requests
import os

app = FastAPI()

TIMES_URL = os.getenv("TIMES_URL")

@app.get("/partidas/{id}")
def get_partida(id: int):
    try:
        response = requests.get(f"{TIMES_URL}/times/{id}", timeout=2)
        time = response.json()
    except Exception:
        time = {"erro": "Serviço de times indisponível"}

    return {
        "id": id,
        "adversario": "Real Madrid",
        "placar": "2x1",
        "time": time
    }