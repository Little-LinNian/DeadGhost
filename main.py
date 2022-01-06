import asyncio

from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.element import Plain
from botlibs.db import initdb
from graia.broadcast import Broadcast
from graia.scheduler import GraiaScheduler
from graia.ariadne.event.message import FriendMessage, GroupMessage
from graia.scheduler.timers import crontabify

from graia.ariadne.adapter import DefaultAdapter
from graia.ariadne.app import Ariadne
from graia.ariadne.model import Friend, Group, MiraiSession
from graia.saya import Saya
from graia.saya.builtins.broadcast import BroadcastBehaviour

loop = asyncio.new_event_loop()

bcc = Broadcast(loop=loop)
app = Ariadne(
        MiraiSession(
            host="http://localhost:8080",  # 填入 httpapi 服务运行的地址
            verify_key="qaq1940QAQ",  # 填入 verifyKey
            account=2595201156,  # 你的机器人的 qq 号
    ),broadcast=bcc)

saya = Saya(bcc)
saya.install_behaviours(BroadcastBehaviour(bcc))
initdb(bcc)
with saya.module_context():
    saya.require("modules.sign_in")
    saya.require("modules.gm")
    saya.require("modules.key_reply")
    saya.require("modules.scheduler")
    saya.require("modules.event")
    saya.require("modules.admin")






loop.run_until_complete(app.lifecycle())
