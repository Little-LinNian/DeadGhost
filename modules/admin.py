from pathlib import Path
from graia.saya import Saya, Channel
from graia.saya.builtins.broadcast.schema import ListenerSchema
from graia.ariadne.app import Ariadne
from loguru import logger
from botlibs.gm import BlackListManager, AdminManager
from graia.ariadne.event.message import FriendMessage, GroupMessage, MessageEvent
from graia.ariadne.event.mirai import BotInvitedJoinGroupRequestEvent, MemberJoinRequestEvent, NewFriendRequestEvent
from graia.ariadne.model import Friend, Group, Member, MemberPerm
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.element import Image as IMG, Plain
import ujson
import aiofiles
saya = Saya.current()
channel = Channel.current()

@channel.use(ListenerSchema([GroupMessage]))
async def on_msg(msg: MessageChain,app: Ariadne,member: Member,group: Group):
    if not msg.asDisplay().startswith("#群管"):
        return
    if not member.id == 2544704967:
        await app.sendGroupMessage(group,MessageChain.create(
                    "你不是我主人，爬"
            )
        )
        return
    cmd = msg.asDisplay().split(" ")
    if cmd[1] == "禁言":
        if int(cmd[2]) == 2544704967:
            await app.sendGroupMessage(group,MessageChain.create(
                    "怎么真有傻逼自己给自己禁言"
            )
        )
        await app.muteMember(group,int(cmd[2]),int(cmd[3]))
                
