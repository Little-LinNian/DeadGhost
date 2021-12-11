from graia.broadcast import Broadcast
from motor import motor_asyncio






def initdb(bcc: Broadcast):
    global client
    client = motor_asyncio.AsyncIOMotorClient('localhost', 27017,io_loop=bcc.loop)



def get_db(db_name):
    return client[db_name]

