from urllib import response

from openai import OpenAI

from app.core.config import settings
from app.providers.base import BaseProvider


class OpenRouterProvider(BaseProvider):

    def __init__(self):
        self.client = OpenAI(
            api_key=settings.OPENROUTER_API_KEY,
            base_url=settings.OPENROUTER_BASE_URL,
        )

    def generate(
        self,
        system_prompt: str,
        user_prompt: str,
        temperature: float = 0.7,
        max_tokens: int = 1000,
    ) -> str:

        response = self.client.chat.completions.create(
            model=settings.MODEL_NAME,
            messages=[
                {
                    "role": "system",
                    "content": system_prompt,
                },
                {
                    "role": "user",
                    "content": user_prompt,
                },
            ],
            max_tokens=max_tokens,
            temperature=temperature,
        )

        usage = response.usage

        return {
            "content": response.choices[0].message.content or "",

            "model": response.model,

            "prompt_tokens": usage.prompt_tokens,

            "completion_tokens": usage.completion_tokens,

            "total_tokens": usage.total_tokens,
        }