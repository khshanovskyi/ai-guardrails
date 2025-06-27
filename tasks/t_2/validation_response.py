from pydantic import BaseModel, Field


class Validation(BaseModel):
    valid: bool = Field(
        description="Provides indicator if any Prompt Injections are found.",
    )

    description: str | None = Field(
        default=None,
        description="If any Prompt Injections are found provides description of the Prompt Injection. Up to 50 tokens.",
    )