"""
API routes for the assistant application.

Handles user interactions via HTTP endpoints.
"""

from fastapi import APIRouter
from app.api.v1.schemas import AskRequest, AskResponse, HistoryResponse, HistoryEntry
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
        Retrieve all previously asked questions and their responses.

        Returns
        -------
        HistoryResponse
            A list of historical question-response pairs with timestamps.
        """
        history = await service.get_history()
        return HistoryResponse(
            history=[
                HistoryEntry(
                    question=entry.text,
                    response=entry.response,
                    timestamp=entry.timestamp
                )
                for entry in history
            ]
        )

    return router
