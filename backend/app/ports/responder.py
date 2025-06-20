"""
Responder port definition.

Defines the abstract interface for generating responses to user questions.
"""

from abc import ABC, abstractmethod


class Responder(ABC):
    """
    Abstract base class for a responder.

    Methods
    -------
    respond(question: str)
        Generate a response for a given question.
    """

    @abstractmethod
    async def respond(self, question: str) -> str:
        """
        Generate a response based on the user's question.

        Parameters
        ----------
        question : str
            The input question text.

        Returns
        -------
        str
            A generated assistant response.
        """
