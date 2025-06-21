"""Responder adapter using OpenAI API to generate dynamic answers."""

import os

import openai

from dotenv import load_dotenv
from app.ports.responder import Responder

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


class OpenAIResponder(Responder):
    """
    Adapter that uses OpenAI's Chat API to generate a response.

    Methods
    -------
    respond(question: str) -> str
        Returns a model-generated response to the given question.
    """

    async def respond(self, question: str) -> str:
        """
        Call OpenAI API to get a response to the user's question.

        Parameters
        ----------
        question : str
            The user input.

        Returns
        -------
        str
            Model-generated reply.
        """
        try:
            client = openai.OpenAI(api_key=OPENAI_API_KEY)

            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": question}
                ],
                temperature=0.7,
                max_tokens=150,
            )
            content = response.choices[0].message.content
            return content.strip() if content else "Thanks for your question, I'll think about it."

        except Exception as e:
            return f"Failed to get answer: {str(e)}"
