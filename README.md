# Cadastro de Clientes API

API REST para cadastro e gerenciamento de pessoas, construída com FastAPI, Pydantic e SQLAlchemy. Os dados são armazenados em um banco SQLite local.

## Requisitos

- Python 3.15 ou superior
- [uv](https://docs.astral.sh/uv/) para instalar as dependências e executar o projeto

## Como executar

Na raiz do projeto, instale as dependências e inicie o servidor:

```bash
uv sync
uv run uvicorn app.main:app --reload
```

A API ficará disponível em `http://127.0.0.1:8000`. A documentação interativa do Swagger fica em `/docs`, a documentação ReDoc em `/redoc` e o schema OpenAPI em `/openapi.json`.

Na primeira inicialização, as tabelas são criadas automaticamente no arquivo `Luizapp.db`, no diretório de execução.

## Endpoints

| Método | Caminho | Descrição |
| --- | --- | --- |
| `GET` | `/` | Verifica se a aplicação está respondendo |
| `POST` | `/v1/people` | Cadastra uma pessoa (retorna `201`) |
| `GET` | `/v1/persons` | Lista as pessoas cadastradas |
| `PUT` | `/v1/people/{people_id}` | Atualiza uma pessoa pelo UUID |
| `DELETE` | `/v1/people/{people_id}` | Exclui uma pessoa pelo UUID |

As operações de criação e atualização recebem `name`, `age`, `email` e, opcionalmente, `is_active`. O campo `id` pode ser informado; caso contrário, é gerado automaticamente. `is_active` aceita `ATIVO` ou `INATIVO` e assume `ATIVO` por padrão.

Exemplo de cadastro:

```bash
curl -X POST http://127.0.0.1:8000/v1/people \
  -H 'Content-Type: application/json' \
  -d '{
    "name": "Maria Silva",
    "age": 30,
    "email": "maria@example.com",
    "is_active": "ATIVO"
  }'
```

Exemplo de resposta:

```json
{
  "id": "UUID-gerado-pela-api",
  "is_active": "ATIVO",
  "name": "Maria Silva",
  "age": 30,
  "email": "maria@example.com"
}
```

Para atualizar ou excluir, substitua `{people_id}` pelo UUID retornado no cadastro. A aplicação organiza o código em rotas (`app/api`), schemas (`app/schema`), serviços (`app/service`), repositório (`app/repo`) e configuração do banco (`app/database`).
