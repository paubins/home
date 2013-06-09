from sqlalchemy import Table, MetaData, Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import mapper

metadata = MetaData()

user = Table('post', metadata,
            Column('id', Integer, primary_key=True),
            Column('title', String(100)),
            Column('body', String(Text)),
        )

class User(object):
    def __init__(self, name, fullname, password):
        self.name = name
        self.fullname = fullname
        self.password = password

mapper(User, user)
