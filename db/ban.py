import aiosqlite
from assets.config import DATABASE_PATH

class Ban:
    def __init__(self, db_path, user_id):
        self.db_path = db_path
        self.user_id = user_id

    @staticmethod
    async def create_table() -> None:
        async with aiosqlite.connect(DATABASE_PATH) as db:
            await db.execute(
                '''
CREATE TABLE IF NOT EXISTS [Bans] (
    [UserId] INTEGER UNIQUE NOT NULL
)
                '''
            )
            await db.commit()
            print(f"✅ {__class__.__name__} table initialized")

    @staticmethod
    async def create(user_id: int) -> None:
        async with aiosqlite.connect(DATABASE_PATH) as db:
            await db.execute(
                '''
INSERT INTO [Bans]
([UserId]) 
VALUES(?)
                ''',
                (user_id,)
            )
            await db.commit()
    @staticmethod
    async def delete(user_id: int) -> None:
        async with aiosqlite.connect(DATABASE_PATH) as db:
            await db.execute(
                '''
DELETE FROM [Bans]
WHERE [UserId] = ? 
                ''',
                (user_id,)
            )
            await db.commit()

    @staticmethod
    async def is_user_banned(user_id: int) -> bool:
        async with aiosqlite.connect(DATABASE_PATH) as db:
            cursor = await db.execute(
                '''
SELECT * 
FROM [Bans] 
WHERE [UserId] = ?
                ''',
                (user_id,)
            )
            result = await cursor.fetchone()
            return bool(result)
