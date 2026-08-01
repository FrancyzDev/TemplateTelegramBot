import asyncio
from assets.bot import bot, dp
from db.database import database

async def main():
    create_table_task = asyncio.create_task(database.init_tables())
    await asyncio.gather(
        create_table_task,
    )
    bot_info = await bot.get_me()
    print(f"✅ Bot @{bot_info.username} ({bot_info.id}) is active")
    await bot.delete_webhook(drop_pending_updates=True)
    bot_task = asyncio.create_task(dp.start_polling(bot))
    await asyncio.gather(bot_task)

asyncio.run(main())
