"""
Service layer containing core business logic for question handling.

This layer coordinates the use of domain models and ports to
execute application use cases such as asking questions and
retrieving conversation history.
"""

from datetime import datetime, timezone
from app.domain.models import Question
from app.ports.repository import QuestionRepository
from app.ports.responder import Responder


class QuestionService:
    """
    Service for processing user questions.

    Coordinates the saving of questions and generation of responses
    using the provided repository and responder interfaces.

    Attributes
    ----------
    _repository : QuestionRepository
        Interface to persist and retrieve questions.
    _responder : Responder
        Interface to generate responses for questions.
    """

    def __init__(self, repository: QuestionRepository, responder: Responder) -> None:
        """
        Initialize the QuestionService with required dependencies.

        Parameters
        ----------
        repository : QuestionRepository
            An implementation of the repository port.
        responder : Responder
            An implementation of the responder port.
        """
        self._repository = repository
        self._responder = responder

    async def ask_question(self, question_text: str) -> str:
        """
        Process a user's question and return a response.

        Steps:
        - Create a Question domain model with a timestamp.
        - Persist the question via the repository.
        - Get a response via the responder.

        Parameters
        ----------
        question_text : str
            The question submitted by the user.

        Returns
        -------
        str
            The generated assistant response.
        """
        _timestamp = datetime.now(timezone.utc)

        response = await self._responder.respond(question_text)
        question = Question(text=question_text,
                            response=response,
                            timestamp=_timestamp)
        await self._repository.save(question)
        # return await self._responder.respond(question_text)
        return response

    async def get_history(self) -> list[Question]:
        """
        Retrieve the full list of questions from the repository.

        Returns
        -------
        list of Question
            The list of all questions in order of submission.
        """
        return await self._repository.get_all()
