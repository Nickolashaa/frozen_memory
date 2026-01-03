from datetime import datetime

from pydantic import BaseModel


class UserDTO(BaseModel):
    id: int
    nickname: str | None = None
    first_name: str
    last_name: str | None = None
    created_at: datetime

    class config:
        from_attributes = True
