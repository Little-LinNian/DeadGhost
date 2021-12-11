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

@channel.use(ListenerSchema([BotInvitedJoinGroupRequestEvent]))
async def on_invite(event: BotInvitedJoinGroupRequestEvent,app: Ariadne):
    logger.info(f"{event.nickname} 邀请你加入了群 {event.groupName}")
    await app.sendFriendMessage(2544704967, MessageChain.create(Plain(f"{event.nickname} 邀请鬼鬼加入了群 {event.groupName}")))
    await event.accept()

@channel.use(ListenerSchema([FriendMessage]))
async def on_group_message(msg: MessageChain,app: Ariadne,friend: Friend):
    if friend.id == 2544704967 and msg.asDisplay().startswith("#允许邀请"):
        group =  int(msg.asDisplay().split(" ")[1])
        async with aiofiles.open("./data/allow_group.json", "r") as f:
            allow_group = ujson.loads(await f.read())
        allow_group.append(group)
        async with aiofiles.open("./data/allow_group.json", "w") as f:
            await f.write(ujson.dumps(allow_group))
        await app.sendFriendMessage(friend.id, MessageChain.create(Plain(f"已允许邀请 {group}")))
        logger.info(f"已允许邀请 {group}")
    elif friend.id == 2544704967 and msg.asDisplay().startswith("#禁止邀请"):
        group =  int(msg.asDisplay().split(" ")[1])
        async with aiofiles.open("./data/allow_group.json", "r") as f:
            allow_group = ujson.loads(await f.read())
        allow_group.remove(group)
        async with aiofiles.open("./data/allow_group.json", "w") as f:
            await f.write(ujson.dumps(allow_group))
        await app.sendFriendMessage(friend.id, MessageChain.create(Plain(f"已禁止邀请 {group}")))
        logger.info(f"已禁止邀请 {group}")
    
