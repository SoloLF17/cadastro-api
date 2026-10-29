# Cadastro de Clientes API

API REST para cadastrar e gerenciar pessoas. O projeto usa FastAPI, Pydantic, SQLAlchemy e SQLite, e inclui um painel web servido pela própria aplicação.

## Requisitos

- Python 3.15 ou superior
- [uv](https://docs.astral.sh/uv/)

## Instalação e execução

Na raiz do projeto, instale as dependências e inicie o servidor:

```bash
uv sync
uv run uvicorn app.main:app --reload
```

A aplicação ficará disponível em <http://127.0.0.1:8000>. A página inicial abre o painel de cadastro; a documentação interativa fica em `/docs`, a ReDoc em `/redoc` e o schema OpenAPI em `/openapi.json`.

O banco SQLite é criado em `Luizapp.db`, relativo ao diretório de execução. As tabelas são criadas automaticamente na inicialização. Para preservar os dados, mantenha esse arquivo; para começar com um banco vazio, remova-o com o servidor parado.

## Painel web

A página inicial permite cadastrar, listar, pesquisar, editar e excluir pessoas. O painel consulta a API local e precisa do servidor em execução. A lista é carregada ao abrir a página; use **Pessoas cadastradas** para exibi-la.

## Endpoints

| Método | Caminho | Descrição |
| --- | --- | --- |
| `GET` | `/` | Exibe o painel web |
| `POST` | `/v1/people` | Cadastra uma pessoa (`201 Created`) |
| `GET` | `/v1/persons` | Lista as pessoas cadastradas |
| `PUT` | `/v1/people/{people_id}` | Atualiza uma pessoa identificada por UUID |
| `DELETE` | `/v1/people/{people_id}` | Exclui uma pessoa identificada por UUID |

Os campos `name`, `age` e `email` são obrigatórios. `email` deve ter formato válido. `id` é opcional e gerado automaticamente como UUID quando omitido. `is_active` é opcional, aceita `true` ou `false` e assume `true` por padrão.

### Cadastrar uma pessoa

```bash
curl -X POST http://127.0.0.1:8000/v1/people \
  -H 'Content-Type: application/json' \
  -d '{
    "name": "Maria Silva",
    "age": 30,
    "email": "maria@example.com",
    "is_active": true
  }'
```

Exemplo de resposta:

```json
{
  "id": "UUID-gerado-pela-api",
  "is_active": true,
  "name": "Maria Silva",
  "age": 30,
  "email": "maria@example.com"
}
```

Para atualizar ou excluir, use o `id` retornado no cadastro no lugar de `{people_id}`. O `PUT` recebe os mesmos campos de criação. A listagem retorna um array, inclusive quando ainda não há registros.

## Organização do código

- `app/api`: rotas HTTP
- `app/schema`: schemas de entrada e resposta
- `app/service`: serviços da aplicação
- `app/repo`: acesso aos dados
- `app/models`: modelo SQLAlchemy
- `app/database`: configuração e sessão SQLite
- `frontend/index.html`: painel web
