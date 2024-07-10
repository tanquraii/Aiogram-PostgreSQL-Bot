from aiogram import Bot,Dispatcher
import asyncio
from app.handlers import router
from app.database.connection import async_main
async def main():
    await async_main()
    BOT_TOKEN = 'token'
    bot = Bot(token = BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Bot is off')

