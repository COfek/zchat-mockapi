from pydantic import BaseModel


class ChatRequest(BaseModel):
    message: str
    session_id: str | None = None
    unit: str | None = None
    reality: str | None = None
    module: str | None = None
    role: str | None = None
    plan: str | None = None
    case: str | None = None


class Entity(BaseModel):
    layer: str | None = None
    entity_id: str | None = None
    geometry: str | None = None


class ChatResponse(BaseModel):
    response: str
    session_id: str
    needs_clarification: bool
    clarify_for: str | None = None
    reasoning_content: str | None = None
    entities: list[Entity] = []
