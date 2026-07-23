class PricingService:
    """
    Calculates estimated LLM execution cost.
    Prices are USD per 1 million tokens.
    """

    MODEL_PRICING = {
        "openai/gpt-4.1-mini": {
            "prompt": 0.40,
            "completion": 1.60,
        },
    }

    def estimate_cost(
        self,
        model: str,
        prompt_tokens: int,
        completion_tokens: int,
    ) -> float:

        pricing = self.MODEL_PRICING.get(model)

        if pricing is None:
            return 0.0

        prompt_cost = (
            prompt_tokens / 1_000_000
        ) * pricing["prompt"]

        completion_cost = (
            completion_tokens / 1_000_000
        ) * pricing["completion"]

        return round(
            prompt_cost + completion_cost,
            6,
        )


pricing_service = PricingService()