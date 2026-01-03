from datetime import datetime
from typing import Required, TypedDict


class NoteParams(TypedDict):
    user_id: Required[int]
    text: Required[str]
