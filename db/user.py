import time
import aiosqlite
from assets.config import DATABASE_PATH

class User:
    def __init__(self, user_id, language, join_date):
        self.user_id = user_id
        self.language = language
        self.join_date = join_date

    @staticmethod
    async def create_table() -> None:
        async with aiosqlite.connect(DATABASE_PATH) as db:
            await db.execute(
                '''
CREATE TABLE IF NOT EXISTS [Users] (
    [UserId] INTEGER PRIMARY KEY,
    [LangCode] STRING NOT NULL,
    [JoinDate] INTEGER
)
                '''
            )
            await db.commit()
            print(f"✅ {__class__.__name__} table initialized")

    @staticmethod
    async def get_all():
        async with aiosqlite.connect(DATABASE_PATH) as db:
            cursor = await db.execute(
                '''
SELECT *
FROM [Users] 
                '''
            )
            result = await cursor.fetchall()
            return result

    @staticmethod
    async def get(user_id: int):
        async with aiosqlite.connect(DATABASE_PATH) as db:
            cursor = await db.execute(
                '''
SELECT *
FROM [Users] 
WHERE [UserId] = ?
                ''',
                (user_id,)
            )
            result = await cursor.fetchone()
            return User(*result) if result else None

    @staticmethod
    async def create(user_id: int, lang_code: str) -> None:
        async with aiosqlite.connect(DATABASE_PATH) as db:
            await db.execute(
                '''
INSERT INTO [Users] ([UserId], [LangCode], [JoinDate]) VALUES(?, ?, ?)
                ''',
                (user_id, lang_code, time.time())
            )
            await db.commit()

    @staticmethod
    async def is_user_exist(user_id) -> bool:
        async with aiosqlite.connect(DATABASE_PATH) as db:
            cursor = await db.execute(
                '''
SELECT COUNT(*) 
FROM [Users] 
WHERE [UserId] = ?
                ''',
                (user_id,)
            )
            result = await cursor.fetchone()
            return bool(result)
    @staticmethod
    async def get_user_lang(user_id):
        async with aiosqlite.connect(DATABASE_PATH) as db:
            cursor = await db.execute(
                '''
SELECT [LangCode] 
FROM [Users] 
WHERE [UserId] = ?
                ''',
                (user_id,)
            )
            result = await cursor.fetchone()
            if result:
                return result[0]
            return None

    @staticmethod
    async def update_user_lang(user_id: int, lang_code: str) -> None:
        async with aiosqlite.connect(DATABASE_PATH) as db:
            await db.execute(
                '''
UPDATE [Users] 
SET [LangCode] = ? 
WHERE [UserId] = ?
                ''',
                (lang_code, user_id)
            )
            await db.commit()
