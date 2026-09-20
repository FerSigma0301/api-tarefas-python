# API de Tarefas

API REST para gerenciamento de tarefas, desenvolvida com Python, FastAPI, SQLAlchemy e SQLite.

## Funcionalidades

- Criar tarefas
- Listar tarefas
- Consultar uma tarefa por ID
- Atualizar título, descrição e status
- Excluir tarefas
- Validação automática dos dados
- Documentação interativa com Swagger
- Testes automatizados com Pytest

## Tecnologias

- Python 3.10+
- FastAPI
- SQLAlchemy
- SQLite
- Pytest

## Instalação

```bash
python -m venv .venv
```

No Windows:

```bash
.venv\Scripts\activate
```

No Linux/macOS:

```bash
source .venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

## Executar a aplicação

```bash
uvicorn app.main:app --reload
```

A API estará disponível em `http://127.0.0.1:8000`.

Documentação Swagger: `http://127.0.0.1:8000/docs`

## Executar os testes

```bash
pytest
```

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

### Exemplo de criação

```json
{
  "title": "Estudar FastAPI",
  "description": "Criar uma API com CRUD"
}
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

## Possíveis melhorias

- Autenticação de usuários
- Paginação e filtros
- Docker
- Migrações com Alembic
- Deploy em um serviço de nuvem
