import random
from graia.saya import Saya, Channel
from graia.saya.builtins.broadcast.schema import ListenerSchema
from graia.ariadne.app import Ariadne
from botlibs.gm import BlackListManager, AdminManager
from graia.ariadne.event.message import FriendMessage, GroupMessage, MessageEvent
from graia.ariadne.event.mirai import MemberJoinRequestEvent
from graia.ariadne.model import Group, Member, MemberInfo, MemberPerm
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.element import Image as IMG, Plain,At
saya = Saya.current()
channel = Channel.current()


@channel.use(ListenerSchema([GroupMessage]))
async def _(app: Ariadne, msg: MessageChain, member: Member, group: Group):
    async def quick_reply(text: str):
        await app.sendGroupMessage(group,MessageChain.create([Plain(text)]))
    if msg.has(Plain):
        textmsg = msg.getFirst(Plain).text
        if textmsg == "奈何是谁":
            await quick_reply("呐呐，龙窝上层唯一的男生(确信)")
        elif textmsg == "霖念是谁":
            await quick_reply(random.choice(["是傻逼！（不我","是创造我的人（嗯"]))
        elif textmsg == "子南是谁":
            await quick_reply("<突然开溜>")
        elif textmsg == "创君是谁":
            await quick_reply("龙窝上层画稿很快那个就是啦")
        elif textmsg == "破龙是谁":
            await quick_reply(random.choice(["破龙，是酷姐（？","虽然不知道为什么，霖念好像很喜欢她画的画"]))
        elif textmsg == "峰卡是谁":
            await quick_reply("是富婆！")
        elif textmsg == "毛熊是谁":
            await quick_reply("dame")
        elif textmsg == "子助是谁":
            await quick_reply('"公子，嘿嘿🤤我的公子（不他"')
        elif "是谁" in textmsg:
            await quick_reply("不知道(直答")
        elif textmsg == "鬼鬼生命周期结束" and member.id == 2544704967:
            await quick_reply("好!")
            await app.stop()
    if msg.has(At):
        at = msg.getFirst(At).target
        if at == 2595201156:
            await quick_reply("你好啊，这里是什么都不会的机器人")

