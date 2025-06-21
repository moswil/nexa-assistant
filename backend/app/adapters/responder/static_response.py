"""
Static responder adapter.

Implements the Responder port by returning a hardcoded response string.
"""

from app.ports.responder import Responder


class StaticResponder(Responder):
    """
    Simple implementation of Responder that returns a fixed message.
    """

    async def respond(self, question: str) -> str:
        """
        Generate a static response to any question.

        Parameters
        ----------
        question : str
            The user's question.

        Returns
        -------
        str
            A static response string.
        """
        return "Thanks for your question, I'll think about it."
