from pydantic import BaseModel


class InitRequest(BaseModel):
    unit: str | None = None
    reality: str | None = None
    module: str | None = None
    role: str | None = None
    plan: str | None = None
    case: str | None = None


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
    """
    WKT geometry string using lat/lon (WGS84) coordinates.
    Coordinate order: latitude longitude (e.g. POINT (32.0853 34.7818))
    Supported types: POINT, LINESTRING, POLYGON
    """


class ChatResponse(BaseModel):
    response: str
    session_id: str
    needs_clarification: bool
    clarify_for: str | None = None
    reasoning_content: str | None = None
    entities: list[Entity] = []
