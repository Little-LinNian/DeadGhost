from .db import get_db


class AdminManager():

    def __init__(self, group: int):
        self.group = group
        self.db = get_db("G"+str(group))

    async def get_admins(self):
        admins  = self.db.admins.find({})
        return await admins.to_list(length=None)
        

    async def is_admin(self, user: int):
        if not await self.db.admins.find_one({str(user): True}):
            return False
        return True
    
    async def add_admin(self, user: int):
        if await self.is_admin(user):
            return False
        self.db.admins.insert_one({str(user): True})
        return True
    
    async def remove_admin(self, user: int):
        if not await self.is_admin(user):
            return False
        await self.db.admins.delete_one({str(user): True})
        return True



class BlackListManager():

    def __init__(self, group: int):
        self.group = group
        self.db = get_db("G"+str(group))

    async def get_blacklist(self):
        blacklist  = self.db.blacklist.find({})
        return await blacklist.to_list(length=None)
        

    async def is_blacklisted(self, user: int):
        if await self.db.blacklist.find_one({str(user): True}):
            return True
        return False
    async def add_blacklist(self, user: int):
        if await self.is_blacklisted(user):
            return False
        self.db.blacklist.insert_one({str(user): True})
        return True
    
    async def remove_blacklist(self, user: int):
        if not await self.is_blacklisted(user):
            return False
        await self.db.blacklist.delete_one({str(user): True})
        return True
