"""
Dependency injection container.

Creates and wires application components and adapters using env-based config.
"""

import os
from dotenv import load_dotenv

from motor.motor_asyncio import AsyncIOMotorClient

from app.domain.services import QuestionService
from app.adapters.mongo.repo import MongoQuestionRepository
from app.adapters.responder.static_response import StaticResponder
from app.adapters.responder.togetherai_responder import TogetherAIResponder


# Load environment variables
load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
MONGO_DB = os.getenv("MONGO_DB", "assistant")
MONGO_COLLECTION = os.getenv("MONGO_COLLECTION", "questions")

# MongoDB client and repository
mongo_client = AsyncIOMotorClient(MONGO_URI)  # type: ignore
repository = MongoQuestionRepository(
    client=mongo_client,
    db_name=MONGO_DB,
    collection_name=MONGO_COLLECTION
)

# Responder (can be replaced later)
responder = StaticResponder()
togetherai_responder = TogetherAIResponder()

# Application service
question_service = QuestionService(
    repository=repository, responder=togetherai_responder)
