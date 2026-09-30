from fastapi import FastAPI

app = FastAPI(
    title="Mourão Vision API",
    description="API do sistema de monitoramento urbano Mourão Vision",
    version="0.1.0"
)

@app.get("/")
def root():
    return {
        "mensagem": "Mourão Vision API",
        "versão": "0.1.0",
        "status": "online",
    }

