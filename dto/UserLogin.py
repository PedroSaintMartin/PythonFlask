from dataclasses import dataclass

@dataclass
class UserLogin:
    idUser: int
    emailUser: str
    nomeUser: str