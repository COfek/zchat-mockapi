# Zchat Mock API

A mock FastAPI server that simulates the Zchat backend API for local frontend development. Responses are hardcoded — no real logic is implemented.

## Stack

- **Python** + **FastAPI**
- **Uvicorn** (ASGI server)
- **Pydantic** (request/response validation)

## Project Structure

```
app/
├── main.py           # App factory, CORS, router registration
├── models/
│   └── schemas.py    # Pydantic models (ChatRequest, ChatResponse, Entity)
└── routers/
    └── chat.py       # POST /chat endpoint
requirements.txt
run.py                # Entry point
```

## Getting Started

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the server

```bash
python run.py
```

The API will be available at `http://localhost:8000`.  
Interactive docs at `http://localhost:8000/docs`.

---

## Endpoint

### `POST /chat`

#### Headers

| Header | Required |
|--------|----------|
| `api-key` | ✅ — any non-empty string is accepted |
| `user-personal-number` | ✅ — any non-empty string is accepted |

#### Request Body

```json
{
  "message": "string",
  "session_id": "string | null",
  "unit": "string | null",
  "reality": "string | null",
  "module": "string | null",
  "role": "string | null",
  "plan": "string | null",
  "case": "string | null"
}
```

#### Response Body

```json
{
  "response": "string",
  "session_id": "string",
  "needs_clarification": "bool",
  "clarify_for": "string | null",
  "reasoning_content": "string | null",
  "entities": [
    {
      "layer": "string | null",
      "entity_id": "string | null",
      "geometry": "string | null"
    }
  ]
}
```

#### Notes

- `session_id` is optional on the first request — a new one will be generated automatically. Pass it back on subsequent requests to maintain conversation context.
- `entities` contains map entities to be rendered on the frontend.

---

## CORS

All origins are allowed (`*`) for local development.
