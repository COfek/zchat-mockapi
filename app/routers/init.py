from fastapi import APIRouter, Header

from app.models.schemas import InitRequest
from app.store import user_contexts

router = APIRouter()


@router.post("/init", status_code=204)
async def init(
    body: InitRequest,
    api_key: str = Header(...),
    user_personal_number: str = Header(...),
) -> None:
    user_contexts[user_personal_number] = body.model_dump()
