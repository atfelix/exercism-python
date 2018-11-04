import json

from collections import defaultdict
from functools import reduce

def convert_payload(payload):
    return json.loads(payload)

class User(object):
    def __init__(self, name='', user='', owed_by=None, owes=None, balance=0):
        self.name = name or user
        self.balance_dict = owed_by or {}
        for (name, amount) in (owes or {}).items():
            self.balance_dict[name] = self.balance_dict.get(name, 0) - amount
    
    @property
    def owes(self):
        return {name: -amount for (name, amount) in self.balance_dict.items() if amount < 0}

    @property
    def owed_by(self):
        return {name: amount for (name, amount) in self.balance_dict.items() if amount > 0}
    
    @property
    def balance(self):
        return reduce(lambda balance, name_amount: balance + name_amount[1], self.balance_dict.items(), 0)

    def borrow(self, borrower, amount):
        self.add_balance(borrower, -amount)
    
    def lend(self, lender, amount):
        self.add_balance(lender, amount)

    def add_balance(self, name, amount):
        self.balance_dict[name] = self.balance_dict.get(name, 0) + amount
    
    @property
    def regular_json(self):
        return {
            'name': self.name,
            'owes': self.owes,
            'owed_by': self.owed_by,
            'balance': self.balance
        }
    
    @property
    def add_json(self):
        return {
            'user': self.name,
            'owes': self.owes,
            'owed_by': self.owed_by,
            'balance': self.balance
        }


class RestAPI(object):
    def __init__(self, database=None):
        self.database = {user_dict['name']: User(**user_dict) for user_dict in database['users']} or {}

    def get(self, url, payload=None):
        name = convert_payload(payload).get('users') if payload else None
        users = self.usersWithNames(set([name]) if name else None)

        return json.dumps({'users': users}, default=lambda user: user.regular_json)
    
    def usersWithNames(self, names=None):
        if names is None:
            return list(self.database.values())
        return sorted([self.database[name] for name in names if name in self.database], key=lambda user: user.name)

    def post(self, url, payload=None):
        json_payload = json.loads(payload)
        if url == '/add':
            return self.addUser(**json_payload)
        if url == '/iou':
            return self.addIOU(**json_payload)
    
    def addUser(self, user):
        user = User(user=user)
        self.database[user.name] = user

        return json.dumps(user, default=lambda user: user.add_json)

    def addIOU(self, lender, borrower, amount):
        self.database[lender].lend(borrower, amount)
        self.database[borrower].borrow(lender, amount)

        return json.dumps(
            {'users': self.usersWithNames([lender, borrower])}, 
            default=lambda user: user.regular_json
        )

