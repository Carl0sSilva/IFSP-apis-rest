from fastapi import FastAPI
import time

app = FastAPI()

@app.get("/times/{id}")
def get_time(id: int):
    return {
        "id": id,
        "nome": "Barcelona",
        "pais": "Espanha"
    }


# Simulando timeout
#@app.get("/times/{id}")
#def get_time(id: int):
#    time.sleep(5)  # demora 5 segundos
#    return {
#        "id": id,
#        "nome": "Barcelona",
#        "pais": "Espanha"
#    }