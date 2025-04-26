from dto.UserLogin import UserLogin
from service.SqLiteConnectionFactory import SqLiteConnectionFactory
from typing import Optional

class UserService:
    @staticmethod
    def getUserByEmailAndPass(email: str, senha: str) -> Optional[UserLogin]:
        with SqLiteConnectionFactory.getConnection() as conn:
            resp = conn.execute(f"select idUser, emailUser, nameUser from user where emailUser = ? and senhaUser = ?", (email, senha)).fetchone()

            return UserLogin(resp[0], resp[1], resp[2]) if resp != None else None
