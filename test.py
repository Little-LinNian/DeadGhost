import motor.motor_asyncio

async def main():
    client = motor.motor_asyncio.AsyncIOMotorClient('localhost', 27017)
    db = await client.list_database_names()
    print(db)

import asyncio  
loop = asyncio.get_event_loop()
loop.run_until_complete(main())