from flask import Flask, render_template, request
from service.UserService import UserService
from service.SqLiteConnectionFactory import SqLiteConnectionFactory
from dto.InsertUser import InsertUser
from dto.UserLogin import UserLogin

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index() -> str:
    if request.method == "GET":
        return render_template("index.html")
    else:
        resp: UserLogin = UserService.getUserByEmailAndPass(request.form.get("email"), request.form.get("senha"))
        return render_template("cadastro.html", user=resp)
    
@app.route("/cadastro", methods=["GET", "POST"])
def cadastro() -> str:
    if request.method == "POST":
        data: InsertUser = InsertUser(
            nomeUser=request.form.get("nome"),
            emailUser=request.form.get("email"),
            telefoneUser=request.form.get("telefone"),
            senhaUser=request.form.get("senha")
        )
        UserService.insertUser(data)
        return render_template("cadastro.html", user=UserService.selectUserByEmail(data.emailUser))
    else:
        return render_template("cadastro.html")

if __name__ == "__main__":
    with open("import.sql", 'r', encoding='utf-8') as f:
        with SqLiteConnectionFactory.getConnection() as conn:
            conn.executescript(f.read())
            conn.commit()
        
    app.run()