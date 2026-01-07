from typing import Any

from aiogram import Bot

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

import pytz

from .note_reminder import note_remind


def setup_sheduler(bot: Bot) -> Any:
    scheduler = AsyncIOScheduler(
        timezone=pytz.timezone("Europe/Moscow"),
    )
    scheduler.add_job(
        func=note_remind,
        kwargs={"bot": bot},
        trigger=CronTrigger(
            hour=23, minute=30, timezone=pytz.timezone("Europe/Moscow")
        ),
        id="notify_before_lesson_job",
        replace_existing=True,
    )
    return scheduler
