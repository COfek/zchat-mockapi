import uuid

from fastapi import APIRouter, Header

from app.models.schemas import ChatRequest, ChatResponse, Entity

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
async def chat(
    body: ChatRequest,
    api_key: str = Header(...),
    user_personal_number: str = Header(...),
) -> ChatResponse:
    session_id = body.session_id or str(uuid.uuid4())

    return ChatResponse(
        response="This is a mock response.",
        session_id=session_id,
        needs_clarification=False,
        clarify_for=None,
        reasoning_content=None,
        entities=[
            Entity(
                layer="mock-layer",
                entity_id="mock-entity-1",
                geometry=None,
            )
        ],
    )
