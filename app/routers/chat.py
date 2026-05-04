import uuid

from fastapi import APIRouter, Header

from app.mocks.scenarios import match_scenario
from app.models.schemas import ChatRequest, ChatResponse

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
async def chat(
    body: ChatRequest,
    api_key: str = Header(...),
    user_personal_number: str = Header(...),
) -> ChatResponse:
    session_id = body.session_id or str(uuid.uuid4())
    scenario = match_scenario(body.message)

    return ChatResponse(
        response=scenario["response"],
        session_id=session_id,
        needs_clarification=scenario.get("needs_clarification", False),
        clarify_for=scenario.get("clarify_for"),
        reasoning_content=None,
        entities=scenario["entities"],
    )
