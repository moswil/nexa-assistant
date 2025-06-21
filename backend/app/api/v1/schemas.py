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


class HistoryEntry(BaseModel):
    """
    Schema representing a single conversation history entry.

    Attributes
    ----------
    question : str
        The user's original question.
    response : str
        The assistant's generated response.
    timestamp : datetime
        Time the question-response pair was stored.
    """
    question: str
    response: str
    timestamp: datetime


class HistoryResponse(BaseModel):
    """
    Schema for the /history endpoint response.

    Attributes
    ----------
    history : list[HistoryEntry]
        List of previous Q&A entries.
    """
    history: list[HistoryEntry]
