"""Responder adapter using Together.ai API to generate dynamic answers."""

import os
from typing import Optional

import httpx

from dotenv import load_dotenv

from app.ports.responder import Responder

load_dotenv()

TOGETHER_API_KEY: Optional[str] = os.getenv("TOGETHER_API_KEY")
MODEL: Optional[str] = os.getenv("TOGETHER_MODEL")


class TogetherAIResponder(Responder):
    """
    Adapter that uses Together.ai's OpenAI-compatible API to generate responses.
    """

    async def respond(self, question: str) -> str:
        """
        Sends a user question to the Together.ai API and returns the generated assistant reply.

        Parameters
        ----------
        question : str
            The user's input question.

        Returns
        -------
        str
            The generated assistant response or error message.
        """
        if not TOGETHER_API_KEY:
            return "Missing Together.ai API key."

        url = "https://api.together.xyz/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {TOGETHER_API_KEY}",
            "Content-Type": "application/json"
        }
        payload = {  # type: ignore
            "model": MODEL,
            "messages": [
                {
                    "role": "user",
                    "content": question
                }
            ],
            "temperature": 0.7,
            "max_tokens": 256
        }

        async with httpx.AsyncClient(timeout=60.0) as client:
            try:
                response = await client.post(url, headers=headers,
                                             json=payload)  # type: ignore

                response.raise_for_status()
                data = response.json()
                return data["choices"][0]["message"]["content"].strip()
            except Exception as e:
                return f"Failed to generate response: {str(e)}"
