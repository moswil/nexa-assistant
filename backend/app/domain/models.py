"""
Domain models for the assistant application.

This module defines the core entities used within the domain layer,
independent of any external frameworks or infrastructure.
"""

from datetime import datetime
from dataclasses import dataclass


@dataclass(frozen=True)
class Question:
    """
    Represents a user's question in the system.

    Attributes
    ----------
    text : str
        The question text submitted by the user.
    response : str
        The response to the question submitted by the user.
    timestamp : datetime
        The UTC timestamp of when the question was submitted.
    """
    text: str
    response: str
    timestamp: datetime
