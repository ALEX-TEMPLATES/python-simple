import asyncio

import psycopg

from settings import settings

# Получаем DSN из настроек (pydantic-settings загрузит из .env)


async def main():
    # Асинхронное подключение
    async with await psycopg.AsyncConnection.connect(settings.dsn) as aconn:
        async with aconn.cursor() as cur:
            # Создание таблицы с одним полем id
            await cur.execute("""
                CREATE TABLE IF NOT EXISTS test_table (
                    id SERIAL PRIMARY KEY
                )
            """)
            print("Таблица успешно создана!")


if __name__ == "__main__":
    asyncio.run(main())
