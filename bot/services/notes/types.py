from typing import Literal, Required, TypedDict


class NoteParams(TypedDict):
    user_id: Required[int]
    text: Required[str]


type TimeInterval = Literal[
    "MONTH",
    "YEAR",
    "ALL_TIME",
]
