from typing import Required, TypedDict


class UserParams(TypedDict):
    id: Required[int]
    username: Required[str | None]
    first_name: Required[str]
    last_name: Required[str | None]
