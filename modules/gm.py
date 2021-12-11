
from pathlib import Path
from graia.saya import Saya, Channel
from graia.saya.builtins.broadcast.schema import ListenerSchema
from graia.ariadne.app import Ariadne
from botlibs.gm import BlackListManager, AdminManager
from graia.ariadne.event.message import FriendMessage, GroupMessage, MessageEvent
from graia.ariadne.event.mirai import MemberJoinRequestEvent, NewFriendRequestEvent
from graia.ariadne.model import Friend, Group, Member, MemberPerm
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.element import Image as IMG, Plain
saya = Saya.current()
channel = Channel.current()



@channel.use(ListenerSchema([GroupMessage]))
async def on_group_message(app:Ariadne,msg: MessageChain,member: Member,group: Group):
    if not msg.asDisplay().startswith('#黑名单'):
        return
    admin = AdminManager(group=group.id)
    if not await admin.is_admin(member.id):
        await app.sendGroupMessage(
            group,
            MessageChain.create([
                Plain('你不是Bot管理员，无法使用此命令')
            ])
        )
        return
    cmd = msg.asDisplay().split(' ')
    if len(cmd) != 3:
        await app.sendGroupMessage(
            group,
            MessageChain.create([
                Plain('命令格式错误，请使用#黑名单 添加/删除 QQ')
            ])
        )
        return


    bl = BlackListManager(group=group.id)
    if cmd[1] == '添加':
        if await bl.is_blacklisted(cmd[2]):
            await app.sendGroupMessage(
                group,
                MessageChain.create([
                    Plain('QQ已在黑名单中')
                ])
            )
            return
        await bl.add_blacklist(cmd[2])
        await app.sendGroupMessage(
            group,
            MessageChain.create([
                Plain('QQ已添加到黑名单')
            ])
        )
    elif cmd[1] == '删除':
        if not await bl.is_blacklisted(cmd[2]):
            await app.sendGroupMessage(
                group,
                MessageChain.create([
                    Plain('QQ不在黑名单中')
                ])
            )
            return
        await bl.remove_blacklist(cmd[2])
        await app.sendGroupMessage(
            group,
            MessageChain.create([
                Plain('QQ已从黑名单中删除')
            ])
        )
    else:
        await app.sendGroupMessage(
            group,
            MessageChain.create([
                Plain('命令格式错误，请使用#黑名单 添加/删除 QQ')
            ])
        )

@channel.use(ListenerSchema([GroupMessage]))
async def on_group_message(app:Ariadne,msg: MessageChain,member: Member,group: Group):
    if not msg.asDisplay().startswith('#管理员'):
        return
    admin = AdminManager(group=group.id)
    if not member.id == 2544704967:
        await app.sendGroupMessage(
            group,
            MessageChain.create([
                Plain('你不是Bot超级管理员，无法使用此命令')
            ])
        )
        return
    cmd = msg.asDisplay().split(' ')
    if len(cmd) != 3:
        await app.sendGroupMessage(
            group,
            MessageChain.create([
                Plain('命令格式错误，请使用#管理员 添加/删除 QQ')
            ])
        )
        return
    if cmd[1] == '添加':
        if await admin.is_admin(cmd[2]):
            await app.sendGroupMessage(
                group,
                MessageChain.create([
                    Plain('QQ已在管理员列表中')
                ])
            )
            return
        await admin.add_admin(cmd[2])
        await app.sendGroupMessage(
            group,
            MessageChain.create([
                Plain('QQ已添加到管理员列表')
            ])
        )
    elif cmd[1] == '删除':
        if not await admin.is_admin(cmd[2]):
            await app.sendGroupMessage(
                group,
                MessageChain.create([
                    Plain('QQ不在管理员列表中')
                ])
            )
            return
        await admin.remove_admin(cmd[2])
        await app.sendGroupMessage(
            group,
            MessageChain.create([
                Plain('QQ已从管理员列表中删除')
            ])
        )
    else:
        await app.sendGroupMessage(
            group,
            MessageChain.create([
                Plain('命令格式错误，请使用#管理员 添加/删除 QQ')
            ])
        )

@channel.use(ListenerSchema([FriendMessage]))
async def on_friend_message(app:Ariadne,msg: MessageChain,friend: Friend):
        if not msg.asDisplay().startswith('#黑名单'):
            return

        cmd = msg.asDisplay().split(' ')
        if len(cmd) == 4:
            group = cmd[1]
            admin = AdminManager(group=group)
            if not await admin.is_admin(friend.id):
                await app.sendFriendMessage(
                    friend,
                    MessageChain.create([
                        Plain(f'你不是 群({group})的Bot管理员，无法使用此命令')
                    ])
                )
                return
            bl = BlackListManager(group=group)
            if cmd[2] == '添加':
                if await bl.is_blacklisted(cmd[3]):
                    await app.sendFriendMessage(
                        friend,
                        MessageChain.create([
                            Plain('QQ已在黑名单中')
                        ])
                    )
                    return
                await bl.add_blacklist(cmd[3])
                await app.sendFriendMessage(
                    friend,
                    MessageChain.create([
                        Plain('QQ已成功添加到黑名单')
                    ])
                )
            elif cmd[2] == '删除':
                if not await bl.is_blacklisted(cmd[3]):
                    await app.sendFriendMessage(
                        friend,
                        MessageChain.create([
                            Plain('QQ不在黑名单中')
                        ])
                    )
                    return
                await bl.remove_blacklist(cmd[3])
                await app.sendFriendMessage(
                    friend,
                    MessageChain.create([
                        Plain('QQ已成功从黑名单中删除')
                    ])
                )
            else:
                await app.sendFriendMessage(
                    friend,
                    MessageChain.create([
                        Plain('命令格式错误，请使用#黑名单 添加/删除 QQ')
                    ])
                )
        else:
            await app.sendFriendMessage(
                friend,
                MessageChain.create([
                    Plain('命令格式错误，请使用#黑名单 群号 添加/删除 QQ')
                ])
            )
@channel.use(ListenerSchema([MemberJoinRequestEvent]))
async def on_member_join_request(event: MemberJoinRequestEvent):
    bl = BlackListManager(group=event.groupId)
    if await bl.is_blacklisted(event.supplicant):
        await event.reject("你已被管理员拉入黑名单")
        print(f"{event.supplicant} 已被管理员拉入黑名单")
    else:
        pass

@channel.use(ListenerSchema([NewFriendRequestEvent]))
async def on_add(e: NewFriendRequestEvent):
    print(e)
    await e.accept()