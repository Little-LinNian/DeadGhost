from typing import List, Union

from graia.broadcast.exceptions import ExecutionStop
from graia.broadcast.entities.dispatcher import BaseDispatcher
from graia.broadcast.interfaces.dispatcher import DispatcherInterface

from graia.ariadne.model import Member, Friend
from graia.ariadne.event.message import MessageEvent

class OnlyForOne(BaseDispatcher):

    def __init__(self, user: Union[Member,Friend]):
        self.user = user

    def catch(self, interface: DispatcherInterface[MessageEvent]):
        if interface.event.sender.id != self.user.id:
            raise ExecutionStop()


class OnlyForSomePeople(BaseDispatcher):

    def __init__(self, users: List[Union[Member,Friend]]):
        self.users = users

    def catch(self, interface: DispatcherInterface[MessageEvent]):
        if interface.event.sender.id not in self.users:
            raise ExecutionStop()

