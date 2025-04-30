from dto.UserLogin import UserLogin
from dto.InsertUser import InsertUser
from service.SqLiteConnectionFactory import SqLiteConnectionFactory
from typing import Optional

class UserService:
    @staticmethod
    def getUserByEmailAndPass(email: str, senha: str) -> Optional[UserLogin]:
        with SqLiteConnectionFactory.getConnection() as conn:
            resp = conn.execute(
                f"select idUser, emailUser, nomeUser from user where emailUser = ? and senhaUser = ?", (email, senha)
            ).fetchone()

            return UserLogin(resp[0], resp[1], resp[2]) if resp != None else resp

    @staticmethod
    def selectUserByEmail(email: str) -> Optional[InsertUser]:
        with SqLiteConnectionFactory.getConnection() as conn:
            resp = conn.execute(
                  f"select"
                + f" nomeUser, emailUser, telefoneUser, senhaUser"
                + f" from user"
                + f" where emailUser = ?", (email,)
            ).fetchone()

            return InsertUser(resp[0], resp[1], resp[2], resp[3])
    
    @staticmethod
    def insertUser(user: InsertUser) -> None:
        with SqLiteConnectionFactory.getConnection() as conn:
            conn.execute(
                  f"insert into user ("
                + f" nomeUser, emailUser, telefoneUser, senhaUser"
                + f" )"
                + f" values ("
                + f" ?, ?, ?, ?"
                + f")", (user.nomeUser, user.emailUser, user.telefoneUser, user.senhaUser)
            )

            conn.commit()

