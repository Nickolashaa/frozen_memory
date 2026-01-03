from datetime import datetime
from pydantic import BaseModel


class NoteDTO(BaseModel):
    id: int
    user_id: int
    text: str
    created_at: datetime
