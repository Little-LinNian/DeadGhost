from graia.scheduler import GraiaScheduler
from graia.broadcast import Broadcast
import asyncio
from datetime import datetime
from graia.scheduler.timers import every

loop = asyncio.get_event_loop()
bcc  = Broadcast(loop=loop)
sc = GraiaScheduler(loop,bcc)

def timer():
    while True:
        yield datetime(year=2021,month=11,day=8,hour=16,minute=40,second=00,microsecond=00)

@sc.schedule(timer=timer())
def _():
    print(datetime.now())
    loop.stop()

loop.run_forever()