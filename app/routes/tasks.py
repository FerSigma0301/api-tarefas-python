from fastapi import APIRouter

router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.get("/")
def list_tasks() -> list[dict[str, str | bool]]:
    return []
