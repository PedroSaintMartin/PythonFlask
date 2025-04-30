from dataclasses import dataclass

@dataclass
class InsertUser(object):
    nomeUser: str
    emailUser: str
    telefoneUser: str
    senhaUser: str