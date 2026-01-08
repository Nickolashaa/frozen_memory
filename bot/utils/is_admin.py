from config import settings


def is_admin(id: str | int) -> bool:
    return str(id) == settings.ADMIN
