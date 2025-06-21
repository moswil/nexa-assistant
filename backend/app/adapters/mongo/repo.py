"""
MongoDB adapter for question persistence.

Implements the QuestionRepository port using Motor (async MongoDB driver).
"""

from typing import List, Any
from motor.motor_asyncio import AsyncIOMotorClient

from app.domain.models import Question
from app.ports.repository import QuestionRepository


class MongoQuestionRepository(QuestionRepository):
    """
    MongoDB implementation of the QuestionRepository interface.

    Parameters
    ----------
    client : AsyncIOMotorClient
        The Motor client used to connect to MongoDB.
    db_name : str
        The name of the MongoDB database to use.
    collection_name : str
        The name of the collection to store questions.
    """

    def __init__(
        self,
        client: AsyncIOMotorClient,  # type:ignore
        db_name: str,
        collection_name: str
    ) -> None:
        self._collection: Any = client[db_name][collection_name]

    async def save(self, question: Question) -> None:
        """
        Save a question document into the MongoDB collection.

        Parameters
        ----------
        question : Question
            The question domain model to persist.
        """
        await self._collection.insert_one({
            "text": question.text,
            "response": question.response,
            "timestamp": question.timestamp
        })

    async def get_all(self) -> List[Question]:
        """
        Retrieve all questions from the MongoDB collection.

        Returns
        -------
        list of Question
            A list of all stored questions.
        """
        documents = self._collection.find().sort("timestamp", 1)
        return [Question(text=doc["text"], response=doc["response"],
                         timestamp=doc["timestamp"]) async for doc in documents]
