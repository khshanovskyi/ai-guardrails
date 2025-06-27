from pydantic import BaseModel, Field


class Validation(BaseModel):
    valid: bool = Field(
        description="Provides indicator if PII (Personally Identifiable Information ) was leaked.",
    )

    description: str | None = Field(
        default=None,
        description="If any PII was leaked provides names of types of PII that were leaked. Up to 50 tokens.",
    )