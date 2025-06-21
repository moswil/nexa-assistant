"""
API routes for the assistant application.

Handles user interactions via HTTP endpoints.
"""

from fastapi import APIRouter
from app.api.v1.schemas import AskRequest, AskResponse, HistoryResponse, QuestionHistoryItem
from app.domain.services import QuestionService


def get_routes(service: QuestionService) -> APIRouter:
    """
    Create API routes for the assistant service.

    Parameters
    ----------
    service : QuestionService
        The service coordinating question processing.

    Returns
    -------
    APIRouter
        A router with /ask and /history endpoints.
    """
    router = APIRouter()

    @router.post("/ask", response_model=AskResponse)
    async def ask_question(payload: AskRequest):
        """
        Handle incoming user question.

        Parameters
        ----------
        payload : AskRequest
            Contains the user question.

        Returns
        -------
        AskResponse
            The assistant's reply.
        """
        response = await service.ask_question(payload.question)
        return AskResponse(response=response)

    @router.get("/history", response_model=HistoryResponse)
    async def get_history():
        """
        Retrieve all previously asked questions.

        Returns
        -------
        HistoryResponse
            A list of historical questions and timestamps.
        """
        history = await service.get_history()
        return HistoryResponse(
            history=[
                QuestionHistoryItem(text=q.text, timestamp=q.timestamp) for q in history
            ]
        )

    return router
