# API de Tarefas

API REST para gerenciamento de tarefas, criada com Python e FastAPI.

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115%2B-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Tests](https://img.shields.io/badge/tests-Pytest-0A9EDC?logo=pytest&logoColor=white)](https://pytest.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](#licença)

## Sobre o projeto

Projeto de portfólio desenvolvido para praticar a construção de APIs backend organizadas, documentadas e testáveis.

## Funcionalidades

- Criar, listar, consultar, atualizar e excluir tarefas
- Validação automática dos dados
- Persistência com SQLite e SQLAlchemy
- Documentação interativa com Swagger e ReDoc
- Testes automatizados com Pytest
- Endpoint de verificação de saúde da aplicação

## Tecnologias

| Tecnologia | Uso |
|---|---|
| Python 3.10+ | Linguagem principal |
| FastAPI | API REST e documentação |
| SQLAlchemy | ORM e persistência |
| SQLite | Banco de dados local |
| Pydantic | Validação e schemas |
| Pytest | Testes automatizados |

## Como executar

```bash
git clone -b feature/api-tarefas-inicial https://github.com/FerSigma0301/api-tarefas-python.git
cd api-tarefas-python
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

A API estará disponível em `http://127.0.0.1:8000`.

- Swagger: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## Endpoints

| Método | Endpoint | Descrição |
|---|---|---|
| GET | `/` | Verifica se a API está online |
| GET | `/health` | Health check |
| POST | `/tasks/` | Cria uma tarefa |
| GET | `/tasks/` | Lista todas as tarefas |
| GET | `/tasks/{task_id}` | Busca uma tarefa |
| PUT | `/tasks/{task_id}` | Atualiza uma tarefa |
| DELETE | `/tasks/{task_id}` | Exclui uma tarefa |

## Exemplo de criação

```json
{
  "title": "Estudar FastAPI",
  "description": "Criar uma API com CRUD"
}
```

## Testes

```bash
pytest
```

## Estrutura

```text
app/
├── database.py
├── main.py
├── models.py
├── schemas.py
└── routes/
    └── tasks.py

tests/
├── test_health.py
└── test_tasks.py
```

## Roadmap

- [ ] Autenticação de usuários
- [ ] Paginação e filtros
- [ ] Docker
- [ ] Migrações com Alembic
- [ ] Deploy em nuvem

## Licença

Este projeto está sob a licença MIT.
