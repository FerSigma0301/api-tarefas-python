from fastapi import FastAPI

app = FastAPI(
    title="API de Tarefas",
    version="0.1.0",
    description="API REST para gerenciamento de tarefas.",
)


@app.get("/health", tags=["Health"])
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/", tags=["Health"])
def root() -> dict[str, str]:
    return {"message": "API de Tarefas online"}
