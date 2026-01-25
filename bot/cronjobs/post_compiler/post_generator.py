from openai import AsyncOpenAI

from config import settings

from ...schemas.report_compiler import CompiledData


class PostGenerator:
    client = AsyncOpenAI(
        api_key=settings.AI_TOKEN,
        base_url="https://api.proxyapi.ru/openai/v1",
    )

    @classmethod
    async def generate_post(cls, data: CompiledData) -> str:
        """Генерирует пост с итогами месяца на основе записей пользователя"""

        system_prompt = """Ты - персональный ассистент для ведения дневника и саморефлексии.
Твоя задача - составить пост "Мои итоги месяца" на основе записей пользователя.

ТРЕБОВАНИЯ К ПОСТУ:
1. Пиши от первого лица ("я", "мне", "мой")
2. Выдели ключевые события и достижения месяца
3. Отметь изменения в настроении и эмоциональном состоянии
4. Укажи повторяющиеся темы (работа, хобби, отношения, здоровье)
5. Сделай пост структурированным, но живым и личным
6. Длина: 400-600 слов
7. Тон: рефлексивный, честный, но позитивный
8. НИ В КОЕМ СЛУЧАЕ НЕ ВЫДУМЫВАЙ. Информацию Берем исключительно из Записей пользователя. Если информации мало, то получится маленький пост. Гоавное не выдумывать ничего самому. Задача - аккуратно обернуть уже существующие данные.


Пиши естественно, используй конкретные примеры из записей, избегай клише и банальностей."""

        notes_text = "\n".join(f"{i+1}. {note}" for i, note in enumerate(data.notes))

        user_prompt = f"""Имя пользователя: {data.user_name}
Количество записей: {len(data.notes)}

ЗАПИСИ ЗА МЕСЯЦ:
{notes_text}

Составь пост "Мои итоги месяца" на основе этих записей."""

        chat_completion = await cls.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            temperature=0.7,
            max_tokens=1500,
        )

        return chat_completion.choices[0].message.content
