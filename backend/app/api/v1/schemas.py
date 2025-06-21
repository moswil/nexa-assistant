"""
Pydantic schemas for API input and output.

These models handle FastAPI request/response validation and serialization.
"""

from typing import Any
from datetime import datetime
from pydantic import BaseModel, Field


class AskRequest(BaseModel):
    """
    Schema for incoming question submission.

    Attributes
    ----------
    question : str
        The question submitted by the user.
    """
    question: Any = Field(...,  # type: ignore
                          example="What is the capital of Kenya?")  # type: ignore


class AskResponse(BaseModel):
    """
    Schema for assistant response.

    Attributes
    ----------
    response : str
        The assistant's reply.
    """
    response: str


class QuestionHistoryItem(BaseModel):
    """
    Schema for a single entry in the conversation history.

    Attributes
    ----------
    text : str
        The question text.
    timestamp : datetime
        When the question was submitted.
    """
    text: str
    timestamp: datetime


class HistoryResponse(BaseModel):
    """
    Schema for the history endpoint response.

    Attributes
    ----------
    history : list[QuestionHistoryItem]
        The list of previously submitted questions.
    """
    history: list[QuestionHistoryItem]
