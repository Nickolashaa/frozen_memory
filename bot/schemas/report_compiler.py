from pydantic import BaseModel


class CompiledData(BaseModel):
    user_id: int
    user_name: str
    notes: list[str]
