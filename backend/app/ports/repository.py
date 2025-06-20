"""
Repository port definition.

Defines the abstract interface for any persistence adapter
that handles question storage and retrieval.
"""

from abc import ABC, abstractmethod
from typing import List
from app.domain.models import Question


class QuestionRepository(ABC):
    """
    Abstract base class for a question repository.

    Methods
    -------
    save(question: Question)
        Persist a new question.
    get_all()
        Retrieve all stored questions.
    """

    @abstractmethod
    async def save(self, question: Question) -> None:
        """
        Save a question to the storage medium.

        Parameters
        ----------
        question : Question
            The question to persist.
        """

    @abstractmethod
    async def get_all(self) -> List[Question]:
        """
        Fetch all stored questions.

        Returns
        -------
        list of Question
            A list of all previously stored questions.
        """
