from fastapi import FastAPI

from app.routes.tasks import router as tasks_router

app = FastAPI(
    title="API de Tarefas",
    version="0.1.0",
    description="API REST para gerenciamento de tarefas.",
)

app.include_router(tasks_router)


@app.get("/health", tags=["Health"])
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/", tags=["Health"])
def root() -> dict[str, str]:
    return {"message": "API de Tarefas online"}
