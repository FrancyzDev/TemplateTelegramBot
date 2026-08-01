from .ban import Ban
from .user import User

class Database:
    users = User
    bans = Ban

    async def init_tables(self):
        await self.users.create_table()
        await self.bans.create_table()
        print(f"✅ {self.__class__.__name__} fully initialized")

database = Database()