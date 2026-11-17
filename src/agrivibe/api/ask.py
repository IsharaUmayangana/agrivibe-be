from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated

from agrivibe.models.ask import AskRequest, AskResponse
from agrivibe.service.answering import AnswerService
from agrivibe.dependencies import get_answer_service

router = APIRouter(tags=["Agents"])

Service = Annotated[AnswerService, Depends(get_answer_service)]

@router.post("/ask")
def ask(request: AskRequest, service: Service) -> AskResponse:
    return service.ask(request.question)