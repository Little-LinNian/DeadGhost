import asyncio
from datetime import datetime
import random
from graia import broadcast
from graia.scheduler import GraiaScheduler
from graia.saya import Saya
from graia.ariadne.app import Ariadne
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.element import Plain
from graia.scheduler.timers import crontabify

saya = Saya.current()
broadcast = saya.broadcast
scheduler = GraiaScheduler(saya.broadcast.loop, broadcast)


@scheduler.schedule(crontabify("32 8 * * *"))
async def morning(app: Ariadne):
    await asyncio.sleep(random.randint(0, 10))
    await app.sendGroupMessage(
        982502747, MessageChain.create(Plain(f"早安龙窝，今天是{datetime.now().date()}"))
    )
