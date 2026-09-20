from collections.abc import Generator

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from app.database import Base, get_db
from app.main import app


@pytest.fixture
def client(tmp_path) -> Generator[TestClient, None, None]:
    engine = create_engine(
        f"sqlite:///{tmp_path / 'test.db'}",
        connect_args={"check_same_thread": False},
    )
    Base.metadata.create_all(bind=engine)
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    def override_get_db() -> Generator[Session, None, None]:
        db = TestingSessionLocal()
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)
    app.dependency_overrides.clear()
    Base.metadata.drop_all(bind=engine)


def test_create_and_list_task(client: TestClient) -> None:
    create_response = client.post(
        "/tasks/",
        json={"title": "Estudar FastAPI", "description": "Praticar CRUD"},
    )

    assert create_response.status_code == 201
    assert create_response.json()["title"] == "Estudar FastAPI"
    assert create_response.json()["completed"] is False

    list_response = client.get("/tasks/")
    assert list_response.status_code == 200
    assert len(list_response.json()) == 1


def test_update_task(client: TestClient) -> None:
    task_id = client.post("/tasks/", json={"title": "Tarefa original"}).json()["id"]

    response = client.put(
        f"/tasks/{task_id}",
        json={"title": "Tarefa atualizada", "completed": True},
    )

    assert response.status_code == 200
    assert response.json()["title"] == "Tarefa atualizada"
    assert response.json()["completed"] is True


def test_delete_and_get_missing_task(client: TestClient) -> None:
    task_id = client.post("/tasks/", json={"title": "Excluir tarefa"}).json()["id"]

    delete_response = client.delete(f"/tasks/{task_id}")
    assert delete_response.status_code == 204

    missing_response = client.get(f"/tasks/{task_id}")
    assert missing_response.status_code == 404
