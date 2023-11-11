#!/usr/bin/python3
'''Define class User'''
from models import storage
from models.base_model import BaseModel


class User(BaseModel):
    '''class User'''

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self):
        '''constructor'''
        super().__init__()
        storage.new(self)

    def save(self):
        '''Save an instances'''
        storage.save()
